# Update README.md with included report content
update-readme:
	uv run python scripts/include_replace.py README.md
install:
	uv sync

run:
	uv run run_evaluation.py