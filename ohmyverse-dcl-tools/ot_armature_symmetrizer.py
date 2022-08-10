import bpy

class OMV_OT_ArmatureSymmetrizer(bpy.types.Operator):
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
        if (context.area.ui_type == 'VIEW_3D') and context.scene.Armature:
            return True

    def execute(self, context):
        # current_active = bpy.context.active_object

        if bpy.context.scene.Armature is not None:
            active = bpy.context.scene.Armature
        
        # bpy.context.active_object = active
        context.view_layer.objects.active = active
        
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        if self.action == 'SYMMETRIZE':
            if not "SYMMETRIZED_" in active.name:
                # Fix naming and bone rolling
                bpy.ops.object.mode_set(mode = 'EDIT')
                for bone in active.data.edit_bones:
                    if "_Right" in bone.name:
                        bone.name = bone.name.replace("_Right", "_") + ".R"
                        if "Sho" in bone.name \
                        or "Han" in bone.name \
                        or "Arm" in bone.name:
                            bone.roll += 3.14159
                    if "_Left" in bone.name:
                        bone.name = bone.name.replace("_Left", "_") + ".L"
                bpy.ops.object.mode_set(mode = 'OBJECT')
                active.name = "SYMMETRIZED_" + active.name
                self.report({'INFO'}, "Successful armature symmetrization")
            else:    
                self.report({'WARNING'}, "The armature is already symmetrical")

        elif self.action == 'RESTORE_DCL' and "SYMMETRIZED_" in active.name:
            # Fix naming and bone rolling
            bpy.ops.object.mode_set(mode = 'EDIT')
            for bone in active.data.edit_bones:
                if ".R" in bone.name:
                    bone.name = bone.name.replace("_", "_Right").replace(".R", "")
                    if "Sho" in bone.name \
                    or "Han" in bone.name \
                    or "Arm" in bone.name:
                        bone.roll -= 3.14159
                if ".L" in bone.name:
                    bone.name = bone.name.replace("_", "_Left").replace(".L", "")
            bpy.ops.object.mode_set(mode = 'OBJECT')
            active.name = active.name.replace("SYMMETRIZED_", "")
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