# Edge Symmetry

**Edges** mirrors seam and sharp-edge states using the active mesh's persistent symmetry config. The mesh needs a compatible config, but it may be used in Object Mode or Edit Mode.

## Where to Find It

In the 3D View sidebar, open:

`OmniMirror > Edges`

## Symmetrize All

Set **Flow**, then use one of the buttons under **Symmetrize All:**:

- **Seams** mirrors seam marks.
- **Sharp** mirrors sharp-edge marks.
- **Both** mirrors both kinds of edge flag.

The flow uses the config's axis labels: **`-X -> +X`** copies from the negative axis side to the positive axis side, and **`+X -> -X`** copies in the other direction. The displayed axis changes to match the config, and the direction is defined by the sides recorded when that config was created.

Enable **Only Add** to copy marked seams or sharp edges without clearing any existing marks on the target side.

## Selected Edges

In Edit Mode, the panel also shows selected-edge actions:

- Under **From Selected:**, use **Seams**, **Sharp**, or **Both** to copy the selected edges' flags to their mirrored counterparts.
- Under **To Selected:**, use the same buttons to copy each counterpart's flags to the selected edges.

These actions only affect selected edges that have a matching edge in the config.
