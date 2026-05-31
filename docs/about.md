# About

Hello! I’m Mykyta Petrenko (aka SqueezyPixels). I love symmetry, so I built this add-on for my own character workflow. I used it privately for a while because Blender’s native tools… well, they don’t always give the results I expect. Even on meshes that look symmetrical.

So I polished my tool to a point where I’m not embarrassed to share it with others.

This isn’t trying to replace Blender’s native tools. And I’m not going to say it’s an ultimate must-have. It just solves a specific set of problems I kept running into personally.

## How it works (short version. See the next sections for more)
The add-on relies on a persistent symmetry configuration. Think of it like baking the symmetry information at the right moment - when your mesh is still nearly perfectly symmetrical (right after applying the Mirror modifier, for example).

That configuration stores which vertices belong to the left side, right side, or center line. Then, even after you add asymmetrical details (because perfect symmetry looks unnatural and falls into uncanny valley territory), the add-on remembers the original symmetry info. It doesn’t care about current vertex positions anymore - it just refers back to that baked configuration.

## What you can do with it
Once the configuration is saved, you can use it to symmetrize:

- Base meshes
- Shape keys
- Vertex groups
- UV maps

All based on the original symmetry, not on whatever messy positions vertices have drifted to.

## Limitations:
- This works on vertex order. You can’t change topology after creating the config.
- The config should be created on a genuinely symmetrical mesh.
- I’m actively developing it, so limitations may change — check the Marketplace page for the latest info.