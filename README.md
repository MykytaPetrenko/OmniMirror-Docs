# OmniMirror Docs

Public documentation for OmniMirror, a Blender add-on for persistent symmetry workflows across meshes, UVs, vertex groups, and shape keys.

The published documentation is built from Markdown files with MkDocs and deployed to the `gh-pages` branch for GitHub Pages.

## Local build

Install the documentation dependencies:

```powershell
python -m pip install -r requirements.txt
```

Build the site:

```powershell
python -m mkdocs build
```

Preview locally:

```powershell
python -m mkdocs serve
```

GitHub Pages should be configured to publish from the `gh-pages` branch, folder `/ (root)`.
