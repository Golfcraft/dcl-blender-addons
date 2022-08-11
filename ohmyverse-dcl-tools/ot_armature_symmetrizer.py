import bpy

class OMV_OT_ArmatureSymmetrizer(bpy.types.Operator):
    """Symmetrize DCL armatures, and restore to asymmetry"""
    bl_idname = "dcl.armature_symmetrizer"
    bl_label = "Symmetrize and restore dcl armatures"
    bl_options = {'REGISTER', 'UNDO'}
    enum_items = (
        ('SYMMETRIZE', 'Symmetrize Armature', '', 'MOD_MIRROR', 0),
        ('RESTORE_DCL', 'Restore to original', '', 'RECOVER_LAST', 1),
    )

    action: bpy.props.EnumProperty(items=enum_items)

    # Poll for enables operator
    @classmethod
    def poll(cls, context):
        if (context.area.ui_type == 'VIEW_3D') and context.scene.Armature:
            return True

    # Operator execution
    def execute(self, context):

        # Get dcl armature object
        if bpy.context.scene.Armature is not None:
            dcl_armature = bpy.context.scene.Armature
        # Set dcl_armature as active object
        context.view_layer.objects.active = dcl_armature
        # Set active to object mode
        bpy.ops.object.mode_set(mode='OBJECT')
        # Symmetrize dcl_armature bones
        if self.action == 'SYMMETRIZE':
            # Check name to avoid symmetrize twice
            if not "SYMMETRIZED_" in dcl_armature.name:
                # Fix naming and bone rolling (in edit mode)
                bpy.ops.object.mode_set(mode='EDIT')
                for edit_bone in dcl_armature.data.edit_bones:
                    if "_Right" in edit_bone.name:
                        # Fix right side bones names
                        edit_bone.name = edit_bone.name.replace("_Right", "_") + ".R"
                        # Fix wrong bone roll in right side
                        if "Sho" in edit_bone.name \
                        or "Han" in edit_bone.name \
                        or "Arm" in edit_bone.name:
                            edit_bone.roll += 3.14159
                    if "_Left" in edit_bone.name:
                        # Fix left side bones names
                        edit_bone.name = edit_bone.name.replace("_Left", "_") + ".L"
                # Return armature to object mode
                bpy.ops.object.mode_set(mode='OBJECT')
                # Set new name for Armature and print success message
                dcl_armature.name = "SYMMETRIZED_" + dcl_armature.name
                self.report({'INFO'}, "Successful armature symmetrization")
            # If armature is already symmetrical, print warning message
            else:
                self.report({'WARNING'}, "The armature is already symmetrical")
        # Restore asymmetrical DCL original armature
        elif self.action == 'RESTORE_DCL' and "SYMMETRIZED_" in dcl_armature.name:
            # Restore naming and bone rolling (in edit mode)
            bpy.ops.object.mode_set(mode='EDIT')
            for edit_bone in dcl_armature.data.edit_bones:
                if ".R" in edit_bone.name:
                    # Restore right side bones names
                    edit_bone.name = edit_bone.name.replace("_", "_Right").replace(".R", "")
                    # Restore wrong bone roll in right side
                    if "Sho" in edit_bone.name \
                    or "Han" in edit_bone.name \
                    or "Arm" in edit_bone.name:
                        edit_bone.roll -= 3.14159
                if ".L" in edit_bone.name:
                    # Fix left side bones names
                    edit_bone.name = edit_bone.name.replace("_", "_Left").replace(".L", "")
            # Return armature to object mode
            bpy.ops.object.mode_set(mode='OBJECT')
            dcl_armature.name = dcl_armature.name.replace("SYMMETRIZED_", "")
            self.report({'INFO'}, "DCL armature was restored")
        # Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')
        # Set active object to None
        context.view_layer.objects.active = None

        return{'FINISHED'}


####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.utils.register_class(OMV_OT_ArmatureSymmetrizer)

def unregister():
    bpy.utils.unregister_class(OMV_OT_ArmatureSymmetrizer)
    