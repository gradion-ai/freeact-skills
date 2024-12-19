# Freeact Skills

Freeact Skills is a curated set of Python-based modules designed for integration with [freeact](https://github.com/gradion-ai/freeact) agents. These skills offer a wide range of capabilities, from basic operations like internet searches to more advanced tasks such as Zotero library management, for example. In freeact applications, these skills are typically executed within [ipybox](https://github.com/gradion-ai/ipybox) sandboxed environments. While currently experimental, this repository will be continuously expanded to support more advanced skills over time.

## Installation

### Local installation

To install all skills, run:

```bash
pip install freeact-skills[all]
```

To install a specific skill, run one or more of:

```bash
# Readwise Reader integration
pip install freeact-skills[reader]

# Google search integration
pip install freeact-skills[search-google]

# Perplexity search integration
pip install freeact-skills[search-perplexity]

# Zotero integration
pip install freeact-skills[zotero]
```

### ipybox installation

If you want to pre-install these skills on [ipybox](https://github.com/gradion-ai/ipybox), install the `ipybox` package first:

```bash
pip install ipybox
```

Then create a `dependencies.txt` file with the following content:

```
# all skills (or alternatively a list of specific skills)
freeact-skills = {version = "*", extras = ["all"]}
```

Build an ipybox Docker image with the skills pre-installed:

```bash
python -m ipybox build -t your-image-tag -d dependencies.txt
```

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
poetry install --all-extras
```

Run tests:

```bash
pytest -s tests
```
