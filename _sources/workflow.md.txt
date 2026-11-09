# Workflow

Create a persistent symmetry config for the mesh and reuse it as you work. The config is saved with the mesh in the `.blend` file and remains valid as long as topology and vertex order stay the same.

## Basic Order

1. Use **Coordinate Based** on a symmetrical mesh or **Topology Based** on a mesh with enough matching topology. See [Persistent Symmetry Config](config.md).
2. Continue editing the model while keeping topology and vertex order unchanged.
3. Use the OmniMirror tools whenever you need symmetry again.

## Main Tools

- Use [Basis Mesh Symmetrization](basis_mesh.md) when the base mesh becomes asymmetrical but still has the same topology and vertex order.
- Use [Vertex Group Symmetrization](vertex_group.md) when painting weights on one side and copying or averaging them to the other side.
- Use [Shape Key Symmetrization](shape_key_symmetrization.md) when creating a shape key on one side and symmetrizing the deformation.
- Use [Shape Key Split](shape_key_split.md) when one shape key affects both sides and you need separate left/right controls.
- Use [UV Symmetry](uv.md) for UV side preview, selected UV symmetrization, axis snapping, and ICP snapping for paired UV islands.
- Use [Edge Symmetry](edges.md) to copy seams, sharp marks, crease values, bevel weights, and Freestyle marks.
- Use [Pose Symmetry](pose.md) to mirror pose transforms and, experimentally, selected-bone constraint stacks.

## Important Rule

The configuration remains valid only while topology and vertex order remain the same. Moving vertices, editing shape keys, painting weights, and moving UVs are fine. Adding, deleting, merging, splitting, remeshing, or reordering vertices requires a new configuration.
