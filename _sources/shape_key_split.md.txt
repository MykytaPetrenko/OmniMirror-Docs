# Shape Key Split

Shape key splitting creates separate left and right shape keys from a single source shape key.

This is useful for shapes that were created as one combined deformation, but later need independent side controls. For example, one shape key that moves both ears can be split into two shape keys: one for the left ear and one for the right ear.

Before using this tool, make sure the active mesh has a compatible config in **Persistent Symmetry Config**.

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

2. **Side Mapping** controls how the config's axis sides are written into left/right shape keys.
    - **`+X -> Left | -X -> Right`** writes the positive axis side to the left shape key and the negative axis side to the right shape key.
    - **`-X -> Left | +X -> Right`** writes the negative axis side to the left shape key and the positive axis side to the right shape key.

    The displayed axis changes to match the config. For a character facing negative Y with X as the mirror axis, `+X -> Left | -X -> Right` is usually correct. If the model uses another orientation, choose the mapping that matches the sides recorded when the config was created.

3. **Preview Side** controls which split side is shown after splitting. OmniMirror sets the original shape key's value to `0` and gives the chosen left or right split shape key the original value, so you can immediately inspect the transition.

4. **Remove Original** removes the source shape key after the left and right versions are created. Leave it disabled if you want to keep the original combined shape key for comparison or backup.

5. **Skip Symmetrical** skips shape keys that already contain left/right indicators such as `.L`, `.R`, `_L`, `_R`, `Left`, or `Right`. This option is enabled by default and is mostly useful for batch processing, where the list may contain both central shape keys and already separated side controls.

6. **Falloff** controls the blend distance around the symmetry plane. A value of `0` creates a hard split, while values greater than `0` create a smoother transition near the center line.

7. **Falloff Shape** controls the curve used inside the falloff area.
    - **`Linear`** uses a direct linear transition.
    - **`Smooth`** uses a smoothstep-style transition and is the default.
    - **`Sharp`** keeps the transition tighter near the center.
    - **`Soft`** spreads the transition more gently.

## Split Active

Click **Split Active** to split only the currently active shape key.

After splitting, use Blender's **Adjust Last Operation** popup in the lower-left corner of the 3D View to adjust the operator settings in real time. This is useful for testing the suffix, side mapping, preview side, or falloff before processing a larger batch.

## Batch Processing

Click **Split All** to process every shape key except the Basis shape key.

If you enable **Advanced Batch Options**, the button changes to **Split Custom Batch**. The checklist lets you choose exactly which shape keys should be processed. Use **Refresh** to rebuild the list, **Check All** to select every item, and **Uncheck All** to clear the selection.
