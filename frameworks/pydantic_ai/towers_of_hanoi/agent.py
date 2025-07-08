"""Pydantic AI agent implementation for Towers of Hanoi."""

import logging
from pydantic_ai import Agent, RunContext, PromptedOutput
from pydantic_ai.models.bedrock import BedrockConverseModel
from puzzles.towers_of_hanoi.tools import (
    get_tower_state, move_disk, check_if_solved, reset_puzzle
)
from puzzles.towers_of_hanoi.checker import TowersOfHanoiResponse

logger = logging.getLogger(__name__)


class AgentTestContext:
    """Context for tracking tool calls during testing."""
    def __init__(self):
        self.moves_made = []

def _patched_map_tool_config(self, model_request_parameters):
    """Patched version that always uses 'auto' instead of 'any' for tool choice"""
    tools = self._get_tools(model_request_parameters)
    if not tools:
        return None

    # Always use 'auto' for Meta Llama models instead of 'any'
    tool_choice = {"auto": {}}
    tool_config = {"tools": tools, "toolChoice": tool_choice}

    return tool_config


def make_agent(model_id: str) -> Agent[AgentTestContext, TowersOfHanoiResponse]:
    """Create a Pydantic AI agent with Towers of Hanoi tools."""
    logger.info(f"Creating Pydantic AI agent with model: {model_id}")
    model = BedrockConverseModel(model_name=model_id)
    if "meta.llama" in model_id.lower() or "llama" in model_id.lower():
        logger.info(f"Applying Meta Llama patch for 'any'/'auto' tool calling for model: {model_id}")
        if hasattr(model, '_map_tool_config'):
            model._map_tool_config = _patched_map_tool_config.__get__(model, type(model))

    agent = Agent(
        model=model,
        deps_type=AgentTestContext,
        output_type=PromptedOutput(TowersOfHanoiResponse),
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

# --- Added for AgentGym runner ---
async def run_agent(model_id: str):
    """Create and run the agent for the given model_id."""
    await reset_puzzle(None)
    agent = make_agent(model_id)
    prompt = "Solve the Towers of Hanoi puzzle. Move all disks from tower A to tower C following the rules."
    return await agent.run(prompt, deps=AgentTestContext())
