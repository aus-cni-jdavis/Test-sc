# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Test-sc (Python Calculator)

Located in `python-app/`.

```bash
# Install dependencies
pip install -r requirements.txt

# Run the interactive calculator
python calculator.py

# Run all tests
pytest

# Run a single test
pytest test_calculator.py::test_add -v
```

### Architecture

- `calculator.py` — Four arithmetic functions (`add`, `subtract`, `multiply`, `divide`) plus an interactive CLI loop. `divide` raises `ValueError` on division by zero.
- `test_calculator.py` — Pytest suite covering all four operations and the division-by-zero error path.
- `db.py` — Connects to `TestDB` on `(localdb)\MSSQLLocalDB` via Windows Auth. Provides product price lookup and table browsing for the calculator.
