import bpy
import os
from bpy.types import (
    Operator,
)

class PTX_OT_Change_Posemode_OP(Operator):
    bl_idname = "object.change_posemode"
    bl_label = "Change posemode"
    bl_description = "Change current mode to posemode"

    @classmethod
    def poll(cls, context):
        current_mode = bpy.context.object.mode
        if current_mode == "POSE":
            return False
        return True

    def execute(self, context):
        bpy.ops.object.mode_set(mode='POSE')
        return {'FINISHED'}


class PTX_OT_Export_All_Pose_Op(Operator):
    bl_idname = "object.export_all_pose"
    bl_label = "Export All Pose thumbnail"
    bl_description = "Export all Pose thumbnail"

    @classmethod
    def poll(cls, context):
        current_mode = bpy.context.object.mode
        if current_mode == "POSE":
            return True
        return False

    def execute(self, context):
        # armature 오브젝트 찾기
        for obj in bpy.data.objects:
            target = obj.find_armature()
            if target is not None:
                armatureObj = target
            # skybox 렌더 제외
            if obj.name == "skybox":
                obj.hide_render=True
        
        # 포즈 개수 배열
        actionsLength = len(bpy.data.actions)

        armatureObj.animation_data_create()

        # 렌더 세팅 설정하기
        bpy.context.scene.frame_start = 0
        bpy.context.scene.frame_end = actionsLength
        bpy.context.scene.render.engine = 'BLENDER_WORKBENCH'
        bpy.context.scene.render.resolution_x = 768
        bpy.context.scene.render.resolution_y = 768

        filename = bpy.path.basename(bpy.data.filepath)
        print(filename)
        print(bpy.context.scene.directory, ':::bpy.types.Scene.directory:::')

        for idx in range(actionsLength):
            # 키프레임 이동
            bpy.context.scene.frame_set(idx)
            action = bpy.data.actions[idx]
            
            # 포즈 적용
            armatureObj.animation_data.action = action

            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
            bpy.context.scene.render.filepath = os.path.join(bpy.context.scene.directory, ('pose_thumb_%d.jpg' % idx))
            bpy.ops.render.render(write_still = True)

        return {'FINISHED'}