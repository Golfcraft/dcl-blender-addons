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


## Scene Export
A Decentraland scene is a combination of multiple 3D models, until now the artist only where able to work on one 3D model at the time, exporting it and positioning it by trial and error of the position and rotation Transformation on code.

Our Blender addon allows the export of multiple glTF files (including animation) and its transformation in just one click. It also allows to export additional transformations for positioning objects on code.

![](/demo/export_scene_01.png)

### Create collections
Under de main Scene Collection create 3 collections:
- Main (Here we will store the instances)
- Empties (Here we will add empties to export additional transformations)
- Others (Here we will add collections to be instanced on Main)

![](/demo/export_scene_02.png)

### Create elements
Lets create an example scene to export:
1. Under the Others collection create a new collection labeled Sphere
1. Create a sphere in the Sphere collection with position 0,0,0
1. Drag and drop the Sphere collection into the 3D View to create a new instance
1. Press M and select the Main collection, to move the new instance there
1. Under the Empties collection create some additional Empties

### Addon setup
Save the Blender project, and on the Export scene section:
1. On glTFs path enter a path to a folder where the 3D models should be saved
1. On glTFs metadata path enter the path to a .ts file where the position, rotation and scale of the instances will be saved
1. On Main collection name enter the name of the collection storing instances (in our example Main)
1. On Empties collection name enter the name if the collection storing additional empties to export positions (in our example Empties)
1. Check the export glTFs option

### Exporting
Now you can click on Export to DCL , that will result on:
1. A .glb file stored on the glTFs path, will be named as the collection instansed
1. A .ts file stored on the glTFs metadata path, you can later import that file into your scene code

![](/demo/export_scene_03.png)

---
# Instalation
1. Download last release [here](https://github.com/Golfcraft/dcl-blender-addons/tree/main/releases)
2. In Blender go to Edit->Preferences->Addons->Install
3. Choose the downloaded zip file and install
4. You can find the panel in 3d-View Sidebar. Enjoy!
