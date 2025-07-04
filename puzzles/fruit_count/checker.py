# Add FruitCountResponse definition here (moved from solver.py)

import logging
from typing import Any, Dict
from pydantic import BaseModel, ValidationError


class FruitCountResponse(BaseModel):
    """Response from the fruit counting agent."""
    fruit_count_by_color: Dict[str, int]
"""Checker for the fruit counting puzzle."""

# If needed, define FruitCountResponse here or import from a shared location

logger = logging.getLogger(__name__)


def check(result: Any) -> None:
    """Validate the agent's output for the fruit counting puzzle.
    Raises AssertionError if the result is not valid.
    """
    logger.info(f"🔎 Checking agent result: {result}")
    # Try to coerce result to FruitCountResponse
    try:
        if isinstance(result, FruitCountResponse):
            response = result
        elif isinstance(result, dict):
            response = FruitCountResponse(**result)
        elif hasattr(result, 'output'):
            response = result.output
        else:
            import json
            import re
            result_text = str(result)
            json_match = re.search(r'\{.*\}', result_text)
            if json_match:
                parsed_result = json.loads(json_match.group())
                if 'fruit_count_by_color' in parsed_result:
                    response = FruitCountResponse(**parsed_result)
                else:
                    raise AssertionError(f"Missing fruit_count_by_color in {parsed_result}")
            else:
                raise AssertionError(f"Could not parse response: {result_text}")
    except (ValidationError, Exception) as e:
        raise AssertionError(f"Invalid agent output: {e}")

    # Validate fruit_count_by_color structure and required keys/values
    expected = {'orange': 25, 'apple': 30}
    if response.fruit_count_by_color != expected:
        raise AssertionError(f"fruit_count_by_color must match {expected}, got: {response.fruit_count_by_color}")
    logger.info(f"📊 Fruit breakdown: {response.fruit_count_by_color}")
    logger.info("✅ Fruit count puzzle passed check")
