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
        col = layout.column(align=True)
        col.label(text="Symmetrize Weights of:", icon='MOD_VERTEX_WEIGHT')
        objects = bpy.context.selected_objects
        if len(objects) == 1:
            col.operator("dcl.weights_symmetrizer", text="Selected vertex group")
        else:   
            col.operator("dcl.weights_symmetrizer", text="Selected pose bones")

def type_object_poll(self, object):
    return object.type == 'ARMATURE'


####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.utils.register_class(OMV_PT_OhmyverseDclTools) 
    bpy.utils.register_class(OMV_PT_Armatures) 
    bpy.utils.register_class(OMV_PT_VertexWeights) 

    bpy.types.Scene.Armature = bpy.props.PointerProperty(
        type=bpy.types.Object,
        poll=type_object_poll
    )
        
def unregister():
    bpy.utils.unregister_class(OMV_PT_OhmyverseDclTools)
    bpy.utils.unregister_class(OMV_PT_Armatures)
    bpy.utils.unregister_class(OMV_PT_VertexWeights)

    del bpy.types.Scene.Armature