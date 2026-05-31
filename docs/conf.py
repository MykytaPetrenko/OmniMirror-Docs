project = "OmniMirror"
copyright = "2026, Sqeezy Pixels (Mykyta Petrenko)"
author = "Mykyta Petrenko"
release = "0.0.1"

extensions = [
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_wagtail_theme"
html_title = "OmniMirror Docs"
html_show_sourcelink = True
html_show_sphinx = False

html_theme_options = {
    "project_name": "OmniMirror",
    "logo": "OmniMirror",
    "github_url": "https://github.com/MykytaPetrenko/OmniMirror-Docs",
    "footer_links": "",
}

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

