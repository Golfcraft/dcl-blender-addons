####################################
# DRAW PANEL
####################################

import bpy

from bpy.props import (
    BoolProperty,
    FloatProperty,
    StringProperty,
    EnumProperty,
    PointerProperty,
    CollectionProperty,
    IntProperty
)

class OMV_PT_OhmyverseDclTools(bpy.types.Panel):
    bl_label = "Ohmyverse DCL Tools"
    bl_idname = "OMV_PT_ohmyverse_dcl_tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'DCL'

    def draw(self, context):
        pass

class OMV_PT_Armatures(bpy.types.Panel):
    bl_label = "Armatures"
    bl_idname = "OMV_PT_armatures_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'DCL'
    bl_parent_id = "OMV_PT_ohmyverse_dcl_tools"
 
    def draw(self,context):
        layout = self.layout
        col = layout.column()
        col.label(text="Select Armature:")
        col.prop(context.scene, "Armature", text="")

        col = layout.column(align=True)
        col.operator_enum("dcl.armature_symmetrizer",  "action")

class OMV_PT_VertexWeights(bpy.types.Panel):
    bl_label = "Vertex Weights"
    bl_idname = "OMV_PT_vertexweights_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'DCL'
    bl_parent_id = "OMV_PT_ohmyverse_dcl_tools"
 
    def draw(self,context):
        layout = self.layout
        objects = context.selected_objects
        pose_bones = context.selected_pose_bones
        active = context.active_object

        col = layout.column(align=True)
        col.label(text="Symmetrize Weights of:")

        if (len(objects) == 1) and (active.type == 'MESH'):
            col.operator("dcl.weights_symmetrizer", text="Selected vertex group", icon='GROUP_VERTEX')
        elif (pose_bones is not None) and (len(pose_bones) >= 1):
            col.operator("dcl.weights_symmetrizer", text="Selected pose bones", icon='BONE_DATA')
        else:
            col.enabled = False
            col.operator("dcl.weights_symmetrizer", text="Selection is not valid")
        
class OMV_PT_MeshCleanup(bpy.types.Panel):
    bl_label = "Mesh Cleanup"
    bl_idname = "OMV_PT_mesh_cleanup_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'DCL'
    bl_parent_id = "OMV_PT_ohmyverse_dcl_tools"

    def draw(self,context):
        layout = self.layout
        col = layout.column()
        active = context.active_object
        if active is not None \
            and active.type == 'MESH' \
            and active.data.has_custom_normals:
            col.operator("mesh.customdata_custom_splitnormals_clear", text="Clear custom split normals", icon="CANCEL")
        else:
            col.enabled = False
            col.operator("mesh.customdata_custom_splitnormals_clear", text="Clear custom split normals", icon="CANCEL")

class OMV_PT_ExportGltfs(bpy.types.Panel):
    bl_label = "Export glTFs"
    bl_idname = "OMV_PT_export_gltfs_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'DCL'
    bl_parent_id = "OMV_PT_ohmyverse_dcl_tools"

    def draw(self,context):
        gltfs_export_setup = context.scene.omv_gltfsexportsetup
        layout = self.layout
        col = layout.column()
        col.prop(gltfs_export_setup, "export_path_3dmodels")
        col.prop(gltfs_export_setup, "export_path_metadata")
        col.prop(gltfs_export_setup, "collection_name_main")
        col.prop(gltfs_export_setup, "collection_name_empties")
        col.operator("dcl.export_gltfs", text="Export to DCL", icon="EXPORT")

def type_object_poll(self, object):
    return object.type == 'ARMATURE'


####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.utils.register_class(OMV_PT_OhmyverseDclTools)
    bpy.utils.register_class(OMV_PT_Armatures)
    bpy.utils.register_class(OMV_PT_VertexWeights)
    bpy.utils.register_class(OMV_PT_MeshCleanup)
    bpy.utils.register_class(OMV_PT_ExportGltfs)

    bpy.types.Scene.Armature = bpy.props.PointerProperty(
        type=bpy.types.Object,
        poll=type_object_poll
    )

def unregister():
    bpy.utils.unregister_class(OMV_PT_OhmyverseDclTools)
    bpy.utils.unregister_class(OMV_PT_Armatures)
    bpy.utils.unregister_class(OMV_PT_VertexWeights)
    bpy.utils.unregister_class(OMV_PT_MeshCleanup)
    bpy.utils.unregister_class(OMV_PT_ExportGltfs)

    del bpy.types.Scene.Armature