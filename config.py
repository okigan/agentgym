
import boto3
from functools import lru_cache

# Puzzles to evaluate
PUZZLES = [
    "fruit_count",
    "towers_of_hanoi",
    # Add more puzzles here as they're implemented
]

@lru_cache(maxsize=1)
def get_aws_account_id():
    """Fetch and cache the current AWS account ID using boto3."""
    sts = boto3.client("sts")
    return sts.get_caller_identity()["Account"]


# Framework-model combinations - explicit control over which models each framework supports
FRAMEWORK_MODEL_COMBINATIONS = [
    {
        "frameworks": [
            "raw_openai_api", 
            "pydantic_ai_openai",
        ],
        "models": [
            # Custom OpenAI-compatible endpoints
            {
                "type": "custom_endpoint",
                "name": "qwen/qwen3-14b",
                "base_url": "http://127.0.0.1:1234/v1",
                "model": "qwen/qwen3-14b",
            },
            {
                "type": "custom_endpoint",
                "name": "gemma-3-12b-it ",
                "base_url": "http://127.0.0.1:1234/v1",
                "model": "gemma-3-12b-it"
            },
        ],
    },
    {
        "frameworks": [
            "pydantic_ai", 
            "pydantic_ai_enhanced", 
            "strands"],
        "models": [
            # AWS Bedrock models
            "mistral.mistral-large-2407-v1:0",
            f"arn:aws:bedrock:us-west-2:{get_aws_account_id()}:inference-profile/us.meta.llama3-2-90b-instruct-v1:0",
            f"arn:aws:bedrock:us-west-2:{get_aws_account_id()}:inference-profile/us.meta.llama3-3-70b-instruct-v1:0",
            f"arn:aws:bedrock:us-west-2:{get_aws_account_id()}:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0",
        ],
    },
]

# Number of runs per (puzzle, framework, model) combination
NUM_RUNS = 2

# Timeout settings (in seconds)
TEST_TIMEOUT = 120
