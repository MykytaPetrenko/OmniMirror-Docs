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

Armature subtargets use Blender's standard left/right name flipping. Selecting both bones of a pair skips that pair.

```eval_rst
.. important::
    Constraint symmetrization is experimental and replaces the target bone's entire constraint stack. Review the result before relying on a complex rig.
```

### Reviewed Constraints

The following constraints have been reviewed in the order shown in Blender's constraint menu:

```eval_rst
.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Constraint
     - Mirrored behavior
   * - Copy Location
     - Copied unchanged.
   * - Copy Rotation
     - Copied unchanged.
   * - Copy Scale
     - Copied unchanged.
   * - Copy Transforms
     - Copied unchanged.
   * - Limit Distance
     - Copied unchanged; it does not need a symmetry-specific range conversion.
   * - Limit Location
     - The X range is inverted: ``target min_x = -source max_x`` and
       ``target max_x = -source min_x``.
   * - Limit Rotation
     - The X range is copied. The Y and Z ranges are inverted.
   * - Limit Scale
     - Copied unchanged.
   * - Maintain Volume
     - Copied unchanged.
   * - Transformation
     - Location X ranges are inverted; rotation Y and Z ranges are inverted;
       scale ranges are copied. This applies to both **From** and **To** ranges.
   * - Transform Cache
     - Not copied. OmniMirror reports a warning.
```

Other constraint types are copied with their writable settings and mirrored armature subtargets, but do not yet have reviewed type-specific axis or range conversion.
