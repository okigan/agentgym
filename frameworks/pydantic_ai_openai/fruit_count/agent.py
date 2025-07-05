"""Pydantic AI agent implementation with OpenAI-compatible endpoints."""

import logging
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers import Provider
from openai import AsyncOpenAI
from puzzles.fruit_count.tools import get_count_of_oranges, get_count_of_apples
from puzzles.fruit_count.checker import FruitCountResponse

logger = logging.getLogger(__name__)


class AgentTestContext:
    """Context for tracking tool calls during testing."""
    def __init__(self):
        pass


class CustomOpenAIProvider(Provider[AsyncOpenAI]):
    """Custom OpenAI provider for custom endpoints."""
    
    def __init__(self, base_url: str, api_key: str):
        self._base_url = base_url
        self._api_key = api_key
        self._client = AsyncOpenAI(base_url=base_url, api_key=api_key)
    
    @property
    def name(self) -> str:
        return 'custom-openai'
    
    @property
    def base_url(self) -> str:
        return self._base_url
    
    @property
    def client(self) -> AsyncOpenAI:
        return self._client


def make_agent(model_config) -> Agent[AgentTestContext, FruitCountResponse]:
    """Create a Pydantic AI agent with OpenAI-compatible endpoints."""
    
    # Handle both string (not supported) and dict (custom endpoint) model configs
    if isinstance(model_config, str):
        # This framework only handles custom endpoints, skip Bedrock models
        raise Exception("Pydantic AI OpenAI framework only supports custom endpoints")
    
    if model_config.get("type") != "custom_endpoint":
        raise Exception("Invalid model config for Pydantic AI OpenAI framework")
    
    base_url = model_config["base_url"]
    model_name = model_config["model"]
    
    logger.info(f"Creating Pydantic AI OpenAI agent with endpoint: {base_url}")
    logger.info(f"Requested model: {model_name}")
    
    # Create custom OpenAI provider
    provider = CustomOpenAIProvider(
        base_url=base_url,
        api_key="dummy-key"  # Many local endpoints don't require real API keys
    )
    
    # Create OpenAI model with custom provider
    model = OpenAIModel(
        model_name=model_name,
        provider=provider
    )
    
    agent = Agent(
        model=model,
        deps_type=AgentTestContext,
        output_type=FruitCountResponse,
        system_prompt="""You are a fruit counting assistant. You MUST use the available tools to get fruit counts.
When asked about fruit counts:
1. Call relevant tools to get fruit count
2. Respond ONLY with a valid JSON object in this exact format, and nothing else (no explanation, no extra text):
{"fruit_count_by_color": {"orange": <orange_count>, "apple": <apple_count>}}
Replace <orange_count> and <apple_count> with the actual numbers you get from the tools. 
Do not include any text before or after the JSON. The response must be a single valid JSON object.""",
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


async def run_agent(model_config):
    """Create and run the agent for the given model_config."""
    agent = make_agent(model_config)
    prompt = "How many oranges and apples are there?"
    result = await agent.run(prompt, deps=AgentTestContext())
    return result.output


def get_context() -> AgentTestContext:
    """Get the current test context for checking tool calls."""
    return AgentTestContext()
