# Rubrics

A Python library for managing rubrics with criterion rules.

## Installation

```bash
pip install rubrics
```

## Usage

```python
from rubrics import CriterionRule, RubricService

# Create a criterion rule
rule = CriterionRule(
    weight=1.0,
    requirement="Must meet the specified criteria"
)

# Use the rubric service
service = RubricService()
```

## Features

- Define criterion rules with weights and requirements
- Manage rubrics for evaluation and assessment
- Built with Pydantic for robust data validation

## Requirements

- Python 3.13 or higher
- pydantic >= 2.0.0

## Development

This package is built using the [uv](https://github.com/astral-sh/uv) build backend.

## License

MIT License - see LICENSE file for details.

