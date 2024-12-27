# freeact-skills

The `freeact-skills` project provides a curated set of predefined skill modules for the [freeact](https://gradion-ai.github.io/freeact) agent system.

## Documentation

The official documentation is available [here](https://gradion-ai.github.io/freeact-skills/).

## Development

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

Install dependencies with Poetry:

```bash
poetry install --all-extras --with docs
```

Install pre-commit hooks:

```bash
invoke precommit-install
```

Run tests:

```bash
pytest -s tests
```
