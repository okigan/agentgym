"""Tools for the Towers of Hanoi puzzle."""

import asyncio
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

# --- Shared logic for Towers of Hanoi ---

# Global state for the puzzle
_TOWERS = {
    'A': [3, 2, 1],  # Tower A starts with 3 disks (largest to smallest)
    'B': [],         # Tower B starts empty
    'C': []          # Tower C starts empty
}

def _reset_towers():
    """Reset towers to initial state."""
    global _TOWERS
    _TOWERS = {
        'A': [3, 2, 1],
        'B': [],
        'C': []
    }
    logger.info("🗼 Towers reset to initial state")

def _is_valid_move(from_tower: str, to_tower: str) -> bool:
    """Check if a move is valid (smaller disk on larger disk)."""
    if not _TOWERS[from_tower]:
        return False  # Can't move from empty tower
    
    if not _TOWERS[to_tower]:
        return True  # Can always move to empty tower
    
    # Check if top disk of from_tower is smaller than top disk of to_tower
    return _TOWERS[from_tower][-1] < _TOWERS[to_tower][-1]

def _make_move(from_tower: str, to_tower: str) -> bool:
    """Make a move if valid, return success status."""
    if not _is_valid_move(from_tower, to_tower):
        return False
    
    disk = _TOWERS[from_tower].pop()
    _TOWERS[to_tower].append(disk)
    logger.info(f"🔄 Moved disk {disk} from tower {from_tower} to tower {to_tower}")
    return True

def _is_solved() -> bool:
    """Check if puzzle is solved (all disks on tower C)."""
    return _TOWERS['C'] == [3, 2, 1]

def _get_tower_state() -> Dict[str, List[int]]:
    """Get the current state of all towers."""
    return dict(_TOWERS)

def _move_disk_impl(from_tower: str, to_tower: str) -> Dict[str, Any]:
    """Implementation for moving a disk."""
    # Validate tower names
    if from_tower not in ['A', 'B', 'C'] or to_tower not in ['A', 'B', 'C']:
        return {
            'success': False,
            'message': "Invalid tower names. Use 'A', 'B', or 'C'"
        }
    
    if from_tower == to_tower:
        return {
            'success': False,
            'message': "Cannot move disk to the same tower"
        }
    
    # Check if move is valid
    if not _TOWERS[from_tower]:
        return {
            'success': False,
            'message': f"Tower {from_tower} is empty"
        }
    
    if not _is_valid_move(from_tower, to_tower):
        return {
            'success': False,
            'message': "Invalid move: cannot place larger disk on smaller disk"
        }
    
    # Make the move
    success = _make_move(from_tower, to_tower)
    if success:
        return {
            'success': True,
            'message': f"Successfully moved disk from {from_tower} to {to_tower}"
        }
    else:
        return {
            'success': False,
            'message': f"Failed to move disk from {from_tower} to {to_tower}"
        }

def _check_if_solved_impl() -> Dict[str, Any]:
    """Implementation for checking if puzzle is solved."""
    solved = _is_solved()
    if solved:
        logger.info("🎉 Puzzle solved!")
        return {
            'solved': True,
            'message': "Congratulations! All disks are on tower C."
        }
    else:
        return {
            'solved': False,
            'message': "Puzzle not yet solved. All disks must be on tower C."
        }

def _reset_puzzle_impl() -> Dict[str, str]:
    """Implementation for resetting the puzzle."""
    _reset_towers()
    return {
        'message': "Puzzle reset to initial state. All disks are on tower A."
    }

# --- Async tools ---

async def get_tower_state(ctx) -> Dict[str, List[int]]:
    """Get the current state of all towers.
    
    Returns:
        Dict mapping tower names ('A', 'B', 'C') to lists of disk sizes.
        Disks are ordered from bottom to top (largest to smallest numbers).
    """
    logger.info("🔍 get_tower_state tool called")
    await asyncio.sleep(0.1)  # Simulate async operation
    state = _get_tower_state()
    logger.info(f"📊 Current tower state: {state}")
    return state

async def move_disk(ctx, from_tower: str, to_tower: str) -> Dict[str, Any]:
    """Move a disk from one tower to another.
    
    Args:
        from_tower: Source tower ('A', 'B', or 'C')
        to_tower: Destination tower ('A', 'B', or 'C')
    
    Returns:
        Dict with 'success' (bool) and 'message' (str) keys.
    """
    logger.info(f"🎯 move_disk tool called: {from_tower} → {to_tower}")
    await asyncio.sleep(0.1)  # Simulate async operation
    return _move_disk_impl(from_tower, to_tower)

async def check_if_solved(ctx) -> Dict[str, Any]:
    """Check if the puzzle is solved.
    
    Returns:
        Dict with 'solved' (bool) and 'message' (str) keys.
    """
    logger.info("🎯 check_if_solved tool called")
    await asyncio.sleep(0.1)  # Simulate async operation
    return _check_if_solved_impl()

async def reset_puzzle(ctx) -> Dict[str, str]:
    """Reset the puzzle to initial state.
    
    Returns:
        Dict with 'message' key confirming reset.
    """
    logger.info("🔄 reset_puzzle tool called")
    await asyncio.sleep(0.1)  # Simulate async operation
    return _reset_puzzle_impl()

# --- Sync tools (delegate to async implementations) ---

def get_tower_state_sync() -> Dict[str, List[int]]:
    """Get the current state of all towers (sync version)."""
    logger.info("🔍 get_tower_state_sync tool called")
    return _get_tower_state()

def move_disk_sync(from_tower: str, to_tower: str) -> Dict[str, Any]:
    """Move a disk from one tower to another (sync version)."""
    logger.info(f"🎯 move_disk_sync tool called: {from_tower} → {to_tower}")
    return _move_disk_impl(from_tower, to_tower)

def check_if_solved_sync() -> Dict[str, Any]:
    """Check if the puzzle is solved (sync version)."""
    logger.info("🎯 check_if_solved_sync tool called")
    return _check_if_solved_impl()

def reset_puzzle_sync() -> Dict[str, str]:
    """Reset the puzzle to initial state (sync version)."""
    logger.info("🔄 reset_puzzle_sync tool called")
    return _reset_puzzle_impl()
