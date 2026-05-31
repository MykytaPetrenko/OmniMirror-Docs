# OmniMirror-Docs

Public documentation for OmniMirror, a Blender add-on for persistent symmetry workflows across meshes, UVs, vertex groups, and shape keys.
The published documentation is built with Sphinx and deployed with GitHub Pages.

## Local build

Install the documentation dependencies:

```powershell
python -m pip install -r requirements.txt
```

Build the site:

```powershell
python -m sphinx -b html docs docs/_build/html
```

Open `docs/_build/html/index.html` in a browser to preview the generated site.

