## ipybox installation

For use with `freeact` agents, `freeact-skills` needs to be pre-installed on [ipybox](https://gradion-ai.github.io/ipybox) Docker images. First, install `ipybox`:

```bash
pip install ipybox
```

Create a `dependencies.txt` file with one of the following configurations:

```toml title="dependencies.txt"
# Install all available skills
freeact-skills = {version = "*", extras = ["all"]}
```

The `extras=["all"]` option includes all available skills: `["reader", "search-google", "search-perplexity", "zotero"]`. Alternatively, you can install specific skills:

```toml title="dependencies.txt"
# Install selected skills only
freeact-skills = {version = "*", extras = ["search-google", "zotero"]}
```

Note: `dependencies.txt` must follow the [Poetry dependency specification format](https://python-poetry.org/docs/dependency-specification/).

Build the `ipybox` Docker image with your selected skills:

```bash
python -m ipybox build -t your-image-tag -d dependencies.txt
```

Replace `your-image-tag` with your preferred image name.

## Local installation

For local development or direct usage, install with `pip`:

```bash
pip install freeact-skills[all]
```

This is equivalent to:

```bash
pip install freeact-skills[reader,search-google,search-perplexity,zotero]
```

To install specific skills only:

```bash
pip install freeact-skills[search-google,zotero]
```
