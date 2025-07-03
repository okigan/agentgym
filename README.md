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

Generated on: 2025-07-03 16:21:39

## Summary

Total evaluations: 120

## Results by Puzzle



### Fruit_count


| Framework | Model | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Run 6 | Run 7 | Run 8 | Run 9 | Run 10 | Success Rate |
|-----------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|--------------|
| pydantic_ai | mistral.mistral-large-2407-v1:0 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 100.0% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 0.0% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 0.0% |
| pydantic_ai | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 0.0% |
| pydantic_ai_enhanced | mistral.mistral-large-2407-v1:0 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 100.0% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 0.0% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 0.0% |
| pydantic_ai_enhanced | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 0.0% |
| strands | mistral.mistral-large-2407-v1:0 | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | 30.0% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 100.0% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 100.0% |
| strands | arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | 0.0% |




## Detailed Results


- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 1: ✅

  - Time: 4.54s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 2: ✅

  - Time: 3.82s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 3: ✅

  - Time: 3.89s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 4: ✅

  - Time: 3.78s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 5: ✅

  - Time: 3.77s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 6: ✅

  - Time: 3.73s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 7: ✅

  - Time: 3.75s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 8: ✅

  - Time: 4.08s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 9: ✅

  - Time: 3.73s

- **fruit_count** / pydantic_ai / mistral.mistral-large-2407-v1:0 / Run 10: ✅

  - Time: 4.27s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.9s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.8s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.94s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 4: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 3.24s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 5: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.93s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 6: ❌
  - Error: Total fruit count 0 does not match expected value 55
  - Time: 2.86s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 7: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.79s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 8: ❌
  - Error: Total fruit count 0 does not match expected value 55
  - Time: 2.84s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 9: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.86s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 10: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.83s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.2s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.23s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.12s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 4: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.24s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 5: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.23s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 6: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.21s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 7: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.11s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 8: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.36s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 9: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.11s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 10: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.21s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.33s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.08s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.06s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 4: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 1.92s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 5: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.06s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 6: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.09s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 7: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 1.96s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 8: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.1s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 9: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.34s

- **fruit_count** / pydantic_ai / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 10: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.25s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 1: ✅

  - Time: 4.18s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 2: ✅

  - Time: 3.76s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 3: ✅

  - Time: 3.85s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 4: ✅

  - Time: 3.86s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 5: ✅

  - Time: 3.8s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 6: ✅

  - Time: 4.17s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 7: ✅

  - Time: 3.71s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 8: ✅

  - Time: 3.56s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 9: ✅

  - Time: 3.83s

- **fruit_count** / pydantic_ai_enhanced / mistral.mistral-large-2407-v1:0 / Run 10: ✅

  - Time: 3.87s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.76s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ❌
  - Error: Total fruit count 0 does not match expected value 55
  - Time: 2.75s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ❌
  - Error: Total fruit count 0 does not match expected value 55
  - Time: 2.83s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 4: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.81s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 5: ❌
  - Error: Total fruit count 0 does not match expected value 55
  - Time: 2.81s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 6: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.81s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 7: ❌
  - Error: Total fruit count 0 does not match expected value 55
  - Time: 2.79s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 8: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.95s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 9: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 3.49s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 10: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.85s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.21s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.22s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.09s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 4: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.2s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 5: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.17s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 6: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.13s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 7: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.12s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 8: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.16s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 9: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.23s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 10: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.13s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.06s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 1.94s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 1.9s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 4: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.02s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 5: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.02s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 6: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.27s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 7: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.06s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 8: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.08s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 9: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 1.88s

- **fruit_count** / pydantic_ai_enhanced / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 10: ❌
  - Error: Exceeded maximum retries (1) for result validation
  - Time: 2.06s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 1: ✅

  - Time: 6.34s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 2: ✅

  - Time: 3.26s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 3: ❌
  - Error: Invalid agent output: Could not parse response: ```json
{
  "fruit_count_by_color": {
    "orange": 25,
    "apple": 30
  }
}
```

  - Time: 4.97s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 4: ❌
  - Error: Invalid agent output: Could not parse response: ```json
{
  "fruit_count_by_color": {
    "orange": 25,
    "apple": 30
  }
}
```

  - Time: 3.63s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 5: ❌
  - Error: Invalid agent output: Could not parse response: ```json
{
  "fruit_count_by_color": {
    "orange": 25,
    "apple": 30
  }
}
```

  - Time: 5.18s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 6: ❌
  - Error: Invalid agent output: Could not parse response: ```json
{
  "fruit_count_by_color": {
    "orange": 25,
    "apple": 30
  }
}
```

  - Time: 4.05s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 7: ❌
  - Error: Invalid agent output: Could not parse response: ```json
{
  "fruit_count_by_color": {
    "orange": 25,
    "apple": 30
  }
}
```

  - Time: 4.81s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 8: ❌
  - Error: Invalid agent output: Could not parse response: ```json
{
  "fruit_count_by_color": {
    "orange": 25,
    "apple": 30
  }
}
```

  - Time: 4.11s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 9: ❌
  - Error: Invalid agent output: Could not parse response: ```json
{
  "fruit_count_by_color": {
    "orange": 25,
    "apple": 30
  }
}
```

  - Time: 3.78s

- **fruit_count** / strands / mistral.mistral-large-2407-v1:0 / Run 10: ✅

  - Time: 3.92s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 1: ✅

  - Time: 2.59s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 2: ✅

  - Time: 2.56s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 3: ✅

  - Time: 2.73s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 4: ✅

  - Time: 2.72s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 5: ✅

  - Time: 2.64s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 6: ✅

  - Time: 2.63s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 7: ✅

  - Time: 2.64s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 8: ✅

  - Time: 2.32s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 9: ✅

  - Time: 2.64s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-2-90b-instruct-v1:0 / Run 10: ✅

  - Time: 2.62s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 1: ✅

  - Time: 2.55s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 2: ✅

  - Time: 4.23s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 3: ✅

  - Time: 2.23s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 4: ✅

  - Time: 2.41s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 5: ✅

  - Time: 2.38s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 6: ✅

  - Time: 2.36s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 7: ✅

  - Time: 2.32s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 8: ✅

  - Time: 2.41s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 9: ✅

  - Time: 2.38s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama3-3-70b-instruct-v1:0 / Run 10: ✅

  - Time: 2.32s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 1: ❌
  - Error: Invalid agent output: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
  - Time: 1.47s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 2: ❌
  - Error: Invalid agent output: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
  - Time: 1.46s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 3: ❌
  - Error: Invalid agent output: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
  - Time: 1.54s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 4: ❌
  - Error: Invalid agent output: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
  - Time: 1.5s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 5: ❌
  - Error: Invalid agent output: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
  - Time: 1.5s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 6: ❌
  - Error: Invalid agent output: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
  - Time: 1.53s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 7: ❌
  - Error: Invalid agent output: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
  - Time: 1.34s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 8: ❌
  - Error: Invalid agent output: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
  - Time: 1.39s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 9: ❌
  - Error: Invalid agent output: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
  - Time: 1.36s

- **fruit_count** / strands / arn:aws:bedrock:us-west-2:***:inference-profile/us.meta.llama4-maverick-17b-instruct-v1:0 / Run 10: ❌
  - Error: Invalid agent output: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
  - Time: 1.32s


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
