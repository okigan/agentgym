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

Generated on: 2025-07-04 20:42:57

## Summary

Total evaluations: 64

## Results by Puzzle



### Fruit_count


| Framework | Model | Run 1 | Run 2 | Success Rate |
|-----------|-------|-------|-------|--------------|
| raw_openai_api | qwen/qwen3-14b | ✅ | ✅ | 100.0% |
| raw_openai_api | gemma-3-12b-it  | ✅ | ✅ | 100.0% |
| pydantic_ai_openai | qwen/qwen3-14b | ❌ | ❌ | 0.0% |
| pydantic_ai_openai | gemma-3-12b-it  | ✅ | ✅ | 100.0% |
| pydantic_ai | mistral.mistral-large-2407-v1:0 | ✅ | ✅ | 100.0% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ❌ | ❌ | 0.0% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ❌ | ❌ | 0.0% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ❌ | ❌ | 0.0% |
| pydantic_ai_enhanced | mistral.mistral-large-2407-v1:0 | ✅ | ✅ | 100.0% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ❌ | ❌ | 0.0% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ❌ | ❌ | 0.0% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ❌ | ❌ | 0.0% |
| strands | mistral.mistral-large-2407-v1:0 | ✅ | ❌ | 50.0% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ✅ | ✅ | 100.0% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ✅ | ✅ | 100.0% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ❌ | ❌ | 0.0% |



### Towers_of_hanoi


| Framework | Model | Run 1 | Run 2 | Success Rate |
|-----------|-------|-------|-------|--------------|
| raw_openai_api | qwen/qwen3-14b | ❌ | ❌ | 0.0% |
| raw_openai_api | gemma-3-12b-it  | ❌ | ❌ | 0.0% |
| pydantic_ai_openai | qwen/qwen3-14b | ❌ | ❌ | 0.0% |
| pydantic_ai_openai | gemma-3-12b-it  | ❌ | ❌ | 0.0% |
| pydantic_ai | mistral.mistral-large-2407-v1:0 | ✅ | ✅ | 100.0% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ❌ | ❌ | 0.0% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ❌ | ✅ | 50.0% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ❌ | ❌ | 0.0% |
| pydantic_ai_enhanced | mistral.mistral-large-2407-v1:0 | ❌ | ❌ | 0.0% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ❌ | ❌ | 0.0% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ❌ | ❌ | 0.0% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ❌ | ❌ | 0.0% |
| strands | mistral.mistral-large-2407-v1:0 | ❌ | ❌ | 0.0% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ❌ | ❌ | 0.0% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ❌ | ❌ | 0.0% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ❌ | ❌ | 0.0% |




## Detailed Results


- **fruit_count** / raw_openai_api / qwen/qwen3-14b / Run 1: ✅

  - Time: 19.86s

- **fruit_count** / raw_openai_api / qwen/qwen3-14b / Run 2: ✅

  - Time: 19.99s

- **fruit_count** / raw_openai_api / gemma-3-12b-it  / Run 1: ✅

  - Time: 11.59s

- **fruit_count** / raw_openai_api / gemma-3-12b-it  / Run 2: ✅

  - Time: 11.15s

- **fruit_count** / pydantic_ai_openai / qwen/qwen3-14b / Run 1: ❌
  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm
  - Time: 0.54s

- **fruit_count** / pydantic_ai_openai / qwen/qwen3-14b / Run 2: ❌
  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm
  - Time: 0.03s

- **fruit_count** / pydantic_ai_openai / gemma-3-12b-it  / Run 1: ✅

  - Time: 11.73s

- **fruit_count** / pydantic_ai_openai / gemma-3-12b-it  / Run 2: ✅

  - Time: 8.18s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 1: ✅

  - Time: 4.11s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 2: ✅

  - Time: 3.78s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 3.14s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.9s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.36s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.21s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.5s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 1.95s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 1: ✅

  - Time: 3.7s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 2: ✅

  - Time: 4.01s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.78s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ❌
  - Error: Total fruit count 0 does not match expected value 55
  - Time: 2.84s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.19s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.15s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.21s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.26s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 1: ✅

  - Time: 6.01s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 2: ❌
  - Error: Invalid agent output: Could not parse response: ```json
{
  "fruit_count_by_color": {
    "orange": 25,
    "apple": 30
  }
}
```

  - Time: 3.58s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ✅

  - Time: 2.53s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ✅

  - Time: 2.66s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ✅

  - Time: 2.49s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ✅

  - Time: 2.49s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ❌
  - Error: Invalid agent output: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
  - Time: 1.33s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌
  - Error: Invalid agent output: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
  - Time: 1.28s

- **towers_of_hanoi** / raw_openai_api / qwen/qwen3-14b / Run 1: ❌
  - Error: No module named 'frameworks.raw_openai_api.towers_of_hanoi'
  - Time: 0.01s

- **towers_of_hanoi** / raw_openai_api / qwen/qwen3-14b / Run 2: ❌
  - Error: No module named 'frameworks.raw_openai_api.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / raw_openai_api / gemma-3-12b-it  / Run 1: ❌
  - Error: No module named 'frameworks.raw_openai_api.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / raw_openai_api / gemma-3-12b-it  / Run 2: ❌
  - Error: No module named 'frameworks.raw_openai_api.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_openai / qwen/qwen3-14b / Run 1: ❌
  - Error: No module named 'frameworks.pydantic_ai_openai.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_openai / qwen/qwen3-14b / Run 2: ❌
  - Error: No module named 'frameworks.pydantic_ai_openai.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_openai / gemma-3-12b-it  / Run 1: ❌
  - Error: No module named 'frameworks.pydantic_ai_openai.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_openai / gemma-3-12b-it  / Run 2: ❌
  - Error: No module named 'frameworks.pydantic_ai_openai.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 1: ✅

  - Time: 20.33s

- **towers_of_hanoi** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 2: ✅

  - Time: 6.78s

- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 6.23s

- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 6.31s

- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.89s

- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ✅

  - Time: 1.92s

- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 5.32s

- **towers_of_hanoi** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 5.93s

- **towers_of_hanoi** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 1: ❌
  - Error: No module named 'frameworks.pydantic_ai_enhanced.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 2: ❌
  - Error: No module named 'frameworks.pydantic_ai_enhanced.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ❌
  - Error: No module named 'frameworks.pydantic_ai_enhanced.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ❌
  - Error: No module named 'frameworks.pydantic_ai_enhanced.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ❌
  - Error: No module named 'frameworks.pydantic_ai_enhanced.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ❌
  - Error: No module named 'frameworks.pydantic_ai_enhanced.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ❌
  - Error: No module named 'frameworks.pydantic_ai_enhanced.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌
  - Error: No module named 'frameworks.pydantic_ai_enhanced.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / strands / mistral.mistral-large-2407-v1:0 / Run 1: ❌
  - Error: No module named 'frameworks.strands.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / strands / mistral.mistral-large-2407-v1:0 / Run 2: ❌
  - Error: No module named 'frameworks.strands.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ❌
  - Error: No module named 'frameworks.strands.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ❌
  - Error: No module named 'frameworks.strands.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ❌
  - Error: No module named 'frameworks.strands.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ❌
  - Error: No module named 'frameworks.strands.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ❌
  - Error: No module named 'frameworks.strands.towers_of_hanoi'
  - Time: 0.0s

- **towers_of_hanoi** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌
  - Error: No module named 'frameworks.strands.towers_of_hanoi'
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
