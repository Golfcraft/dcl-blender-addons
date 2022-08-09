####################################
# DRAW PANEL
####################################

import bpy

class PT_OhmyverseDclTools(bpy.types.Panel):
    bl_label = "Ohmyverse DCL Tools"
    bl_idname = "PT_ohmyverse_dcl_tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'DCL'

    def draw(self, context):
        pass

class PT_Armatures(bpy.types.Panel):
    bl_label = "Armatures"
    bl_idname = "PT_armatures_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'DCL'
    bl_parent_id = "PT_ohmyverse_dcl_tools"
 
    def draw(self,context):
        layout = self.layout
        col = layout.column(align=True)
        col.operator_enum("dcl.armature_symmetrizer",  "action")

class PT_VertexWeights(bpy.types.Panel):
    bl_label = "Vertex Weights"
    bl_idname = "PT_vertexweights_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'DCL'
    bl_parent_id = "PT_ohmyverse_dcl_tools"
 
    def draw(self,context):
        layout = self.layout
        col = layout.column(align=True)
        col.label(text="Symmetrize Weights of:", icon='MOD_VERTEX_WEIGHT')
        objects = bpy.context.selected_objects
        if len(objects) == 1:
            col.operator("dcl.weights_symmetrizer", text="Selected vertex group")
        else:   
            col.operator("dcl.weights_symmetrizer", text="Selected pose bones")

####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.utils.register_class(PT_OhmyverseDclTools) 
    bpy.utils.register_class(PT_Armatures) 
    bpy.utils.register_class(PT_VertexWeights) 
        
def unregister():
    bpy.utils.unregister_class(PT_OhmyverseDclTools)
    bpy.utils.unregister_class(PT_Armatures)
    bpy.utils.unregister_class(PT_VertexWeights)