# Update README.md with included report content
update-readme:
	uv run python scripts/include_replace.py README.md

install:
	uv sync

run_evaluation:
	@if [ -f .env ]; then \
		export $$(cat .env | xargs) && uv run run_evaluation.py; \
	else \
		echo "No .env file found. Creating from template..."; \
		cp .env.example .env; \
		echo "Please edit .env with your configuration"; \
	fi