# About

Hello! I am Mykyta Petrenko, also known as SqueezyPixels. I love symmetry, so I built this add-on for my own character workflow. I used it privately for a while because Blender's native tools do not always give me the results I expect, even on meshes that look symmetrical.

Eventually, I polished the tool to a point where I was no longer embarrassed to share it with others.

OmniMirror is not trying to replace Blender's native tools, and I am not going to claim that it is an ultimate must-have. It solves a specific set of problems I kept running into personally.

## How It Works

The add-on relies on a persistent symmetry configuration. Think of it as baking the symmetry information at the right moment, when your mesh is still nearly perfectly symmetrical, such as right after applying the Mirror modifier.

That configuration stores which vertices belong to the left side, the right side, or the center line. Later, even after you add asymmetrical details, the add-on remembers the original symmetry information. It no longer depends on the current vertex positions. Instead, it refers back to the saved configuration.

## What You Can Do With It

Once the configuration is saved, you can use it to symmetrize:

- Base meshes
- Shape keys
- Vertex groups
- UV maps

All of these operations are based on the original symmetry, not on the messy positions vertices may have drifted to later.

## Limitations

- OmniMirror relies on vertex order, so you cannot change topology after creating the configuration.
- The configuration should be created on a genuinely symmetrical mesh.
- The add-on is actively developed, so limitations may change.

