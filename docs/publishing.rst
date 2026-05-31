Publishing
==========

This repository is prepared for GitHub Pages publishing through GitHub Actions.

Repository Layout
-----------------

``docs/``
    Sphinx documentation source files.

``docs/conf.py``
    Sphinx configuration and theme settings.

``requirements.txt``
    Python dependencies used by the local build and GitHub Actions.

``.github/workflows/pages.yml``
    Build and deploy workflow for GitHub Pages.

Enable GitHub Pages
-------------------

1. Push this repository to GitHub.
2. Open the repository settings.
3. Go to ``Pages``.
4. Set the source to ``GitHub Actions``.
5. Push to ``main`` to trigger the first deployment.

Local Preview
-------------

Install dependencies:

.. code-block:: powershell

   python -m pip install -r requirements.txt

Build the site:

.. code-block:: powershell

   python -m sphinx -b html docs docs/_build/html

The generated page will be available at ``docs/_build/html/index.html``.

