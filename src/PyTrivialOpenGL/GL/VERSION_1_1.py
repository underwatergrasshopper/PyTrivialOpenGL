import ctypes as _ctypes

from ..C_GL.VERSION_1_1.Constants import *
from ..C_GL import VERSION_1_1 as _C_GL_1_1
from ._Support import (
    _get_num_of_get_values, 
    _get_read_pixels_format_count, 
    _get_read_pixels_type_size, 
    _get_tex_parameter_length,
    _get_tex_format_element_number,
    _get_tex_type_mul_div_size,
    _get_tex_level_parameter_number,
    _get_acceptable_tex_target_ids,
    _get_call_lists_c_type,
    _get_call_lists_py_type,
    _get_tex_env_params_length,
    _get_tex_gen_params_length,
)
from ..Exceptions import CacheMismatch

### inner support ###

def _list_part_to_c_array(l_type, l, exact_len, c_type):
    num_of_elements_to_take = min(exact_len, len(l))

    return (c_type * exact_len)(*(l_type(l[ix]) for ix in range(num_of_elements_to_take)))

def _list_to_c_array(l_type, l, min_len, c_type):
    return (c_type * max(min_len, len(l)))(*(l_type(e) for e in l))

def _gl_type_id_to_c_type(type_):
    if type_ == GL_BYTE:                return _C_GL_1_1.GLbyte
    elif type_ == GL_UNSIGNED_BYTE:     return _C_GL_1_1.GLubyte
    elif type_ == GL_SHORT:             return _C_GL_1_1.GLshort
    elif type_ == GL_UNSIGNED_SHORT:    return _C_GL_1_1.GLushort
    elif type_ == GL_INT:               return _C_GL_1_1.GLint
    elif type_ == GL_UNSIGNED_INT:      return _C_GL_1_1.GLuint
    elif type_ == GL_FLOAT:             return _C_GL_1_1.GLfloat
    elif type_ == GL_DOUBLE:            return _C_GL_1_1.GLdouble
    elif type_ == GL_2_BYTES:           return _C_GL_1_1.GLbyte
    elif type_ == GL_3_BYTES:           return _C_GL_1_1.GLbyte
    elif type_ == GL_4_BYTES:           return _C_GL_1_1.GLbyte
    else:
        raise ValueError("Unexpected 'type_' value.")

def _gl_type_id_to_py_type(type_):
    if type_ == GL_BYTE:                return int
    elif type_ == GL_UNSIGNED_BYTE:     return int
    elif type_ == GL_SHORT:             return int
    elif type_ == GL_UNSIGNED_SHORT:    return int
    elif type_ == GL_INT:               return int
    elif type_ == GL_UNSIGNED_INT:      return int
    elif type_ == GL_FLOAT:             return float
    elif type_ == GL_DOUBLE:            return float
    elif type_ == GL_2_BYTES:           return int   
    elif type_ == GL_3_BYTES:           return int   
    elif type_ == GL_4_BYTES:           return int   
    else:
        raise ValueError("Unexpected 'type_' value.")

def _cache_make_c_array(c_type, length):
    _cache.c_array = (c_type * length)()
    return _cache.c_array

def _cache_c_array_to_list(py_type):
    c_array = _cache.c_array
    _cache.c_array = None
    return [py_type(element) for element in c_array]

def _make_c_array(c_type, length):
    return (c_type * length)()

def _c_array_to_list(py_type, c_array):
    return [py_type(element) for element in c_array]

class _Cache:
    def __init__(self):
        self.c_vertex_array_pointer     = None
        self.c_normal_array_pointer     = None
        self.c_color_array_pointer      = None
        self.c_index_array_pointer      = None
        self.c_edge_flag_array_pointer  = None
        self.c_tex_coord_array_pointer  = None

        self.c_array                    = None


_cache = _Cache()

### Command Execution ###

def glGetError():
    """
    Returns (int).
    """
    return int(_C_GL_1_1.glGetError())

### Vertex Specification ###

# Begin and End

def glBegin(mode):
    """
    mode             : int
    """
    _C_GL_1_1.glBegin(int(mode))

def glEnd():
    _C_GL_1_1.glEnd()


# Polygon Edges

def glEdgeFlag(flag):
    """
    flag             : int
    """
    _C_GL_1_1.glEdgeFlag(int(flag))

def glEdgeFlagv(flag):
    """
    flag             : List[bool]
    """
    c_flag = _list_part_to_c_array(bool, flag, 1, _C_GL_1_1.GLboolean)
    _C_GL_1_1.glEdgeFlagv(c_flag)

# Vertex Specification

def glVertex2d(x, y):
    """
    x                : float
    y                : float
    """
    _C_GL_1_1.glVertex2d(float(x), float(y))

def glVertex2dv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 2, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glVertex2dv(c_v)

def glVertex2f(x, y):
    """
    x                : float
    y                : float
    """
    _C_GL_1_1.glVertex2f(float(x), float(y))

def glVertex2fv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 2, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glVertex2fv(c_v)

def glVertex2i(x, y):
    """
    x                : int
    y                : int
    """
    _C_GL_1_1.glVertex2i(int(x), int(y))

def glVertex2iv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 2, _C_GL_1_1.GLint)
    _C_GL_1_1.glVertex2iv(c_v)

def glVertex2s(x, y):
    """
    x                : int
    y                : int
    """
    _C_GL_1_1.glVertex2s(int(x), int(y))

def glVertex2sv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 2, _C_GL_1_1.GLshort)
    _C_GL_1_1.glVertex2sv(c_v)

def glVertex3d(x, y, z):
    """
    x                : float
    y                : float
    z                : float
    """
    _C_GL_1_1.glVertex3d(float(x), float(y), float(z))

def glVertex3dv(v):
    """
    v                : List[double]
    """
    c_v = _list_part_to_c_array(float, v, 3, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glVertex3dv(c_v)

def glVertex3f(x, y, z):
    """
    x                : float
    y                : float
    z                : float
    """
    _C_GL_1_1.glVertex3f(float(x), float(y), float(z))

def glVertex3fv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 3, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glVertex3fv(c_v)

def glVertex3i(x, y, z):
    """
    x                : int
    y                : int
    z                : int
    """
    _C_GL_1_1.glVertex3i(int(x), int(y), int(z))

def glVertex3iv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 3, _C_GL_1_1.GLint)
    _C_GL_1_1.glVertex3iv(c_v)

def glVertex3s(x, y, z):
    """
    x                : int
    y                : int
    z                : int
    """
    _C_GL_1_1.glVertex3s(int(x), int(y), int(z))

def glVertex3sv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 3, _C_GL_1_1.GLshort)
    _C_GL_1_1.glVertex3sv(c_v)

def glVertex4d(x, y, z, w):
    """
    x                : float
    y                : float
    z                : float
    w                : float
    """
    _C_GL_1_1.glVertex4d(float(x), float(y), float(z), float(w))

def glVertex4dv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 4, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glVertex4dv(c_v)

def glVertex4f(x, y, z, w):
    """
    x                : float
    y                : float
    z                : float
    w                : float
    """
    _C_GL_1_1.glVertex4f(float(x), float(y), float(z), float(w))

def glVertex4fv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 4, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glVertex4fv(c_v)

def glVertex4i(x, y, z, w):
    """
    x                : int
    y                : int
    z                : int
    w                : int
    """
    _C_GL_1_1.glVertex4i(int(x), int(y), int(z), int(w))

def glVertex4iv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 4, _C_GL_1_1.GLint)
    _C_GL_1_1.glVertex4iv(c_v)

def glVertex4s(x, y, z, w):
    """
    x                : int
    y                : int
    z                : int
    w                : int
    """
    _C_GL_1_1.glVertex4s(int(x), int(y), int(z), int(w))

def glVertex4sv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 4, _C_GL_1_1.GLshort)
    _C_GL_1_1.glVertex4sv(c_v)


def glTexCoord1d(s):
    """
    s                : float
    """
    _C_GL_1_1.glTexCoord1d(float(s))

def glTexCoord1dv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 1, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glTexCoord1dv(c_v)

def glTexCoord1f(s):
    """
    s                : float
    """
    _C_GL_1_1.glTexCoord1f(float(s))

def glTexCoord1fv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 1, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glTexCoord1fv(c_v)

def glTexCoord1i(s):
    """
    s                : int
    """
    _C_GL_1_1.glTexCoord1i(int(s))

def glTexCoord1iv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 1, _C_GL_1_1.GLint)
    _C_GL_1_1.glTexCoord1iv(c_v)

def glTexCoord1s(s):
    """
    s                : int
    """
    _C_GL_1_1.glTexCoord1s(int(s))

def glTexCoord1sv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 1, _C_GL_1_1.GLshort)
    _C_GL_1_1.glTexCoord1sv(c_v)

def glTexCoord2d(s, t):
    """
    s                : float
    t                : float
    """
    _C_GL_1_1.glTexCoord2d(float(s), float(t))

def glTexCoord2dv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 2, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glTexCoord2dv(c_v)

def glTexCoord2f(s, t):
    """
    s                : float
    t                : float
    """
    _C_GL_1_1.glTexCoord2f(float(s), float(t))

def glTexCoord2fv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 2, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glTexCoord2fv(c_v)

def glTexCoord2i(s, t):
    """
    s                : int
    t                : int
    """
    _C_GL_1_1.glTexCoord2i(int(s), int(t))

def glTexCoord2iv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 2, _C_GL_1_1.GLint)
    _C_GL_1_1.glTexCoord2iv(c_v)

def glTexCoord2s(s, t):
    """
    s                : int
    t                : int
    """
    _C_GL_1_1.glTexCoord2s(int(s), int(t))

def glTexCoord2sv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 2, _C_GL_1_1.GLshort)
    _C_GL_1_1.glTexCoord2sv(c_v)

def glTexCoord3d(s, t, r):
    """
    s                : float
    t                : float
    r                : float
    """
    _C_GL_1_1.glTexCoord3d(float(s), float(t), float(r))

def glTexCoord3dv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 3, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glTexCoord3dv(c_v)

def glTexCoord3f(s, t, r):
    """
    s                : float
    t                : float
    r                : float
    """
    _C_GL_1_1.glTexCoord3f(float(s), float(t), float(r))

def glTexCoord3fv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 3, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glTexCoord3fv(c_v)

def glTexCoord3i(s, t, r):
    """
    s                : int
    t                : int
    r                : int
    """
    _C_GL_1_1.glTexCoord3i(int(s), int(t), int(r))

def glTexCoord3iv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 3, _C_GL_1_1.GLint)
    _C_GL_1_1.glTexCoord3iv(c_v)

def glTexCoord3s(s, t, r):
    """
    s                : int
    t                : int
    r                : int
    """
    _C_GL_1_1.glTexCoord3s(int(s), int(t), int(r))

def glTexCoord3sv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 3, _C_GL_1_1.GLshort)
    _C_GL_1_1.glTexCoord3sv(c_v)

def glTexCoord4d(s, t, r, q):
    """
    s                : float
    t                : float
    r                : float
    q                : float
    """
    _C_GL_1_1.glTexCoord4d(float(s), float(t), float(r), float(q))

def glTexCoord4dv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 4, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glTexCoord4dv(c_v)

def glTexCoord4f(s, t, r, q):
    """
    s                : float
    t                : float
    r                : float
    q                : float
    """
    _C_GL_1_1.glTexCoord4f(float(s), float(t), float(r), float(q))

def glTexCoord4fv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 4, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glTexCoord4fv(c_v)

def glTexCoord4i(s, t, r, q):
    """
    s                : int
    t                : int
    r                : int
    q                : int
    """
    _C_GL_1_1.glTexCoord4i(int(s), int(t), int(r), int(q))

def glTexCoord4iv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 4, _C_GL_1_1.GLint)
    _C_GL_1_1.glTexCoord4iv(c_v)

def glTexCoord4s(s, t, r, q):
    """
    s                : int
    t                : int
    r                : int
    q                : int
    """
    _C_GL_1_1.glTexCoord4s(int(s), int(t), int(r), int(q))

def glTexCoord4sv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 4, _C_GL_1_1.GLshort)
    _C_GL_1_1.glTexCoord4sv(c_v)


def glNormal3b(nx, ny, nz):
    """
    nx               : int
    ny               : int
    nz               : int
    """
    _C_GL_1_1.glNormal3b(int(nx), int(ny), int(nz))

def glNormal3bv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 3, _C_GL_1_1.GLbyte)
    _C_GL_1_1.glNormal3bv(c_v)

def glNormal3d(nx, ny, nz):
    """
    nx               : float
    ny               : float
    nz               : float
    """
    _C_GL_1_1.glNormal3d(float(nx), float(ny), float(nz))

def glNormal3dv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 3, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glNormal3dv(c_v)

def glNormal3f(nx, ny, nz):
    """
    nx               : float
    ny               : float
    nz               : float
    """
    _C_GL_1_1.glNormal3f(float(nx), float(ny), float(nz))

def glNormal3fv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 3, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glNormal3fv(c_v)

def glNormal3i(nx, ny, nz):
    """
    nx               : int
    ny               : int
    nz               : int
    """
    _C_GL_1_1.glNormal3i(int(nx), int(ny), int(nz))

def glNormal3iv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 3, _C_GL_1_1.GLint)
    _C_GL_1_1.glNormal3iv(c_v)

def glNormal3s(nx, ny, nz):
    """
    nx               : int
    ny               : int
    nz               : int
    """
    _C_GL_1_1.glNormal3s(int(nx), int(ny), int(nz))

def glNormal3sv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 3, _C_GL_1_1.GLshort)
    _C_GL_1_1.glNormal3sv(c_v)


def glColor3b(red, green, blue):
    """
    red              : int
    green            : int
    blue             : int
    """
    _C_GL_1_1.glColor3b(int(red), int(green), int(blue))

def glColor3bv(v):
    """
    v                : List[int] | bytes
        Value range <-128, 127>.
    """
    c_v = _list_part_to_c_array(int, v, 3, _C_GL_1_1.GLbyte)
    _C_GL_1_1.glColor3bv(c_v)

def glColor3d(red, green, blue):
    """
    red              : float
    green            : float
    blue             : float
    """
    _C_GL_1_1.glColor3d(float(red), float(green), float(blue))

def glColor3dv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 3, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glColor3dv(c_v)

def glColor3f(red, green, blue):
    """
    red              : float
    green            : float
    blue             : float
    """
    _C_GL_1_1.glColor3f(float(red), float(green), float(blue))

def glColor3fv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 3, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glColor3fv(c_v)

def glColor3i(red, green, blue):
    """
    red              : int
    green            : int
    blue             : int
    """
    _C_GL_1_1.glColor3i(int(red), int(green), int(blue))

def glColor3iv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 3, _C_GL_1_1.GLint)
    _C_GL_1_1.glColor3iv(c_v)

def glColor3s(red, green, blue):
    """
    red              : int
    green            : int
    blue             : int
    """
    _C_GL_1_1.glColor3s(int(red), int(green), int(blue))

def glColor3sv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 3, _C_GL_1_1.GLshort)
    _C_GL_1_1.glColor3sv(c_v)

def glColor3ub(red, green, blue):
    """
    red              : int
    green            : int
    blue             : int
    """
    _C_GL_1_1.glColor3ub(int(red), int(green), int(blue))

def glColor3ubv(v):
    """
    v                : List[int] | bytes
        Value range <0, 255>.
    """
    c_v = _list_part_to_c_array(int, v, 3, _C_GL_1_1.GLubyte)
    _C_GL_1_1.glColor3ubv(c_v)

def glColor3ui(red, green, blue):
    """
    red              : int
    green            : int
    blue             : int
    """
    _C_GL_1_1.glColor3ui(int(red), int(green), int(blue))

def glColor3uiv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 3, _C_GL_1_1.GLuint)
    _C_GL_1_1.glColor3uiv(c_v)

def glColor3us(red, green, blue):
    """
    red              : int
    green            : int
    blue             : int
    """
    _C_GL_1_1.glColor3us(int(red), int(green), int(blue))

def glColor3usv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 3, _C_GL_1_1.GLushort)
    _C_GL_1_1.glColor3usv(c_v)

def glColor4b(red, green, blue, alpha):
    """
    red              : int
    green            : int
    blue             : int
    alpha            : int
    """
    _C_GL_1_1.glColor4b(int(red), int(green), int(blue), int(alpha))

def glColor4bv(v):
    """
    v                : List[int] | bytes
        Value range <-128, 127>.
    """
    c_v = _list_part_to_c_array(int, v, 4, _C_GL_1_1.GLbyte)
    _C_GL_1_1.glColor4bv(c_v)

def glColor4d(red, green, blue, alpha):
    """
    red              : float
    green            : float
    blue             : float
    alpha            : float
    """
    _C_GL_1_1.glColor4d(float(red), float(green), float(blue), float(alpha))

def glColor4dv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 4, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glColor4dv(c_v)

def glColor4f(red, green, blue, alpha):
    """
    red              : float
    green            : float
    blue             : float
    alpha            : float
    """
    _C_GL_1_1.glColor4f(float(red), float(green), float(blue), float(alpha))

def glColor4fv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 4, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glColor4fv(c_v)

def glColor4i(red, green, blue, alpha):
    """
    red              : int
    green            : int
    blue             : int
    alpha            : int
    """
    _C_GL_1_1.glColor4i(int(red), int(green), int(blue), int(alpha))

def glColor4iv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 4, _C_GL_1_1.GLint)
    _C_GL_1_1.glColor4iv(c_v)

def glColor4s(red, green, blue, alpha):
    """
    red              : int
    green            : int
    blue             : int
    alpha            : int
    """
    _C_GL_1_1.glColor4s(int(red), int(green), int(blue), int(alpha))

def glColor4sv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 4, _C_GL_1_1.GLshort)
    _C_GL_1_1.glColor4sv(c_v)

def glColor4ub(red, green, blue, alpha):
    """
    red              : int
    green            : int
    blue             : int
    alpha            : int
    """
    _C_GL_1_1.glColor4ub(int(red), int(green), int(blue), int(alpha))

def glColor4ubv(v):
    """
    v                : List[int] | bytes
        Value range <0, 255>
    """
    c_v = _list_part_to_c_array(int, v, 4, _C_GL_1_1.GLubyte)
    _C_GL_1_1.glColor4ubv(c_v)

def glColor4ui(red, green, blue, alpha):
    """
    red              : int
    green            : int
    blue             : int
    alpha            : int
    """
    _C_GL_1_1.glColor4ui(int(red), int(green), int(blue), int(alpha))

def glColor4uiv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 4, _C_GL_1_1.GLuint)
    _C_GL_1_1.glColor4uiv(c_v)

def glColor4us(red, green, blue, alpha):
    """
    red              : int
    green            : int
    blue             : int
    alpha            : int
    """
    _C_GL_1_1.glColor4us(int(red), int(green), int(blue), int(alpha))

def glColor4usv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 4, _C_GL_1_1.GLushort)
    _C_GL_1_1.glColor4usv(c_v)


def glIndexd(c):
    """
    c                : float
    """
    _C_GL_1_1.glIndexd(float(c))

def glIndexdv(c):
    """
    c                : List[float]
    """
    c_c = _list_part_to_c_array(float, c, 1, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glIndexdv(c_c)

def glIndexf(c):
    """
    c                : float
    """
    _C_GL_1_1.glIndexf(float(c))

def glIndexfv(c):
    """
    c                : List[float]
    """
    c_c = _list_part_to_c_array(float, c, 1, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glIndexfv(c_c)

def glIndexi(c):
    """
    c                : int
    """
    _C_GL_1_1.glIndexi(int(c))

def glIndexiv(c):
    """
    c                : List[int]
    """
    c_c = _list_part_to_c_array(int, c, 1, _C_GL_1_1.GLint)
    _C_GL_1_1.glIndexiv(c_c)

def glIndexs(c):
    """
    c                : int
    """
    _C_GL_1_1.glIndexs(int(c))

def glIndexsv(c):
    """
    c                : List[int]
    """
    c_c = _list_part_to_c_array(int, c, 1, _C_GL_1_1.GLshort)
    _C_GL_1_1.glIndexsv(c_c)

def glIndexub(c):
    """
    c                : int
    """
    _C_GL_1_1.glIndexub(int(c))

def glIndexubv(c):
    """
    c                : List[int] | bytes
    """
    c_c = _list_part_to_c_array(int, c, 1, _C_GL_1_1.GLubyte)
    _C_GL_1_1.glIndexubv(c_c)


### Vertex Arrays ###

def glVertexPointer(size, type_, stride, pointer):
    """
    size             : int
    type_            : int
    stride           : int
    pointer          : List[int | float]
    """
    py_type = _gl_type_id_to_py_type(type_)
    c_type  = _gl_type_id_to_c_type(type_)

    _cache.c_vertex_array_pointer = _list_to_c_array(py_type, pointer, 0, c_type)
    _C_GL_1_1.glVertexPointer(int(size), int(type_), int(stride), _cache.c_vertex_array_pointer)

def glNormalPointer(type_, stride, pointer):
    """
    type_            : int
    stride           : int
    pointer          : List[int | float]
    """
    py_type = _gl_type_id_to_py_type(type_)
    c_type  = _gl_type_id_to_c_type(type_)

    _cache.c_normal_array_pointer = _list_to_c_array(py_type, pointer, 0, c_type)
    _C_GL_1_1.glNormalPointer(int(type_), int(stride), _cache.c_normal_array_pointer)

def glColorPointer(size, type_, stride, pointer):
    """
    size             : int
    type_            : int
    stride           : int
    pointer          : List[int | float]
    """
    py_type = _gl_type_id_to_py_type(type_)
    c_type  = _gl_type_id_to_c_type(type_)

    _cache.c_color_array_pointer = _list_to_c_array(py_type, pointer, 0, c_type)
    _C_GL_1_1.glColorPointer(int(size), int(type_), int(stride), _cache.c_color_array_pointer)

def glIndexPointer(type_, stride, pointer):
    """
    type_            : int
    stride           : int
    pointer          : List[int | float]
    """
    py_type = _gl_type_id_to_py_type(type_)
    c_type  = _gl_type_id_to_c_type(type_)

    _cache.c_index_array_pointer = _list_to_c_array(py_type, pointer, 0, c_type)
    _C_GL_1_1.glIndexPointer(int(type_), int(stride), _cache.c_index_array_pointer)

def glEdgeFlagPointer(stride, pointer):
    """
    stride           : int
    pointer          : List[int]
    """
    _cache.c_edge_flag_array_pointer = _list_to_c_array(int, pointer, 0, _C_GL_1_1.GLboolean)
    _C_GL_1_1.glEdgeFlagPointer(int(stride), _cache.c_edge_flag_array_pointer)

def glTexCoordPointer(size, type_, stride, pointer):
    """
    size             : int
    type_            : int
    stride           : int
    pointer          : List[int | float]
    """
    py_type = _gl_type_id_to_py_type(type_)
    c_type  = _gl_type_id_to_c_type(type_)

    _cache.c_tex_coord_array_pointer = _list_to_c_array(py_type, pointer, 0, c_type)
    _C_GL_1_1.glTexCoordPointer(int(size), int(type_), int(stride), _cache.c_tex_coord_array_pointer)

def glEnableClientState(array):
    """
    array            : int
    """
    _C_GL_1_1.glEnableClientState(int(array))

def glDisableClientState(array):
    """
    array            : int
    """
    _C_GL_1_1.glDisableClientState(int(array))

def glArrayElement(i):
    """
    i                : int
    """
    _C_GL_1_1.glArrayElement(int(i))

# Drawing Commands

def glDrawArrays(mode, first, count):
    """
    mode             : int
    first            : int
    count            : int
    """
    _C_GL_1_1.glDrawArrays(int(mode), int(first), int(count))

def glDrawElements(mode, count, type_, indices):
    """
    mode             : int
    count            : int
    type_            : int
    indices          : List[int | float]
    """
    py_type = _gl_type_id_to_py_type(type_)
    c_type  = _gl_type_id_to_c_type(type_)

    c_indices = _list_to_c_array(py_type, indices, int(count), c_type)
    _C_GL_1_1.glDrawElements(int(mode), int(count), int(type_), c_indices)

# ToDo: Implement.
#def glInterleavedArrays(format_, stride, pointer):
#    """
#    format_          : int
#    stride           : int
#    pointer          : ???
#    """
#    _C_GL_1_1.glInterleavedArrays(int(format_), int(stride), ???(pointer))


### Rectangles, Matrices, Texture Coordinates ###

# Rectangles

def glRectd(x1, y1, x2, y2):
    """
    x1               : float
    y1               : float
    x2               : float
    y2               : float
    """
    _C_GL_1_1.glRectd(float(x1), float(y1), float(x2), float(y2))

def glRectdv(v1, v2):
    """
    v1               : List[float]
    v2               : List[float]
    """
    c_v1 = _list_part_to_c_array(float, v1, 2, _C_GL_1_1.GLdouble)
    c_v2 = _list_part_to_c_array(float, v2, 2, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glRectdv(c_v1, c_v2)

def glRectf(x1, y1, x2, y2):
    """
    x1               : float
    y1               : float
    x2               : float
    y2               : float
    """
    _C_GL_1_1.glRectf(float(x1), float(y1), float(x2), float(y2))

def glRectfv(v1, v2):
    """
    v1               : List[float]
    v2               : List[float]
    """
    c_v1 = _list_part_to_c_array(float, v1, 2, _C_GL_1_1.GLfloat)
    c_v2 = _list_part_to_c_array(float, v2, 2, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glRectfv(c_v1, c_v2)

def glRecti(x1, y1, x2, y2):
    """
    x1               : int
    y1               : int
    x2               : int
    y2               : int
    """
    _C_GL_1_1.glRecti(int(x1), int(y1), int(x2), int(y2))

def glRectiv(v1, v2):
    """
    v1               : List[int]
    v2               : List[int]
    """
    c_v1 = _list_part_to_c_array(int, v1, 2, _C_GL_1_1.GLint)
    c_v2 = _list_part_to_c_array(int, v2, 2, _C_GL_1_1.GLint)
    _C_GL_1_1.glRectiv(c_v1, c_v2)

def glRects(x1, y1, x2, y2):
    """
    x1               : int
    y1               : int
    x2               : int
    y2               : int
    """
    _C_GL_1_1.glRects(int(x1), int(y1), int(x2), int(y2))

def glRectsv(v1, v2):
    """
    v1               : List[int]
    v2               : List[int]
    """
    c_v1 = _list_part_to_c_array(int, v1, 2, _C_GL_1_1.GLshort)
    c_v2 = _list_part_to_c_array(int, v2, 2, _C_GL_1_1.GLshort)
    _C_GL_1_1.glRectsv(c_v1, c_v2)

# Matrices

def glMatrixMode(mode):
    """
    mode             : int
    """
    _C_GL_1_1.glMatrixMode(int(mode))

def glLoadMatrixd(m):
    """
    m                : ???
    """
    c_m = _list_part_to_c_array(float, m, 16, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glLoadMatrixd(c_m)

def glLoadMatrixf(m):
    """
    m                : ???
    """
    c_m = _list_part_to_c_array(float, m, 16, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glLoadMatrixf(c_m)

def glMultMatrixd(m):
    """
    m                : ???
    """
    c_m = _list_part_to_c_array(float, m, 16, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glMultMatrixd(c_m)

def glMultMatrixf(m):
    """
    m                : ???
    """
    c_m = _list_part_to_c_array(float, m, 16, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glMultMatrixf(c_m)

def glLoadIdentity():
    _C_GL_1_1.glLoadIdentity()

def glRotated(angle, x, y, z):
    """
    angle            : float
    x                : float
    y                : float
    z                : float
    """
    _C_GL_1_1.glRotated(float(angle), float(x), float(y), float(z))

def glRotatef(angle, x, y, z):
    """
    angle            : float
    x                : float
    y                : float
    z                : float
    """
    _C_GL_1_1.glRotatef(float(angle), float(x), float(y), float(z))

def glTranslated(x, y, z):
    """
    x                : float
    y                : float
    z                : float
    """
    _C_GL_1_1.glTranslated(float(x), float(y), float(z))

def glTranslatef(x, y, z):
    """
    x                : float
    y                : float
    z                : float
    """
    _C_GL_1_1.glTranslatef(float(x), float(y), float(z))

def glScaled(x, y, z):
    """
    x                : float
    y                : float
    z                : float
    """
    _C_GL_1_1.glScaled(float(x), float(y), float(z))

def glScalef(x, y, z):
    """
    x                : float
    y                : float
    z                : float
    """
    _C_GL_1_1.glScalef(float(x), float(y), float(z))

def glFrustum(left, right, bottom, top, zNear, zFar):
    """
    left             : float
    right            : float
    bottom           : float
    top              : float
    zNear            : float
    zFar             : float
    """
    _C_GL_1_1.glFrustum(float(left), float(right), float(bottom), float(top), float(zNear), float(zFar))

def glOrtho(left, right, bottom, top, zNear, zFar):
    """
    left             : float
    right            : float
    bottom           : float
    top              : float
    zNear            : float
    zFar             : float
    """
    _C_GL_1_1.glOrtho(float(left), float(right), float(bottom), float(top), float(zNear), float(zFar))

def glPushMatrix():
    _C_GL_1_1.glPushMatrix()

def glPopMatrix():
    _C_GL_1_1.glPopMatrix()


# Generating Texture Coordinates

def glTexGend(coord, pname, param):
    """
    coord            : int
    pname            : int
    param            : float
    """
    _C_GL_1_1.glTexGend(int(coord), int(pname), float(param))


def glTexGendv(coord, pname, params):
    """
    coord            : int
    pname            : int
    params           : List[float] | Iterable[SupportsFloat]
        Parameter is converted to list.
        All items of list are converted to float.
    """    
    params = list(params)
    n = _get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _list_part_to_c_array(float, params, n, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glTexGendv(int(coord), int(pname), c_params)

def glTexGenf(coord, pname, param):
    """
    coord            : int
    pname            : int
    param            : float
    """
    _C_GL_1_1.glTexGenf(int(coord), int(pname), float(param))

def glTexGenfv(coord, pname, params):
    """
    coord            : int
    pname            : int
    params           : List[float] | Iterable[SupportsFloat]
        Parameter is converted to list.
        All items of list are converted to float.
    """    
    params = list(params)
    n = _get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _list_part_to_c_array(float, params, n, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glTexGenfv(int(coord), int(pname), c_params)

def glTexGeni(coord, pname, param):
    """
    coord            : int
    pname            : int
    param            : int
    """
    _C_GL_1_1.glTexGeni(int(coord), int(pname), int(param))

def glTexGeniv(coord, pname, params):
    """
    coord            : int
    pname            : int
    params           : List[int] | Iterable[SupportsInt]
        Parameter is converted to list.
        All items of list are converted to int.
    """    
    params = list(params)
    n = _get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _list_part_to_c_array(int, params, n, _C_GL_1_1.GLint)
    _C_GL_1_1.glTexGeniv(int(coord), int(pname), c_params)

### Viewport and Clipping ###

# Controlling the Viewport

def glDepthRange(zNear, zFar):
    """
    zNear            : float
    zFar             : float
    """
    _C_GL_1_1.glDepthRange(float(zNear), float(zFar))

def glViewport(x, y, width, height):
    """
    x                : int
    y                : int
    width            : int
    height           : int
    """
    _C_GL_1_1.glViewport(int(x), int(y), int(width), int(height))


# Clipping

def glClipPlane(plane, equation):
    """
    plane            : int
    equation         : List[float]
    """
    c_equation = _list_part_to_c_array(float, equation, 4, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glClipPlane(int(plane), c_equation)

def glGetClipPlane(plane):
    """
    plane           : int
    Returns         : List[float]
        Corresponds to 'equation' parameter from OpenGL function specification.
    """
    c_equation = _make_c_array(_C_GL_1_1.GLdouble, 4)
    _C_GL_1_1.glGetClipPlane(int(plane), c_equation)
    return _c_array_to_list(float, c_equation)

### Lighting and Color ###

# Lighting/ Lighting Parameter Specification

def glMaterialf(face, pname, param):
    """
    face             : int
    pname            : int
    param            : float
    """
    _C_GL_1_1.glMaterialf(int(face), int(pname), float(param))

def glMaterialfv(face, pname, params):
    """
    face             : int
    pname            : int
    params           : List[float]
    """
    c_params = _list_to_c_array(float, params, 1, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glMaterialfv(int(face), int(pname), c_params)

def glMateriali(face, pname, param):
    """
    face             : int
    pname            : int
    param            : int
    """
    _C_GL_1_1.glMateriali(int(face), int(pname), int(param))

def glMaterialiv(face, pname, params):
    """
    face             : int
    pname            : int
    params           : List[int]
    """
    c_params = _list_to_c_array(int, params, 1, _C_GL_1_1.GLint)
    _C_GL_1_1.glMaterialiv(int(face), int(pname), c_params)


def glLightf(light, pname, param):
    """
    light            : int
    pname            : int
    param            : float
    """
    _C_GL_1_1.glLightf(int(light), int(pname), float(param))

def glLightfv(light, pname, params):
    """
    light            : int
    pname            : int
    params           : List[float]
    """
    c_params = _list_to_c_array(float, params, 1, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glLightfv(int(light), int(pname), c_params)

def glLighti(light, pname, param):
    """
    light            : int
    pname            : int
    param            : int
    """
    _C_GL_1_1.glLighti(int(light), int(pname), int(param))

def glLightiv(light, pname, params):
    """
    light            : int
    pname            : int
    params           : List[int]
    """
    c_params = _list_to_c_array(int, params, 1, _C_GL_1_1.GLint)
    _C_GL_1_1.glLightiv(int(light), int(pname), c_params)


def glLightModelf(pname, param):
    """
    pname            : int
    param            : float
    """
    _C_GL_1_1.glLightModelf(int(pname), float(param))

def glLightModelfv(pname, params):
    """
    pname            : int
    params           : List[float]
    """
    c_params = _list_to_c_array(float, params, 1, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glLightModelfv(int(pname), c_params)

def glLightModeli(pname, param):
    """
    pname            : int
    param            : int
    """
    _C_GL_1_1.glLightModeli(int(pname), int(param))

def glLightModeliv(pname, params):
    """
    pname            : int
    params           : List[int]
    """
    c_params = _list_to_c_array(int, params, 1, _C_GL_1_1.GLint)
    _C_GL_1_1.glLightModeliv(int(pname), c_params)


# ColorMaterial 

def glColorMaterial(face, mode):
    """
    face             : int
    mode             : int
    """
    _C_GL_1_1.glColorMaterial(int(face), int(mode))


# Flatshading

def glShadeModel(mode):
    """
    mode             : int
    """
    _C_GL_1_1.glShadeModel(int(mode))


# Queries

def glGetLightfv(light, pname):
    """
    light            : int
    pname            : int
    ReturnType       : List[float]
    """
    if pname in [GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, GL_POSITION]:
        length = 4
    elif pname in [GL_SPOT_DIRECTION]:
        length = 3
    elif pname in [GL_SPOT_EXPONENT, GL_SPOT_CUTOFF, GL_CONSTANT_ATTENUATION, GL_LINEAR_ATTENUATION, GL_QUADRATIC_ATTENUATION]:
        length = 1
    else:
        raise ValueError("Unexpected 'pname' value.")

    c_params = _make_c_array(_C_GL_1_1.GLfloat, length)
    _C_GL_1_1.glGetLightfv(int(light), int(pname), c_params)
    return _c_array_to_list(float, c_params)

def glGetLightiv(light, pname):
    """
    light            : int
    pname            : int
    ReturnType       : List[int]
    """
    if pname in [GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, GL_POSITION]:
        length = 4
    elif pname in [GL_SPOT_DIRECTION]:
        length = 3
    elif pname in [GL_SPOT_EXPONENT, GL_SPOT_CUTOFF, GL_CONSTANT_ATTENUATION, GL_LINEAR_ATTENUATION, GL_QUADRATIC_ATTENUATION]:
        length = 1
    else:
        raise ValueError("Unexpected 'pname' value.")

    c_params = _make_c_array(_C_GL_1_1.GLint, length)
    _C_GL_1_1.glGetLightiv(int(light), int(pname), c_params)
    return _c_array_to_list(int, c_params)

def glGetMaterialfv(face, pname):
    """
    face             : int
    pname            : int
    ReturnType       : List[float]
    """
    if pname in [GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, GL_EMISSION]:
        length = 4
    elif pname in [GL_COLOR_INDEXES]:
        length = 3
    elif pname in [GL_SHININESS]:
        length = 1
    else:
        raise ValueError("Unexpected 'pname' value.")

    c_params = _make_c_array(_C_GL_1_1.GLfloat, length)
    _C_GL_1_1.glGetMaterialfv(int(face), int(pname), c_params)
    return _c_array_to_list(float, c_params)

def glGetMaterialiv(face, pname):
    """
    face             : int
    pname            : int
    ReturnType       : List[int]
    """
    if pname in [GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, GL_EMISSION]:
        length = 4
    elif pname in [GL_COLOR_INDEXES]:
        length = 3
    elif pname in [GL_SHININESS]:
        length = 1
    else:
        raise ValueError("Unexpected 'pname' value.")

    c_params = _make_c_array(_C_GL_1_1.GLint, length)
    _C_GL_1_1.glGetMaterialiv(int(face), int(pname), c_params)
    return _c_array_to_list(int, c_params)

### Rendering Control and Queries ###

# Current Raster Position

def glRasterPos2d(x, y):
    """
    x                : float
    y                : float
    """
    _C_GL_1_1.glRasterPos2d(float(x), float(y))

def glRasterPos2dv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 2, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glRasterPos2dv(c_v)

def glRasterPos2f(x, y):
    """
    x                : float
    y                : float
    """
    _C_GL_1_1.glRasterPos2f(float(x), float(y))

def glRasterPos2fv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 2, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glRasterPos2fv(c_v)

def glRasterPos2i(x, y):
    """
    x                : int
    y                : int
    """
    _C_GL_1_1.glRasterPos2i(int(x), int(y))

def glRasterPos2iv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 2, _C_GL_1_1.GLint)
    _C_GL_1_1.glRasterPos2iv(c_v)

def glRasterPos2s(x, y):
    """
    x                : int
    y                : int
    """
    _C_GL_1_1.glRasterPos2s(int(x), int(y))

def glRasterPos2sv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 2, _C_GL_1_1.GLshort)
    _C_GL_1_1.glRasterPos2sv(c_v)

def glRasterPos3d(x, y, z):
    """
    x                : float
    y                : float
    z                : float
    """
    _C_GL_1_1.glRasterPos3d(float(x), float(y), float(z))

def glRasterPos3dv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 3, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glRasterPos3dv(c_v)

def glRasterPos3f(x, y, z):
    """
    x                : float
    y                : float
    z                : float
    """
    _C_GL_1_1.glRasterPos3f(float(x), float(y), float(z))

def glRasterPos3fv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 3, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glRasterPos3fv(c_v)

def glRasterPos3i(x, y, z):
    """
    x                : int
    y                : int
    z                : int
    """
    _C_GL_1_1.glRasterPos3i(int(x), int(y), int(z))

def glRasterPos3iv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 3, _C_GL_1_1.GLint)
    _C_GL_1_1.glRasterPos3iv(c_v)

def glRasterPos3s(x, y, z):
    """
    x                : int
    y                : int
    z                : int
    """
    _C_GL_1_1.glRasterPos3s(int(x), int(y), int(z))

def glRasterPos3sv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 3, _C_GL_1_1.GLshort)
    _C_GL_1_1.glRasterPos3sv(c_v)

def glRasterPos4d(x, y, z, w):
    """
    x                : float
    y                : float
    z                : float
    w                : float
    """
    _C_GL_1_1.glRasterPos4d(float(x), float(y), float(z), float(w))

def glRasterPos4dv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 4, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glRasterPos4dv(c_v)

def glRasterPos4f(x, y, z, w):
    """
    x                : float
    y                : float
    z                : float
    w                : float
    """
    _C_GL_1_1.glRasterPos4f(float(x), float(y), float(z), float(w))

def glRasterPos4fv(v):
    """
    v                : List[float]
    """
    c_v = _list_part_to_c_array(float, v, 4, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glRasterPos4fv(c_v)

def glRasterPos4i(x, y, z, w):
    """
    x                : int
    y                : int
    z                : int
    w                : int
    """
    _C_GL_1_1.glRasterPos4i(int(x), int(y), int(z), int(w))

def glRasterPos4iv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 4, _C_GL_1_1.GLint)
    _C_GL_1_1.glRasterPos4iv(c_v)

def glRasterPos4s(x, y, z, w):
    """
    x                : int
    y                : int
    z                : int
    w                : int
    """
    _C_GL_1_1.glRasterPos4s(int(x), int(y), int(z), int(w))

def glRasterPos4sv(v):
    """
    v                : List[int]
    """
    c_v = _list_part_to_c_array(int, v, 4, _C_GL_1_1.GLshort)
    _C_GL_1_1.glRasterPos4sv(c_v)

### Rasterization ###

# Points

def glPointSize(size):
    """
    size             : float
    """
    _C_GL_1_1.glPointSize(float(size))

# Line Segments

def glLineWidth(width):
    """
    width            : float
    """
    _C_GL_1_1.glLineWidth(float(width))


# Other Line Segments Features

def glLineStipple(factor, pattern):
    """
    factor           : int
    pattern          : int
    """
    _C_GL_1_1.glLineStipple(int(factor), int(pattern))

# Stipple Query


def glGetPolygonStipple():
    """
    Returns         : bytes
        Equivalent of 'mask' parameter.
    """
    size = 32 * 32 // 8
    c_mask = (_C_GL_1_1.GLubyte * size)()
    _C_GL_1_1.glGetPolygonStipple(c_mask)
    return bytes(c_mask)

# Polygons

def glFrontFace(mode):
    """
    mode             : int
    """
    _C_GL_1_1.glFrontFace(int(mode))

def glCullFace(mode):
    """
    mode             : int
    """
    _C_GL_1_1.glCullFace(int(mode))

# Stippling


def glPolygonStipple(mask):
    """
    mask             : bytes
    """
    size = 32 * 32 // 8
    c_mask = (_C_GL_1_1.GLubyte * size).from_buffer_copy(mask)
    _C_GL_1_1.glPolygonStipple(c_mask)

# Polygon Rasterization & Depth Offset

def glPolygonMode(face, mode):
    """
    face             : int
    mode             : int
    """
    _C_GL_1_1.glPolygonMode(int(face), int(mode))

def glPolygonOffset(factor, units):
    """
    factor           : float
    units            : float
    """
    _C_GL_1_1.glPolygonOffset(float(factor), float(units))

# Pixel Rectangles

def glPixelStoref(pname, param):
    """
    pname            : int
    param            : float
    """
    _C_GL_1_1.glPixelStoref(int(pname), float(param))

def glPixelStorei(pname, param):
    """
    pname            : int
    param            : int
    """
    _C_GL_1_1.glPixelStorei(int(pname), int(param))


# Pixel Transfer Modes

def glPixelTransferf(pname, param):
    """
    pname            : int
    param            : float
    """
    _C_GL_1_1.glPixelTransferf(int(pname), float(param))

def glPixelTransferi(pname, param):
    """
    pname            : int
    param            : int
    """
    _C_GL_1_1.glPixelTransferi(int(pname), int(param))

# ToDo: Implement.
#def glPixelMapfv(map_, mapsize, values):
#    """
#    map_             : int
#    mapsize          : int
#    values           : ???
#    """
#    _C_GL_1_1.glPixelMapfv(int(map_), int(mapsize), ???(values))

#def glPixelMapuiv(map_, mapsize, values):
#    """
#    map_             : int
#    mapsize          : int
#    values           : ???
#    """
#    _C_GL_1_1.glPixelMapuiv(int(map_), int(mapsize), ???(values))

#def glPixelMapusv(map_, mapsize, values):
#    """
#    map_             : int
#    mapsize          : int
#    values           : ???
#    """
#    _C_GL_1_1.glPixelMapusv(int(map_), int(mapsize), ???(values))


# Enumerated Queries

#def glGetPixelMapfv(map_, values):
#    """
#    map_             : int
#    values           : ???
#    """
#    _C_GL_1_1.glGetPixelMapfv(int(map_), ???(values))

#def glGetPixelMapuiv(map_, values):
#    """
#    map_             : int
#    values           : ???
#    """
#    _C_GL_1_1.glGetPixelMapuiv(int(map_), ???(values))

#def glGetPixelMapusv(map_, values):
#    """
#    map_             : int
#    values           : ???
#    """
#    _C_GL_1_1.glGetPixelMapusv(int(map_), ???(values))


# Rasterization of Pixel Rectangles

def glDrawPixels(width, height, format_, type_, pixels):
    """
    width            : int
    height           : int
    format_          : int
    type_            : int
    pixels           : bytes
    pixels           : List[float | int]
        Acceptable when 'type_' is GL_FLOAT and 'format_' is either GL_RGB or GL_RGBA.
        Each element of list 'pixels' represents single color channel or alpha channel.
    """
    if isinstance(pixels, list):
        if type_ == GL_FLOAT and format_ in [GL_RGB, GL_RGBA]:
            pixel_size  = 3 if format_ is GL_RGB else 4
            size        = int(width) * int(height) * pixel_size
            c_pixels    = _list_part_to_c_array(float, pixels, size, _C_GL_1_1.GLfloat)
        else:
            raise ValueError("Parameter 'pixels' is accepted as list of integers or floats, only when 'type_' is GL_FLOAT and 'format_' is either GL_RGB or GL_RGBA.")
    else:
        c_pixels = bytes(pixels)

    _C_GL_1_1.glDrawPixels(int(width), int(height), int(format_), int(type_), c_pixels)

def glPixelZoom(xfactor, yfactor):
    """
    xfactor          : float
    yfactor          : float
    """
    _C_GL_1_1.glPixelZoom(float(xfactor), float(yfactor))

# Bitmaps

def glBitmap(width, height, xorig, yorig, xmove, ymove, bitmap):
    """
    width            : int
    height           : int
    xorig            : float
    yorig            : float
    xmove            : float
    ymove            : float
    bitmap           : bytes
    """
    width = int(width)
    hight = int(height)
    size = (width * height) // 8

    c_bitmap = (_C_GL_1_1.GLubyte * size).from_buffer_copy(bitmap)
    _C_GL_1_1.glBitmap(int(width), int(height), float(xorig), float(yorig), float(xmove), float(ymove), c_bitmap)

### Texturing ###

# Texture Image Specification

def glTexImage1D(target, level, internalformat, width, border, format_, type_, pixels):
    """
    target           : int
    level            : int
    internalformat   : int
    width            : int
    border           : int
    format_          : int
    type_            : int
    pixels           : Lists[float | int]
        Acceptable, when parameter 'type_' is GL_FLOAT and parameter 'format_' is either GL_RGB or GL_RGBA.
        All elements of list are converted to floats
    """
    n = _get_tex_format_element_number(format_)
    if n is None:
        raise ValueError("Unexpected value of 'format_' parameter")

    md = _get_tex_type_mul_div_size(type_)
    if md is None:
        raise ValueError("Unexpected value of 'type_' parameter")

    m, d = md

    expected_size = int(width)      # in pixels
    single_item_size = (n * m // d) # in bytes

    if isinstance(pixels, list):
        if type_ != GL_FLOAT:
            raise ValueError("Unexpected value of parameter 'type_'. For parameter 'pixels' being list of ints or floats, parameter 'type_' must be GL_FLOAT.")
        if format_ not in [GL_RGB, GL_RGBA]:
            raise ValueError("Unexpected value of parameter 'format_'. For parameter 'lists' being list of ints or floats, parameter 'type_' must be either GL_RGB or GL_RGBA.")
        else:
            # adjusted by size of single precision float
            size = len(pixels) * 4 // single_item_size  # in pixels

            if expected_size != size: 
                raise ValueError("Unexpected size of 'pixels' parameter")

            c_pixels = _list_to_c_array(float, pixels, len(pixels), _C_GL_1_1.GLfloat)
    else:
        pixels = bytes(pixels)

        size = len(pixels) // single_item_size

        if expected_size != size:
            raise ValueError("Unexpected size of 'pixels' parameter. Should be %d pixels. It's %d pixels." % (expected_size, size))

        c_pixels = pixels

    _C_GL_1_1.glTexImage1D(int(target), int(level), int(internalformat), int(width), int(border), int(format_), int(type_), c_pixels)

def glTexImage2D(target, level, internalformat, width, height, border, format_, type_, pixels):
    """
    target           : int
    level            : int
    internalformat   : int
    width            : int
    height           : int
    border           : int
    format_          : int
    type_            : int
    pixels           : bytes
    pixels           : Lists[float | Any]
        Acceptable, when parameter 'type_' is GL_FLOAT and parameter 'format_' is either GL_RGB or GL_RGBA.
        All items are converted to floats.
    """
    n = _get_tex_format_element_number(format_)
    if n is None:
        raise ValueError("Unexpected value of 'format_' parameter")

    md = _get_tex_type_mul_div_size(type_)
    if md is None:
        raise ValueError("Unexpected value of 'type_' parameter")

    m, d = md

    width = int(width)
    height = int(height)

    expected_size = width * height  # in pixels
    single_item_size = (n * m // d) # in bytes

    if isinstance(pixels, list):
        if type_ != GL_FLOAT:
            raise ValueError("Unexpected value of 'type_' parameter. For 'pixels' parameter being list of ints or floats, 'type_' parameter must be GL_FLOAT.")
        if format_ not in [GL_RGB, GL_RGBA]:
            raise ValueError("Unexpected value of 'format_' parameter. For 'lists' parameter being list of ints or floats, 'type_' parameter must be either GL_RGB or GL_RGBA.")
        else:
            # adjusted by size of single precision float
            size = len(pixels) * 4 // single_item_size # in pixels

            if expected_size != size: 
                raise ValueError("Unexpected size of 'pixels' parameter")

            c_pixels = _list_to_c_array(float, pixels, len(pixels), _C_GL_1_1.GLfloat)
    else:
        pixels = bytes(pixels)

        size = len(pixels) // single_item_size

        if expected_size != size:
            raise ValueError("Unexpected size of 'pixels' parameter. Should be %d pixels. It's %d pixels." % (expected_size, size))

        c_pixels = pixels

    _C_GL_1_1.glTexImage2D(int(target), int(level), int(internalformat), width, height, int(border), int(format_), int(type_), c_pixels)


# Alt. Texture Image Specification Commands 

def glCopyTexImage1D(target, level, internalFormat, x, y, width, border):
    """
    target           : int
    level            : int
    internalFormat   : int
    x                : int
    y                : int
    width            : int
    border           : int
    """
    _C_GL_1_1.glCopyTexImage1D(int(target), int(level), int(internalFormat), int(x), int(y), int(width), int(border))

def glCopyTexImage2D(target, level, internalFormat, x, y, width, height, border):
    """
    target           : int
    level            : int
    internalFormat   : int
    x                : int
    y                : int
    width            : int
    height           : int
    border           : int
    """
    _C_GL_1_1.glCopyTexImage2D(int(target), int(level), int(internalFormat), int(x), int(y), int(width), int(height), int(border))

def glTexSubImage1D(target, level, xoffset, width, format_, type_, pixels):
    """
    target           : int
    level            : int
    xoffset          : int
    width            : int
    format_          : int
    type_            : int
    pixels           : Lists[float | int]
        Acceptable, when parameter 'type_' is GL_FLOAT and parameter 'format_' is either GL_RGB or GL_RGBA.
        All elements of list are converted to floats
    """
    n = _get_tex_format_element_number(format_)
    if n is None:
        raise ValueError("Unexpected value of 'format_' parameter")

    md = _get_tex_type_mul_div_size(type_)
    if md is None:
        raise ValueError("Unexpected value of 'type_' parameter")

    m, d = md

    expected_size = int(width)      # in pixels
    single_item_size = (n * m // d) # in bytes

    if isinstance(pixels, list):
        if type_ != GL_FLOAT:
            raise ValueError("Unexpected value of parameter 'type_'. For parameter 'pixels' being list of ints or floats, parameter 'type_' must be GL_FLOAT.")
        if format_ not in [GL_RGB, GL_RGBA]:
            raise ValueError("Unexpected value of parameter 'format_'. For parameter 'lists' being list of ints or floats, parameter 'type_' must be either GL_RGB or GL_RGBA.")
        else:
            # adjusted by size of single precision float
            size = len(pixels) * 4 // single_item_size  # in pixels

            if expected_size != size: 
                raise ValueError("Unexpected size of 'pixels' parameter")

            c_pixels = _list_to_c_array(float, pixels, len(pixels), _C_GL_1_1.GLfloat)
    else:
        pixels = bytes(pixels)

        size = len(pixels) // single_item_size

        if expected_size != size:
            raise ValueError("Unexpected size of 'pixels' parameter. Should be %d pixels. It's %d pixels." % (expected_size, size))

        c_pixels = pixels

    _C_GL_1_1.glTexSubImage1D(int(target), int(level), int(xoffset), int(width), int(format_), int(type_), c_pixels)

def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format_, type_, pixels):
    """
    target           : int
    level            : int
    xoffset          : int
    yoffset          : int
    width            : int
    height           : int
    format_          : int
    type_            : int
    pixels           : Lists[float | Any]
        Acceptable, when parameter 'type_' is GL_FLOAT and parameter 'format_' is either GL_RGB or GL_RGBA.
        All items are converted to floats.
    """
    n = _get_tex_format_element_number(format_)
    if n is None:
        raise ValueError("Unexpected value of 'format_' parameter")

    md = _get_tex_type_mul_div_size(type_)
    if md is None:
        raise ValueError("Unexpected value of 'type_' parameter")

    m, d = md

    width = int(width)
    height = int(height)

    expected_size = width * height  # in pixels
    single_item_size = (n * m // d) # in bytes

    if isinstance(pixels, list):
        if type_ != GL_FLOAT:
            raise ValueError("Unexpected value of 'type_' parameter. For 'pixels' parameter being list of ints or floats, 'type_' parameter must be GL_FLOAT.")
        if format_ not in [GL_RGB, GL_RGBA]:
            raise ValueError("Unexpected value of 'format_' parameter. For 'lists' parameter being list of ints or floats, 'type_' parameter must be either GL_RGB or GL_RGBA.")
        else:
            # adjusted by size of single precision float
            size = len(pixels) * 4 // single_item_size # in pixels

            if expected_size != size: 
                raise ValueError("Unexpected size of 'pixels' parameter")

            c_pixels = _list_to_c_array(float, pixels, len(pixels), _C_GL_1_1.GLfloat)
    else:
        pixels = bytes(pixels)

        size = len(pixels) // single_item_size

        if expected_size != size:
            raise ValueError("Unexpected size of 'pixels' parameter. Should be %d pixels. It's %d pixels." % (expected_size, size))

        c_pixels = pixels

    _C_GL_1_1.glTexSubImage2D(int(target), int(level), int(xoffset), int(yoffset), int(width), int(height), int(format_), int(type_), c_pixels)

def glCopyTexSubImage1D(target, level, xoffset, x, y, width):
    """
    target           : int
    level            : int
    xoffset          : int
    x                : int
    y                : int
    width            : int
    """
    _C_GL_1_1.glCopyTexSubImage1D(int(target), int(level), int(xoffset), int(x), int(y), int(width))

def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
    """
    target           : int
    level            : int
    xoffset          : int
    yoffset          : int
    x                : int
    y                : int
    width            : int
    height           : int
    """
    _C_GL_1_1.glCopyTexSubImage2D(int(target), int(level), int(xoffset), int(yoffset), int(x), int(y), int(width), int(height))


# Texture Parameters

def glTexParameterf(target, pname, param):
    """
    target           : int
    pname            : int
    param            : float
    """
    _C_GL_1_1.glTexParameterf(int(target), int(pname), float(param))

def glTexParameterfv(target, pname, params):
    """
    target           : int
    pname            : int
    params           : List[int | float]
        Values will be casted to float.
    """
    length = _get_tex_parameter_length(pname)
    if length is None:
        raise ValueError("Unexpected value of parameter 'pname'.")
    elif length > len(params):
        raise ValueError("To small length of parameter 'params'.")
    
    c_params = _list_to_c_array(float, params, length, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glTexParameterfv(int(target), int(pname), c_params)

def glTexParameteri(target, pname, param):
    """
    target           : int
    pname            : int
    param            : int
    """
    _C_GL_1_1.glTexParameteri(int(target), int(pname), int(param))

def glTexParameteriv(target, pname, params):
    """
    target           : int
    pname            : int
    params           : List[int | float]
        Values will be casted to int.
    """    
    length = _get_tex_parameter_length(pname)
    if length is None:
        raise ValueError("Unexpected value of parameter 'pname'.")
    elif length > len(params):
        raise ValueError("To small length of parameter 'params'.")
    
    c_params = _list_to_c_array(int, params, length, _C_GL_1_1.GLint)
    _C_GL_1_1.glTexParameteriv(int(target), int(pname), c_params)

# Texture Objects

def glBindTexture(target, texture):
    """
    target           : int
    texture          : int

    Note: According to OpenGL specification of this function, 
    binding with 0 should generate GL_INVALID_VALUE, 
    because default texture is not generated by glGenTextures function.
    """
    _C_GL_1_1.glBindTexture(int(target), int(texture))

def glDeleteTextures(textures):
    """
    textures         : List[int]
    """
    n = len(textures)
    c_textures = _list_to_c_array(int, textures, n, _C_GL_1_1.GLuint)
    _C_GL_1_1.glDeleteTextures(n, c_textures)

def glGenTextures(n):
    """
    n               : int
    Returns         : List[int]
        Refers to 'textures' parameter from OpenGL function specification. 
    """
    n = int(n)
    c_textures = _make_c_array(_C_GL_1_1.GLuint, n)
    _C_GL_1_1.glGenTextures(n, c_textures)
    return _c_array_to_list(int, c_textures)

def glAreTexturesResident(textures, residences = None):
    """
    textures        : List[int]
    residences      : List[bool] | None
    Returns         : bool
        True
            All textures are resident, and parameter 'residences' is untouched.
        False
            Not all textures are resident, and when parameter 'residences' is list,
            then it is set with residence information of each texture provided in parameter 'texture'.

    Note: glAreTexturesResident is deprecated. Information provided by this function might not be correct.
    """
    n = len(textures)

    c_textures      = _list_to_c_array(int, textures, n, _C_GL_1_1.GLuint)
    c_residences    = _make_c_array(_C_GL_1_1.GLboolean, n)

    is_all_resident = bool(_C_GL_1_1.glAreTexturesResident(n, c_textures, c_residences))
    if not is_all_resident and residences is not None:
        residences.clear()
        residences.extend(_c_array_to_list(bool, c_residences))

    return is_all_resident

def glPrioritizeTextures(textures, priorities):
    """
    textures         : List[int]
    priorities       : List[float]
    """
    n = len(textures)

    c_textures      = _list_to_c_array(int, textures, n, _C_GL_1_1.GLuint)
    c_priorities    = _list_to_c_array(float, priorities, n, _C_GL_1_1.GLclampf)

    _C_GL_1_1.glPrioritizeTextures(n, c_textures, c_priorities)


# Texture Environments & Texture Functions 

def glTexEnvf(target, pname, param):
    """
    target           : int
    pname            : int
    param            : float
    """
    _C_GL_1_1.glTexEnvf(int(target), int(pname), float(param))

def glTexEnvfv(target, pname, params):
    """
    target           : int
    pname            : int
    params           : List[float] | Iterable[SupportsFloat]
    """
    params = list(params)
    n = _get_tex_env_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _list_part_to_c_array(float, params, n, _C_GL_1_1.GLfloat)

    _C_GL_1_1.glTexEnvfv(int(target), int(pname), c_params)

def glTexEnvi(target, pname, param):
    """
    target           : int
    pname            : int
    param            : int
    """
    _C_GL_1_1.glTexEnvi(int(target), int(pname), int(param))

def glTexEnviv(target, pname, params):
    """
    target           : int
    pname            : int
    params           : List[int] | Iterable[SupportsInt]
    """
    params = list(params)
    n = _get_tex_env_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _list_part_to_c_array(int, params, n, _C_GL_1_1.GLint)

    _C_GL_1_1.glTexEnviv(int(target), int(pname), c_params)


# Enumerated Queries

def glGetTexEnvfv(target, pname):
    """
    target          : int | SupportsInt
    pname           : int | SupportsInt
    Returns         : List[float]
        Corresponds to 'params' parameter from OpenGL function specification.
    """
    n = _get_tex_env_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _make_c_array(_C_GL_1_1.GLfloat, n)
    _C_GL_1_1.glGetTexEnvfv(int(target), int(pname), c_params)
    return _c_array_to_list(float, c_params)

def glGetTexEnviv(target, pname):
    """
    target          : int | SupportsInt
    pname           : int | SupportsInt
    Returns         : List[int]
        Corresponds to 'params' parameter from OpenGL function specification. 
    """
    n = _get_tex_env_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _make_c_array(_C_GL_1_1.GLint, n)
    _C_GL_1_1.glGetTexEnviv(int(target), int(pname), c_params)
    return _c_array_to_list(int, c_params)

def glGetTexGendv(coord, pname):
    """
    coord           : int
    pname           : int
    Returns         : List[float]
        Corresponds to 'params' parameter from OpenGL function specification. 
    """
    n = _get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _make_c_array(_C_GL_1_1.GLdouble, n)
    _C_GL_1_1.glGetTexGendv(int(coord), int(pname), c_params)
    return _c_array_to_list(float, c_params)

def glGetTexGenfv(coord, pname):
    """
    coord           : int
    pname           : int
    Returns         : List[float]
        Corresponds to 'params' parameter from OpenGL function specification. 
    """
    n = _get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _make_c_array(_C_GL_1_1.GLfloat, n)
    _C_GL_1_1.glGetTexGenfv(int(coord), int(pname), c_params)
    return _c_array_to_list(float, c_params)

def glGetTexGeniv(coord, pname):
    """
    coord            : int
    pname            : int
    Returns         : List[int]
        Corresponds to 'params' parameter from OpenGL function specification. 
    """
    n = _get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _make_c_array(_C_GL_1_1.GLint, n)
    _C_GL_1_1.glGetTexGeniv(int(coord), int(pname), c_params)
    return _c_array_to_list(int, c_params)

def glGetTexParameterfv(target, pname):
    """
    target          : int
    pname           : int
    Returns         : List[float]
        Equivalent of parameter 'params' from OpenGL functions specification.
    """
    length = _get_tex_parameter_length(pname)
    if length is None:
        raise ValueError("Unexpected value of parameter 'pname'.")
    
    c_params = _make_c_array(_C_GL_1_1.GLfloat, length)
    _C_GL_1_1.glGetTexParameterfv(int(target), int(pname), c_params)
    return _c_array_to_list(float, c_params)

def glGetTexParameteriv(target, pname):
    """
    target          : int
    pname           : int
    Returns         : List[int]
        Equivalent of parameter 'params' from OpenGL functions specification.
    """
    length = _get_tex_parameter_length(pname)
    if length is None:
        raise ValueError("Unexpected value of parameter 'pname'.")
    
    c_params = _make_c_array(_C_GL_1_1.GLint, length)
    _C_GL_1_1.glGetTexParameteriv(int(target), int(pname), c_params)
    return _c_array_to_list(int, c_params)

def glGetTexLevelParameterfv(target, level, pname):
    """
    target           : int
    level            : int
    pname            : int
    Returns          : List[float]
        Corresponds to 'params' parameter from OpenGL functions specification.
    """
    n = _get_tex_level_parameter_number(pname)
    c_params = _make_c_array(_C_GL_1_1.GLfloat, n)
    _C_GL_1_1.glGetTexLevelParameterfv(int(target), int(level), int(pname), c_params)
    return _c_array_to_list(float, c_params)

def glGetTexLevelParameteriv(target, level, pname):
    """
    target           : int
    level            : int
    pname            : int
    Returns          : List[int]
        Corresponds to 'params' parameter from OpenGL functions specification.
    """
    n = _get_tex_level_parameter_number(pname)
    c_params = _make_c_array(_C_GL_1_1.GLint, n)
    _C_GL_1_1.glGetTexLevelParameteriv(int(target), int(level), int(pname), c_params)
    return _c_array_to_list(int, c_params)

# Texture Queries

def glGetTexImage(target, level, format_, type_, is_return_list = False):
    """
    target           : int
    level            : int
    format_          : int
        Any from expected values: GL_COLOR_INDEX, GL_STENCIL_INDEX, GL_DEPTH_COMPONENT, 
        GL_RED, GL_GREEN, GL_BLUE, GL_ALPHA, GL_RGB, GL_RGBA, GL_LUMINANCE, GL_LUMINANCE_ALPHA.
    type_            : int
        Any from expected values: GL_UNSIGNED_BYTE, GL_BYTE, GL_UNSIGNED_SHORT, GL_SHORT, 
        GL_UNSIGNED_INT, GL_INT, GL_FLOAT.
    is_return_list   : bool
    Returns          : bytes | List[float]
        list of floats, when 'is_return_list' is True and 'type_' is GL_FLOAT and 'format_' is either GL_RGB or GL_RGBA.
        bytes, when 'is_return_list' is False.

        Corresponds to 'pixels' parameter from OpenGL functions specification.

    Exceptions
        ValueError 
            When any parameter have unexpected value.
        ValueError 
            When 'is_return_list' is True and 'type_' is not GL_FLOAT or 'format_' is neither GL_RGB nor GL_RGBA.
    """
    target = int(target)
    if target not in _get_acceptable_tex_target_ids():
        raise ValueError("Unexpected value of 'target' parameter")

    width   = glGetTexLevelParameteriv(target, level, GL_TEXTURE_WIDTH)[0]
    height  = glGetTexLevelParameteriv(target, level, GL_TEXTURE_HEIGHT)[0]
    # depth # for OpengGL 2.1+ for sure

    format_ = int(format_)
    type_   = int(type_)

    n = _get_tex_format_element_number(format_)
    if n is None:
        raise ValueError("Unexpected value of 'format_' parameter.")

    md = _get_tex_type_mul_div_size(type_)
    if md is None:
        raise ValueError("Unexpected value of 'type_' parameter.")

    m, d = md

    if is_return_list:
        if type_ == GL_FLOAT and format_ in [GL_RGB, GL_RGBA]:
            num_of_elements = _get_tex_format_element_number(format_)

            length = width * height * num_of_elements
            c_pixels = _make_c_array(_C_GL_1_1.GLfloat, length)

            _C_GL_1_1.glGetTexImage(int(target), int(level), format_, type_, _ctypes.cast(c_pixels, _ctypes.c_void_p))

            return _c_array_to_list(float, c_pixels)
        else:
            raise ValueError("Unexpected value of 'type_' and/or 'format_' parameters when 'is_return_list' parameter is True.")
    else:
        single_item_size = (n * m // d)             # in bytes
        size = width * height * single_item_size    # in bytes
        c_pixels = _make_c_array(_C_GL_1_1.GLubyte, size)

        _C_GL_1_1.glGetTexImage(int(target), int(level), format_, type_, _ctypes.cast(c_pixels, _ctypes.c_void_p))

        return bytes(c_pixels)


def glIsTexture(texture):
    """
    texture         : int
    Returns         : bool
    """
    return bool(_C_GL_1_1.glIsTexture(int(texture)))


### Color Sum, Fog, and Hints  ###

# Fog

def glFogf(pname, param):
    """
    pname            : int
    param            : float
    """
    _C_GL_1_1.glFogf(int(pname), float(param))

#def glFogfv(pname, params):
#    """
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glFogfv(int(pname), ???(params))

def glFogi(pname, param):
    """
    pname            : int
    param            : int
    """
    _C_GL_1_1.glFogi(int(pname), int(param))

#def glFogiv(pname, params):
#    """
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glFogiv(int(pname), ???(params))


# Hints

def glHint(target, mode):
    """
    target           : int
    mode             : int
    """
    _C_GL_1_1.glHint(int(target), int(mode))


### Drawing, Reading, and Copying Pixels ###

# Reading Pixels

def glReadPixels(x, y, width, height, format_, type_):
    """
    x               : int
    y               : int
    width           : int
    height          : int
    format_         : int
        Equivalent of 'format' parameter.
    type_           : int
        Equivalent of 'type' parameter.

    Returns         : bytes | None
        Equivalent of 'pixels' parameter.
        If type of returned object is bytes, then returned object contains pixel data.
        If type of returned object is None, then computed size of pixels is below one byte (parameter 'width' or 'height' might be zero).
    """

    format_count = _get_read_pixels_format_count(format_)
    if format_count is None:
        raise ValueError("Unexpected value of 'format_' parameter.")

    type_size = _get_read_pixels_type_size(type_)
    if type_size is None:
        raise ValueError("Unexpected value of 'type_' parameter.")

    width       = int(width)
    height      = int(height)
    pixel_size  = int(format_count * type_size)
    size        = width * height * pixel_size

    if size > 0:
        c_pixels = _make_c_array(_C_GL_1_1.GLubyte, size)
        _C_GL_1_1.glReadPixels(int(x), int(y), width, height, int(format_), int(type_), c_pixels)
        return bytes(c_pixels)
    else:
        _C_GL_1_1.glReadPixels(int(x), int(y), width, height, int(format_), int(type_), None)
        return None

def glReadBuffer(mode):
    """
    mode             : int
    """
    _C_GL_1_1.glReadBuffer(int(mode))


# Copying Pixels

def glCopyPixels(x, y, width, height, type_):
    """
    x                : int
    y                : int
    width            : int
    height           : int
    type_            : int
    """
    _C_GL_1_1.glCopyPixels(int(x), int(y), int(width), int(height), int(type_))


### Per-Fragment Operations ###

# Scissor Test

def glScissor(x, y, width, height):
    """
    x                : int
    y                : int
    width            : int
    height           : int
    """
    _C_GL_1_1.glScissor(int(x), int(y), int(width), int(height))


# Alpha Test

def glAlphaFunc(func, ref):
    """
    func             : int
    ref              : float
    """
    _C_GL_1_1.glAlphaFunc(int(func), float(ref))


# Stencil Test

def glStencilFunc(func, ref, mask):
    """
    func             : int
    ref              : int
    mask             : int
    """
    _C_GL_1_1.glStencilFunc(int(func), int(ref), int(mask))

def glStencilOp(fail, zfail, zpass):
    """
    fail             : int
    zfail            : int
    zpass            : int
    """
    _C_GL_1_1.glStencilOp(int(fail), int(zfail), int(zpass))


# Depth Buffer Test

def glDepthFunc(func):
    """
    func             : int
    """
    _C_GL_1_1.glDepthFunc(int(func))


# Blending

def glBlendFunc(sfactor, dfactor):
    """
    sfactor          : int
    dfactor          : int
    """
    _C_GL_1_1.glBlendFunc(int(sfactor), int(dfactor))


# Logical Operation 

def glLogicOp(opcode):
    """
    opcode           : int
    """
    _C_GL_1_1.glLogicOp(int(opcode))


### Whole Framebuffer Operations ###

# Selecting a Buffer for Writing

def glDrawBuffer(mode):
    """
    mode             : int
    """
    _C_GL_1_1.glDrawBuffer(int(mode))


# Fine Control of Buffer Updates

def glIndexMask(mask):
    """
    mask             : int
    """
    _C_GL_1_1.glIndexMask(int(mask))

def glColorMask(red, green, blue, alpha):
    """
    red              : bool
    green            : bool
    blue             : bool
    alpha            : bool
    """
    _C_GL_1_1.glColorMask(bool(red), bool(green), bool(blue), bool(alpha))

def glDepthMask(flag):
    """
    flag             : bool
    """
    _C_GL_1_1.glDepthMask(bool(flag))

def glStencilMask(mask):
    """
    mask             : int
    """
    _C_GL_1_1.glStencilMask(int(mask))


# Clearing the Buffers

def glClear(mask):
    """
    mask             : int
    """
    _C_GL_1_1.glClear(int(mask))

def glClearColor(red, green, blue, alpha):
    """
    red              : float
    green            : float
    blue             : float
    alpha            : float
    """
    _C_GL_1_1.glClearColor(float(red), float(green), float(blue), float(alpha))

def glClearIndex(c):
    """
    c                : float
    """
    _C_GL_1_1.glClearIndex(float(c))

def glClearDepth(depth):
    """
    depth            : float
    """
    _C_GL_1_1.glClearDepth(float(depth))

def glClearStencil(s):
    """
    s                : int
    """
    _C_GL_1_1.glClearStencil(int(s))

def glClearAccum(red, green, blue, alpha):
    """
    red              : float
    green            : float
    blue             : float
    alpha            : float
    """
    _C_GL_1_1.glClearAccum(float(red), float(green), float(blue), float(alpha))


# Accumulation Buffer

def glAccum(op, value):
    """
    op               : int
    value            : float
    """
    _C_GL_1_1.glAccum(int(op), float(value))


### Special Functions ###

# Evaluators

#def glMap1d(target, u1, u2, stride, order, points):
#    """
#    target           : int
#    u1               : float
#    u2               : float
#    stride           : int
#    order            : int
#    points           : List[float]
#    """
#    c_points = (_C_GL_1_1.GLdouble * max(int(stride) * int(order), len(points)))(*(float(point) for point in points))
#    _C_GL_1_1.glMap1d(int(target), float(u1), float(u2), int(stride), int(order), c_points)

#def glMap1f(target, u1, u2, stride, order, points):
#    """
#    target           : int
#    u1               : float
#    u2               : float
#    stride           : int
#    order            : int
#    points           : ???
#    """
#    _C_GL_1_1.glMap1f(int(target), float(u1), float(u2), int(stride), int(order), ???(points))

#def glMap2d(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
#    """
#    target           : int
#    u1               : float
#    u2               : float
#    ustride          : int
#    uorder           : int
#    v1               : float
#    v2               : float
#    vstride          : int
#    vorder           : int
#    points           : ???
#    """
#    _C_GL_1_1.glMap2d(int(target), float(u1), float(u2), int(ustride), int(uorder), float(v1), float(v2), int(vstride), int(vorder), ???(points))

#def glMap2f(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points):
#    """
#    target           : int
#    u1               : float
#    u2               : float
#    ustride          : int
#    uorder           : int
#    v1               : float
#    v2               : float
#    vstride          : int
#    vorder           : int
#    points           : ???
#    """
#    _C_GL_1_1.glMap2f(int(target), float(u1), float(u2), int(ustride), int(uorder), float(v1), float(v2), int(vstride), int(vorder), ???(points))


def glEvalCoord1d(u):
    """
    u                : float
    """
    _C_GL_1_1.glEvalCoord1d(float(u))

#def glEvalCoord1dv(u):
#    """
#    u                : ???
#    """
#    _C_GL_1_1.glEvalCoord1dv(???(u))

def glEvalCoord1f(u):
    """
    u                : float
    """
    _C_GL_1_1.glEvalCoord1f(float(u))

#def glEvalCoord1fv(u):
#    """
#    u                : ???
#    """
#    _C_GL_1_1.glEvalCoord1fv(???(u))

def glEvalCoord2d(u, v):
    """
    u                : float
    v                : float
    """
    _C_GL_1_1.glEvalCoord2d(float(u), float(v))

#def glEvalCoord2dv(u):
#    """
#    u                : ???
#    """
#    _C_GL_1_1.glEvalCoord2dv(???(u))

def glEvalCoord2f(u, v):
    """
    u                : float
    v                : float
    """
    _C_GL_1_1.glEvalCoord2f(float(u), float(v))

#def glEvalCoord2fv(u):
#    """
#    u                : ???
#    """
#    _C_GL_1_1.glEvalCoord2fv(???(u))


def glMapGrid1d(un, u1, u2):
    """
    un               : int
    u1               : float
    u2               : float
    """
    _C_GL_1_1.glMapGrid1d(int(un), float(u1), float(u2))

def glMapGrid1f(un, u1, u2):
    """
    un               : int
    u1               : float
    u2               : float
    """
    _C_GL_1_1.glMapGrid1f(int(un), float(u1), float(u2))

def glMapGrid2d(un, u1, u2, vn, v1, v2):
    """
    un               : int
    u1               : float
    u2               : float
    vn               : int
    v1               : float
    v2               : float
    """
    _C_GL_1_1.glMapGrid2d(int(un), float(u1), float(u2), int(vn), float(v1), float(v2))

def glMapGrid2f(un, u1, u2, vn, v1, v2):
    """
    un               : int
    u1               : float
    u2               : float
    vn               : int
    v1               : float
    v2               : float
    """
    _C_GL_1_1.glMapGrid2f(int(un), float(u1), float(u2), int(vn), float(v1), float(v2))


def glEvalMesh1(mode, i1, i2):
    """
    mode             : int
    i1               : int
    i2               : int
    """
    _C_GL_1_1.glEvalMesh1(int(mode), int(i1), int(i2))

def glEvalMesh2(mode, i1, i2, j1, j2):
    """
    mode             : int
    i1               : int
    i2               : int
    j1               : int
    j2               : int
    """
    _C_GL_1_1.glEvalMesh2(int(mode), int(i1), int(i2), int(j1), int(j2))


def glEvalPoint1(i):
    """
    i                : int
    """
    _C_GL_1_1.glEvalPoint1(int(i))

def glEvalPoint2(i, j):
    """
    i                : int
    j                : int
    """
    _C_GL_1_1.glEvalPoint2(int(i), int(j))


# Enumerated Query

#def glGetMapdv(target, query, v):
#    """
#    target           : int
#    query            : int
#    v                : ???
#    """
#    _C_GL_1_1.glGetMapdv(int(target), int(query), ???(v))

#def glGetMapfv(target, query, v):
#    """
#    target           : int
#    query            : int
#    v                : ???
#    """
#    _C_GL_1_1.glGetMapfv(int(target), int(query), ???(v))

#def glGetMapiv(target, query, v):
#    """
#    target           : int
#    query            : int
#    v                : ???
#    """
#    _C_GL_1_1.glGetMapiv(int(target), int(query), ???(v))


# Selection

def glInitNames():
    _C_GL_1_1.glInitNames()

def glPopName():
    _C_GL_1_1.glPopName()

def glPushName(name):
    """
    name             : int
    """
    _C_GL_1_1.glPushName(int(name))

def glLoadName(name):
    """
    name             : int
    """
    _C_GL_1_1.glLoadName(int(name))

def glRenderMode(mode):
    """
    mode             : int
    Returns (int).
    """
    return int(_C_GL_1_1.glRenderMode(int(mode)))

#def glSelectBuffer(size, buffer):
#    """
#    size             : int
#    buffer           : ???
#    """
#    _C_GL_1_1.glSelectBuffer(int(size), ???(buffer))


# Feedback

#def glFeedbackBuffer(size, type_, buffer):
#    """
#    size             : int
#    type_            : int
#    buffer           : ???
#    """
#    _C_GL_1_1.glFeedbackBuffer(int(size), int(type_), ???(buffer))

def glPassThrough(token):
    """
    token            : float
    """
    _C_GL_1_1.glPassThrough(float(token))


# Display Lists

def glNewList(list_, mode):
    """
    list_            : int
    mode             : int
    """
    _C_GL_1_1.glNewList(int(list_), int(mode))

def glEndList():
    _C_GL_1_1.glEndList()

def glCallList(list_):
    """
    list_            : int
    """
    _C_GL_1_1.glCallList(int(list_))

def glCallLists(type_, lists):
    """
    type_            : int
    lists            : List[int | float]
    lists            : bytes
        Acceptable when parameter 'type_' is  GL_UNSIGNED_BYTE.
    lists            : str
        Acceptable when parameter 'type_' is  GL_UNSIGNED_INT.
    """

    if isinstance(lists, bytes):
        if type_ == GL_UNSIGNED_BYTE:
            n = len(lists)
            _C_GL_1_1.glCallLists(n, int(type_), lists)
        else:
            raise ValueError("Unexpected value of parameter 'type_'. For parameter 'lists' being bytes, parameter 'type_' must be GL_UNSIGNED_BYTE.")

    elif isinstance(lists, str):
        if type_ == GL_UNSIGNED_INT:
            n = len(lists)
            c_lists = (_C_GL_1_1.GLuint * n)(*(ord(c) for c in lists))
            _C_GL_1_1.glCallLists(n, int(type_), c_lists)
        else:
            raise ValueError("Unexpected value of parameter 'type_'. For parameter 'lists' being list of integers or floats, parameter 'type_' must be GL_UNSIGNED_INT.")

    else:
        n = len(lists)
        if type_ == GL_2_BYTES:     n //= 2
        elif type_ == GL_3_BYTES:   n //= 3
        elif type_ == GL_4_BYTES:   n //= 4

        c_type      = _get_call_lists_c_type(type_)
        py_types    = _get_call_lists_py_type(type_)

        c_lists = _list_part_to_c_array(py_types, lists, len(lists), c_type)
        _C_GL_1_1.glCallLists(n, int(type_), c_lists)

def glListBase(base):
    """
    base             : int
    """
    _C_GL_1_1.glListBase(int(base))

def glGenLists(range_):
    """
    range_           : int
    Returns (int).
    """
    return int(_C_GL_1_1.glGenLists(int(range_)))

def glIsList(list_):
    """
    list_            : int
    Returns (bool).
    """
    return bool(_C_GL_1_1.glIsList(int(list_)))

def glDeleteLists(list_, range_):
    """
    list_            : int
    range_           : int
    """
    _C_GL_1_1.glDeleteLists(int(list_), int(range_))


### Synchronization ###

# Flush and Finish 

def glFlush():
    _C_GL_1_1.glFlush()

def glFinish():
    _C_GL_1_1.glFinish()


### State and State Requests  ###

def glDisable(cap):
    """
    cap              : int
    """
    _C_GL_1_1.glDisable(int(cap))

def glEnable(cap):
    """
    cap              : int
    """
    _C_GL_1_1.glEnable(int(cap))


# Simple Queries

def glGetBooleanv(pname):
    """
    pname            : int
    params           : List[bool]
        Equivalent of 'params'.
    """
    num = _get_num_of_get_values(pname)
    if num is None:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _make_c_array(_C_GL_1_1.GLboolean, num)
    _C_GL_1_1.glGetBooleanv(int(pname), c_params)
    return _c_array_to_list(bool, c_params)

def glGetIntegerv(pname):
    """
    pname           : int
    ReturnType      : List[int]
        Equivalent of 'params'.
    """
    num = _get_num_of_get_values(pname)
    if num is None:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _make_c_array(_C_GL_1_1.GLint, num)
    _C_GL_1_1.glGetIntegerv(int(pname), c_params)
    return _c_array_to_list(int, c_params)

def glGetFloatv(pname):
    """
    pname            : int
    ReturnType       : List[float]
        Equivalent of 'params'.
    """
    num = _get_num_of_get_values(pname)
    if num is None:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _make_c_array(_C_GL_1_1.GLfloat, num)
    _C_GL_1_1.glGetFloatv(int(pname), c_params)
    return _c_array_to_list(float, c_params)


def glGetDoublev(pname):
    """
    pname            : int
    n                : int
        Number of floats to get.
    ReturnType       : List[float]
        Equivalent of 'params'.
    """
    num = _get_num_of_get_values(pname)
    if num is None:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _make_c_array(_C_GL_1_1.GLdouble, num)
    _C_GL_1_1.glGetDoublev(int(pname), c_params)
    return _c_array_to_list(float, c_params)

def glIsEnabled(cap):
    """
    cap              : int
    Returns (bool).
    """
    return bool(_C_GL_1_1.glIsEnabled(int(cap)))

# Pointer and String Queries 

def glGetPointerv(pname):
    """
    pname           : int
    Returns         : List[int | float]
        List of all array elements.
        Equivalent of 'params' from OpenGl function specification.
    Exceptions
        CacheMismatch
            When cashed array mismatch actual array pointer. 
            To get actual array pointer, use function 'PyTrivialOpenGL.C_GL.glGetPointerv'.
    """

    if pname in [GL_FEEDBACK_BUFFER_POINTER, GL_SELECTION_BUFFER_POINTER]:
        raise ValueError("Unsupported value of 'pname'.")

    c_array = {
        # Note: Commented elements are from OpenGL above 1.1 or unsupported by this package.
        GL_COLOR_ARRAY_POINTER              : _cache.c_color_array_pointer, 
        GL_EDGE_FLAG_ARRAY_POINTER          : _cache.c_edge_flag_array_pointer, 
        # GL_FOG_COORD_ARRAY_POINTER          : _cache.???, 
        # GL_FEEDBACK_BUFFER_POINTER          : _cache.???, 
        GL_INDEX_ARRAY_POINTER              : _cache.c_index_array_pointer, 
        GL_NORMAL_ARRAY_POINTER             : _cache.c_normal_array_pointer, 
        # GL_SECONDARY_COLOR_ARRAY_POINTER    : _cache.???, 
        # GL_SELECTION_BUFFER_POINTER         : _cache.???, 
        GL_TEXTURE_COORD_ARRAY_POINTER      : _cache.c_tex_coord_array_pointer,
        GL_VERTEX_ARRAY_POINTER             : _cache.c_vertex_array_pointer,
    }.get(pname, None)

    if pname is None:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _ctypes.c_void_p(None)
    _C_GL_1_1.glGetPointerv(int(pname), _ctypes.byref(c_params))

    if c_array is None:
        if c_params.value is None or c_params.value == 0:
            return []
        else:
            # This happens when first is called C_GL.gl{...}Pointer (which not cache any arrays) instead of GL.gl{...}Pointer and then this function is called.
            raise CacheMismatch("Mismatch of cached array (by PyTrivialOpenGL) and actual array pointer. To get actual array pointer, use function 'PyTrivialOpenGL.C_GL.glGetPointerv'.")

    if c_params.value != _ctypes.cast(c_array, _ctypes.c_void_p).value:
        # This happens when first is called C_GL.gl{...}Pointer (which not cache any arrays) instead of GL.gl{...}Pointer and then this function is called.
        raise CacheMismatch("Mismatch of cached array (by PyTrivialOpenGL) and actual array pointer. To get actual array pointer, use function 'PyTrivialOpenGL.C_GL.glGetPointerv'.")

    if len(c_array) > 0:
        if isinstance(c_array[0], float):
            return [float(e) for e in c_array]
        elif isinstance(c_array[0], int):
            return [int(e) for e in c_array]
        else:
            raise RuntimeError("Unexpected cached array type.")
    return []

def glGetString(name):
    """
    name   : int
    Returns (str).
    """
    return _ctypes.cast(_C_GL_1_1.glGetString(int(name)), _ctypes.c_char_p).value.decode()

# Saving and Restoring State

def glPushAttrib(mask):
    """
    mask             : int
    """
    _C_GL_1_1.glPushAttrib(int(mask))

def glPushClientAttrib(mask):
    """
    mask             : int
    """
    _C_GL_1_1.glPushClientAttrib(int(mask))

def glPopAttrib():
    _C_GL_1_1.glPopAttrib()

def glPopClientAttrib():
    _C_GL_1_1.glPopClientAttrib()

