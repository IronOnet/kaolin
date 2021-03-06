# Copyright (c) 2017 Hiroharu Kato
# Copyright (c) 2018 Nikos Kolotouros
# Copyright (c) 2019 Shichen Liu

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from .get_points_from_angles import get_points_from_angles
from .ambient_lighting import ambient_lighting
from .directional_lighting import directional_lighting
from .load_obj import load_obj
from .look import look
from .look_at import look_at
from .perspective import perspective
from .orthogonal import orthogonal
from .projection import projection
from .soft_rasterize import soft_rasterize
from .save_obj import (save_obj, save_voxel)
from .face_vertices import face_vertices
from .vertex_normals import vertex_normals
from .voxelization import voxelization
