import bpy

class OMV_OT_UnlockDeformBones(bpy.types.Operator):
    """Unlock deform-bones for skinning poses"""
    bl_idname = "dcl.unlock_deform_bones"
    bl_label = "Unlock bones and mute constraints"
    bl_options = {'REGISTER', 'UNDO'}
    operations = (
        ('UNLOCK', 'Unlock and mute constraints', '', 'UNLOCKED', 0),
        ('RESTORE_LOCK', 'Restore locks and constraints', '', 'LOCKED', 1),
    )

    operation: bpy.props.EnumProperty(items=operations)

    # Poll for enables operator
    @classmethod
    def poll(cls, context):
        if context.area.ui_type == 'VIEW_3D' and context.scene.Armature:
            return True

    def execute(self, context):

        # Get dcl armature object
        if bpy.context.scene.Armature is not None:
            dcl_armature = bpy.context.scene.Armature
        # Set dcl_armature as active object
        context.view_layer.objects.active = dcl_armature

        pose_bones = dcl_armature.pose.bones
        if self.operation == 'UNLOCK':
            for pb in pose_bones:
                if pb.bone.use_deform == True:
                    for constraint in pb.constraints:
                        constraint.mute = True

                    pb.lock_location[0] = False
                    pb.lock_location[1] = False
                    pb.lock_location[2] = False
                    pb.lock_rotation_w = False
                    pb.lock_rotation[0] = False
                    pb.lock_rotation[1] = False
                    pb.lock_rotation[2] = False
                    pb.lock_scale[0] = False
                    pb.lock_scale[1] = False
                    pb.lock_scale[2] = False

        else:
            for pb in pose_bones:
                if pb.bone.use_deform == True:
                    for constraint in pb.constraints:
                        constraint.mute = False

                    pb.lock_rotation[2] = True
                    pb.lock_location[0] = True
                    pb.lock_location[1] = True
                    pb.lock_location[2] = True
                    pb.lock_rotation_w = True
                    pb.lock_rotation[0] = True
                    pb.lock_rotation[1] = True
                    pb.lock_rotation[2] = True
                    pb.lock_scale[0] = True
                    pb.lock_scale[1] = True
                    pb.lock_scale[2] = True
                    
        # Return armature to object mode
        bpy.ops.object.mode_set(mode='OBJECT')
        # Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')
        # Set active object to None
        context.view_layer.objects.active = None


        return{'FINISHED'}


####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.utils.register_class(OMV_OT_UnlockDeformBones)
        
def unregister():
    bpy.utils.unregister_class(OMV_OT_UnlockDeformBones)