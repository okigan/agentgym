"""Strands agent implementation."""

import logging
from pydantic import BaseModel, Field
from strands import Agent, tool

from puzzles.fruit_count.tools import get_count_of_oranges_sync, get_count_of_apples_sync

logger = logging.getLogger(__name__)


class FruitCountByColor(BaseModel):
    """Fruit count organized by color/type."""
    orange: int = Field(description="Number of oranges in inventory")
    apple: int = Field(description="Number of apples in inventory")


class FruitCountResponse(BaseModel):
    """Complete fruit count response structure."""
    fruit_count_by_color: FruitCountByColor = Field(description="Fruit counts organized by color/type")


class AgentTestContext:
    """Context for tracking tool calls during testing."""
    def __init__(self):
        pass


# Global context for tracking tool calls in Strands
test_context = AgentTestContext()


@tool
def get_count_of_oranges() -> int:
    """Get the current count of oranges in inventory.

    Use this tool when you need to know how many oranges are currently in stock.
    This tool provides real-time inventory count for orange fruits.

    Returns:
        int: The current number of oranges in inventory (always 25 for testing)
    """
    return get_count_of_oranges_sync()


@tool
def get_count_of_apples() -> int:
    """Get the current count of apples in inventory.

    Use this tool when you need to know how many apples are currently in stock.
    This tool provides real-time inventory count for apple fruits.

    Returns:
        int: The current number of apples in inventory (always 30 for testing)
    """
    return get_count_of_apples_sync()



def make_agent(model_id: str) -> Agent:
    """Create a Strands agent with fruit counting tools."""
    logger.info(f"Creating Strands agent with model: {model_id}")
    logger.info("🦙 Using non-streaming mode for model to support tool use")
    try:
        from strands.models.bedrock import BedrockModel
        bedrock_model = BedrockModel(
            model_id=model_id,
            streaming=False
        )
        agent = Agent(
            model=bedrock_model,
            tools=[get_count_of_oranges, get_count_of_apples],
            system_prompt="""
            You are a fruit counting assistant. You MUST use the available tools to get fruit counts.
            When asked about fruit counts:
            1. Call relevant tools to get fruit count
            2. Respond ONLY with a valid JSON object in this exact format, and nothing else (no explanation, no extra text):
            {"fruit_count_by_color": {"orange": <orange_count>, "apple": <apple_count>}}
            Replace <orange_count> and <apple_count> with the actual numbers you get from the tools. Do not include any text before or after the JSON. The response must be a single valid JSON object.
            You have access to these tools:
            - get_count_of_oranges: Get current orange inventory count
            - get_count_of_apples: Get current apple inventory count
            """,
        )
    except ImportError as e:
        logger.error(f"Strands framework not available: {e}")
        raise ImportError("Strands framework is required but not installed")
    return agent

# --- Added for AgentGym runner ---
async def run_agent(model_id: str):
    """Create and run the agent for the given model_id."""
    agent = make_agent(model_id)
    prompt = "How many oranges and apples are there?"
    response = agent(prompt)

    logger.info(f"Agent response: {response}")
    
    # Extract structured information with existing conversation context
    result = agent.structured_output(FruitCountResponse, "Extract structured information")

    logger.info(f"Structured output: {result}")
    
    # Convert the Pydantic model to a dict for compatibility with the existing system
    return {
        "fruit_count_by_color": {
            "orange": result.fruit_count_by_color.orange,
            "apple": result.fruit_count_by_color.apple
        }
    }


def get_context() -> AgentTestContext:
    """Get the current test context for checking tool calls."""
    return test_context
