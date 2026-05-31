Workflow
========

This page is the first draft of the OmniMirror user workflow. It will grow into a step-by-step guide with screenshots once the UI states and example assets are ready.

1. Prepare The Mesh
-------------------

Open the mesh that should define the symmetry relationship. The mesh does not need to be perfectly symmetrical, but the closer the paired vertices are to their expected mirrored positions, the easier it is for OmniMirror to create a useful configuration.

2. Save A Mirror Configuration
------------------------------

In ``View3D > Sidebar > OMNI``, use the OmniMirror panel to choose the mirror axis and save a configuration file. The configuration stores detected mirrored pairs and center vertices so later operations can use the same mapping.

Useful checks at this stage:

* Select center vertices to confirm the mirror plane.
* Select unassigned vertices to find areas that were not matched.
* Adjust absolute or relative thresholds when detection needs to be stricter or more forgiving.

3. Symmetrize Mesh Data
-----------------------

After a valid configuration is available, use the mesh symmetrize tools to average both sides or copy one side to the other. This is the main repair pass for object-space vertex positions.

4. Symmetrize Vertex Groups
---------------------------

Vertex group tools can work on individual groups or left/right pairs. Pair mode is useful when weights are stored in side-named groups, while single mode is useful when a group should be internally symmetrical.

5. Symmetrize Or Split Shape Keys
---------------------------------

Shape key tools can symmetrize active or batched keys, use raw coordinates or deltas, and create left/right split keys from a broader shape. This is especially useful for corrective shapes and facial workflows where small asymmetries are hard to repair manually.

6. Work With UV Symmetry
------------------------

In the UV editor, OmniMirror can preview UV sides, symmetrize selected UVs, snap islands to the symmetry axis, and align mirrored UV islands. These tools use the saved mesh configuration as the source of truth for which vertices correspond.

