# OmniMirror Docs

Public documentation for OmniMirror, a Blender add-on for persistent symmetry workflows across meshes, UVs, vertex groups, and shape keys.

The published documentation is built with Sphinx, using the same Wagtail theme workflow as MetaReForge Docs. Source pages live in `docs/`, and the generated site is deployed to the `gh-pages` branch for GitHub Pages.

## Local build

Install the documentation dependencies:

```powershell
python -m pip install -r requirements.txt
```

Build the site:

```powershell
python -m sphinx -b html docs docs/_build/html
```

Open `docs/_build/html/index.html` to preview the generated site.
