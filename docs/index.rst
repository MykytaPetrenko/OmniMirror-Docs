Welcome to OmniMirror Docs!
===========================

OmniMirror is a Blender add-on for building reliable symmetry workflows around a saved mirror configuration. Instead of repeatedly guessing which vertices, UVs, weights, or shape key coordinates belong together, OmniMirror lets you describe the symmetry relationship once and reuse it across the editing process.

This is useful when a model is mostly symmetrical but still needs controlled edits, repair, or production cleanup. You can create a persistent configuration from the mesh, inspect center and unassigned vertices, then use that same mapping to symmetrize mesh positions, vertex groups, shape keys, and selected UVs.

Core Idea
---------

The add-on separates symmetry into two stages:

1. Create a mirror configuration that records vertex pairs and center vertices for a chosen axis.
2. Apply that configuration to the data you want to repair, average, copy, or split.

That makes the workflow predictable. The same configuration can drive object-space symmetry, weight symmetry, facial or corrective shape key symmetry, and UV operations without relying on fragile one-off selections.

Typical Workflow
----------------

1. Open the mesh in Blender and choose the mirror axis.
2. Save a mirror configuration from the OmniMirror panel in ``View3D > Sidebar > OMNI``.
3. Inspect center vertices and unassigned vertices if the model needs cleanup.
4. Load the saved configuration.
5. Symmetrize mesh positions, vertex groups, shape keys, or UVs depending on the task.

Current Documentation
---------------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   about
   publishing
   workflow

