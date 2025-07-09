# AgentGym

A Python-based evaluation framework for testing different AI agent frameworks against various LLM models using structured "puzzles" or tasks.

## Overview

AgentGym allows you to systematically evaluate how different agent frameworks (like Pydantic AI, Strands) perform when using different LLM models (AWS Bedrock hosted models like Llama, Mistral) across various challenges.

## Features

- **Multi-Framework Support**: Test different agent frameworks side-by-side
- **Multi-Model Testing**: Evaluate various LLM models from AWS Bedrock
- **Puzzle-Based Evaluation**: Structured tasks with validation
- **Stochastic Testing**: Multiple runs per combination to account for model variance
- **GitHub Pages Reports**: Markdown output suitable for publishing
- **Observability**: Built-in monitoring and tracing with Logfire

## Setup

### Prerequisites

- Python 3.11+
- AWS credentials configured
- Optional: Logfire account for monitoring

### Installation

```bash
make install
```

### Environment Configuration

Copy the example environment file and configure your settings:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```bash
# AWS Configuration
AWS_PROFILE=your-aws-profile
AWS_REGION=us-west-2

# Logfire Configuration (optional)
# Get your token from https://logfire.pydantic.dev/
LOGFIRE_TOKEN=your-logfire-token

# Development Settings
AGENTGYM_ENVIRONMENT=development
AGENTGYM_SERVICE_NAME=agentgym-evaluation
```

## Run evaluation

```bash
AWS_PROFILE=<your aws profile> make run
```

## Monitoring with Logfire

AgentGym includes built-in observability and monitoring using [Logfire](https://logfire.pydantic.dev/). This provides:

- **Real-time monitoring**: Track evaluation progress and performance
- **Distributed tracing**: See detailed execution flow for each evaluation
- **Error tracking**: Capture and analyze failures
- **Performance metrics**: Monitor execution times and success rates

### Setting up Logfire

1. Create a free account at [https://logfire.pydantic.dev/](https://logfire.pydantic.dev/)
2. Create a new project
3. Copy your project token
4. Set the `LOGFIRE_TOKEN` environment variable

```bash
export LOGFIRE_TOKEN=your-logfire-token
```

Or add it to your `.env` file.

### Logfire Features

- **Evaluation tracking**: Each evaluation run is traced with spans
- **Performance monitoring**: Execution times and success rates
- **Error analysis**: Detailed error messages and stack traces
- **Resource monitoring**: Track AWS Bedrock API calls
- **Console output**: Local development feedback

If no Logfire token is provided, the system will still work but only provide console logging.


<!-- INCLUDE reports/latest.md -->
# AgentGym Evaluation Results

Generated on: 2025-07-08 22:31:05

## Summary

Total evaluations: 96

## Results by Puzzle

### Fruit_count

| Framework | Model| Run 1| Run 2| Run 3| Success Rate | Prompt Tokens | Prediction Tokens | Avg Time (s) |
|-----------|-------|-------|-------|-------|--------------|--------------|------------------|--------------|
| raw_openai_api | qwen/qwen3-14b| ✅| ✅| ✅| 100.0% | 203.0 | 138.66666666666666 | 20.22 |
| raw_openai_api | gemma-3-12b-it | ✅| ✅| ✅| 100.0% | 532.0 | 23.0 | 14.14 |
| pydantic_ai_openai | qwen/qwen3-14b| ❌| ❌| ❌| 0.0% | 0.0 | 0.0 | 0.14 |
| pydantic_ai_openai | gemma-3-12b-it | ✅| ✅| ✅| 100.0% | 0.0 | 0.0 | 9.17 |
| pydantic_ai | mistral.mistral-large-2407-v1:0| ✅| ✅| ✅| 100.0% | 0.0 | 0.0 | 31.55 |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0| ✅| ✅| ✅| 100.0% | 0.0 | 0.0 | 3.6 |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0| ✅| ✅| ✅| 100.0% | 0.0 | 0.0 | 2.74 |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0| ✅| ✅| ✅| 100.0% | 0.0 | 0.0 | 2.7 |
| pydantic_ai_enhanced | mistral.mistral-large-2407-v1:0| ✅| ✅| ✅| 100.0% | 0.0 | 0.0 | 3.74 |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0| ❌| ❌| ❌| 0.0% | 0.0 | 0.0 | 2.9 |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0| ❌| ❌| ❌| 0.0% | 0.0 | 0.0 | 2.32 |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0| ❌| ❌| ❌| 0.0% | 0.0 | 0.0 | 2.35 |
| strands | mistral.mistral-large-2407-v1:0| ✅| ❌| ✅| 66.7% | 0.0 | 0.0 | 6.67 |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0| ✅| ✅| ✅| 100.0% | 0.0 | 0.0 | 4.7 |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0| ❌| ❌| ❌| 0.0% | 0.0 | 0.0 | 4.06 |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0| ❌| ❌| ❌| 0.0% | 0.0 | 0.0 | 2.5 |


### Towers_of_hanoi

| Framework | Model| Run 1| Run 2| Run 3| Success Rate | Prompt Tokens | Prediction Tokens | Avg Time (s) |
|-----------|-------|-------|-------|-------|--------------|--------------|------------------|--------------|
| raw_openai_api | qwen/qwen3-14b| ✅| ✅| ✅| 100.0% | 3758.0 | 3262.0 | 1.93 |
| raw_openai_api | gemma-3-12b-it | ❌| ❌| ❌| 0.0% | 38639.0 | 968.0 | 29.37 |
| pydantic_ai_openai | qwen/qwen3-14b| ❌| ❌| ❌| 0.0% | 0.0 | 0.0 | 0.18 |
| pydantic_ai_openai | gemma-3-12b-it | ❌| ❌| ❌| 0.0% | 0.0 | 0.0 | 79.35 |
| pydantic_ai | mistral.mistral-large-2407-v1:0| ✅| ✅| ✅| 100.0% | 0.0 | 0.0 | 34.17 |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0| ✅| ❌| ❌| 33.3% | 0.0 | 0.0 | 37.95 |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0| ❌| ❌| ❌| 0.0% | 0.0 | 0.0 | 3.45 |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0| ❌| ❌| ❌| 0.0% | 0.0 | 0.0 | 15.63 |
| pydantic_ai_enhanced | mistral.mistral-large-2407-v1:0| ⚪| ⚪| ⚪| N/A% | 0.0 | 0.0 | 0.0 |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0| ⚪| ⚪| ⚪| N/A% | 0.0 | 0.0 | 0.0 |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0| ⚪| ⚪| ⚪| N/A% | 0.0 | 0.0 | 0.0 |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0| ⚪| ⚪| ⚪| N/A% | 0.0 | 0.0 | 0.0 |
| strands | mistral.mistral-large-2407-v1:0| ⚪| ⚪| ⚪| N/A% | 0.0 | 0.0 | 0.0 |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0| ⚪| ⚪| ⚪| N/A% | 0.0 | 0.0 | 0.0 |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0| ⚪| ⚪| ⚪| N/A% | 0.0 | 0.0 | 0.0 |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0| ⚪| ⚪| ⚪| N/A% | 0.0 | 0.0 | 0.0 |


## Detailed Results
- **fruit_count** / raw_openai_api / qwen/qwen3-14b / Run 1: ✅  - Time: 19.94s
- **fruit_count** / raw_openai_api / qwen/qwen3-14b / Run 2: ✅  - Time: 22.14s
- **fruit_count** / raw_openai_api / qwen/qwen3-14b / Run 3: ✅  - Time: 18.57s
- **fruit_count** / raw_openai_api / gemma-3-12b-it  / Run 1: ✅  - Time: 19.88s
- **fruit_count** / raw_openai_api / gemma-3-12b-it  / Run 2: ✅  - Time: 11.31s
- **fruit_count** / raw_openai_api / gemma-3-12b-it  / Run 3: ✅  - Time: 11.23s
- **fruit_count** / pydantic_ai_openai / qwen/qwen3-14b / Run 1: ❌  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm  - Time: 0.36s
- **fruit_count** / pydantic_ai_openai / qwen/qwen3-14b / Run 2: ❌  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm  - Time: 0.03s
- **fruit_count** / pydantic_ai_openai / qwen/qwen3-14b / Run 3: ❌  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm  - Time: 0.03s
- **fruit_count** / pydantic_ai_openai / gemma-3-12b-it  / Run 1: ✅  - Time: 11.51s
- **fruit_count** / pydantic_ai_openai / gemma-3-12b-it  / Run 2: ✅  - Time: 7.98s
- **fruit_count** / pydantic_ai_openai / gemma-3-12b-it  / Run 3: ✅  - Time: 8.01s
- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 1: ✅  - Time: 4.62s
- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 2: ✅  - Time: 3.89s
- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 3: ✅  - Time: 86.14s
- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ✅  - Time: 4.27s
- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ✅  - Time: 3.49s
- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ✅  - Time: 3.05s
- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ✅  - Time: 2.69s
- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ✅  - Time: 2.81s
- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ✅  - Time: 2.71s
- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ✅  - Time: 2.87s
- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ✅  - Time: 2.41s
- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ✅  - Time: 2.83s
- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 1: ✅  - Time: 3.72s
- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 2: ✅  - Time: 3.67s
- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 3: ✅  - Time: 3.84s
- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ❌  - Error: Exceeded maximum retries (1) for result validation  - Time: 2.88s
- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ❌  - Error: fruit_count_by_color must match {'orange': 25, 'apple': 30}, got: {}  - Time: 2.83s
- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ❌  - Error: fruit_count_by_color must match {'orange': 25, 'apple': 30}, got: {}  - Time: 2.98s
- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ❌  - Error: Exceeded maximum retries (1) for result validation  - Time: 2.57s
- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ❌  - Error: Exceeded maximum retries (1) for result validation  - Time: 2.17s
- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ❌  - Error: Exceeded maximum retries (1) for result validation  - Time: 2.22s
- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ❌  - Error: Exceeded maximum retries (1) for result validation  - Time: 2.25s
- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌  - Error: Exceeded maximum retries (1) for result validation  - Time: 2.13s
- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ❌  - Error: Exceeded maximum retries (1) for result validation  - Time: 2.68s
- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 1: ✅  - Time: 8.59s
- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 2: ❌  - Error: No valid tool use or tool use input was found in the Bedrock response.  - Time: 6.06s
- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 3: ✅  - Time: 5.37s
- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ✅  - Time: 4.66s
- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ✅  - Time: 4.65s
- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ✅  - Time: 4.8s
- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ❌  - Error: fruit_count_by_color must match {'orange': 25, 'apple': 30}, got: {'orange': 10, 'apple': 20}  - Time: 4.01s
- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ❌  - Error: fruit_count_by_color must match {'orange': 25, 'apple': 30}, got: {'orange': 10, 'apple': 20}  - Time: 4.06s
- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ❌  - Error: fruit_count_by_color must match {'orange': 25, 'apple': 30}, got: {'orange': 10, 'apple': 20}  - Time: 4.11s
- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ❌  - Error: 2 validation errors for FruitCountResponse
fruit_count_by_color.orange
  Field required [type=missing, input_value={'type': 'dict', 'value':...ange': 10, 'apple': 20}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.11/v/missing
fruit_count_by_color.apple
  Field required [type=missing, input_value={'type': 'dict', 'value':...ange': 10, 'apple': 20}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.11/v/missing  - Time: 2.53s
- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌  - Error: No valid tool use or tool use input was found in the Bedrock response.  - Time: 2.62s
- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ❌  - Error: 2 validation errors for FruitCountResponse
fruit_count_by_color.orange
  Field required [type=missing, input_value={'type': 'dict', 'value':...f_apples', 'args': []}}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.11/v/missing
fruit_count_by_color.apple
  Field required [type=missing, input_value={'type': 'dict', 'value':...f_apples', 'args': []}}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.11/v/missing  - Time: 2.35s
- **towers_of_hanoi** / raw_openai_api / qwen/qwen3-14b / Run 1: ✅  - Time: 1.94s
- **towers_of_hanoi** / raw_openai_api / qwen/qwen3-14b / Run 2: ✅  - Time: 1.92s
- **towers_of_hanoi** / raw_openai_api / qwen/qwen3-14b / Run 3: ✅  - Time: 1.92s
- **towers_of_hanoi** / raw_openai_api / gemma-3-12b-it  / Run 1: ❌  - Error: Puzzle was not solved  - Time: 83.31s
- **towers_of_hanoi** / raw_openai_api / gemma-3-12b-it  / Run 2: ❌  - Error: Puzzle was not solved  - Time: 2.4s
- **towers_of_hanoi** / raw_openai_api / gemma-3-12b-it  / Run 3: ❌  - Error: Puzzle was not solved  - Time: 2.4s
- **towers_of_hanoi** / pydantic_ai_openai / qwen/qwen3-14b / Run 1: ❌  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm  - Time: 0.2s
- **towers_of_hanoi** / pydantic_ai_openai / qwen/qwen3-14b / Run 2: ❌  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm  - Time: 0.17s
- **towers_of_hanoi** / pydantic_ai_openai / qwen/qwen3-14b / Run 3: ❌  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm  - Time: 0.16s
- **towers_of_hanoi** / pydantic_ai_openai / gemma-3-12b-it  / Run 1: ❌  - Error: Final state incorrect. Tower Z should have [3, 2, 1], got None  - Time: 40.3s
- **towers_of_hanoi** / pydantic_ai_openai / gemma-3-12b-it  / Run 2: ❌  - Error: The next request would exceed the request_limit of 50  - Time: 164.56s
- **towers_of_hanoi** / pydantic_ai_openai / gemma-3-12b-it  / Run 3: ❌  - Error: Final state incorrect. Tower Z should have [3, 2, 1], got None  - Time: 33.18s
- **towers_of_hanoi** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 1: ✅  - Time: 28.73s
- **towers_of_hanoi** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 2: ✅  - Time: 21.14s
- **towers_of_hanoi** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 3: ✅  - Time: 52.64s
- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ✅  - Time: 17.4s
- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ❌  - Error: The next request would exceed the request_limit of 50  - Time: 47.34s
- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ❌  - Error: The next request would exceed the request_limit of 50  - Time: 49.09s
- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ❌  - Error: Exceeded maximum retries (1) for result validation  - Time: 4.83s
- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ❌  - Error: Exceeded maximum retries (1) for result validation  - Time: 3.19s
- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ❌  - Error: Exceeded maximum retries (1) for result validation  - Time: 2.33s
- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ❌  - Error: Final state incorrect. Tower Z should have [3, 2, 1], got None  - Time: 4.74s
- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌  - Error: The next request would exceed the request_limit of 50  - Time: 37.74s
- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ❌  - Error: Final state incorrect. Tower Z should have [3, 2, 1], got None  - Time: 4.42s
- **towers_of_hanoi** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 1: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 2: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 3: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / strands / mistral.mistral-large-2407-v1:0 / Run 1: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / strands / mistral.mistral-large-2407-v1:0 / Run 2: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / strands / mistral.mistral-large-2407-v1:0 / Run 3: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s
- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ⚪  - Error: No implementation for towers_of_hanoi puzzle  - Time: 0.0s

---
*Generated by AgentGym evaluation framework*
<!-- /INCLUDE -->

## Dependencies

- **pydantic-ai**: Agent framework
- **strands**: Alternative agent framework  
- **boto3**: AWS Bedrock integration
- **pytest**: Testing framework
- **jinja2**: Report templating
- **logfire**: Observability and monitoring

## AWS Bedrock Models

Currently supports:
- Mistral Large
- Meta Llama 3.2/3.3/4 variants
- Custom model ARNs

## Contributing

1. Add new puzzles to test different capabilities
2. Implement support for additional agent frameworks
3. Enhance reporting and visualization
4. Add more sophisticated validation logic

## License

MIT License
