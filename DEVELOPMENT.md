# Development Guide

This guide provides instructions for setting up a development environment for `freeact-skills`. Follow these steps to get started with development, testing, and contributing to the project.

Clone the repository:

```bash
git clone https://github.com/gradion-ai/freeact-skills.git
cd freeact-skills
```

Create a new Conda environment and activate it:

```bash
conda env create -f environment.yml
conda activate freeact-skills
```

Install the poetry dynamic versioning plugin:

```bash
poetry self add "poetry-dynamic-versioning[plugin]"
```

Install dependencies with Poetry:

```bash
poetry install --all-extras --with docs
```

Install pre-commit hooks:

```bash
invoke precommit-install
```

Enforce coding conventions (done automatically by pre-commit hooks):

```bash
invoke cc
```

Run tests:

```bash
pytest -s tests
```
