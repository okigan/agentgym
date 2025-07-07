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

Generated on: 2025-07-07 14:04:40

## Summary

Total evaluations: 96

## Results by Puzzle



### Fruit_count


| Framework | Model | Run 1 | Run 2 | Run 3 | Success Rate |
|-----------|-------|-------|-------|-------|--------------|
| raw_openai_api | qwen/qwen3-14b | ✅ | ✅ | ✅ | 100.0% |
| raw_openai_api | gemma-3-12b-it  | ✅ | ✅ | ✅ | 100.0% |
| pydantic_ai_openai | qwen/qwen3-14b | ❌ | ❌ | ❌ | 0.0% |
| pydantic_ai_openai | gemma-3-12b-it  | ✅ | ✅ | ✅ | 100.0% |
| pydantic_ai | mistral.mistral-large-2407-v1:0 | ✅ | ✅ | ✅ | 100.0% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ✅ | ✅ | ✅ | 100.0% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ✅ | ✅ | ✅ | 100.0% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ✅ | ✅ | ✅ | 100.0% |
| pydantic_ai_enhanced | mistral.mistral-large-2407-v1:0 | ✅ | ✅ | ✅ | 100.0% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ❌ | ❌ | ❌ | 0.0% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ❌ | ❌ | ❌ | 0.0% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ❌ | ❌ | ❌ | 0.0% |
| strands | mistral.mistral-large-2407-v1:0 | ❌ | ✅ | ✅ | 66.7% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ✅ | ✅ | ✅ | 100.0% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ❌ | ❌ | ❌ | 0.0% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ❌ | ❌ | ❌ | 0.0% |



### Towers_of_hanoi


| Framework | Model | Run 1 | Run 2 | Run 3 | Success Rate |
|-----------|-------|-------|-------|-------|--------------|
| raw_openai_api | qwen/qwen3-14b | ✅ | ✅ | ✅ | 100.0% |
| raw_openai_api | gemma-3-12b-it  | ❌ | ✅ | ✅ | 66.7% |
| pydantic_ai_openai | qwen/qwen3-14b | ❌ | ❌ | ❌ | 0.0% |
| pydantic_ai_openai | gemma-3-12b-it  | ✅ | ✅ | ✅ | 100.0% |
| pydantic_ai | mistral.mistral-large-2407-v1:0 | ✅ | ✅ | ✅ | 100.0% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ✅ | ✅ | ❌ | 66.7% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ❌ | ❌ | ❌ | 0.0% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ✅ | ❌ | ✅ | 66.7% |
| pydantic_ai_enhanced | mistral.mistral-large-2407-v1:0 | ⚪ | ⚪ | ⚪ | N/A% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ⚪ | ⚪ | ⚪ | N/A% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ⚪ | ⚪ | ⚪ | N/A% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ⚪ | ⚪ | ⚪ | N/A% |
| strands | mistral.mistral-large-2407-v1:0 | ⚪ | ⚪ | ⚪ | N/A% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ⚪ | ⚪ | ⚪ | N/A% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ⚪ | ⚪ | ⚪ | N/A% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ⚪ | ⚪ | ⚪ | N/A% |




## Detailed Results


- **fruit_count** / raw_openai_api / qwen/qwen3-14b / Run 1: ✅

  - Time: 21.05s

- **fruit_count** / raw_openai_api / qwen/qwen3-14b / Run 2: ✅

  - Time: 20.72s

- **fruit_count** / raw_openai_api / qwen/qwen3-14b / Run 3: ✅

  - Time: 18.74s

- **fruit_count** / raw_openai_api / gemma-3-12b-it  / Run 1: ✅

  - Time: 11.79s

- **fruit_count** / raw_openai_api / gemma-3-12b-it  / Run 2: ✅

  - Time: 11.24s

- **fruit_count** / raw_openai_api / gemma-3-12b-it  / Run 3: ✅

  - Time: 11.28s

- **fruit_count** / pydantic_ai_openai / qwen/qwen3-14b / Run 1: ❌
  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm
  - Time: 0.37s

- **fruit_count** / pydantic_ai_openai / qwen/qwen3-14b / Run 2: ❌
  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm
  - Time: 0.03s

- **fruit_count** / pydantic_ai_openai / qwen/qwen3-14b / Run 3: ❌
  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm
  - Time: 0.03s

- **fruit_count** / pydantic_ai_openai / gemma-3-12b-it  / Run 1: ✅

  - Time: 11.72s

- **fruit_count** / pydantic_ai_openai / gemma-3-12b-it  / Run 2: ✅

  - Time: 8.15s

- **fruit_count** / pydantic_ai_openai / gemma-3-12b-it  / Run 3: ✅

  - Time: 8.01s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 1: ✅

  - Time: 4.59s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 2: ✅

  - Time: 6.45s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 3: ✅

  - Time: 5.66s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ✅

  - Time: 3.01s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ✅

  - Time: 2.81s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ✅

  - Time: 2.99s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ✅

  - Time: 2.64s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ✅

  - Time: 2.54s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ✅

  - Time: 2.58s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ✅

  - Time: 2.23s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ✅

  - Time: 2.13s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ✅

  - Time: 2.43s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 1: ✅

  - Time: 3.6s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 2: ✅

  - Time: 3.7s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 3: ✅

  - Time: 3.95s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ❌
  - Error: fruit_count_by_color must match {'orange': 25, 'apple': 30}, got: {}
  - Time: 2.9s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.83s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.95s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.34s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.32s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.21s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.0s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.32s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 1.86s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 1: ❌
  - Error: No valid tool use or tool use input was found in the Bedrock response.
  - Time: 6.41s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 2: ✅

  - Time: 5.7s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 3: ✅

  - Time: 5.94s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ✅

  - Time: 4.57s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ✅

  - Time: 4.41s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ✅

  - Time: 4.42s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ❌
  - Error: fruit_count_by_color must match {'orange': 25, 'apple': 30}, got: {'orange': 10, 'apple': 20}
  - Time: 4.05s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ❌
  - Error: fruit_count_by_color must match {'orange': 25, 'apple': 30}, got: {'orange': 10, 'apple': 20}
  - Time: 3.9s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ❌
  - Error: fruit_count_by_color must match {'orange': 25, 'apple': 30}, got: {'orange': 10, 'apple': 20}
  - Time: 4.15s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ❌
  - Error: 2 validation errors for FruitCountResponse
fruit_count_by_color.orange
  Field required [type=missing, input_value={'type': 'dict', 'value':...ange': 10, 'apple': 20}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.11/v/missing
fruit_count_by_color.apple
  Field required [type=missing, input_value={'type': 'dict', 'value':...ange': 10, 'apple': 20}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.11/v/missing
  - Time: 2.18s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌
  - Error: 2 validation errors for FruitCountResponse
fruit_count_by_color.orange
  Field required [type=missing, input_value={'type': 'dict', 'value':...ange': 10, 'apple': 20}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.11/v/missing
fruit_count_by_color.apple
  Field required [type=missing, input_value={'type': 'dict', 'value':...ange': 10, 'apple': 20}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.11/v/missing
  - Time: 2.17s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ❌
  - Error: 2 validation errors for FruitCountResponse
fruit_count_by_color.orange
  Field required [type=missing, input_value={'type': 'dict', 'value':...ange': 10, 'apple': 20}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.11/v/missing
fruit_count_by_color.apple
  Field required [type=missing, input_value={'type': 'dict', 'value':...ange': 10, 'apple': 20}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.11/v/missing
  - Time: 2.14s

- **towers_of_hanoi** / raw_openai_api / qwen/qwen3-14b / Run 1: ✅

  - Time: 68.36s

- **towers_of_hanoi** / raw_openai_api / qwen/qwen3-14b / Run 2: ✅

  - Time: 54.5s

- **towers_of_hanoi** / raw_openai_api / qwen/qwen3-14b / Run 3: ✅

  - Time: 57.92s

- **towers_of_hanoi** / raw_openai_api / gemma-3-12b-it  / Run 1: ❌
  - Error: Puzzle was not solved
  - Time: 122.11s

- **towers_of_hanoi** / raw_openai_api / gemma-3-12b-it  / Run 2: ✅

  - Time: 64.84s

- **towers_of_hanoi** / raw_openai_api / gemma-3-12b-it  / Run 3: ✅

  - Time: 62.81s

- **towers_of_hanoi** / pydantic_ai_openai / qwen/qwen3-14b / Run 1: ❌
  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm
  - Time: 0.11s

- **towers_of_hanoi** / pydantic_ai_openai / qwen/qwen3-14b / Run 2: ❌
  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm
  - Time: 0.04s

- **towers_of_hanoi** / pydantic_ai_openai / qwen/qwen3-14b / Run 3: ❌
  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm
  - Time: 0.03s

- **towers_of_hanoi** / pydantic_ai_openai / gemma-3-12b-it  / Run 1: ✅

  - Time: 42.6s

- **towers_of_hanoi** / pydantic_ai_openai / gemma-3-12b-it  / Run 2: ✅

  - Time: 33.46s

- **towers_of_hanoi** / pydantic_ai_openai / gemma-3-12b-it  / Run 3: ✅

  - Time: 36.68s

- **towers_of_hanoi** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 1: ✅

  - Time: 18.83s

- **towers_of_hanoi** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 2: ✅

  - Time: 21.92s

- **towers_of_hanoi** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 3: ✅

  - Time: 23.48s

- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ✅

  - Time: 17.79s

- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ✅

  - Time: 14.83s

- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ❌
  - Error: The next request would exceed the request_limit of 50
  - Time: 45.25s

- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 3.06s

- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.91s

- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.98s

- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ✅

  - Time: 4.28s

- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 5.61s

- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ✅

  - Time: 8.51s

- **towers_of_hanoi** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 1: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 2: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 3: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / strands / mistral.mistral-large-2407-v1:0 / Run 1: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / strands / mistral.mistral-large-2407-v1:0 / Run 2: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / strands / mistral.mistral-large-2407-v1:0 / Run 3: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s

- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ⚪
  - Error: No implementation for towers_of_hanoi puzzle
  - Time: 0.0s


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
