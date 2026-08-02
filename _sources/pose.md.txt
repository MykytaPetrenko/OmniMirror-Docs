# Pose Symmetry

Pose symmetry mirrors pose-bone transforms from Blender-style left/right bone names. It works on an active armature in **Pose Mode** and does not require a mesh config.

## Where to Find It

In the 3D View sidebar, open:

`OmniMirror > Pose`

## Pose Transforms

Under **All Bones:**, set **Flow** and **Influence**, then click **Symmetrize All Bones**.

- **Average** averages each left/right pose pair.
- **Left -> Right** copies the left pose to the right bone.
- **Right -> Left** copies the right pose to the left bone.
- **Influence** blends the current target pose toward the mirrored result. At `1.0`, the mirrored result is applied fully.

Under **Selected Bones:**, select one or more source bones and use:

- **From Selected** to copy selected bones to their mirrored counterparts.
- **To Selected** to copy each counterpart to the selected bone.

If both bones of a pair are selected, the transform action averages that pair. Bones without a Blender-recognized left/right counterpart are skipped.

## Constraints (Experimental)

The **Constraints:** actions mirror the constraint stack for selected source bones:

- **From Selected** replaces the counterpart bone's entire constraint stack with mirrored copies of the selected bone's stack.
- **To Selected** replaces the selected bone's entire constraint stack with mirrored copies of its counterpart's stack.

This feature is experimental. It mirrors armature subtargets that use standard left/right naming and applies specific range conversion for common limit and transformation constraints. Review the result before relying on complex constraint setups. **Transform Cache** constraints are skipped, and selecting both bones of a pair skips that pair.
