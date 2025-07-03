"""Tools for the fruit counting puzzle."""

import asyncio
import logging

logger = logging.getLogger(__name__)



# --- Shared logic for fruit counts ---
_FRUIT_COUNTS = {
    "orange": 25,
    "apple": 30,
}

def _get_fruit_count(fruit: str) -> int:
    count = _FRUIT_COUNTS[fruit]
    logger.info(f"Returning {fruit} count: {count}")
    return count

# --- Async tools ---
async def get_count_of_oranges(ctx) -> int:
    """Get the current count of oranges in inventory."""
    logger.info("🍊 get_count_of_oranges tool called")
    await asyncio.sleep(0.1)
    return _get_fruit_count("orange")

async def get_count_of_apples(ctx) -> int:
    """Get the current count of apples in inventory."""
    logger.info("🍎 get_count_of_apples tool called")
    await asyncio.sleep(0.1)
    return _get_fruit_count("apple")

# --- Sync tools ---
def get_count_of_oranges_sync() -> int:
    """Get the current count of oranges in inventory (sync version)."""
    logger.info("🍊 get_count_of_oranges_sync tool called")
    return _get_fruit_count("orange")

def get_count_of_apples_sync() -> int:
    """Get the current count of apples in inventory (sync version)."""
    logger.info("🍎 get_count_of_apples_sync tool called")
    return _get_fruit_count("apple")
