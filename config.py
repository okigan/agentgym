
import boto3
from functools import lru_cache

# Puzzles to evaluate
PUZZLES = [
    "fruit_count",
    # Add more puzzles here as they're implemented
]

# Frameworks to test
FRAMEWORKS = [
    "pydantic_ai",
    "pydantic_ai_enhanced",
    "strands",
]

@lru_cache(maxsize=1)
def get_aws_account_id():
    """Fetch and cache the current AWS account ID using boto3."""
    sts = boto3.client("sts")
    return sts.get_caller_identity()["Account"]

ACCOUNT_ID = get_aws_account_id()

# AWS Bedrock models to test
MODELS = [
    "mistral.mistral-large-2407-v1:0",
    f"arn:aws:bedrock:us-west-2:{ACCOUNT_ID}:inference-profile/us.meta.llama3-2-90b-instruct-v1:0",
    f"arn:aws:bedrock:us-west-2:{ACCOUNT_ID}:inference-profile/us.meta.llama3-3-70b-instruct-v1:0",
    f"arn:aws:bedrock:us-west-2:{ACCOUNT_ID}:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0",
]

# Number of runs per (puzzle, framework, model) combination
NUM_RUNS = 10

# Timeout settings (in seconds)
TEST_TIMEOUT = 120
