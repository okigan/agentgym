"""Shared utilities for AgentGym."""

import os
import logging
from typing import Optional
from typing import TypedDict, Any
import hashlib
import json
import diskcache

import logfire


# Helper to aggregate OpenAI usage dicts (prompt_tokens, completion_tokens, total_tokens)
def aggregate_usages(usage_list):
    agg = {}
    for k in ("prompt_tokens", "completion_tokens", "total_tokens"):
        agg[k] = sum(u.get(k, 0) for u in usage_list if u)
    # Optionally, include the full list for debugging
    agg["calls"] = usage_list
    return agg

# Shared result type for AgentGym agent frameworks
class AgentGymAgentResult(TypedDict):
    result: Any  # Use Any to avoid circular import issues; frameworks should document expected type
    usage: dict[str, Any]



def setup_aws_environment(profile: str | None = None):
    """Set up AWS environment variable for AWS_PROFILE only."""
    pass


def setup_logfire(
    token: Optional[str] = None,
    project_name: str = "agentgym",
    service_name: str = "agentgym-evaluation",
    environment: str = "development"
) -> None:
    """Configure Logfire for observability and monitoring."""
    
    # Use token from environment if not provided
    if token is None:
        token = os.getenv("LOGFIRE_TOKEN")
    
    # Only configure if token is available
    if token:
        # Configure Logfire
        logfire.configure(
            token=token,
            service_name=service_name,
            # Enable console output
            console=logfire.ConsoleOptions(colors='auto', verbose=True)
        )
        
        # Log initialization
        logfire.info("Logfire monitoring initialized", 
                    service=service_name, 
                    environment=environment)
    else:
        # Just configure basic console logging if no token
        logfire.configure(
            console=logfire.ConsoleOptions(colors='auto', verbose=False)
        )
        logfire.info("Logfire configured for local development (no token provided)")

    logfire.instrument_pydantic_ai()
    logfire.instrument_httpx(capture_all=True)
    logfire.instrument_aiohttp_client(capture_all=True)


def setup_logging(level: int = logging.INFO):
    """Configure logging for the application."""
    # Remove all handlers associated with the root logger to ensure correct line numbers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s(%(lineno)d) - %(levelname)s - %(message)s",
        force=True
    )
    
    # Configure specific loggers
    pydantic_logger = logging.getLogger("pydantic_ai")
    pydantic_logger.setLevel(logging.DEBUG)
    
    boto_logger = logging.getLogger("botocore")
    boto_logger.setLevel(logging.INFO)  # Keep boto3 at INFO to avoid noise
    
    return logging.getLogger(__name__)


_global_cache = diskcache.Cache('./.cache')

def _make_cache_key_generic(func, args, kwargs):
    # Canonicalize all args/kwargs to a stable JSON string, then hash
    key_data = {
        "func_module": func.__module__,
        "func_name": func.__name__,
        "args": args,
        "kwargs": kwargs,
    }
    key_str = json.dumps(key_data, sort_keys=True, default=str, separators=(",", ":"))
    return hashlib.sha256(key_str.encode()).hexdigest()
    
def disk_cache_async(func):
    """Generic async disk cache decorator for any function signature."""
    async def wrapper(*args, **kwargs):
        key = _make_cache_key_generic(func, args, kwargs)
        if key in _global_cache:
            return _global_cache[key]
        result = await func(*args, **kwargs)
        _global_cache[key] = result
        return result
    return wrapper