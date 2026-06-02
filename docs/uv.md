# UV Symmetry

UV tools use the persistent symmetry configuration to find matching UV loops through the mesh topology. The tools do not guess symmetry only from the current UV layout. They use the saved vertex pairs from the config, then apply that information to selected UVs.

Before using these tools, make sure the **Config File** field in the UV Editor's **OmniMirror** panel points to a compatible configuration JSON file. The mesh must be in **Edit Mode**, and the object must have an active UV layer.

## Where to Find It

In Blender, open the UV Editor sidebar and go to:

`OmniMirror`

The UV panel contains shared settings at the top, followed by:

- **Side Preview**
- **Symmetrize**
- **Rigid Snap**

## Shared Parameters

1. **UV Axis** controls which UV coordinate is used as the symmetry axis.
    - **`U`** mirrors across the U coordinate.
    - **`V`** mirrors across the V coordinate.

2. **Axis Position** controls where the symmetry axis is placed in UV space. The eyedropper button next to it sets the value from the selected UV loop centroid.

3. **Weld Distance** controls how close UV loops need to be to be treated as connected or centered. It is used for center-loop detection, welded UV groups, and UV island detection.

## Side Preview

**Side Preview** draws an overlay in the UV Editor using the persistent symmetry configuration.

It helps you check how OmniMirror classifies UVs before running an operation:

- negative side of the config;
- positive side of the config;
- center vertices.

### Preview Controls

1. **Auto Off** disables the preview automatically when editing input starts. If it is disabled, editing can make the preview outdated until you refresh it.

2. **Start Preview** controls which UVs are shown.
    - **`All UVs`** builds the preview for all UV loops.
    - **`Selected UVs`** builds the preview only for selected UV loops.

3. **Stop Preview** turns the active preview off.

4. **Refresh Preview** rebuilds the overlay after the UV selection or layout changes.

### Viewport Display

The **Viewport Display** subsection only changes how the preview is drawn. It does not affect symmetrization or snapping.

Available display settings:

- **Overlay Line Width**
- **Overlay Fill**
- **Fill Opacity**
- **Overlay Outline**
- **Outline Width**

## Symmetrize

The **Symmetrize** tool processes selected UV loops. A UV loop is processed only when OmniMirror can find its matching loop through the persistent symmetry configuration and the matching loop is also selected.

### Parameters

1. **Mode** controls how selected symmetrical UV pairs are processed.
    - **`Average`** averages paired UVs symmetrically around the configured UV axis.
    - **`Forward`** copies UVs from the negative side to the matching positive side.
    - **`Reverse`** copies UVs from the positive side to the matching negative side.

2. **Force Center To Axis** moves detected center UV loops onto the configured UV axis. This is enabled by default and is useful for keeping center seams aligned.

### Symmetrize Selected UVs

Click **Symmetrize Selected UVs** to apply the selected mode to the current UV selection.

OmniMirror also uses **Weld Distance** to group nearby UV loops that share the same 3D vertex. If multiple selected loops are close enough to be treated as the same welded point, their calculated result is averaged so they stay together.

## Rigid Snap

The **Rigid Snap** tools move selected UV islands without directly reshaping every UV pair one by one. They are useful when you want to align islands while preserving their internal shape as much as possible.

## Axis Snap Selected UV Islands

**Axis Snap Selected UV Islands** aligns a symmetrical UV island to the configured UV axis.

The tool uses the center loops inside the island to estimate its middle line, then rotates and moves the selected UVs so that this middle line lands on the configured UV axis.

Use this when a UV island should be centered on the symmetry axis but is slightly offset or tilted.

### Selection Requirements

Use Axis Snap for a single UV island that contains both sides of the mesh and center loops between them.

The island must include center loops detected from the persistent symmetry configuration. If OmniMirror cannot find center loops inside the selected island, the island is skipped.

## ICP Snap Selected UV Islands

**ICP Snap Selected UV Islands** aligns paired symmetrical UV islands.

The tool uses matched UV pairs as control points, then moves the target island with translation and rotation. If **Use Scale** is enabled, it may also apply uniform scale.

### Parameters

1. **Direction** controls which side stays fixed and which side is moved.
    - **`Forward`** keeps the negative side fixed and snaps the positive side.
    - **`Reverse`** keeps the positive side fixed and snaps the negative side.

2. **Use Scale** allows ICP snapping to apply uniform scale in addition to translation and rotation. Leave it disabled if the island size should stay unchanged.

### Selection Requirements

Use ICP Snap for two separate UV islands that represent symmetrical parts of the mesh.

Select UV loops from both the source and target islands. OmniMirror needs matched selected loop pairs across the two islands to calculate the transform. Center loops are ignored for this operation, and pairs inside the same UV island are skipped.
