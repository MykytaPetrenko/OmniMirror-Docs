# Publishing

This repository uses Markdown source files and MkDocs. The generated website is published to the `gh-pages` branch.

## Repository layout

- `docs/` contains Markdown documentation source files.
- `mkdocs.yml` configures the site navigation, theme, and Markdown extensions.
- `requirements.txt` pins the Python packages used to build the site.
- `.github/workflows/pages.yml` builds the site and publishes generated HTML to `gh-pages`.

## GitHub Pages settings

Set GitHub Pages to publish from:

- Source: `Deploy from a branch`
- Branch: `gh-pages`
- Folder: `/ (root)`

After that, every push to `main` will rebuild the docs and update the `gh-pages` branch.

## Local preview

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run a local preview server:

```powershell
python -m mkdocs serve
```

Build static HTML:

```powershell
python -m mkdocs build
```

The generated site is written to `site/`.

