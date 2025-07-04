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

## Run evaluation

```
make install
AWS_PROFILE=<your aws profile> make run
```


<!-- INCLUDE reports/latest.md -->
# AgentGym Evaluation Results

Generated on: 2025-07-04 00:29:02

## Summary

Total evaluations: 80

## Results by Puzzle



### Fruit_count


| Framework | Model | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Success Rate |
|-----------|-------|-------|-------|-------|-------|-------|--------------|
| raw_openai_api | qwen/qwen3-14b | ✅ | ✅ | ✅ | ✅ | ✅ | 100.0% |
| raw_openai_api | gemma-3-12b-it  | ✅ | ✅ | ✅ | ✅ | ✅ | 100.0% |
| pydantic_ai_openai | qwen/qwen3-14b | ❌ | ❌ | ❌ | ❌ | ❌ | 0.0% |
| pydantic_ai_openai | gemma-3-12b-it  | ✅ | ✅ | ✅ | ✅ | ✅ | 100.0% |
| pydantic_ai | mistral.mistral-large-2407-v1:0 | ✅ | ✅ | ✅ | ✅ | ✅ | 100.0% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ❌ | ❌ | ❌ | ❌ | ❌ | 0.0% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ❌ | ❌ | ❌ | ❌ | ❌ | 0.0% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ❌ | ❌ | ❌ | ❌ | ❌ | 0.0% |
| pydantic_ai_enhanced | mistral.mistral-large-2407-v1:0 | ✅ | ✅ | ✅ | ✅ | ✅ | 100.0% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ❌ | ❌ | ❌ | ❌ | ❌ | 0.0% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ❌ | ❌ | ❌ | ❌ | ❌ | 0.0% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ❌ | ❌ | ❌ | ❌ | ❌ | 0.0% |
| strands | mistral.mistral-large-2407-v1:0 | ✅ | ❌ | ✅ | ✅ | ✅ | 80.0% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ✅ | ✅ | ✅ | ✅ | ✅ | 100.0% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ✅ | ✅ | ✅ | ✅ | ✅ | 100.0% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ❌ | ❌ | ❌ | ❌ | ❌ | 0.0% |




## Detailed Results


- **fruit_count** / raw_openai_api / qwen/qwen3-14b / Run 1: ✅

  - Time: 20.29s

- **fruit_count** / raw_openai_api / qwen/qwen3-14b / Run 2: ✅

  - Time: 18.75s

- **fruit_count** / raw_openai_api / qwen/qwen3-14b / Run 3: ✅

  - Time: 20.61s

- **fruit_count** / raw_openai_api / qwen/qwen3-14b / Run 4: ✅

  - Time: 19.46s

- **fruit_count** / raw_openai_api / qwen/qwen3-14b / Run 5: ✅

  - Time: 20.27s

- **fruit_count** / raw_openai_api / gemma-3-12b-it  / Run 1: ✅

  - Time: 11.67s

- **fruit_count** / raw_openai_api / gemma-3-12b-it  / Run 2: ✅

  - Time: 11.28s

- **fruit_count** / raw_openai_api / gemma-3-12b-it  / Run 3: ✅

  - Time: 11.32s

- **fruit_count** / raw_openai_api / gemma-3-12b-it  / Run 4: ✅

  - Time: 11.17s

- **fruit_count** / raw_openai_api / gemma-3-12b-it  / Run 5: ✅

  - Time: 11.29s

- **fruit_count** / pydantic_ai_openai / qwen/qwen3-14b / Run 1: ❌
  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm
  - Time: 0.52s

- **fruit_count** / pydantic_ai_openai / qwen/qwen3-14b / Run 2: ❌
  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm
  - Time: 0.03s

- **fruit_count** / pydantic_ai_openai / qwen/qwen3-14b / Run 3: ❌
  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm
  - Time: 0.03s

- **fruit_count** / pydantic_ai_openai / qwen/qwen3-14b / Run 4: ❌
  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm
  - Time: 0.04s

- **fruit_count** / pydantic_ai_openai / qwen/qwen3-14b / Run 5: ❌
  - Error: status_code: 400, model_name: qwen/qwen3-14b, body: Cannot set structured output to force tools for engine type: mlx-llm
  - Time: 0.02s

- **fruit_count** / pydantic_ai_openai / gemma-3-12b-it  / Run 1: ✅

  - Time: 11.54s

- **fruit_count** / pydantic_ai_openai / gemma-3-12b-it  / Run 2: ✅

  - Time: 8.01s

- **fruit_count** / pydantic_ai_openai / gemma-3-12b-it  / Run 3: ✅

  - Time: 7.99s

- **fruit_count** / pydantic_ai_openai / gemma-3-12b-it  / Run 4: ✅

  - Time: 8.1s

- **fruit_count** / pydantic_ai_openai / gemma-3-12b-it  / Run 5: ✅

  - Time: 7.97s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 1: ✅

  - Time: 4.07s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 2: ✅

  - Time: 3.93s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 3: ✅

  - Time: 3.74s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 4: ✅

  - Time: 3.61s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 5: ✅

  - Time: 3.76s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.74s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.9s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 3.05s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 4: ❌
  - Error: Total fruit count 0 does not match expected value 55
  - Time: 2.9s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 5: ❌
  - Error: Total fruit count 0 does not match expected value 55
  - Time: 2.75s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.26s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.74s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.3s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 4: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.23s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 5: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.33s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.4s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 1.91s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.09s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 4: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.03s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 5: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.18s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 1: ✅

  - Time: 3.57s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 2: ✅

  - Time: 3.73s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 3: ✅

  - Time: 4.15s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 4: ✅

  - Time: 3.8s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 5: ✅

  - Time: 3.65s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.81s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.85s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.85s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 4: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.74s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 5: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.92s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.24s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.14s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.26s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 4: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.18s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 5: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.18s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.03s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 1.93s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.31s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 4: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.28s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 5: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.49s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 1: ✅

  - Time: 3.46s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 2: ❌
  - Error: Invalid agent output: Could not parse response: ```json
{
  "fruit_count_by_color": {
    "orange": 25,
    "apple": 30
  }
}
```

  - Time: 4.98s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 3: ✅

  - Time: 3.25s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 4: ✅

  - Time: 3.37s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 5: ✅

  - Time: 6.05s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ✅

  - Time: 2.67s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ✅

  - Time: 2.78s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ✅

  - Time: 2.78s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 4: ✅

  - Time: 2.77s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 5: ✅

  - Time: 2.77s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ✅

  - Time: 3.02s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ✅

  - Time: 2.32s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ✅

  - Time: 2.2s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 4: ✅

  - Time: 2.78s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 5: ✅

  - Time: 2.41s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ❌
  - Error: Invalid agent output: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
  - Time: 1.49s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌
  - Error: Invalid agent output: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
  - Time: 1.28s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ❌
  - Error: Invalid agent output: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
  - Time: 1.27s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 4: ❌
  - Error: Invalid agent output: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
  - Time: 1.4s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 5: ❌
  - Error: Invalid agent output: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
  - Time: 1.96s


---
*Generated by AgentGym evaluation framework*
<!-- /INCLUDE -->

## Dependencies

- **pydantic-ai**: Agent framework
- **strands**: Alternative agent framework  
- **boto3**: AWS Bedrock integration
- **pytest**: Testing framework
- **jinja2**: Report templating

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
