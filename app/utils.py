"""Shared utilities for AgentGym."""

import os
import logging


def setup_aws_environment(profile: str | None = None):
    """Set up AWS environment variable for AWS_PROFILE only."""
    pass

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
