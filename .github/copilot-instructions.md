
# Copilot Instructions - AgentGym

## Project Overview
AgentGym is a Python framework for evaluating AI agent frameworks (e.g., Pydantic AI, Strands) against various LLMs (primarily AWS Bedrock-hosted models) using modular "puzzles" (tasks). The goal is to benchmark agent+model performance on tool-augmented tasks, with results published as Markdown reports for GitHub Pages.

## Architecture & Key Components
- **app/**: Cross-cutting utilities and reporting (e.g., `reporting.py` for Markdown/HTML report generation).
- **puzzles/**: Each puzzle/task is a subdirectory (e.g., `fruit_count/`) with its own `tools.py` (agent-callable functions) and `checker.py` (output validation logic).
- **frameworks/**: Each agent framework (e.g., `pydantic_ai/`, `strands/`) has an `agent.py` with a `make_agent(model_id, puzzle_tools)` factory function.
- **config.py**: Central config for listing puzzles, frameworks, models, and run parameters. Dynamically builds Bedrock ARNs using the current AWS account.
- **run_evaluation.py**: Orchestrates N runs per (puzzle, framework, model) combo, collects results, and triggers report generation.
- **reports/**: Contains Jinja2 templates and generated Markdown/HTML reports for GitHub Pages.

## Developer Workflows
- **Dependency Management**: Use `uv` exclusively (`uv add <package>`, `uv sync`, `uv run <cmd>`).
- **Running Evaluations**: Use `make run` or `uv run python run_evaluation.py`.
- **Testing**: Place framework-specific tests in `tests/`, run with `uv run pytest`.
- **AWS Setup**: Requires valid AWS credentials (`AWS_PROFILE`) for Bedrock model access.

## Patterns & Conventions
- **Puzzle Structure**: Each puzzle owns its tools and checker. Example tool:
  ```python
  async def get_count_of_oranges(ctx) -> int:
      # ...
  ```
- **Framework Agent Factory**: Each framework exposes `make_agent(model_id, puzzle_tools)` in its `agent.py`.
- **Model ARNs**: Bedrock model ARNs are constructed dynamically in `config.py` using the current AWS account.
- **Reporting**: Results are rendered as Markdown tables in `reports/latest.md` for GitHub Pages.
- **Defensive Coding**: Expect some agent+model+framework combos to fail; code should handle and report failures gracefully.

## Integration Points
- **AWS Bedrock**: All LLMs are accessed via Bedrock; ensure correct region/account setup.
- **Jinja2**: Used for Markdown/HTML report templating.

## Examples
- Adding a puzzle: create `puzzles/my_puzzle/tools.py` and `checker.py`, then update `config.py`.
- Adding a framework: create `frameworks/my_framework/agent.py` with `make_agent`, update `config.py`, and add tests.

## References
- See `README.md` for high-level overview and `config.py` for current evaluation matrix.
- For report structure, see `reports/template.md.j2` and generated `reports/latest.md`.
