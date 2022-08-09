import bpy

class OT_ArmatureSymmetrizer(bpy.types.Operator):
    """Symmetrize and restore DCL armatures"""
    bl_idname = "dcl.armature_symmetrizer"
    bl_label = "Symmetrize and restore dcl armatures"
    bl_options = {'REGISTER', 'UNDO'}
    enum_items = (
        ('SYMMETRIZE', 'Symmetrize Armature', '', 'MOD_MIRROR',0),
        ('RESTORE_DCL', 'Restore to original', '', 'RECOVER_LAST',1),
    )

    action : bpy.props.EnumProperty(items=enum_items)
    @classmethod
    def poll(cls, context):
        active = bpy.context.active_object
        selected = bpy.context.selected_objects
        if (context.area.ui_type == 'VIEW_3D') and (len(selected) == 1) and (active.type == 'ARMATURE'):
            return True

    def execute(self, context):
        C = bpy.context
        active = bpy.context.active_object
        if self.action == 'SYMMETRIZE' and not "SYMMETRIZED_" in active.name:
            # Fix naming and bone rolling
            bpy.ops.object.mode_set(mode = 'EDIT')
            for bone in C.active_object.data.edit_bones:
                if "_Right" in bone.name:
                    bone.name = bone.name.replace("_Right", "_") + ".R"
                    if "Sho" in bone.name \
                    or "Han" in bone.name \
                    or "Arm" in bone.name:
                        bone.roll += 3.14159
                if "_Left" in bone.name:
                    bone.name = bone.name.replace("_Left", "_") + ".L"
            bpy.ops.object.mode_set(mode = 'OBJECT')
            C.active_object.name = "SYMMETRIZED_" + C.active_object.name
        elif self.action == 'RESTORE_DCL' and "SYMMETRIZED_" in active.name:
            # Fix naming and bone rolling
            bpy.ops.object.mode_set(mode = 'EDIT')
            for bone in C.active_object.data.edit_bones:
                if ".R" in bone.name:
                    bone.name = bone.name.replace("_", "_Right").replace(".R", "")
                    if "Sho" in bone.name \
                    or "Han" in bone.name \
                    or "Arm" in bone.name:
                        bone.roll -= 3.14159
                if ".L" in bone.name:
                    bone.name = bone.name.replace("_", "_Left").replace(".L", "")
            bpy.ops.object.mode_set(mode = 'OBJECT')
            C.active_object.name = C.active_object.name.replace("SYMMETRIZED_", "")
        return{'FINISHED'}


####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.utils.register_class(OT_ArmatureSymmetrizer) 
        
def unregister():
    bpy.utils.unregister_class(OT_ArmatureSymmetrizer)