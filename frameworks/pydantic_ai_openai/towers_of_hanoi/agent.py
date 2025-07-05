"""Pydantic AI agent implementation with OpenAI-compatible endpoints."""

import logging
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers import Provider
from openai import AsyncOpenAI
from puzzles.towers_of_hanoi.tools import (
    get_tower_state, move_disk, check_if_solved, reset_puzzle
)
from puzzles.towers_of_hanoi.checker import TowersOfHanoiResponse

logger = logging.getLogger(__name__)


class AgentTestContext:
    """Context for tracking tool calls during testing."""
    def __init__(self):
        self.moves_made = []


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


def make_agent(model_config) -> Agent[AgentTestContext, TowersOfHanoiResponse]:
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
        output_type=TowersOfHanoiResponse,
        system_prompt="""
        You are a Towers of Hanoi puzzle solver. You MUST use the available tools to solve the puzzle.
        
        RULES:
        - There are 3 towers: A, B, and C
        - Tower A starts with 3 disks (3=largest, 2=medium, 1=smallest)
        - Goal: Move all disks from tower A to tower C
        - You can only move one disk at a time
        - You can only move the top disk from a tower
        - You cannot place a larger disk on a smaller disk
        
        STRATEGY:
        1. Use get_tower_state to see the current state
        2. Plan your moves carefully - minimum 7 moves needed
        3. Use move_disk to make moves one by one
        4. Use check_if_solved to verify completion
        5. Track all your moves
        
        When you're done, respond ONLY with a valid JSON object in this exact format:
        {
            "moves": [{"from": "A", "to": "C"}, {"from": "A", "to": "B"}, ...],
            "solved": true,
            "final_state": {"A": [], "B": [], "C": [3, 2, 1]}
        }
        
        The moves array should contain ALL moves you made in order.
        The solved field should be true if puzzle is completed.
        The final_state should show the final tower configuration.
        """,
    )
    
    @agent.tool
    async def get_tower_state_tool(ctx: RunContext[AgentTestContext]) -> dict:
        """Get the current state of all towers."""
        return await get_tower_state(ctx)
    
    @agent.tool
    async def move_disk_tool(ctx: RunContext[AgentTestContext], from_tower: str, to_tower: str) -> dict:
        """Move a disk from one tower to another."""
        result = await move_disk(ctx, from_tower, to_tower)
        if result.get('success'):
            # Track successful moves
            ctx.deps.moves_made.append({"from": from_tower, "to": to_tower})
        return result
    
    @agent.tool
    async def check_if_solved_tool(ctx: RunContext[AgentTestContext]) -> dict:
        """Check if the puzzle is solved."""
        return await check_if_solved(ctx)
    
    @agent.tool 
    async def reset_puzzle_tool(ctx: RunContext[AgentTestContext]) -> dict:
        """Reset the puzzle to initial state."""
        ctx.deps.moves_made = []  # Reset move tracking
        return await reset_puzzle(ctx)
    
    return agent


async def run_agent(model_config):
    """Create and run the agent for the given model_config."""
    agent = make_agent(model_config)
    prompt = "Solve the Towers of Hanoi puzzle. Move all disks from tower A to tower C following the rules."
    result = await agent.run(prompt, deps=AgentTestContext())
    return result.output


def get_context() -> AgentTestContext:
    """Get the current test context for checking tool calls."""
    return AgentTestContext()
