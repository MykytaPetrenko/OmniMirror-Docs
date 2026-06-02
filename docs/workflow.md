# Workflow

OmniMirror is built around one main idea: create a persistent symmetry configuration while the mesh is still symmetrical, then reuse it later while the topology and vertex order stay unchanged.

## Basic Order

1. Start from a clean symmetrical mesh, usually right after applying the Mirror modifier.
2. Create a persistent symmetry configuration. See [Persistent Symmetry Configuration](config.md).
3. Continue editing the model without changing topology or vertex order.
4. Use the OmniMirror tools when you need symmetry again.

## Main Tools

- Use [Basis Mesh Symmetrization](basis_mesh.md) when the base mesh becomes asymmetrical but still has the same topology and vertex order.
- Use [Vertex Group Symmetrization](vertex_group.md) when painting weights on one side and copying or averaging them to the other side.
- Use [Shape Key Symmetrization](shape_key_symmetrization.md) when creating a shape key on one side and symmetrizing the deformation.
- Use [Shape Key Split](shape_key_split.md) when one shape key affects both sides and you need separate left/right controls.
- Use [UV Symmetry](uv.md) for UV side preview, selected UV symmetrization, axis snapping, and ICP snapping for paired UV islands.

## Important Rule

The configuration remains valid only while topology and vertex order remain the same. Moving vertices, editing shape keys, painting weights, and moving UVs are fine. Adding, deleting, merging, splitting, remeshing, or reordering vertices requires a new configuration.

