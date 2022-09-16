# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "pose-thumbnail-exporter",
    "author" : "eatdesignlove",
    "description" : "add-on for pose's thumbnail exporting",
    "blender" : (3, 2, 2),
    "version" : (0, 0, 1),
    "warning" : "",
    "category" : "Animation"
}

import bpy

from . ptx_op import PTX_OT_Export_All_Pose_Op, PTX_OT_Change_Posemode_OP
from . ptx_pnl import PTX_PT_Panel

classes = (PTX_OT_Change_Posemode_OP, PTX_OT_Export_All_Pose_Op, PTX_PT_Panel)

def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.Scene.directory = bpy.props.StringProperty(subtype='DIR_PATH')

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    
    del(bpy.types.Scene.directory)

if __name__ == "__main__":
    register()