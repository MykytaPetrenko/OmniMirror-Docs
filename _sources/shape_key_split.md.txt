# Shape Key Split

Shape key splitting creates separate left and right shape keys from a single source shape key.

This is useful for shapes that were created as one combined deformation, but later need independent side controls. For example, one shape key that moves both ears can be split into two shape keys: one for the left ear and one for the right ear.

Before using this tool, make sure the **Config File** field in the **Persistent Symmetry Config** section points to a compatible configuration JSON file.

## Where to Find It

In Blender, open the 3D View sidebar and go to:

`OmniMirror > Shape Keys > Split:`

## Parameters

1. **Suffix** controls which left/right suffixes are added to the newly created shape keys.
    - **`.L / .R`** appends Blender-style uppercase dot suffixes.
    - **`_L / _R`** appends uppercase underscore suffixes.
    - **`_l / _r`** appends lowercase underscore suffixes.
    - **`-L / -R`** appends uppercase dash suffixes.
    - **`Left / Right`** appends full side names.

2. **Side Mapping** controls how the positive and negative sides from the persistent symmetry configuration are written into left/right shape keys.
    - **`Positive -> Left`** writes the positive side to the left shape key and the negative side to the right shape key.
    - **`Positive -> Right`** writes the positive side to the right shape key and the negative side to the left shape key.

    For a character facing the negative Y direction with X as the mirror axis, `Positive -> Left` is usually correct. If your character uses the opposite orientation, switch the mapping.

3. **Remove Original** removes the source shape key after the left and right versions are created. Leave it disabled if you want to keep the original combined shape key for comparison or backup.

4. **Skip Symmetrical** skips shape keys that already contain left/right indicators such as `.L`, `.R`, `_L`, `_R`, `Left`, or `Right`. This option is enabled by default and is mostly useful for batch processing, where the list may contain both central shape keys and already separated side controls.

5. **Falloff** controls the blend distance around the symmetry plane. A value of `0` creates a hard split, while values greater than `0` create a smoother transition near the center line.

6. **Falloff Shape** controls the curve used inside the falloff area.
    - **`Linear`** uses a direct linear transition.
    - **`Smooth`** uses a smoothstep-style transition and is the default.
    - **`Sharp`** keeps the transition tighter near the center.
    - **`Soft`** spreads the transition more gently.

## Split Active

Click **Split Active** to split only the currently active shape key.

This is the best option when checking suffix, side mapping, or falloff settings before processing a larger batch.

## Batch Processing

Click **Split All** to process every shape key except the Basis shape key.

If you enable **Advanced Batch Options**, the button changes to **Split Custom Batch**. The checklist lets you choose exactly which shape keys should be processed. Use **Refresh** to rebuild the list, **Check All** to select every item, and **Uncheck All** to clear the selection.
