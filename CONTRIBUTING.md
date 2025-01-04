**This guide is work in progress ...**

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

Enforce coding conventions (done automatically by pre-commit hooks):

```bash
invoke cc
```

Run tests:

```bash
pytest -s tests
```
