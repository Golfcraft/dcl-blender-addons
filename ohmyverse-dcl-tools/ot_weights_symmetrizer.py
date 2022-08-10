import bpy

class OMV_OT_WeightsSymmetrizer(bpy.types.Operator):
    """Symmetrize vertex groups weights"""
    bl_idname = "dcl.weights_symmetrizer"
    bl_label = "VertexGroups / PoseBones"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        active = bpy.context.active_object
        if context.area.ui_type == 'VIEW_3D' and active.type == 'MESH':
        # if context.area.ui_type == 'VIEW_3D' and active.type == 'MESH' and active.mode == 'WEIGHT_PAINT':
            return True

    def execute(self, context):
        C = bpy.context
        active = C.active_object
        vgroups = active.vertex_groups
        active_vg = vgroups.active.name
        pbones = C.selected_pose_bones

        # Clean old _copy vertex groups
        for vg in vgroups:
            if "_copy" in vg.name:
                vgroups.remove(vg)

        # Operator only works with symmetrized armatures
        for mod in active.modifiers:
            if mod.type == 'ARMATURE' and mod.object is not None:
                armature = mod.object
        if not "SYMMETRIZED" in armature.name:
            self.report({'ERROR'}, "Aborted: Only works with symmetrized armatures")
            return {'CANCELLED'}

        # Multibones
        if pbones:
            for bone in context.selected_pose_bones:
                for vg in vgroups:
                    if vg.name == bone.name:
                        bpy.ops.object.vertex_group_set_active(group=vg.name)
                        active_vg = vg.name
                        if ".L" in active_vg or ".R" in active_vg:
                            symmetrize_weights(active_vg, vgroups)
                        else:
                            pass
        # Vertex group selection
        else:
            if ".L" in active_vg or ".R" in active_vg:
                symmetrize_weights(active_vg, vgroups)
            else:
                self.report({'WARNING'}, "Only works with .L or .R vertex groups")
                return {'CANCELLED'}

        self.report({'INFO'}, "Successful weights symmetrization")

        return{'FINISHED'}

def symmetrize_weights(active_vg, vgroups):
    # Save active VG
    current_vg = bpy.context.active_object.vertex_groups.active
    
    # Duplicate active vertex group
    bpy.ops.object.vertex_group_copy()
    # Delete current mirrored
    if ".L" in active_vg:
        wrong_vg = active_vg.replace(".L", ".R")
    elif ".R" in active_vg:
        wrong_vg = active_vg.replace(".R", ".L")

    for vg in vgroups:
        if vg.name == wrong_vg:
            vgroups.remove(vg)

    # Mirror weights
    bpy.ops.object.vertex_group_mirror(use_topology=False)
    # Rename mirrored vgroup
    for vg in vgroups:
        if vg.name == active_vg + "_copy":
            if ".L" in active_vg:
                vg.name = active_vg.replace(".L", ".R").replace("_copy", "")
            elif ".R" in active_vg:
                vg.name = active_vg.replace(".R", ".L").replace("_copy", "")
    

    bpy.context.active_object.vertex_groups.active = current_vg


####################################
# REGISTER/UNREGISTER
####################################
def register():
    bpy.utils.register_class(OMV_OT_WeightsSymmetrizer)
        
def unregister():
    bpy.utils.unregister_class(OMV_OT_WeightsSymmetrizer)