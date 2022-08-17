# Ohmyverse DCL Tools (Blender Addon)

This addon provide some tools for improve the asset creation for Decentraland, specially regarding wearables.

## Symmetrize Armature 
One of the main issues we find when linking a wearable to the decentraland skeleton is that it is not symmetrical. Blender comes with some useful features, like painting weights in x-axis symmetry. But we cannot take advantage of this feature. This happens because decentraland's skeleton structure doesn't have ".L" and ".R" suffixes, which is what blender needs to work in symmetry.

For this reason we make an operator for symmetrize the Decentraland armatures.

Disclaimer: Before exporting make sure to restore the original structure with the second option. If you don't, Decentraland animations won't work.

> Painting weights without symmetry (the painful way, because is broken)

https://user-images.githubusercontent.com/21176686/184263925-5c49fd4a-ef09-4bef-9e78-b43f9a64d4e7.mp4


> Painting with our symmetry solution
The addon rename the bones and fix bone-rolls to fix the issue

https://user-images.githubusercontent.com/21176686/184262854-c571d246-9ac2-4c4e-bcd2-6ba85b8638d0.mp4


### Restore DCL armature to original structure
You must restore the original DCL armature before exporting your wearables, because the animations are made for this specific structure.

https://user-images.githubusercontent.com/21176686/184262829-e1b5a0dc-d132-41a9-b7eb-27fe6325305f.mp4



## Symmetrize Weights
In some cases you may need to mirror the weights you have painted. This operator can be used with the active vertex-group of the selected object, or also with the set of selected pose-bones (you can select multiple bones at the same time in this case).

> Symmetrize weights based on pose bone selection

https://user-images.githubusercontent.com/21176686/184262797-d0db0513-52c5-4a34-838e-eaa3986e6fb9.mp4


> Symmetrize weights based on active vertex group selection

https://user-images.githubusercontent.com/21176686/184262811-908a1fee-dc0a-4b20-b715-40617373f646.mp4


## Mesh Cleanup
### Clear custom split normals
In many cases you will notice that the normals of your mesh don't look as you would like, especially when you have imported the decentraland reference models from a FBX file. It is a common problem, but the solution is a bit hidden. We have added a button to have this function closer.


> Clear custom split normals data

https://user-images.githubusercontent.com/21176686/184262773-9d8b90e3-721c-4839-9460-a7f239fe9233.mp4


---
# Instalation
1. Download last release [here](https://github.com/Golfcraft/dcl-blender-addons/tree/main/releases)
2. In Blender go to Edit->Preferences->Addons->Install
3. Choose the downloaded zip file and install
4. You can find the panel in 3d-View Sidebar. Enjoy!
