# Persistent Symmetry Configuration
A *persistent symmetry configuration* is a saved map that stores the correspondence between vertex indices on the left and right sides of your mesh. It also marks which vertices belong to the center line (the symmetry plane).

Think of it as baking the symmetry information at the right moment — when your mesh is still perfectly or near‑perfectly symmetrical. Later, after you add asymmetrical details, the add-on can still refer back to this saved configuration.

## Mesh Requirements

- **Good symmetry.** OmniMirror works best when the symmetry configuration is created at the moment when the mesh is still genuinely symmetrical. In a typical workflow, this is right after applying a Mirror modifier, before sculpting, posing, editing shape keys, or adding any non-symmetrical details.
- **No vertex duplicates.** The mesh should not contain duplicated vertices. If multiple vertices occupy the same or almost the same position, the add-on may not be able to know which one is the correct match.


## Symmetry Detection (Vertex Classification)

The configuration process classifies every vertex in the mesh as one of three types:

- a vertex on the negative side of the symmetry axis;
- a vertex on the positive side of the symmetry axis;
- a center vertex lying on the symmetry plane.

For the configuration to be valid, every vertex must be classified. If at least one vertex cannot be detected as part of a mirrored pair or as a center vertex, the configuration will not work correctly.

During further processing, all vertices will be handled according to their classification - whether they're on the negative half-space, the positive half-space, or lying directly on the center symmetry plane.

### Symmetrical Vertex Detection (Positive-Negative)

To find symmetrical vertices, OmniMirror takes a vertex from one side of the mesh, mirrors its position across the selected symmetry axis, and searches for the best matching vertex on the opposite side.

The add-on supports two threshold modes for this detection:

- **Absolute threshold** uses a fixed object-space distance. A mirrored vertex must be found within that distance.
- **Relative threshold (Recommended)** uses a distance based on the local mesh density. The threshold is calculated from the shortest edge connected to the vertex, which makes detection less sensitive to differences in mesh scale or density.

In most cases, you should not need to change the default values if you create the configuration immediately after applying a Mirror modifier.

### Center Vertex Detection

If a vertex does not have a mirrored counterpart, OmniMirror checks whether it is close enough to the symmetry plane. If it is within the center detection threshold, it is marked as a center vertex.

The add-on supports two threshold modes for this detection as well.

Center vertices are important because they do not have left/right partners.


### Debugging Detection (Highly recommended)

OmniMirror includes helper operators for checking whether the configuration can be created correctly:

- **Select Center Vertices** selects all vertices detected as belonging to the symmetry plane.
- **Select Unassigned Vertices** selects vertices that could not be clearly classified.

These helpers are **HIGHLY** recommended to run before creating a persistent symmetry configuration.

If `Select Unassigned Vertices` finds anything, the mesh is not ready for a valid configuration yet. You may need to adjust the detection thresholds, clean duplicated vertices, or create the configuration earlier in the workflow while the mesh is still perfectly symmetrical.

## Creating a Configuration File

When you create a symmetry configuration, OmniMirror saves the result as a JSON file. This file stores the symmetry information for the mesh: which vertex indices are paired across the mirror axis, and which vertex indices belong to the center line.

### Topology and Vertex Order 

✅ The configuration is based on **vertex order**. 
That means the same configuration file can be reused on any model that has the exact same topology and the exact same vertex order. The mesh can have different shape key values, different vertex group weights, different UV positions, or non-symmetrical edits, but the underlying vertex indices must still match.

❌ If the topology changes, the configuration is no longer reliable. Adding vertices, deleting vertices, merging vertices, splitting edges, remeshing, or doing anything else that changes vertex order can make the saved configuration invalid.