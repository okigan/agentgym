"""Strands agent implementation."""

import logging
from strands import Agent, tool

from puzzles.fruit_count.tools import get_count_of_oranges_sync, get_count_of_apples_sync

logger = logging.getLogger(__name__)


class AgentTestContext:
    """Context for tracking tool calls during testing."""
    def __init__(self):
        self.called_tools: list[str] = []


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
    test_context.called_tools.append("get_count_of_oranges")
    return get_count_of_oranges_sync()


@tool
def get_count_of_apples() -> int:
    """Get the current count of apples in inventory.

    Use this tool when you need to know how many apples are currently in stock.
    This tool provides real-time inventory count for apple fruits.

    Returns:
        int: The current number of apples in inventory (always 30 for testing)
    """
    test_context.called_tools.append("get_count_of_apples")
    return get_count_of_apples_sync()


def make_agent(model_id: str) -> Agent:
    """Create a Strands agent with fruit counting tools.
    
    Args:
        model_id: The AWS Bedrock model ID to use
        
    Returns:
        Configured Strands agent
    """
    logger.info(f"Creating Strands agent with model: {model_id}")

    # Clear the global context for fresh evaluation
    test_context.called_tools.clear()

    # Create agent with tools passed during initialization
    logger.info("🦙 Using non-streaming mode for model to support tool use")
    
    try:
        from strands.models.bedrock import BedrockModel
        
        bedrock_model = BedrockModel(
            model_id=model_id,
            streaming=False  # Disable streaming for better tool use compatibility
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


def get_context() -> AgentTestContext:
    """Get the current test context for checking tool calls."""
    return test_context
