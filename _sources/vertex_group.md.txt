# Vertex Group Symmetrization

Vertex group symmetrization uses the persistent symmetry configuration to process vertex weights.

Before using this tool, make sure the **Config File** field in the **Persistent Symmetry Config** section points to a compatible configuration JSON file.

## Where to Find It

In Blender, open the 3D View sidebar and go to:

`OmniMirror > Vertex Groups`

## Parameters

1. **Type** controls how vertex groups are matched before processing.
    - **`Single`** treats each vertex group as a standalone group. Weights are symmetrized within the same vertex group.
    - **`Pair`** expects a left/right vertex group pair. OmniMirror tries to find the matching counterpart by using Blender-style side names, such as `.L` and `.R`, `_L` and `_R`, or `Left` and `Right`.
    - **`Auto`** uses paired processing for side-named vertex groups and single-group processing for the rest. `Auto` is a good default for batch processing mixed vertex group lists.

2. **Single Flow** is used when a vertex group is processed as a single group. The positive and negative sides come from the saved symmetry configuration.
    - **`Average`** averages the mirrored weights between both sides.
    - **`Forward`** copies weights from the negative side to the positive side.
    - **`Reverse`** copies weights from the positive side to the negative side.

3. **Pair Flow** is used when a vertex group is processed together with a left/right counterpart. For paired vertex groups, `Left -> Right` and `Right -> Left` are based on the vertex group names, not on the positive/negative side from the persistent symmetry configuration.
    - **`Average`** averages the paired vertex group weights.
    - **`Left -> Right`** copies the left-named vertex group to the right-named vertex group.
    - **`Right -> Left`** copies the right-named vertex group to the left-named vertex group.

4. **Advanced Batch Options** enables a checklist for choosing which vertex groups should be processed by the batch operation.

## Symmetrize Single

Click **Symmetrize Single** to process only the active vertex group or a pair of vertex groups where one of them is active.

This is the best option when checking the selected **Type**, **Single Flow**, or **Pair Flow** settings before processing a larger set.

## Batch Processing

Click **Symmetrize All** to process every vertex group on the active mesh.

If you enable **Advanced Batch Options**, the button changes to **Symmetrize Custom Batch**. The checklist lets you choose exactly which vertex groups should be processed. Use **Refresh** to rebuild the list, **Check All** to select every item, and **Uncheck All** to clear the selection.

During processing, OmniMirror shows progress and allows the operation to be cancelled.

