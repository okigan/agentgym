"""Checker for the Towers of Hanoi puzzle."""

import logging
import json
import re
from typing import Any, Dict, List
from pydantic import BaseModel, ValidationError

logger = logging.getLogger(__name__)

class TowersOfHanoiResponse(BaseModel):
    """Response from the Towers of Hanoi agent."""
    moves: List[Dict[str, str]]  # List of moves made: [{"from": "A", "to": "B"}, ...]
    solved: bool
    final_state: Dict[str, List[int]]  # Final state of towers

def check(result: Any) -> None:
    """Validate the agent's output for the Towers of Hanoi puzzle.
    Raises AssertionError if the result is not valid.
    """
    logger.info(f"🔎 Checking Towers of Hanoi result: {result}")
    
    # Try to coerce result to TowersOfHanoiResponse
    try:
        if isinstance(result, TowersOfHanoiResponse):
            response = result
        elif isinstance(result, dict):
            response = TowersOfHanoiResponse(**result)
        elif hasattr(result, 'output'):
            response = result.output
        else:
            result_text = str(result)
            json_match = re.search(r'\{.*\}', result_text, re.DOTALL)
            if json_match:
                parsed_result = json.loads(json_match.group())
                response = TowersOfHanoiResponse(**parsed_result)
            else:
                raise AssertionError(f"Could not parse response: {result_text}")
    except (ValidationError, Exception) as e:
        raise AssertionError(f"Invalid agent output: {e}")

    # Validate the response
    logger.info(f"📊 Puzzle solved: {response.solved}")
    logger.info(f"📊 Number of moves: {len(response.moves)}")
    logger.info(f"📊 Final state: {response.final_state}")
    
    # Check if puzzle is actually solved
    if not response.solved:
        raise AssertionError("Puzzle was not solved")
    
    # Check if final state is correct (all disks on tower C)
    expected_final_state = [3, 2, 1]
    if response.final_state.get('C') != expected_final_state:
        raise AssertionError(f"Final state incorrect. Tower C should have {expected_final_state}, got {response.final_state.get('C')}")
    
    # Check if towers A and B are empty
    if response.final_state.get('A') != [] or response.final_state.get('B') != []:
        raise AssertionError(f"Towers A and B should be empty. Got A: {response.final_state.get('A')}, B: {response.final_state.get('B')}")
    
    # Check if moves are valid (optional: could validate the entire sequence)
    if len(response.moves) < 7:  # Minimum moves for 3-disk Tower of Hanoi is 7
        logger.warning(f"⚠️ Suspiciously few moves: {len(response.moves)}. Minimum is 7 for 3 disks.")
    
    # Check move format
    for i, move in enumerate(response.moves):
        if not isinstance(move, dict) or 'from' not in move or 'to' not in move:
            raise AssertionError(f"Move {i+1} has invalid format: {move}")
        
        from_tower = move['from']
        to_tower = move['to']
        
        if from_tower not in ['A', 'B', 'C'] or to_tower not in ['A', 'B', 'C']:
            raise AssertionError(f"Move {i+1} has invalid tower names: {from_tower} → {to_tower}")
    
    logger.info("✅ Towers of Hanoi puzzle passed check")
