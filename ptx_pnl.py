import bpy
from bpy.types import Panel

from .lib.easybpy import *

class PTX_PT_Panel(Panel):
    bl_space_type = "VIEW_3D" #패널이 보여지는 화면모드
    bl_region_type = "UI"
    bl_label = "Pose thumbnail exporter" #패널 상단 라벨
    bl_category = "pose.tools" #사이드바 패널명

    @classmethod
    def poll(cls, context):
        return bool(
            context.mode in {'OBJECT','EDIT_MESH', 'EDIT_ARMATURE','POSE'}
            and get_scene().clone_props.files_loaded
        ) 

    def draw(self, context):
      layout = self.layout

      if context.mode == 'POSE':
            row = layout.row().label(text="Output Path")
            self.layout.prop(context.scene, "directory")

            row = layout.row()
            row.scale_y = 1.5
            row.operator("object.export_all_pose", text ="Export Pose Thumnails")
          
      else:
            row = layout.row()
            row.scale_y = 1.5
            row.operator(
                "object.change_posemode",
                text="Switch to Pose Mode", 
                depress=True, icon='POSE_HLT'
            )
