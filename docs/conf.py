# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from recommonmark.transform import AutoStructify


def setup(app):
    app.add_transform(AutoStructify)


# -- Project information -----------------------------------------------------

project = 'OmniMirror Docs'
copyright = '2026, Squeezy Pixels (Mykyta Petrenko)'
author = 'Squeezy Pixels (Mykyta Petrenko)'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'recommonmark'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

extensions.append('sphinx_wagtail_theme')
html_theme = 'sphinx_wagtail_theme'
project = 'OmniMirror'

html_theme_options = dict(
    project_name='OmniMirror',
    logo='img/omnimirror_logo.svg',
    logo_alt='OmniMirror',
    logo_height=75,
    logo_width=75,
    logo_url='https://mykytapetrenko.github.io/OmniMirror-Docs/',
    github_url='https://github.com/MykytaPetrenko/OmniMirror-Docs/tree/main/docs/',
)

html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

