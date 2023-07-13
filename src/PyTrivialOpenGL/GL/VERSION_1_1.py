import ctypes as _ctypes

from .._C_GL.VERSION_1_1.Constants import *
from .._C_GL import VERSION_1_1 as _C_GL_1_1

def _list_to_c_array(l_type, l, min_len, c_type):
    c_array_len             = max(min_len, len(l))
    num_of_elements_to_take = min(min_len, len(l))

    return (c_type * c_array_len)(*(l_type(l[ix]) for ix in range(num_of_elements_to_take)))

### Command Execution ###

def glGetError():
    """
    Returns (int).
    """
    int(_C_GL_1_1.glGetError())


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
    flag             : List[int]
    """
    c_flag = _list_to_c_array(int, flag, 1, _C_GL_1_1.GLboolean)
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
    c_v = _list_to_c_array(float, v, 2, _C_GL_1_1.GLdouble)
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
    c_v = _list_to_c_array(float, v, 2, _C_GL_1_1.GLfloat)
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
    c_v = _list_to_c_array(int, v, 2, _C_GL_1_1.GLint)
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
    c_v = _list_to_c_array(int, v, 2, _C_GL_1_1.GLshort)
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
    c_v = _list_to_c_array(float, v, 3, _C_GL_1_1.GLdouble)
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
    c_v = _list_to_c_array(float, v, 3, _C_GL_1_1.GLfloat)
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
    c_v = _list_to_c_array(int, v, 3, _C_GL_1_1.GLint)
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
    c_v = _list_to_c_array(int, v, 3, _C_GL_1_1.GLshort)
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
    c_v = _list_to_c_array(float, v, 4, _C_GL_1_1.GLdouble)
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
    c_v = _list_to_c_array(float, v, 4, _C_GL_1_1.GLfloat)
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
    c_v = _list_to_c_array(int, v, 4, _C_GL_1_1.GLint)
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
    c_v = _list_to_c_array(int, v, 4, _C_GL_1_1.GLshort)
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
    c_v = _list_to_c_array(float, v, 1, _C_GL_1_1.GLdouble)
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
    c_v = _list_to_c_array(float, v, 1, _C_GL_1_1.GLfloat)
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
    c_v = _list_to_c_array(int, v, 1, _C_GL_1_1.GLint)
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
    c_v = _list_to_c_array(int, v, 1, _C_GL_1_1.GLshort)
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
    c_v = _list_to_c_array(float, v, 2, _C_GL_1_1.GLdouble)
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
    c_v = _list_to_c_array(float, v, 2, _C_GL_1_1.GLfloat)
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
    c_v = _list_to_c_array(int, v, 2, _C_GL_1_1.GLint)
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
    c_v = _list_to_c_array(int, v, 2, _C_GL_1_1.GLshort)
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
    c_v = _list_to_c_array(float, v, 3, _C_GL_1_1.GLdouble)
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
    c_v = _list_to_c_array(float, v, 3, _C_GL_1_1.GLfloat)
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
    c_v = _list_to_c_array(int, v, 3, _C_GL_1_1.GLint)
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
    c_v = _list_to_c_array(int, v, 3, _C_GL_1_1.GLshort)
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
    c_v = _list_to_c_array(float, v, 4, _C_GL_1_1.GLdouble)
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
    c_v = _list_to_c_array(float, v, 4, _C_GL_1_1.GLfloat)
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
    c_v = _list_to_c_array(int, v, 4, _C_GL_1_1.GLint)
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
    c_v = _list_to_c_array(int, v, 4, _C_GL_1_1.GLshort)
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
    c_v = _list_to_c_array(int, v, 3, _C_GL_1_1.GLbyte)
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
    c_v = _list_to_c_array(float, v, 3, _C_GL_1_1.GLdouble)
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
    c_v = _list_to_c_array(float, v, 3, _C_GL_1_1.GLfloat)
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
    c_v = _list_to_c_array(int, v, 3, _C_GL_1_1.GLint)
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
    c_v = _list_to_c_array(int, v, 3, _C_GL_1_1.GLshort)
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
    c_v = _list_to_c_array(int, v, 3, _C_GL_1_1.GLbyte)
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
    c_v = _list_to_c_array(float, v, 3, _C_GL_1_1.GLdouble)
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
    c_v = _list_to_c_array(float, v, 3, _C_GL_1_1.GLfloat)
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
    c_v = _list_to_c_array(int, v, 3, _C_GL_1_1.GLint)
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
    c_v = _list_to_c_array(int, v, 3, _C_GL_1_1.GLshort)
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
    c_v = _list_to_c_array(int, v, 3, _C_GL_1_1.GLubyte)
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
    c_v = _list_to_c_array(int, v, 3, _C_GL_1_1.GLuint)
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
    c_v = _list_to_c_array(int, v, 3, _C_GL_1_1.GLushort)
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
    c_v = _list_to_c_array(int, v, 4, _C_GL_1_1.GLbyte)
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
    c_v = _list_to_c_array(float, v, 4, _C_GL_1_1.GLdouble)
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
    c_v = _list_to_c_array(float, v, 4, _C_GL_1_1.GLfloat)
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
    c_v = _list_to_c_array(int, v, 4, _C_GL_1_1.GLint)
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
    c_v = _list_to_c_array(int, v, 4, _C_GL_1_1.GLshort)
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
    c_v = _list_to_c_array(int, v, 4, _C_GL_1_1.GLubyte)
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
    c_v = _list_to_c_array(int, v, 4, _C_GL_1_1.GLuint)
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
    c_v = _list_to_c_array(int, v, 4, _C_GL_1_1.GLushort)
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
    c_v = _list_to_c_array(float, c, 1, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glIndexdv(c_v)

def glIndexf(c):
    """
    c                : float
    """
    _C_GL_1_1.glIndexf(float(c))

def glIndexfv(c):
    """
    c                : List[float]
    """
    c_v = _list_to_c_array(float, c, 1, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glIndexfv(c_v)

def glIndexi(c):
    """
    c                : int
    """
    _C_GL_1_1.glIndexi(int(c))

def glIndexiv(c):
    """
    c                : List[int]
    """
    c_v = _list_to_c_array(int, c, 1, _C_GL_1_1.GLint)
    _C_GL_1_1.glIndexiv(c_v)

def glIndexs(c):
    """
    c                : int
    """
    _C_GL_1_1.glIndexs(int(c))

def glIndexsv(c):
    """
    c                : List[int]
    """
    c_v = _list_to_c_array(int, c, 1, _C_GL_1_1.GLshort)
    _C_GL_1_1.glIndexsv(c_v)

def glIndexub(c):
    """
    c                : int
    """
    _C_GL_1_1.glIndexub(int(c))

def glIndexubv(c):
    """
    c                : List[int] | bytes
    """
    c_v = _list_to_c_array(int, c, 1, _C_GL_1_1.GLubyte)
    _C_GL_1_1.glIndexubv(c_v)


### Vertex Arrays ###

#def glVertexPointer(size, type_, stride, pointer):
#    """
#    size             : int
#    type_            : int
#    stride           : int
#    pointer          : ???
#    """
#    _C_GL_1_1.glVertexPointer(int(size), int(type_), int(stride), ???(pointer))

#def glNormalPointer(type_, stride, pointer):
#    """
#    type_            : int
#    stride           : int
#    pointer          : ???
#    """
#    _C_GL_1_1.glNormalPointer(int(type_), int(stride), ???(pointer))

#def glColorPointer(size, type_, stride, pointer):
#    """
#    size             : int
#    type_            : int
#    stride           : int
#    pointer          : ???
#    """
#    _C_GL_1_1.glColorPointer(int(size), int(type_), int(stride), ???(pointer))

#def glIndexPointer(type_, stride, pointer):
#    """
#    type_            : int
#    stride           : int
#    pointer          : ???
#    """
#    _C_GL_1_1.glIndexPointer(int(type_), int(stride), ???(pointer))

#def glEdgeFlagPointer(stride, pointer):
#    """
#    stride           : int
#    pointer          : ???
#    """
#    _C_GL_1_1.glEdgeFlagPointer(int(stride), ???(pointer))

#def glTexCoordPointer(size, type_, stride, pointer):
#    """
#    size             : int
#    type_            : int
#    stride           : int
#    pointer          : ???
#    """
#    _C_GL_1_1.glTexCoordPointer(int(size), int(type_), int(stride), ???(pointer))

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

#def glDrawElements(mode, count, type_, indices):
#    """
#    mode             : int
#    count            : int
#    type_            : int
#    indices          : ???
#    """
#    _C_GL_1_1.glDrawElements(int(mode), int(count), int(type_), ???(indices))

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

#def glRectdv(v1, v2):
#    """
#    v1               : ???
#    v2               : ???
#    """
#    _C_GL_1_1.glRectdv(???(v1), ???(v2))

def glRectf(x1, y1, x2, y2):
    """
    x1               : float
    y1               : float
    x2               : float
    y2               : float
    """
    _C_GL_1_1.glRectf(float(x1), float(y1), float(x2), float(y2))

#def glRectfv(v1, v2):
#    """
#    v1               : ???
#    v2               : ???
#    """
#    _C_GL_1_1.glRectfv(???(v1), ???(v2))

def glRecti(x1, y1, x2, y2):
    """
    x1               : int
    y1               : int
    x2               : int
    y2               : int
    """
    _C_GL_1_1.glRecti(int(x1), int(y1), int(x2), int(y2))

#def glRectiv(v1, v2):
#    """
#    v1               : ???
#    v2               : ???
#    """
#    _C_GL_1_1.glRectiv(???(v1), ???(v2))

def glRects(x1, y1, x2, y2):
    """
    x1               : int
    y1               : int
    x2               : int
    y2               : int
    """
    _C_GL_1_1.glRects(int(x1), int(y1), int(x2), int(y2))

#def glRectsv(v1, v2):
#    """
#    v1               : ???
#    v2               : ???
#    """
#    _C_GL_1_1.glRectsv(???(v1), ???(v2))


# Matrices

def glMatrixMode(mode):
    """
    mode             : int
    """
    _C_GL_1_1.glMatrixMode(int(mode))

#def glLoadMatrixd(m):
#    """
#    m                : ???
#    """
#    _C_GL_1_1.glLoadMatrixd(???(m))

#def glLoadMatrixf(m):
#    """
#    m                : ???
#    """
#    _C_GL_1_1.glLoadMatrixf(???(m))

#def glMultMatrixd(m):
#    """
#    m                : ???
#    """
#    _C_GL_1_1.glMultMatrixd(???(m))

#def glMultMatrixf(m):
#    """
#    m                : ???
#    """
#    _C_GL_1_1.glMultMatrixf(???(m))

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

#def glTexGendv(coord, pname, params):
#    """
#    coord            : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glTexGendv(int(coord), int(pname), ???(params))

def glTexGenf(coord, pname, param):
    """
    coord            : int
    pname            : int
    param            : float
    """
    _C_GL_1_1.glTexGenf(int(coord), int(pname), float(param))

#def glTexGenfv(coord, pname, params):
#    """
#    coord            : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glTexGenfv(int(coord), int(pname), ???(params))

def glTexGeni(coord, pname, param):
    """
    coord            : int
    pname            : int
    param            : int
    """
    _C_GL_1_1.glTexGeni(int(coord), int(pname), int(param))

#def glTexGeniv(coord, pname, params):
#    """
#    coord            : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glTexGeniv(int(coord), int(pname), ???(params))


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

#def glClipPlane(plane, equation):
#    """
#    plane            : int
#    equation         : ???
#    """
#    _C_GL_1_1.glClipPlane(int(plane), ???(equation))

#def glGetClipPlane(plane, equation):
#    """
#    plane            : int
#    equation         : ???
#    """
#    _C_GL_1_1.glGetClipPlane(int(plane), ???(equation))


### Lighting and Color ###

# Lighting/ Lighting Parameter Specification

def glMaterialf(face, pname, param):
    """
    face             : int
    pname            : int
    param            : float
    """
    _C_GL_1_1.glMaterialf(int(face), int(pname), float(param))

#def glMaterialfv(face, pname, params):
#    """
#    face             : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glMaterialfv(int(face), int(pname), ???(params))

def glMateriali(face, pname, param):
    """
    face             : int
    pname            : int
    param            : int
    """
    _C_GL_1_1.glMateriali(int(face), int(pname), int(param))

#def glMaterialiv(face, pname, params):
#    """
#    face             : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glMaterialiv(int(face), int(pname), ???(params))


def glLightf(light, pname, param):
    """
    light            : int
    pname            : int
    param            : float
    """
    _C_GL_1_1.glLightf(int(light), int(pname), float(param))

#def glLightfv(light, pname, params):
#    """
#    light            : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glLightfv(int(light), int(pname), ???(params))

def glLighti(light, pname, param):
    """
    light            : int
    pname            : int
    param            : int
    """
    _C_GL_1_1.glLighti(int(light), int(pname), int(param))

#def glLightiv(light, pname, params):
#    """
#    light            : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glLightiv(int(light), int(pname), ???(params))


def glLightModelf(pname, param):
    """
    pname            : int
    param            : float
    """
    _C_GL_1_1.glLightModelf(int(pname), float(param))

#def glLightModelfv(pname, params):
#    """
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glLightModelfv(int(pname), ???(params))

def glLightModeli(pname, param):
    """
    pname            : int
    param            : int
    """
    _C_GL_1_1.glLightModeli(int(pname), int(param))

#def glLightModeliv(pname, params):
#    """
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glLightModeliv(int(pname), ???(params))


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

#def glGetLightfv(light, pname, params):
#    """
#    light            : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glGetLightfv(int(light), int(pname), ???(params))

#def glGetLightiv(light, pname, params):
#    """
#    light            : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glGetLightiv(int(light), int(pname), ???(params))

#def glGetMaterialfv(face, pname, params):
#    """
#    face             : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glGetMaterialfv(int(face), int(pname), ???(params))

#def glGetMaterialiv(face, pname, params):
#    """
#    face             : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glGetMaterialiv(int(face), int(pname), ???(params))


### Rendering Control and Queries ###

# Current Raster Position

def glRasterPos2d(x, y):
    """
    x                : float
    y                : float
    """
    _C_GL_1_1.glRasterPos2d(float(x), float(y))

#def glRasterPos2dv(v):
#    """
#    v                : ???
#    """
#    _C_GL_1_1.glRasterPos2dv(???(v))

def glRasterPos2f(x, y):
    """
    x                : float
    y                : float
    """
    _C_GL_1_1.glRasterPos2f(float(x), float(y))

#def glRasterPos2fv(v):
#    """
#    v                : ???
#    """
#    _C_GL_1_1.glRasterPos2fv(???(v))

def glRasterPos2i(x, y):
    """
    x                : int
    y                : int
    """
    _C_GL_1_1.glRasterPos2i(int(x), int(y))

#def glRasterPos2iv(v):
#    """
#    v                : ???
#    """
#    _C_GL_1_1.glRasterPos2iv(???(v))

def glRasterPos2s(x, y):
    """
    x                : int
    y                : int
    """
    _C_GL_1_1.glRasterPos2s(int(x), int(y))

#def glRasterPos2sv(v):
#    """
#    v                : ???
#    """
#    _C_GL_1_1.glRasterPos2sv(???(v))

def glRasterPos3d(x, y, z):
    """
    x                : float
    y                : float
    z                : float
    """
    _C_GL_1_1.glRasterPos3d(float(x), float(y), float(z))

#def glRasterPos3dv(v):
#    """
#    v                : ???
#    """
#    _C_GL_1_1.glRasterPos3dv(???(v))

def glRasterPos3f(x, y, z):
    """
    x                : float
    y                : float
    z                : float
    """
    _C_GL_1_1.glRasterPos3f(float(x), float(y), float(z))

#def glRasterPos3fv(v):
#    """
#    v                : ???
#    """
#    _C_GL_1_1.glRasterPos3fv(???(v))

def glRasterPos3i(x, y, z):
    """
    x                : int
    y                : int
    z                : int
    """
    _C_GL_1_1.glRasterPos3i(int(x), int(y), int(z))

#def glRasterPos3iv(v):
#    """
#    v                : ???
#    """
#    _C_GL_1_1.glRasterPos3iv(???(v))

def glRasterPos3s(x, y, z):
    """
    x                : int
    y                : int
    z                : int
    """
    _C_GL_1_1.glRasterPos3s(int(x), int(y), int(z))

#def glRasterPos3sv(v):
#    """
#    v                : ???
#    """
#    _C_GL_1_1.glRasterPos3sv(???(v))

def glRasterPos4d(x, y, z, w):
    """
    x                : float
    y                : float
    z                : float
    w                : float
    """
    _C_GL_1_1.glRasterPos4d(float(x), float(y), float(z), float(w))

#def glRasterPos4dv(v):
#    """
#    v                : ???
#    """
#    _C_GL_1_1.glRasterPos4dv(???(v))

def glRasterPos4f(x, y, z, w):
    """
    x                : float
    y                : float
    z                : float
    w                : float
    """
    _C_GL_1_1.glRasterPos4f(float(x), float(y), float(z), float(w))

#def glRasterPos4fv(v):
#    """
#    v                : ???
#    """
#    _C_GL_1_1.glRasterPos4fv(???(v))

def glRasterPos4i(x, y, z, w):
    """
    x                : int
    y                : int
    z                : int
    w                : int
    """
    _C_GL_1_1.glRasterPos4i(int(x), int(y), int(z), int(w))

#def glRasterPos4iv(v):
#    """
#    v                : ???
#    """
#    _C_GL_1_1.glRasterPos4iv(???(v))

def glRasterPos4s(x, y, z, w):
    """
    x                : int
    y                : int
    z                : int
    w                : int
    """
    _C_GL_1_1.glRasterPos4s(int(x), int(y), int(z), int(w))

#def glRasterPos4sv(v):
#    """
#    v                : ???
#    """
#    _C_GL_1_1.glRasterPos4sv(???(v))


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

#def glGetPolygonStipple(mask):
#    """
#    mask             : ???
#    """
#    _C_GL_1_1.glGetPolygonStipple(???(mask))


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

#def glPolygonStipple(mask):
#    """
#    mask             : ???
#    """
#    _C_GL_1_1.glPolygonStipple(???(mask))


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

#def glDrawPixels(width, height, format_, type_, pixels):
#    """
#    width            : int
#    height           : int
#    format_          : int
#    type_            : int
#    pixels           : ???
#    """
#    _C_GL_1_1.glDrawPixels(int(width), int(height), int(format_), int(type_), ???(pixels))

def glPixelZoom(xfactor, yfactor):
    """
    xfactor          : float
    yfactor          : float
    """
    _C_GL_1_1.glPixelZoom(float(xfactor), float(yfactor))


# Bitmaps

#def glBitmap(width, height, xorig, yorig, xmove, ymove, bitmap):
#    """
#    width            : int
#    height           : int
#    xorig            : float
#    yorig            : float
#    xmove            : float
#    ymove            : float
#    bitmap           : ???
#    """
#    _C_GL_1_1.glBitmap(int(width), int(height), float(xorig), float(yorig), float(xmove), float(ymove), ???(bitmap))


### Texturing ###

# Texture Image Specification

#def glTexImage1D(target, level, internalformat, width, border, format_, type_, pixels):
#    """
#    target           : int
#    level            : int
#    internalformat   : int
#    width            : int
#    border           : int
#    format_          : int
#    type_            : int
#    pixels           : ???
#    """
#    _C_GL_1_1.glTexImage1D(int(target), int(level), int(internalformat), int(width), int(border), int(format_), int(type_), ???(pixels))

#def glTexImage2D(target, level, internalformat, width, height, border, format_, type_, pixels):
#    """
#    target           : int
#    level            : int
#    internalformat   : int
#    width            : int
#    height           : int
#    border           : int
#    format_          : int
#    type_            : int
#    pixels           : ???
#    """
#    _C_GL_1_1.glTexImage2D(int(target), int(level), int(internalformat), int(width), int(height), int(border), int(format_), int(type_), ???(pixels))


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

#def glTexSubImage1D(target, level, xoffset, width, format_, type_, pixels):
#    """
#    target           : int
#    level            : int
#    xoffset          : int
#    width            : int
#    format_          : int
#    type_            : int
#    pixels           : ???
#    """
#    _C_GL_1_1.glTexSubImage1D(int(target), int(level), int(xoffset), int(width), int(format_), int(type_), ???(pixels))

#def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format_, type_, pixels):
#    """
#    target           : int
#    level            : int
#    xoffset          : int
#    yoffset          : int
#    width            : int
#    height           : int
#    format_          : int
#    type_            : int
#    pixels           : ???
#    """
#    _C_GL_1_1.glTexSubImage2D(int(target), int(level), int(xoffset), int(yoffset), int(width), int(height), int(format_), int(type_), ???(pixels))

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

#def glTexParameterfv(target, pname, params):
#    """
#    target           : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glTexParameterfv(int(target), int(pname), ???(params))

def glTexParameteri(target, pname, param):
    """
    target           : int
    pname            : int
    param            : int
    """
    _C_GL_1_1.glTexParameteri(int(target), int(pname), int(param))

#def glTexParameteriv(target, pname, params):
#    """
#    target           : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glTexParameteriv(int(target), int(pname), ???(params))


# Texture Objects

def glBindTexture(target, texture):
    """
    target           : int
    texture          : int
    """
    _C_GL_1_1.glBindTexture(int(target), int(texture))

#def glDeleteTextures(n, textures):
#    """
#    n                : int
#    textures         : ???
#    """
#    _C_GL_1_1.glDeleteTextures(int(n), ???(textures))

#def glGenTextures(n, textures):
#    """
#    n                : int
#    textures         : ???
#    """
#    _C_GL_1_1.glGenTextures(int(n), ???(textures))

#def glAreTexturesResident(n, textures, residences):
#    """
#    n                : int
#    textures         : ???
#    residences       : ???
#    Returns (int).
#    """
#    int(_C_GL_1_1.glAreTexturesResident(int(n), ???(textures), ???(residences)))

#def glPrioritizeTextures(n, textures, priorities):
#    """
#    n                : int
#    textures         : ???
#    priorities       : ???
#    """
#    _C_GL_1_1.glPrioritizeTextures(int(n), ???(textures), ???(priorities))


# Texture Environments & Texture Functions 

def glTexEnvf(target, pname, param):
    """
    target           : int
    pname            : int
    param            : float
    """
    _C_GL_1_1.glTexEnvf(int(target), int(pname), float(param))

#def glTexEnvfv(target, pname, params):
#    """
#    target           : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glTexEnvfv(int(target), int(pname), ???(params))

def glTexEnvi(target, pname, param):
    """
    target           : int
    pname            : int
    param            : int
    """
    _C_GL_1_1.glTexEnvi(int(target), int(pname), int(param))

#def glTexEnviv(target, pname, params):
#    """
#    target           : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glTexEnviv(int(target), int(pname), ???(params))


# Enumerated Queries

#def glGetTexEnvfv(target, pname, params):
#    """
#    target           : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glGetTexEnvfv(int(target), int(pname), ???(params))

#def glGetTexEnviv(target, pname, params):
#    """
#    target           : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glGetTexEnviv(int(target), int(pname), ???(params))

#def glGetTexGendv(coord, pname, params):
#    """
#    coord            : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glGetTexGendv(int(coord), int(pname), ???(params))

#def glGetTexGenfv(coord, pname, params):
#    """
#    coord            : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glGetTexGenfv(int(coord), int(pname), ???(params))

#def glGetTexGeniv(coord, pname, params):
#    """
#    coord            : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glGetTexGeniv(int(coord), int(pname), ???(params))


#def glGetTexParameterfv(target, pname, params):
#    """
#    target           : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glGetTexParameterfv(int(target), int(pname), ???(params))

#def glGetTexParameteriv(target, pname, params):
#    """
#    target           : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glGetTexParameteriv(int(target), int(pname), ???(params))

#def glGetTexLevelParameterfv(target, level, pname, params):
#    """
#    target           : int
#    level            : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glGetTexLevelParameterfv(int(target), int(level), int(pname), ???(params))

#def glGetTexLevelParameteriv(target, level, pname, params):
#    """
#    target           : int
#    level            : int
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glGetTexLevelParameteriv(int(target), int(level), int(pname), ???(params))


# Texture Queries

#def glGetTexImage(target, level, format_, type_, pixels):
#    """
#    target           : int
#    level            : int
#    format_          : int
#    type_            : int
#    pixels           : ???
#    """
#    _C_GL_1_1.glGetTexImage(int(target), int(level), int(format_), int(type_), ???(pixels))

def glIsTexture(texture):
    """
    texture          : int
    Returns (int).
    """
    int(_C_GL_1_1.glIsTexture(int(texture)))


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

#def glReadPixels(x, y, width, height, format_, type_, pixels):
#    """
#    x                : int
#    y                : int
#    width            : int
#    height           : int
#    format_          : int
#    type_            : int
#    pixels           : ???
#    """
#    _C_GL_1_1.glReadPixels(int(x), int(y), int(width), int(height), int(format_), int(type_), ???(pixels))

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
    red              : int
    green            : int
    blue             : int
    alpha            : int
    """
    _C_GL_1_1.glColorMask(int(red), int(green), int(blue), int(alpha))

def glDepthMask(flag):
    """
    flag             : int
    """
    _C_GL_1_1.glDepthMask(int(flag))

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
    int(_C_GL_1_1.glRenderMode(int(mode)))

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

#def glCallLists(n, type_, lists):
#    """
#    n                : int
#    type_            : int
#    lists            : ???
#    """
#    _C_GL_1_1.glCallLists(int(n), int(type_), ???(lists))

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
    int(_C_GL_1_1.glGenLists(int(range_)))

def glIsList(list_):
    """
    list_            : int
    Returns (int).
    """
    int(_C_GL_1_1.glIsList(int(list_)))

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

#def glGetBooleanv(pname, params):
#    """
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glGetBooleanv(int(pname), ???(params))

def glGetIntegerv(pname, n):
    """
    pname   : int
    n       : int
        Number of integers to get.
    Returns (List[int]).
    """
    params = (_C_GL_1_1.GLint * n)()
    _C_GL_1_1.glGetIntegerv(int(pname), _ctypes.byref(params))
    return [int(param) for param in params]

#def glGetFloatv(pname, params):
#    """
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glGetFloatv(int(pname), ???(params))

#def glGetDoublev(pname, params):
#    """
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glGetDoublev(int(pname), ???(params))

def glIsEnabled(cap):
    """
    cap              : int
    Returns (int).
    """
    int(_C_GL_1_1.glIsEnabled(int(cap)))


# Pointer and String Queries 

#def glGetPointerv(pname, params):
#    """
#    pname            : int
#    params           : ???
#    """
#    _C_GL_1_1.glGetPointerv(int(pname), ???(params))

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

