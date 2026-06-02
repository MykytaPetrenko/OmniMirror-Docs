# Basis Mesh Symmetrization

Basis mesh symmetrization changes the actual vertex coordinates of the active mesh. It uses the selected persistent symmetry configuration to decide which vertices are paired and which vertices belong to the center line.

Before using this tool, make sure the **Config File** field in the **Persistent Symmetry Config** section points to a valid configuration JSON file. The active mesh must have the same topology and vertex order as the mesh used to create that configuration.

## Where to Find It

In Blender, open the 3D View sidebar and go to:

`OmniMirror > Basis Mesh`

The section contains:

- **Mode**
- **Save Original as Shape Key**
- **Symmetrize**

## Parameters
### Flow

The **Flow** parameter controls how paired vertices are processed.

- `Average` finds the midpoint between each mirrored vertex pair and places both vertices symmetrically around the selected axis.
- `Forward` copies vertex coordinates from the negative side of the symmetry configuration to the positive side.
- `Reverse` copies vertex coordinates from the positive side of the symmetry configuration to the negative side.

`Forward` and `Reverse` flows depend on the saved configuration, not on the current visible position of the mesh. They use the positive and negative sides stored in the configuration.

```eval_rst
.. important::
    To avoid confusion, it is best not to rotate the mesh unnecessarily after creating the configuration. If your character faces the negative Y direction and the mirror axis is X, the usual interpretation is:
    - **Forward** copies from the right side to the left side.
    - **Reverse** copies from the left side to the right side.

    If your model uses a different orientation, think in terms of the saved positive and negative sides rather than visual left and right.
```

### Save Original as Shape Key

Enable **Save Original as Shape Key** if you want to preserve the current mesh coordinates before symmetrizing.

When enabled, OmniMirror creates a shape key named `BEFORE_SYMMETRIZE` before writing the new basis mesh coordinates. This is useful for comparing the result or recovering the previous shape.

## Symmetrize Process

Click **Symmetrize** to apply the selected mode to the active mesh.

OmniMirror will:

1. Load the selected configuration file.
2. Validate that the active mesh has a compatible vertex count.
3. Process all mirrored vertex pairs.
4. Force center vertices onto the selected symmetry axis.
5. Write the processed coordinates back to the basis mesh.

