"""Pydantic AI agent implementation."""

import logging
from pydantic_ai import Agent, RunContext, NativeOutput, PromptedOutput
from pydantic_ai.models.bedrock import BedrockConverseModel
from puzzles.fruit_count.tools import get_count_of_oranges, get_count_of_apples
from puzzles.fruit_count.checker import FruitCountResponse

logger = logging.getLogger(__name__)


class AgentTestContext:
    """Context for tracking tool calls during testing."""
    def __init__(self):
        pass

def _patched_map_tool_config(self, model_request_parameters):
    """Patched version that always uses 'auto' instead of 'any' for tool choice"""
    tools = self._get_tools(model_request_parameters)
    if not tools:
        return None

    # Always use 'auto' for Meta Llama models instead of 'any'
    tool_choice = {"auto": {}}
    tool_config = {"tools": tools, "toolChoice": tool_choice}

    return tool_config



def make_agent(model_id: str) -> Agent[AgentTestContext, FruitCountResponse]:
    """Create a Pydantic AI agent with fruit counting tools."""
    logger.info(f"Creating Pydantic AI agent with model: {model_id}")
    model = BedrockConverseModel(model_name=model_id)
    if "meta.llama" in model_id.lower() or "llama" in model_id.lower():
        logger.info(f"Applying Meta Llama patch for 'any'/'auto' tool calling for model: {model_id}")
        if hasattr(model, '_map_tool_config'):
            model._map_tool_config = _patched_map_tool_config.__get__(model, type(model))

    agent = Agent(
        model=model,
        deps_type=AgentTestContext,
        # output_type=NativeOutput(FruitCountResponse),
        output_type=PromptedOutput(FruitCountResponse),
        system_prompt="""
        You are a fruit counting assistant. You MUST use the available tools to get fruit counts.
        When asked about fruit counts:
        1. Call relevant tools to get fruit count
        2. Respond ONLY with a valid JSON object in this exact format, and nothing else (no explanation, no extra text):
        {"fruit_count_by_color": {"orange": <orange_count>, "apple": <apple_count>}}
        Replace <orange_count> and <apple_count> with the actual numbers you get from the tools. 
        Do not include any text before or after the JSON. The response must be a single valid JSON object.
        """,
    )
    @agent.tool
    async def get_count_of_oranges_tool(ctx: RunContext[AgentTestContext]) -> int:
        """Get the current count of oranges in inventory."""
        return await get_count_of_oranges(ctx)
    @agent.tool
    async def get_count_of_apples_tool(ctx: RunContext[AgentTestContext]) -> int:
        """Get the current count of apples in inventory."""
        return await get_count_of_apples(ctx)
    return agent

# --- Added for AgentGym runner ---
async def run_agent(model_id: str):
    """Create and run the agent for the given model_id."""
    agent = make_agent(model_id)
    prompt = "How many oranges and apples are there?"
    return await agent.run(prompt, deps=AgentTestContext())
