# Shape Key Symmetrization

Shape key symmetrization uses the persistent symmetry configuration to process shape key coordinates.

Before using these tools, make sure the **Config File** field in the **Persistent Symmetry Config** section points to a compatible configuration JSON file.

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

3. **Single Flow** (very similar to Flow parameter from Base Mesh block) is used when a shape key is processed as a single shape key. The positive and negative sides come from the saved symmetry configuration.
    - `Average` averages the mirrored deltas or coordinates between both sides.
    - `Forward` copies from the negative side to the positive side.
    - `Reverse` copies from the positive side to the negative side.

3. **Pair Flow** is used when a shape key is processed together with a left/right counterpart. For paired shape keys, the direction is based on the shape key names, not on the positive/negative side from the persistent symmetry configuration.
    - `Average` averages the paired shape keys.
    - `Left -> Right` copies the left-named shape key to the right-named shape key.
    - `Right -> Left` copies the right-named shape key to the left-named shape key.

## Symmetrize Active

Click **Symmetrize Active** to process only the currently active shape key or a pair of shape keys where one of them is active.

## Batch Processing

Click **Symmetrize All** to process every shape key except the Basis shape key.

If you enable **Advanced Batch Options**, the button changes to **Symmetrize Custom Batch**. The checklist lets you choose exactly which shape keys should be processed. Use **Refresh** to rebuild the list, **Check All** to select every item, and **Uncheck All** to clear the selection.