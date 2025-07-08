"""Raw OpenAI API endpoint agent implementation using raw HTTP requests."""

import json
import logging
import re
from typing import Any, Dict, List, Optional

import httpx

from puzzles.fruit_count.checker import FruitCountResponse
from puzzles.fruit_count.tools import get_count_of_apples, get_count_of_oranges

logger = logging.getLogger(__name__)


class AgentTestContext:
    """Context for tracking tool calls during testing."""
    def __init__(self):
        pass


async def call_openai_api(base_url: str, model: str, messages: List[Dict], tools: Optional[List[Dict]] = None) -> Dict[Any, Any]:
    """Make a raw HTTP request to OpenAI API."""
    url = f"{base_url}/chat/completions"

    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.1,
        "max_tokens": 1000
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
    """Create and run a raw OpenAI API agent with fruit counting tools."""
    
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
                "name": "get_count_of_oranges",
                "description": "Get the current count of oranges in inventory",
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
                "name": "get_count_of_apples",
                "description": "Get the current count of apples in inventory",
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
            "content": """You are a fruit counting assistant. You MUST use the available tools to get fruit counts.
When asked about fruit counts:
1. Call relevant tools to get fruit count
2. Respond ONLY with a valid JSON object in this exact format, and nothing else (no explanation, no extra text):
{"fruit_count_by_color": {"orange": <orange_count>, "apple": <apple_count>}}
Replace <orange_count> and <apple_count> with the actual numbers you get from the tools. 
Do not include any text before or after the JSON. The response must be a single valid JSON object."""
        },
        {
            "role": "user",
            "content": "How many oranges and apples are there?"
        }
    ]
    
    # First API call
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
                
                if function_name == "get_count_of_oranges":
                    result = await get_count_of_oranges(AgentTestContext())
                elif function_name == "get_count_of_apples":
                    result = await get_count_of_apples(AgentTestContext())
                else:
                    result = "Unknown function"
                
                # Add tool result to conversation
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call["id"],
                    "content": str(result)
                })
            
            # Make second API call with tool results
            response = await call_openai_api(base_url, model, messages)
    
    # Extract final response
    if "choices" in response and len(response["choices"]) > 0:
        content = response["choices"][0]["message"]["content"]
        
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
            json_match = re.search(r'\{[^{}]*"fruit_count_by_color"[^{}]*\}', content)
            if json_match:
                content = json_match.group(0)
            
            result = json.loads(content)
            
            # Convert to expected format
            if "fruit_count_by_color" in result:
                return FruitCountResponse(fruit_count_by_color=result["fruit_count_by_color"])
            else:
                raise Exception(f"Invalid response format: {result}")
                
        except json.JSONDecodeError:
            raise Exception(f"Could not parse response as JSON: {content}")
    
    raise Exception("No valid response from API")


async def run_agent(model_config):
    """Create and run the agent for the given model_config."""
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
