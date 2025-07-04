# Update README.md with included report content
update-readme:
	uv run python scripts/include_replace.py README.md
install:
	uv sync

run_evaluation:
	uv run run_evaluation.py