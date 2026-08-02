# Shape Key Symmetrization

Shape key symmetrization uses the persistent symmetry configuration to process shape key coordinates.

Before using these tools, make sure the active mesh has a compatible config in **Persistent Symmetry Config**.

## Where to Find It

In Blender, open the 3D View sidebar and go to:

`OmniMirror > Shape Keys > Symmetrize:`


## Parameters

1. **Data** controls what is symmetrized.
    - `Delta (Recommended)` symmetrizes the offset from the shape key's **Relative To** target. This is usually the safest and most useful mode. For example, if a shape key raises only the right eyebrow, Delta mode can copy that change to the left side without requiring the current basis mesh to be perfectly symmetrical.
    -  `Raw` symmetrizes the final raw coordinates stored in the shape key. This can be useful in specific cases, but it behaves differently from Delta mode. If the basis mesh is already asymmetrical, Raw mode symmetrizes the resulting positions, not just the shape key changes. Use `Raw` when you intentionally want the final shape key coordinates to become symmetrical.
2. **Type** controls how shape keys are matched before processing.
    - **`Single`** treats each shape key as a standalone, central shape key. It symmetrizes the shape key within itself.
    - **`Pair`** expects a left/right shape key pair. OmniMirror tries to find the matching counterpart by using Blender-style side names, such as `.L` and `.R`, `_L` and `_R`, or `Left` and `Right`.
    - **`Auto`** tries to use paired processing when a matching left/right counterpart exists. If no counterpart is found, it falls back to single shape key processing. `Auto` is a good default for batch processing mixed shape key lists.

3. **Single Flow** (similar to **Flow** in **Basis Mesh**) is used when a shape key is processed as a single shape key. The axis labels come from the saved symmetry config.
    - `Average` averages the mirrored deltas or coordinates between both sides.
    - `-X -> +X` copies from the negative axis side to the positive axis side.
    - `+X -> -X` copies from the positive axis side to the negative axis side.

    The displayed axis changes to match the config. Its direction is fixed by the sides recorded at config creation, not by the mesh's current visible position.

4. **Pair Flow** is used when a shape key is processed together with a left/right counterpart. For paired shape keys, the direction is based on the shape key names, not on the config's `-axis` and `+axis` sides.
    - `Average` averages the paired shape keys.
    - `Left -> Right` copies the left-named shape key to the right-named shape key.
    - `Right -> Left` copies the right-named shape key to the left-named shape key.

## Symmetrize Active

Click **Symmetrize Active** to process only the currently active shape key or a pair of shape keys where one of them is active.

## Batch Processing

Click **Symmetrize All** to process every shape key except the Basis shape key.

If you enable **Advanced Batch Options**, the button changes to **Symmetrize Custom Batch**. The checklist lets you choose exactly which shape keys should be processed. Use **Refresh** to rebuild the list, **Check All** to select every item, and **Uncheck All** to clear the selection.
