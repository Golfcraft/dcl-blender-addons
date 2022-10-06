import os
import bpy
import json

from bpy.props import (
    StringProperty,
    PointerProperty,
    BoolProperty,
)


class OMV_OT_ExportGltfs(bpy.types.Operator):
    """Export multiple glTFs and metadata"""
    bl_idname = "dcl.export_gltfs"
    bl_label = "Export glTFs"
    # bl_options = {'REGISTER', 'UNDO'}
    enum_items = (
        ('SYMMETRIZE', 'Symmetrize Armature', '', 'MOD_MIRROR', 0),
        ('RESTORE_DCL', 'Restore to original', '', 'RECOVER_LAST', 1),
    )

    action: bpy.props.EnumProperty(items=enum_items)

    # Poll for enables operator
    @classmethod
    def poll(cls, context):
        C = bpy.context
        D = bpy.data

        gltfs_export_setup = context.scene.omv_gltfsexportsetup
        if (gltfs_export_setup.collection_name_main == ''):
            return False
        if (gltfs_export_setup.export_path_metadata == ''):
            return False
        if (gltfs_export_setup.export_path_3dmodels == ''):
            return False
        
        if not gltfs_export_setup.collection_name_main in D.collections:
            return False
        
        if gltfs_export_setup.collection_name_empties != '' and not gltfs_export_setup.collection_name_empties in D.collections:
            return False

        if (context.area.ui_type == 'VIEW_3D'):
            return True

    # Operator execution
    def execute(self, context):
        C = bpy.context
        D = bpy.data

        gltfs_export_setup = context.scene.omv_gltfsexportsetup

        main_collection = D.collections[gltfs_export_setup.collection_name_main]
        
        metadata_path = gltfs_export_setup.export_path_metadata
        gltf_path = gltfs_export_setup.export_path_3dmodels

        # Checks
        gltf_save_path = bpy.path.abspath(bpy.path.native_pathsep(gltf_path))
        if not os.path.isdir(gltf_save_path):
            self.report({'ERROR'}, "\"{}\" is not a directory".format(gltf_save_path))
            return {'CANCELLED'}

        if not os.path.exists(gltf_save_path):
            self.report({'ERROR'}, "Directory \"{}\" don't exists".format(gltf_save_path))
            return {'CANCELLED'}

        meta_save_path = bpy.path.abspath(bpy.path.native_pathsep(metadata_path))
        if os.path.isdir(meta_save_path):
            self.report({'ERROR'}, "Metadata path \"{}\" is a directory, should be a \".ts\" file".format(meta_save_path))
            return {'CANCELLED'}
        
        if not meta_save_path.endswith(".ts"):
            self.report({'ERROR'}, "Metadata path \"{}\" should be a \".ts\" file".format(meta_save_path))
            return {'CANCELLED'}

        empty_positions = {}

        ## Get empties
        if gltfs_export_setup.collection_name_empties != '' and gltfs_export_setup.collection_name_empties in D.collections:
            empties_collection = D.collections[gltfs_export_setup.collection_name_empties]
            for obj in empties_collection.objects:
                # if is an empty
                if not obj.data:
                    empty_positions[obj.name] = self.transform2dcl(obj)


        collections_to_export = []
        # Show geometry
        for obj in main_collection.objects:
            # if its an instance
            if not obj.data and  obj.instance_type == 'COLLECTION':
                name = self.export_gltf(obj.instance_collection)
                t = self.transform2dcl(obj)
                t["gltf"] = name
                empty_positions[obj.name] = t
        
        
        with open(meta_save_path, 'w') as fp:
            fp.write("export default ")
            json.dump(empty_positions, fp, sort_keys=True, indent=4)
    
        self.report({'INFO'}, "Successful glTFs export")
        return{'FINISHED'}
    
    def transform2dcl(self, obj):
        obj.rotation_mode = 'QUATERNION'
        t = {
                "position": [
                    obj.location[0] * -1,
                    obj.location[2],
                    obj.location[1] * -1
                ],
                "rotation": [
                    obj.rotation_quaternion[1] * -1,
                    obj.rotation_quaternion[3],
                    obj.rotation_quaternion[2] * -1,
                    obj.rotation_quaternion[0] * -1
                ],
                "scale": [
                    obj.scale[0],
                    obj.scale[2],
                    obj.scale[1],
                ]
            }
        return t

    def select_all_collection(self, collection):
        for obj in collection.objects:
            obj.hide_set(False)
            obj.select_set(True)
        for c in collection.children:
            self.select_all_collection(c)

    def export_gltf(self, collection):
        C = bpy.context

        print("Export: ", collection.name)
        gltf_path = C.scene.omv_gltfsexportsetup.export_path_3dmodels
        bpy.ops.object.select_all(action='DESELECT')
        self.select_all_collection(collection)
        gltf_name = "{}.glb".format(collection.name)
        save_path = bpy.path.abspath(os.path.join(bpy.path.native_pathsep(gltf_path), gltf_name))
        if C.scene.omv_gltfsexportsetup.export_gltfs:
            bpy.ops.export_scene.gltf(
                filepath=save_path,
                export_format="GLB",
                use_selection=True,
                export_animations=True
            )
        return gltf_name


class OMV_PG_GltfsExportSetup(bpy.types.PropertyGroup):

    export_path_3dmodels: StringProperty(
        name="glTFs path",
        subtype='DIR_PATH'
    )

    export_path_metadata: StringProperty(
        name="glTFs metadata path",
        subtype='FILE_PATH'
    )

    collection_name_main: StringProperty(
        name="Main collection name"
    )

    collection_name_empties: StringProperty(
        name="Empties collection name"
    )

    export_gltfs: BoolProperty(
        name="Export glTFs",
        default=True
    )


####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.utils.register_class(OMV_OT_ExportGltfs)
    bpy.utils.register_class(OMV_PG_GltfsExportSetup)

    bpy.types.Scene.omv_gltfsexportsetup = PointerProperty(type=OMV_PG_GltfsExportSetup)
        
def unregister():
    bpy.utils.unregister_class(OMV_OT_ExportGltfs)
    bpy.utils.unregister_class(OMV_PG_GltfsExportSetup)

    del bpy.types.Scene.omv_gltfsexportsetup