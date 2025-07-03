## Project Structure

```
.
├── app/                           # Core utilities
│   ├── reporting.py               # Result collection and reporting
│   └── utils.py                   # Shared utilities
│
├── puzzles/                       # Task definitions
│   └── fruit_count/               # Example: fruit counting puzzle
│       ├── tools.py               # Agent tools (get_count_of_oranges, etc.)
│       └── checker.py             # Puzzle result validation
│
├── frameworks/                    # Agent implementations
│   ├── pydantic_ai/               
│   │   └── agent.py               # Pydantic AI agent factory
│   └── strands/                   
│       └── agent.py               # Strands agent factory
│
├── config.py                      # Evaluation configuration
├── run_evaluation.py              # Main evaluation runner
└── reports/                       # Generated reports (GitHub Pages ready)
```

## Quick Start

### Prerequisites

- Python 3.11+
- uv package manager
- AWS credentials configured for Bedrock access

### Installation

```bash
# Clone and setup
git clone <repository>
cd agentgym

# Install dependencies
uv sync

# Configure AWS (if not already done)
export AWS_DEFAULT_REGION=us-west-2
export AWS_PROFILE=your-profile  # optional
```

### Configuration

Edit `config.py` to specify:
- Which puzzles to run
- Which frameworks to test
- Which models to evaluate
- Number of runs per combination

### Running Evaluations

```bash
# Run all evaluations
uv run python run_evaluation.py

# Results will be saved to reports/latest.md
```

## Adding New Components

### Adding a New Puzzle

1. Create directory: `puzzles/your_puzzle/`
2. Add `tools.py` with agent tools (functions)
3. Add `checker.py` with validation logic
4. Update `config.py` to include the puzzle

### Adding a New Framework

1. Create directory: `frameworks/your_framework/`
2. Add `agent.py` with `make_agent(model_id)` function
3. Install framework dependencies: `uv add your-framework`
4. Update `config.py` to include the framework

## Example Results

The evaluation generates reports showing success/failure rates:

```
🧩 FRUIT_COUNT:
   pydantic_ai          [Pass | Pass | Fail] (67%)
   strands              [Pass | Pass | Pass] (100%)
```
