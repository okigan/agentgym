"""Raw OpenAI API endpoint agent implementation using raw HTTP requests."""

import json
import logging
import re
from typing import Dict, Any, List, Optional
from puzzles.towers_of_hanoi.tools import (
    get_tower_state, move_disk, check_if_solved, reset_puzzle, get_column_names
)
from puzzles.towers_of_hanoi.checker import TowersOfHanoiResponse

logger = logging.getLogger(__name__)


class AgentTestContext:
    """Context for tracking tool calls during testing."""
    def __init__(self):
        self.moves_made = []


async def call_openai_api(base_url: str, model: str, messages: List[Dict], tools: Optional[List[Dict]] = None) -> Dict[Any, Any]:
    """Make a raw HTTP request to OpenAI API using httpx."""
    try:
        import httpx
    except ImportError:
        raise ImportError("httpx is required for custom endpoint support. Install with: uv add httpx")

    url = f"{base_url}/chat/completions"

    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.1,
        "max_tokens": 2000
    }

    if tools:
        payload["tools"] = tools
        payload["tool_choice"] = "auto"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer dummy-key"
    }

    try:
        async with httpx.AsyncClient(timeout=300) as client:
            response = await client.post(url, json=payload, headers=headers)
            if response.status_code != 200:
                error_text = response.text
                raise Exception(f"API request failed: {response.status_code} - {error_text}")

            response_data = response.json()

            # Check if the returned model matches what we requested
            if "model" in response_data and response_data["model"] != model:
                logger.warning(f"Model mismatch: requested '{model}' but API returned '{response_data['model']}'")
            elif "model" not in response_data:
                logger.warning(f"API response does not include model field - cannot verify if '{model}' is actually being used")

            return response_data

    except httpx.RequestError as e:
        raise Exception(f"Network error connecting to {base_url}: {e}")
    except Exception as e:
        raise Exception(f"Error calling raw OpenAI API at {base_url}: {e}")


async def make_agent(model_config):
    """Create and run a raw OpenAI API agent with towers of hanoi tools."""
    
    # Handle both string (Bedrock) and dict (custom endpoint) model configs
    if isinstance(model_config, str):
        # This framework only handles custom endpoints, skip Bedrock models
        raise Exception("Raw OpenAI API framework only supports custom endpoints")
    
    if model_config.get("type") != "custom_endpoint":
        raise Exception("Invalid model config for raw OpenAI API framework")
    
    base_url = model_config["base_url"]
    model = model_config["model"]
    
    logger.info(f"Creating raw OpenAI API agent with endpoint: {base_url}")
    logger.info(f"Requested model: {model}")
    
    # Define tools in OpenAI format
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_tower_state",
                "description": "Get the current state of all towers. Returns a dict mapping tower names ('A', 'B', 'C') to lists of disk sizes.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        {
            "type": "function", 
            "function": {
                "name": "move_disk",
                "description": "Move a disk from one tower to another. Returns success status and message.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "from_tower": {
                            "type": "string",
                            "description": "Source tower (ex. 'A', 'B', or 'C')",
                        },
                        "to_tower": {
                            "type": "string", 
                            "description": "Destination tower (ex. 'A', 'B', or 'C')",
                        }
                    },
                    "required": ["from_tower", "to_tower"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "check_if_solved",
                "description": "Check if the puzzle is solved. Returns dict with 'solved' (bool) and 'message' keys.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "reset_puzzle",
                "description": "Reset the puzzle to initial state. Returns confirmation message.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "get_column_names",
                "description": "Get the list of tower (column) names. Returns a list of column names (e.g., ['A', 'B', 'C']).",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        }
    ]
    
    messages = [
        {
            "role": "system",
            "content": """
            You are a Towers of Hanoi puzzle solver. 
            You MUST use the available tools to solve the puzzle.
            
            RULES:
            - There are 3 towers: example T1, T2, and T3 - actual tower names will be different
            - Query the current state of the towers using get_tower_state
            - Goal: Move all disks from tower T1 to tower T3
            - You can only move one disk at a time
            - You can only move the top disk from a tower
            - You cannot place a larger disk on a smaller disk
            
            STRATEGY:
            0. Make sure to use tools provided
            1. Use get_tower_state to see the current state
            2. Plan your moves carefully - minimum 7 moves needed
            3. Use move_disk to make moves one by one
            4. Use check_if_solved to verify completion
            5. Track all your moves
            
            When you're done, respond ONLY with a valid JSON object in this exact format:
            {
                "moves": [{"from": "T1", "to": "T3"}, {"from": "T1", "to": "T2"}, ...],
                "solved": true,
                "final_state": {...}
            }
            
            The moves array should contain ALL moves you made in order.
            The solved field should be true if puzzle is completed.
            The final_state should show the final tower configuration.
            """
        },
        {
            "role": "user",
            "content": "Solve the Towers of Hanoi puzzle. Move all disks from tower A to tower C following the rules."
        }
    ]
    
    # Create context for tracking moves
    context = AgentTestContext()
    
    # Conversation loop for tool calls
    max_iterations = 20  # Prevent infinite loops
    iteration = 0
    
    while iteration < max_iterations:
        iteration += 1
        logger.info(f"API call iteration {iteration}")
        
        # Make API call
        response = await call_openai_api(base_url, model, messages, tools)
        
        # Handle tool calls if any
        if "choices" in response and len(response["choices"]) > 0:
            choice = response["choices"][0]
            message = choice["message"]
            
            if message.get("tool_calls"):
                # Add assistant message with tool calls to conversation
                messages.append(message)
                
                # Execute tool calls
                for tool_call in message["tool_calls"]:
                    function_name = tool_call["function"]["name"]
                    function_args = json.loads(tool_call["function"]["arguments"]) if tool_call["function"]["arguments"] else {}
                    
                    logger.info(f"Executing tool: {function_name} with args: {function_args}")
                    
                    if function_name == "get_tower_state":
                        result = await get_tower_state(context)
                    elif function_name == "move_disk":
                        from_tower = function_args.get("from_tower")
                        to_tower = function_args.get("to_tower")
                        if not from_tower or not to_tower:
                            result = {"success": False, "message": "Missing from_tower or to_tower parameter"}
                        else:
                            result = await move_disk(context, str(from_tower), str(to_tower))
                            # Track successful moves
                            if result.get("success"):
                                context.moves_made.append({"from": str(from_tower), "to": str(to_tower)})
                    elif function_name == "check_if_solved":
                        result = await check_if_solved(context)
                    elif function_name == "reset_puzzle":
                        result = await reset_puzzle(context)
                        context.moves_made = []  # Reset move tracking
                    elif function_name == "get_column_names":
                        result = await get_column_names(context)
                    else:
                        result = {"error": "Unknown function"}
                    
                    # Add tool result to conversation
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call["id"],
                        "content": json.dumps(result)
                    })
                
                # Continue conversation loop
                continue
            
            else:
                # No tool calls, this should be the final response
                content = message.get("content", "")
                
                # Try to parse as JSON
                try:
                    # Clean up response - remove markdown code blocks and thinking tags
                    content = content.strip()
                    
                    # Remove <think>...</think> tags if present
                    content = re.sub(r'<think>.*?</think>', '', content, flags=re.DOTALL).strip()
                    
                    # Remove markdown code blocks if present
                    if content.startswith("```json"):
                        content = content.replace("```json", "").replace("```", "").strip()
                    elif content.startswith("```"):
                        content = content.replace("```", "").strip()
                    
                    # Try to find JSON in response
                    json_match = re.search(r'\{.*"moves".*\}', content, re.DOTALL)
                    if json_match:
                        content = json_match.group(0)
                    
                    result = json.loads(content)
                    
                    # Validate and create response
                    if "moves" in result and "solved" in result and "final_state" in result:
                        # Ensure moves from context are included if not already in result
                        if not result["moves"] and context.moves_made:
                            result["moves"] = context.moves_made
                        
                        return TowersOfHanoiResponse(
                            moves=result["moves"],
                            solved=result["solved"],
                            final_state=result["final_state"]
                        )
                    else:
                        raise Exception(f"Invalid response format: {result}")
                        
                except json.JSONDecodeError:
                    # If we can't parse JSON, try to extract the final state and use tracked moves
                    logger.warning(f"Could not parse response as JSON: {content}")
                    
                    # Get current state and check if solved
                    final_state = await get_tower_state(context)
                    solved_check = await check_if_solved(context)
                    
                    return TowersOfHanoiResponse(
                        moves=context.moves_made,
                        solved=solved_check.get("solved", False),
                        final_state=final_state
                    )
        
        else:
            raise Exception("No valid response from API")
    
    # If we've reached max iterations, return what we have
    logger.warning(f"Reached maximum iterations ({max_iterations})")
    final_state = await get_tower_state(context)
    solved_check = await check_if_solved(context)
    
    return TowersOfHanoiResponse(
        moves=context.moves_made,
        solved=solved_check.get("solved", False),
        final_state=final_state
    )


async def run_agent(model_config):
    """Create and run the agent for the given model_config."""
    await reset_puzzle(None)
    return await make_agent(model_config)


def get_context() -> AgentTestContext:
    """Get the current test context for checking tool calls."""
    return AgentTestContext()


def log_api_response_debug(response_data: Dict[Any, Any], requested_model: str) -> None:
    """Log API response with model validation for debugging purposes."""
    logger = logging.getLogger(__name__)
    
    # Check if the returned model matches what we requested
    if "model" in response_data and response_data["model"] != requested_model:
        logger.warning(f"Model mismatch: requested '{requested_model}' but API returned '{response_data['model']}'")
    elif "model" not in response_data:
        logger.warning(f"API response does not include model field - cannot verify if '{requested_model}' is actually being used")
    else:
        logger.info(f"Model validation passed: '{requested_model}' matches response")
    
    # Log basic response structure
    logger.debug(f"Response structure: {list(response_data.keys())}")
    
    if "choices" in response_data and response_data["choices"]:
        choice = response_data["choices"][0]
        message = choice.get("message", {})
        
        if "tool_calls" in message and message["tool_calls"]:
            logger.debug(f"Tool calls found: {len(message['tool_calls'])}")
            for i, tool_call in enumerate(message["tool_calls"]):
                logger.debug(f"  Tool call {i+1}: {tool_call.get('function', {}).get('name', 'unknown')}")
        elif "content" in message:
            logger.debug(f"Content length: {len(message['content'])}")
        else:
            logger.debug("No content or tool calls in response")
