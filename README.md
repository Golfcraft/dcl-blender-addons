# Ohmyverse DCL Tools (Blender Addon)

This addon provide some tools for improve the asset creation for Decentraland, specially regarding wearables.

## Symmetrize Armature 
One of the main issues we find when linking a wearable to the decentraland skeleton is that it is not symmetrical. Blender comes with some useful features, like painting weights in x-axis symmetry. But we cannot take advantage of this feature.
For this reason we make an operator for symmetrize the Decentraland armatures.

Disclaimer: Before exporting make sure to restore the original structure with the second option. If you don't, Decentraland animations won't work.

<img src="demo/omv_dcl_tools_symmetrize_armature.mp4" width="720">

## Symmetrize Weights
In some cases for any reason you may need to mirror the weights you have painted. This operator can be used with the active vertex-group of the selected object, or also with the set of selected pose-bones.

## Mesh Cleanup
### Clear custom split normals
In many cases you will notice that the normals of your mesh don't look as you would like, especially when you have imported the decentraland reference models from a FBX file. It is a common problem, but the solution is a bit hidden. We have added a button to have this function closer.

---
# Instalation
1. Download last release here
2. In Blender go to Edit->Preferences->Addons->Install
3. Choose the downloaded zip file and install
4. You can find the panel in 3d-View Sidebar. Enjoy!