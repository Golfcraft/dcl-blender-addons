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

from . import ot_armature_symmetrizer
from . import ot_weights_symmetrizer
from . import ot_export
from . import pt_ohmyverse_dcl_tools

bl_info = {
    "name": "Ohmyverse DCL Tools",
    "author": "Ohmyverse Team, carlosmu <carlos.damian.munoz@gmail.com>",
    "blender": (3, 0, 0),
    "version": (0, 1, 0),
    "category": "DCL",
    "location": "3D View -> Sidebar",
    "description": "Ohmyverse tools for improve DCL workflows",
    "warning": "",
    "doc_url": "https://github.com/Golfcraft/dcl-blender-addons",
    "tracker_url": "https://github.com/Golfcraft/dcl-blender-addons",
}

####################################
# REGISTER/UNREGISTER
####################################

def register():
    ot_armature_symmetrizer.register()
    ot_weights_symmetrizer.register()
    # ot_export.register()
    pt_ohmyverse_dcl_tools.register()


def unregister():
    ot_armature_symmetrizer.unregister()
    ot_weights_symmetrizer.unregister()
    # ot_export.unregister()
    pt_ohmyverse_dcl_tools.unregister()