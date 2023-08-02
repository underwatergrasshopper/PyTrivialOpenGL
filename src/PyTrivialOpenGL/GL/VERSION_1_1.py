import ctypes as _ctypes

from ..C_GL.VERSION_1_1.Constants import *
from ..C_GL import VERSION_1_1 as _C_GL_1_1
from ._Private import Support as _Support

from ..Exceptions import CacheMismatch

### Command Execution ###

def glGetError():
    """
    Returns         : int
    """
    return int(_C_GL_1_1.glGetError())

### Vertex Specification ###

# Begin and End

def glBegin(mode):
    """
    mode            : int | SupportsInt
    """
    if not isinstance(mode, int): 
        try:
            mode = int(mode)
        except Exception as exception:
            raise ValueError("Value of 'mode' can not be converted to int.") from exception

    _C_GL_1_1.glBegin(mode)

def glEnd():
    _C_GL_1_1.glEnd()

# Polygon Edges

def glEdgeFlag(flag):
    """
    flag            : bool
    """
    if not isinstance(flag, bool):
        try:
            flag = bool(flag)
        except Exception as exception:
            raise ValueError("Value of 'flag' can not be converted to bool.") from exception

    _C_GL_1_1.glEdgeFlag(flag)

def glEdgeFlagv(flag):
    """
    flag            : List[bool] | Iterable
    """
    if not isinstance(flag, list) or not all(isinstance(item, bool) for item in flag):
        try:
            flag = [bool(item) for item in flag]
        except:
            raise ValueError("Value of 'flag' can not be converted to list of bools.")
            
    c_flag = _Support.list_part_to_c_array_no_conv(flag, 1, _C_GL_1_1.GLboolean)
    _C_GL_1_1.glEdgeFlagv(c_flag)

# Vertex Specification

def glVertex2d(x, y):
    """
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    """
    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    _C_GL_1_1.glVertex2d(x, y)

def glVertex2dv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 2, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glVertex2dv(c_v)

def glVertex2f(x, y):
    """
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    """
    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    _C_GL_1_1.glVertex2f(x, y)

def glVertex2fv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 2, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glVertex2fv(c_v)

def glVertex2i(x, y):
    """
    x               : int | SupportsInt
    y               : int | SupportsInt
    """
    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    _C_GL_1_1.glVertex2i(x, y)

def glVertex2iv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 2, _C_GL_1_1.GLint)
    _C_GL_1_1.glVertex2iv(c_v)

def glVertex2s(x, y):
    """
    x               : int | SupportsInt
    y               : int | SupportsInt
    """
    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    _C_GL_1_1.glVertex2s(x, y)

def glVertex2sv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 2, _C_GL_1_1.GLshort)
    _C_GL_1_1.glVertex2sv(c_v)

def glVertex3d(x, y, z):
    """
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    z               : float | SupportsFloat
    """
    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    if not isinstance(z, float):
        try:
            z = float(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to float.") from exception

    _C_GL_1_1.glVertex3d(x, y, z)

def glVertex3dv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glVertex3dv(c_v)

def glVertex3f(x, y, z):
    """
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    z               : float | SupportsFloat
    """
    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    if not isinstance(z, float):
        try:
            z = float(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to float.") from exception

    _C_GL_1_1.glVertex3f(x, y, z)

def glVertex3fv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glVertex3fv(c_v)

def glVertex3i(x, y, z):
    """
    x               : int | SupportsInt
    y               : int | SupportsInt
    z               : int | SupportsInt
    """
    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    if not isinstance(z, int):
        try:
            z = int(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to int.") from exception

    _C_GL_1_1.glVertex3i(x, y, z)

def glVertex3iv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLint)
    _C_GL_1_1.glVertex3iv(c_v)

def glVertex3s(x, y, z):
    """
    x               : int | SupportsInt
    y               : int | SupportsInt
    z               : int | SupportsInt
    """
    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    if not isinstance(z, int):
        try:
            z = int(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to int.") from exception

    _C_GL_1_1.glVertex3s(x, y, z)

def glVertex3sv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLshort)
    _C_GL_1_1.glVertex3sv(c_v)

def glVertex4d(x, y, z, w):
    """
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    z               : float | SupportsFloat
    w               : float | SupportsFloat
    """
    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    if not isinstance(z, float):
        try:
            z = float(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to float.") from exception

    if not isinstance(w, float):
        try:
            w = float(w)
        except Exception as exception:
            raise ValueError("Value of 'w' can not be converted to float.") from exception

    _C_GL_1_1.glVertex4d(x, y, z, w)

def glVertex4dv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glVertex4dv(c_v)

def glVertex4f(x, y, z, w):
    """
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    z               : float | SupportsFloat
    w               : float | SupportsFloat
    """
    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    if not isinstance(z, float):
        try:
            z = float(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to float.") from exception

    if not isinstance(w, float):
        try:
            w = float(w)
        except Exception as exception:
            raise ValueError("Value of 'w' can not be converted to float.") from exception

    _C_GL_1_1.glVertex4f(x, y, z, w)

def glVertex4fv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glVertex4fv(c_v)

def glVertex4i(x, y, z, w):
    """
    x               : int | SupportsInt
    y               : int | SupportsInt
    z               : int | SupportsInt
    w               : int | SupportsInt
    """
    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    if not isinstance(z, int):
        try:
            z = int(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to int.") from exception

    if not isinstance(w, int):
        try:
            w = int(w)
        except Exception as exception:
            raise ValueError("Value of 'w' can not be converted to int.") from exception

    _C_GL_1_1.glVertex4i(x, y, z, w)

def glVertex4iv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLint)
    _C_GL_1_1.glVertex4iv(c_v)

def glVertex4s(x, y, z, w):
    """
    x               : int | SupportsInt
    y               : int | SupportsInt
    z               : int | SupportsInt
    w               : int | SupportsInt
    """
    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    if not isinstance(z, int):
        try:
            z = int(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to int.") from exception

    if not isinstance(w, int):
        try:
            w = int(w)
        except Exception as exception:
            raise ValueError("Value of 'w' can not be converted to int.") from exception

    _C_GL_1_1.glVertex4s(x, y, z, w)

def glVertex4sv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLshort)
    _C_GL_1_1.glVertex4sv(c_v)


def glTexCoord1d(s):
    """
    s               : float | SupportsFloat
    """
    if not isinstance(s, float):
        try:
            s = float(s)
        except Exception as exception:
            raise ValueError("Value of 's' can not be converted to float.") from exception

    _C_GL_1_1.glTexCoord1d(s)

def glTexCoord1dv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 1, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glTexCoord1dv(c_v)

def glTexCoord1f(s):
    """
    s               : float | SupportsFloat
    """
    if not isinstance(s, float):
        try:
            s = float(s)
        except Exception as exception:
            raise ValueError("Value of 's' can not be converted to float.") from exception

    _C_GL_1_1.glTexCoord1f(s)

def glTexCoord1fv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 1, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glTexCoord1fv(c_v)

def glTexCoord1i(s):
    """
    s               : int | SupportsInt
    """
    if not isinstance(s, int):
        try:
            s = int(s)
        except Exception as exception:
            raise ValueError("Value of 's' can not be converted to int.") from exception

    _C_GL_1_1.glTexCoord1i(s)

def glTexCoord1iv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 1, _C_GL_1_1.GLint)
    _C_GL_1_1.glTexCoord1iv(c_v)

def glTexCoord1s(s):
    """
    s               : int | SupportsInt
    """
    if not isinstance(s, int):
        try:
            s = int(s)
        except Exception as exception:
            raise ValueError("Value of 's' can not be converted to int.") from exception

    _C_GL_1_1.glTexCoord1s(s)

def glTexCoord1sv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")


    c_v = _Support.list_part_to_c_array_no_conv(v, 1, _C_GL_1_1.GLshort)
    _C_GL_1_1.glTexCoord1sv(c_v)

def glTexCoord2d(s, t):
    """
    s               : float | SupportsFloat
    t               : float | SupportsFloat
    """
    if not isinstance(s, float):
        try:
            s = float(s)
        except Exception as exception:
            raise ValueError("Value of 's' can not be converted to float.") from exception

    if not isinstance(t, float):
        try:
            t = float(t)
        except Exception as exception:
            raise ValueError("Value of 't' can not be converted to float.") from exception

    _C_GL_1_1.glTexCoord2d(s, t)

def glTexCoord2dv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 2, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glTexCoord2dv(c_v)

def glTexCoord2f(s, t):
    """
    s               : float | SupportsFloat
    t               : float | SupportsFloat
    """
    if not isinstance(s, float):
        try:
            s = float(s)
        except Exception as exception:
            raise ValueError("Value of 's' can not be converted to float.") from exception

    if not isinstance(t, float):
        try:
            t = float(t)
        except Exception as exception:
            raise ValueError("Value of 't' can not be converted to float.") from exception

    _C_GL_1_1.glTexCoord2f(s, t)

def glTexCoord2fv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 2, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glTexCoord2fv(c_v)

def glTexCoord2i(s, t):
    """
    s               : int | SupportsInt
    t               : int | SupportsInt
    """
    if not isinstance(s, int):
        try:
            s = int(s)
        except Exception as exception:
            raise ValueError("Value of 's' can not be converted to int.") from exception

    if not isinstance(t, int):
        try:
            t = int(t)
        except Exception as exception:
            raise ValueError("Value of 't' can not be converted to int.") from exception

    _C_GL_1_1.glTexCoord2i(s, t)

def glTexCoord2iv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")
    
    c_v = _Support.list_part_to_c_array_no_conv(v, 2, _C_GL_1_1.GLint)
    _C_GL_1_1.glTexCoord2iv(c_v)

def glTexCoord2s(s, t):
    """
    s               : int | SupportsInt
    t               : int | SupportsInt
    """
    if not isinstance(s, int):
        try:
            s = int(s)
        except Exception as exception:
            raise ValueError("Value of 's' can not be converted to int.") from exception

    if not isinstance(t, int):
        try:
            t = int(t)
        except Exception as exception:
            raise ValueError("Value of 't' can not be converted to int.") from exception

    _C_GL_1_1.glTexCoord2s(s, t)

def glTexCoord2sv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")


    c_v = _Support.list_part_to_c_array_no_conv(v, 2, _C_GL_1_1.GLshort)
    _C_GL_1_1.glTexCoord2sv(c_v)

def glTexCoord3d(s, t, r):
    """
    s               : float | SupportsFloat
    t               : float | SupportsFloat
    r               : float | SupportsFloat
    """
    if not isinstance(s, float):
        try:
            s = float(s)
        except Exception as exception:
            raise ValueError("Value of 's' can not be converted to float.") from exception

    if not isinstance(t, float):
        try:
            t = float(t)
        except Exception as exception:
            raise ValueError("Value of 't' can not be converted to float.") from exception

    if not isinstance(r, float):
        try:
            r = float(r)
        except Exception as exception:
            raise ValueError("Value of 'r' can not be converted to float.") from exception

    _C_GL_1_1.glTexCoord3d(s, t, r)

def glTexCoord3dv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glTexCoord3dv(c_v)

def glTexCoord3f(s, t, r):
    """
    s               : float | SupportsFloat
    t               : float | SupportsFloat
    r               : float | SupportsFloat
    """
    if not isinstance(s, float):
        try:
            s = float(s)
        except Exception as exception:
            raise ValueError("Value of 's' can not be converted to float.") from exception

    if not isinstance(t, float):
        try:
            t = float(t)
        except Exception as exception:
            raise ValueError("Value of 't' can not be converted to float.") from exception

    if not isinstance(r, float):
        try:
            r = float(r)
        except Exception as exception:
            raise ValueError("Value of 'r' can not be converted to float.") from exception

    _C_GL_1_1.glTexCoord3f(s, t, r)

def glTexCoord3fv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glTexCoord3fv(c_v)

def glTexCoord3i(s, t, r):
    """
    s               : int | SupportsInt
    t               : int | SupportsInt
    r               : int | SupportsInt
    """
    if not isinstance(s, int):
        try:
            s = int(s)
        except Exception as exception:
            raise ValueError("Value of 's' can not be converted to int.") from exception

    if not isinstance(t, int):
        try:
            t = int(t)
        except Exception as exception:
            raise ValueError("Value of 't' can not be converted to int.") from exception

    if not isinstance(r, int):
        try:
            r = int(r)
        except Exception as exception:
            raise ValueError("Value of 'r' can not be converted to int.") from exception

    _C_GL_1_1.glTexCoord3i(s, t, r)

def glTexCoord3iv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLint)
    _C_GL_1_1.glTexCoord3iv(c_v)

def glTexCoord3s(s, t, r):
    """
    s               : int | SupportsInt
    t               : int | SupportsInt
    r               : int | SupportsInt
    """
    if not isinstance(s, int):
        try:
            s = int(s)
        except Exception as exception:
            raise ValueError("Value of 's' can not be converted to int.") from exception

    if not isinstance(t, int):
        try:
            t = int(t)
        except Exception as exception:
            raise ValueError("Value of 't' can not be converted to int.") from exception

    if not isinstance(r, int):
        try:
            r = int(r)
        except Exception as exception:
            raise ValueError("Value of 'r' can not be converted to int.") from exception

    _C_GL_1_1.glTexCoord3s(s, t, r)

def glTexCoord3sv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLshort)
    _C_GL_1_1.glTexCoord3sv(c_v)

def glTexCoord4d(s, t, r, q):
    """
    s               : float | SupportsFloat
    t               : float | SupportsFloat
    r               : float | SupportsFloat
    q               : float | SupportsFloat
    """
    if not isinstance(s, float):
        try:
            s = float(s)
        except Exception as exception:
            raise ValueError("Value of 's' can not be converted to float.") from exception

    if not isinstance(t, float):
        try:
            t = float(t)
        except Exception as exception:
            raise ValueError("Value of 't' can not be converted to float.") from exception

    if not isinstance(r, float):
        try:
            r = float(r)
        except Exception as exception:
            raise ValueError("Value of 'r' can not be converted to float.") from exception

    if not isinstance(q, float):
        try:
            q = float(q)
        except Exception as exception:
            raise ValueError("Value of 'q' can not be converted to float.") from exception

    _C_GL_1_1.glTexCoord4d(s, t, r, q)

def glTexCoord4dv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glTexCoord4dv(c_v)

def glTexCoord4f(s, t, r, q):
    """
    s               : float | SupportsFloat
    t               : float | SupportsFloat
    r               : float | SupportsFloat
    q               : float | SupportsFloat
    """
    if not isinstance(s, float):
        try:
            s = float(s)
        except Exception as exception:
            raise ValueError("Value of 's' can not be converted to float.") from exception

    if not isinstance(t, float):
        try:
            t = float(t)
        except Exception as exception:
            raise ValueError("Value of 't' can not be converted to float.") from exception

    if not isinstance(r, float):
        try:
            r = float(r)
        except Exception as exception:
            raise ValueError("Value of 'r' can not be converted to float.") from exception

    if not isinstance(q, float):
        try:
            q = float(q)
        except Exception as exception:
            raise ValueError("Value of 'q' can not be converted to float.") from exception

    _C_GL_1_1.glTexCoord4f(s, t, r, q)

def glTexCoord4fv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glTexCoord4fv(c_v)

def glTexCoord4i(s, t, r, q):
    """
    s               : int | SupportsInt
    t               : int | SupportsInt
    r               : int | SupportsInt
    q               : int | SupportsInt
    """
    if not isinstance(s, int):
        try:
            s = int(s)
        except Exception as exception:
            raise ValueError("Value of 's' can not be converted to int.") from exception

    if not isinstance(t, int):
        try:
            t = int(t)
        except Exception as exception:
            raise ValueError("Value of 't' can not be converted to int.") from exception

    if not isinstance(r, int):
        try:
            r = int(r)
        except Exception as exception:
            raise ValueError("Value of 'r' can not be converted to int.") from exception

    if not isinstance(q, int):
        try:
            q = int(q)
        except Exception as exception:
            raise ValueError("Value of 'q' can not be converted to int.") from exception

    _C_GL_1_1.glTexCoord4i(s, t, r, q)

def glTexCoord4iv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLint)
    _C_GL_1_1.glTexCoord4iv(c_v)

def glTexCoord4s(s, t, r, q):
    """
    s               : int | SupportsInt
    t               : int | SupportsInt
    r               : int | SupportsInt
    q               : int | SupportsInt
    """
    if not isinstance(s, int):
        try:
            s = int(s)
        except Exception as exception:
            raise ValueError("Value of 's' can not be converted to int.") from exception

    if not isinstance(t, int):
        try:
            t = int(t)
        except Exception as exception:
            raise ValueError("Value of 't' can not be converted to int.") from exception

    if not isinstance(r, int):
        try:
            r = int(r)
        except Exception as exception:
            raise ValueError("Value of 'r' can not be converted to int.") from exception

    if not isinstance(q, int):
        try:
            q = int(q)
        except Exception as exception:
            raise ValueError("Value of 'q' can not be converted to int.") from exception

    _C_GL_1_1.glTexCoord4s(s, t, r, q)

def glTexCoord4sv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLshort)
    _C_GL_1_1.glTexCoord4sv(c_v)


def glNormal3b(nx, ny, nz):
    """
    nx              : int | SupportsInt
    ny              : int | SupportsInt
    nz              : int | SupportsInt
    """
    if not isinstance(nx, int):
        try:
            nx = int(nx)
        except Exception as exception:
            raise ValueError("Value of 'nx' can not be converted to int.") from exception

    if not isinstance(ny, int):
        try:
            ny = int(ny)
        except Exception as exception:
            raise ValueError("Value of 'ny' can not be converted to int.") from exception

    if not isinstance(nz, int):
        try:
            nz = int(nz)
        except Exception as exception:
            raise ValueError("Value of 'nz' can not be converted to int.") from exception

    _C_GL_1_1.glNormal3b(nx, ny, nz)

def glNormal3bv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")


    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLbyte)
    _C_GL_1_1.glNormal3bv(c_v)

def glNormal3d(nx, ny, nz):
    """
    nx              : float | SupportsFloat
    ny              : float | SupportsFloat
    nz              : float | SupportsFloat
    """
    if not isinstance(nx, float):
        try:
            nx = float(nx)
        except Exception as exception:
            raise ValueError("Value of 'nx' can not be converted to float.") from exception

    if not isinstance(ny, float):
        try:
            ny = float(ny)
        except Exception as exception:
            raise ValueError("Value of 'ny' can not be converted to float.") from exception

    if not isinstance(nz, float):
        try:
            nz = float(nz)
        except Exception as exception:
            raise ValueError("Value of 'nz' can not be converted to float.") from exception

    _C_GL_1_1.glNormal3d(nx, ny, nz)

def glNormal3dv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glNormal3dv(c_v)

def glNormal3f(nx, ny, nz):
    """
    nx              : float | SupportsFloat
    ny              : float | SupportsFloat
    nz              : float | SupportsFloat
    """
    if not isinstance(nx, float):
        try:
            nx = float(nx)
        except Exception as exception:
            raise ValueError("Value of 'nx' can not be converted to float.") from exception

    if not isinstance(ny, float):
        try:
            ny = float(ny)
        except Exception as exception:
            raise ValueError("Value of 'ny' can not be converted to float.") from exception

    if not isinstance(nz, float):
        try:
            nz = float(nz)
        except Exception as exception:
            raise ValueError("Value of 'nz' can not be converted to float.") from exception

    _C_GL_1_1.glNormal3f(nx, ny, nz)

def glNormal3fv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glNormal3fv(c_v)

def glNormal3i(nx, ny, nz):
    """
    nx              : int | SupportsInt
    ny              : int | SupportsInt
    nz              : int | SupportsInt
    """
    if not isinstance(nx, int):
        try:
            nx = int(nx)
        except Exception as exception:
            raise ValueError("Value of 'nx' can not be converted to int.") from exception

    if not isinstance(ny, int):
        try:
            ny = int(ny)
        except Exception as exception:
            raise ValueError("Value of 'ny' can not be converted to int.") from exception

    if not isinstance(nz, int):
        try:
            nz = int(nz)
        except Exception as exception:
            raise ValueError("Value of 'nz' can not be converted to int.") from exception

    _C_GL_1_1.glNormal3i(nx, ny, nz)

def glNormal3iv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLint)
    _C_GL_1_1.glNormal3iv(c_v)

def glNormal3s(nx, ny, nz):
    """
    nx              : int | SupportsInt
    ny              : int | SupportsInt
    nz              : int | SupportsInt
    """
    if not isinstance(nx, int):
        try:
            nx = int(nx)
        except Exception as exception:
            raise ValueError("Value of 'nx' can not be converted to int.") from exception

    if not isinstance(ny, int):
        try:
            ny = int(ny)
        except Exception as exception:
            raise ValueError("Value of 'ny' can not be converted to int.") from exception

    if not isinstance(nz, int):
        try:
            nz = int(nz)
        except Exception as exception:
            raise ValueError("Value of 'nz' can not be converted to int.") from exception

    _C_GL_1_1.glNormal3s(nx, ny, nz)

def glNormal3sv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLshort)
    _C_GL_1_1.glNormal3sv(c_v)


def glColor3b(red, green, blue):
    """
    red             : int | SupportsInt
    green           : int | SupportsInt
    blue            : int | SupportsInt
    """
    if not isinstance(red, int):
        try:
            red = int(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to int.") from exception

    if not isinstance(green, int):
        try:
            green = int(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to int.") from exception

    if not isinstance(blue, int):
        try:
            blue = int(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to int.") from exception

    _C_GL_1_1.glColor3b(red, green, blue)

def glColor3bv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
        Value range <-128, 127>.
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLbyte)
    _C_GL_1_1.glColor3bv(c_v)

def glColor3d(red, green, blue):
    """
    red             : float | SupportsFloat
    green           : float | SupportsFloat
    blue            : float | SupportsFloat
    """
    if not isinstance(red, float):
        try:
            red = float(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to float.") from exception

    if not isinstance(green, float):
        try:
            green = float(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to float.") from exception

    if not isinstance(blue, float):
        try:
            blue = float(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to float.") from exception

    _C_GL_1_1.glColor3d(red, green, blue)

def glColor3dv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")


    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glColor3dv(c_v)

def glColor3f(red, green, blue):
    """
    red             : float | SupportsFloat
    green           : float | SupportsFloat
    blue            : float | SupportsFloat
    """
    if not isinstance(red, float):
        try:
            red = float(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to float.") from exception

    if not isinstance(green, float):
        try:
            green = float(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to float.") from exception

    if not isinstance(blue, float):
        try:
            blue = float(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to float.") from exception

    _C_GL_1_1.glColor3f(red, green, blue)

def glColor3fv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glColor3fv(c_v)

def glColor3i(red, green, blue):
    """
    red             : int | SupportsInt
    green           : int | SupportsInt
    blue            : int | SupportsInt
    """
    if not isinstance(red, int):
        try:
            red = int(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to int.") from exception

    if not isinstance(green, int):
        try:
            green = int(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to int.") from exception

    if not isinstance(blue, int):
        try:
            blue = int(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to int.") from exception

    _C_GL_1_1.glColor3i(red, green, blue)

def glColor3iv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLint)
    _C_GL_1_1.glColor3iv(c_v)

def glColor3s(red, green, blue):
    """
    red              : int
    green            : int
    blue             : int
    """
    if not isinstance(red, int):
        try:
            red = int(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to int.") from exception

    if not isinstance(green, int):
        try:
            green = int(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to int.") from exception

    if not isinstance(blue, int):
        try:
            blue = int(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to int.") from exception

    _C_GL_1_1.glColor3s(red, green, blue)

def glColor3sv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLshort)
    _C_GL_1_1.glColor3sv(c_v)

def glColor3ub(red, green, blue):
    """
    red             : int | SupportsInt
    green           : int | SupportsInt
    blue            : int | SupportsInt
    """
    if not isinstance(red, int):
        try:
            red = int(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to int.") from exception

    if not isinstance(green, int):
        try:
            green = int(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to int.") from exception

    if not isinstance(blue, int):
        try:
            blue = int(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to int.") from exception

    _C_GL_1_1.glColor3ub(red, green, blue)

def glColor3ubv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLubyte)
    _C_GL_1_1.glColor3ubv(c_v)

def glColor3ui(red, green, blue):
    """
    red             : int | SupportsInt
    green           : int | SupportsInt
    blue            : int | SupportsInt
    """
    if not isinstance(red, int):
        try:
            red = int(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to int.") from exception

    if not isinstance(green, int):
        try:
            green = int(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to int.") from exception

    if not isinstance(blue, int):
        try:
            blue = int(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to int.") from exception

    _C_GL_1_1.glColor3ui(red, green, blue)

def glColor3uiv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLuint)
    _C_GL_1_1.glColor3uiv(c_v)

def glColor3us(red, green, blue):
    """
    red             : int | SupportsInt
    green           : int | SupportsInt
    blue            : int | SupportsInt
    """
    if not isinstance(red, int):
        try:
            red = int(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to int.") from exception

    if not isinstance(green, int):
        try:
            green = int(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to int.") from exception

    if not isinstance(blue, int):
        try:
            blue = int(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to int.") from exception

    _C_GL_1_1.glColor3us(red, green, blue)

def glColor3usv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLushort)
    _C_GL_1_1.glColor3usv(c_v)

def glColor4b(red, green, blue, alpha):
    """
    red             : int | SupportsInt
    green           : int | SupportsInt
    blue            : int | SupportsInt
    alpha           : int | SupportsInt
    """
    if not isinstance(red, int):
        try:
            red = int(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to int.") from exception

    if not isinstance(green, int):
        try:
            green = int(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to int.") from exception

    if not isinstance(blue, int):
        try:
            blue = int(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to int.") from exception

    if not isinstance(alpha, int):
        try:
            alpha = int(alpha)
        except Exception as exception:
            raise ValueError("Value of 'alpha' can not be converted to int.") from exception

    _C_GL_1_1.glColor4b(red, green, blue, alpha)

def glColor4bv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLbyte)
    _C_GL_1_1.glColor4bv(c_v)

def glColor4d(red, green, blue, alpha):
    """
    red             : float | SupportsFloat
    green           : float | SupportsFloat
    blue            : float | SupportsFloat
    alpha           : float | SupportsFloat
    """
    if not isinstance(red, float):
        try:
            red = float(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to float.") from exception

    if not isinstance(green, float):
        try:
            green = float(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to float.") from exception

    if not isinstance(blue, float):
        try:
            blue = float(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to float.") from exception

    if not isinstance(alpha, float):
        try:
            alpha = float(alpha)
        except Exception as exception:
            raise ValueError("Value of 'alpha' can not be converted to float.") from exception

    _C_GL_1_1.glColor4d(red, green, blue, alpha)

def glColor4dv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glColor4dv(c_v)

def glColor4f(red, green, blue, alpha):
    """
    red             : float | SupportsFloat
    green           : float | SupportsFloat
    blue            : float | SupportsFloat
    alpha           : float | SupportsFloat
    """
    if not isinstance(red, float):
        try:
            red = float(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to float.") from exception

    if not isinstance(green, float):
        try:
            green = float(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to float.") from exception

    if not isinstance(blue, float):
        try:
            blue = float(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to float.") from exception

    if not isinstance(alpha, float):
        try:
            alpha = float(alpha)
        except Exception as exception:
            raise ValueError("Value of 'alpha' can not be converted to float.") from exception

    _C_GL_1_1.glColor4f(red, green, blue, alpha)

def glColor4fv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")
            
    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glColor4fv(c_v)

def glColor4i(red, green, blue, alpha):
    """
    red             : int | SupportsInt
    green           : int | SupportsInt
    blue            : int | SupportsInt
    alpha           : int | SupportsInt
    """
    if not isinstance(red, int):
        try:
            red = int(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to int.") from exception

    if not isinstance(green, int):
        try:
            green = int(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to int.") from exception

    if not isinstance(blue, int):
        try:
            blue = int(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to int.") from exception

    if not isinstance(alpha, int):
        try:
            alpha = int(alpha)
        except Exception as exception:
            raise ValueError("Value of 'alpha' can not be converted to int.") from exception

    _C_GL_1_1.glColor4i(red, green, blue, alpha)

def glColor4iv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLint)
    _C_GL_1_1.glColor4iv(c_v)

def glColor4s(red, green, blue, alpha):
    """
    red             : int | SupportsInt
    green           : int | SupportsInt
    blue            : int | SupportsInt
    alpha           : int | SupportsInt
    """
    if not isinstance(red, int):
        try:
            red = int(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to int.") from exception

    if not isinstance(green, int):
        try:
            green = int(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to int.") from exception

    if not isinstance(blue, int):
        try:
            blue = int(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to int.") from exception

    if not isinstance(alpha, int):
        try:
            alpha = int(alpha)
        except Exception as exception:
            raise ValueError("Value of 'alpha' can not be converted to int.") from exception

    _C_GL_1_1.glColor4s(red, green, blue, alpha)

def glColor4sv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLshort)
    _C_GL_1_1.glColor4sv(c_v)

def glColor4ub(red, green, blue, alpha):
    """
    red             : int | SupportsInt
    green           : int | SupportsInt
    blue            : int | SupportsInt
    alpha           : int | SupportsInt
    """
    if not isinstance(red, int):
        try:
            red = int(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to int.") from exception

    if not isinstance(green, int):
        try:
            green = int(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to int.") from exception

    if not isinstance(blue, int):
        try:
            blue = int(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to int.") from exception

    if not isinstance(alpha, int):
        try:
            alpha = int(alpha)
        except Exception as exception:
            raise ValueError("Value of 'alpha' can not be converted to int.") from exception

    _C_GL_1_1.glColor4ub(red, green, blue, alpha)

def glColor4ubv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLubyte)
    _C_GL_1_1.glColor4ubv(c_v)

def glColor4ui(red, green, blue, alpha):
    """
    red             : int | SupportsInt
    green           : int | SupportsInt
    blue            : int | SupportsInt
    alpha           : int | SupportsInt
    """
    if not isinstance(red, int):
        try:
            red = int(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to int.") from exception

    if not isinstance(green, int):
        try:
            green = int(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to int.") from exception

    if not isinstance(blue, int):
        try:
            blue = int(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to int.") from exception

    if not isinstance(alpha, int):
        try:
            alpha = int(alpha)
        except Exception as exception:
            raise ValueError("Value of 'alpha' can not be converted to int.") from exception

    _C_GL_1_1.glColor4ui(red, green, blue, alpha)

def glColor4uiv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLuint)
    _C_GL_1_1.glColor4uiv(c_v)

def glColor4us(red, green, blue, alpha):
    """
    red             : int | SupportsInt
    green           : int | SupportsInt
    blue            : int | SupportsInt
    alpha           : int | SupportsInt
    """
    if not isinstance(red, int):
        try:
            red = int(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to int.") from exception

    if not isinstance(green, int):
        try:
            green = int(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to int.") from exception

    if not isinstance(blue, int):
        try:
            blue = int(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to int.") from exception

    if not isinstance(alpha, int):
        try:
            alpha = int(alpha)
        except Exception as exception:
            raise ValueError("Value of 'alpha' can not be converted to int.") from exception

    _C_GL_1_1.glColor4us(red, green, blue, alpha)

def glColor4usv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLushort)
    _C_GL_1_1.glColor4usv(c_v)


def glIndexd(c):
    """
    c               : float | SupportsFloat
    """
    if not isinstance(c, float):
        try:
            c = float(c)
        except Exception as exception:
            raise ValueError("Value of 'c' can not be converted to float.") from exception

    _C_GL_1_1.glIndexd(c)

def glIndexdv(c):
    """
    c               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(c, list) or not all(isinstance(item, float) for item in c):
        try:
            c = [float(item) for item in c]
        except:
            raise ValueError("Value of 'c' can not be converted to list of floats.")

    c_c = _Support.list_part_to_c_array_no_conv(c, 1, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glIndexdv(c_c)

def glIndexf(c):
    """
    c               : float | SupportsFloat
    """
    if not isinstance(c, float):
        try:
            c = float(c)
        except Exception as exception:
            raise ValueError("Value of 'c' can not be converted to float.") from exception

    _C_GL_1_1.glIndexf(c)

def glIndexfv(c):
    """
    c               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(c, list) or not all(isinstance(item, float) for item in c):
        try:
            c = [float(item) for item in c]
        except:
            raise ValueError("Value of 'c' can not be converted to list of floats.")

    c_c = _Support.list_part_to_c_array_no_conv(c, 1, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glIndexfv(c_c)

def glIndexi(c):
    """
    c               : int | SupportsInt
    """
    if not isinstance(c, int):
        try:
            c = int(c)
        except Exception as exception:
            raise ValueError("Value of 'c' can not be converted to int.") from exception

    _C_GL_1_1.glIndexi(c)

def glIndexiv(c):
    """
    c               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(c, list) or not all(isinstance(item, int) for item in c):
        try:
            c = [int(item) for item in c]
        except:
            raise ValueError("Value of 'c' can not be converted to list of ints.")

    c_c = _Support.list_part_to_c_array_no_conv(c, 1, _C_GL_1_1.GLint)
    _C_GL_1_1.glIndexiv(c_c)

def glIndexs(c):
    """
    c               : int | SupportsInt
    """
    if not isinstance(c, int):
        try:
            c = int(c)
        except Exception as exception:
            raise ValueError("Value of 'c' can not be converted to int.") from exception

    _C_GL_1_1.glIndexs(c)

def glIndexsv(c):
    """
    c               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(c, list) or not all(isinstance(item, int) for item in c):
        try:
            c = [int(item) for item in c]
        except:
            raise ValueError("Value of 'c' can not be converted to list of ints.")

    c_c = _Support.list_part_to_c_array_no_conv(c, 1, _C_GL_1_1.GLshort)
    _C_GL_1_1.glIndexsv(c_c)

def glIndexub(c):
    """
    c               : int | SupportsInt
    """
    if not isinstance(c, int):
        try:
            c = int(c)
        except Exception as exception:
            raise ValueError("Value of 'c' can not be converted to int.") from exception

    _C_GL_1_1.glIndexub(c)

def glIndexubv(c):
    """
    c               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(c, list) or not all(isinstance(item, int) for item in c):
        try:
            c = [int(item) for item in c]
        except:
            raise ValueError("Value of 'c' can not be converted to list of ints.")

    c_c = _Support.list_part_to_c_array_no_conv(c, 1, _C_GL_1_1.GLubyte)
    _C_GL_1_1.glIndexubv(c_c)


### Vertex Arrays ###

def glVertexPointer(size, type_, stride, pointer):
    """
    size            : int | SupportsInt
    type_           : int | SupportsInt
    stride          : int | SupportsInt
    pointer         : bytes | List[int | float] | Iterable[SupportsInt | SupportsFloat]
    """
    if not isinstance(size, int):
        try:
            size = int(size)
        except Exception as exception:
            raise ValueError("Value of 'size' can not be converted to int.") from exception

    if not isinstance(type_, int):
        try:
            type_ = int(type_)
        except Exception as exception:
            raise ValueError("Value of 'type_' can not be converted to int.") from exception

    if not isinstance(stride, int):
        try:
            stride = int(stride)
        except Exception as exception:
            raise ValueError("Value of 'stride' can not be converted to int.") from exception

    if isinstance(pointer, bytes):
        _Support.to_cache().c_vertex_array_pointer = pointer
    else:
        if stride != 0:
            raise ValueError("Value of 'stride' parameter can't be other than 0, when 'pointer' parameter type is not bytes.")

        py_type = _Support.gl_type_id_to_py_type(type_)
        if py_type is None:
            raise ValueError("Unexpected value of 'type_' parameter. Can not detect python type.")
            
        try:
            pointer = [py_type(item) for item in pointer]
        except:
            py_type_str = {
                int : "int",
                float : "float",
            }.get(py_type, "???")
            
            raise ValueError("Value of 'pointer' can not be converted to list of %ss." % py_type_str)

        c_type  = _Support.gl_type_id_to_c_type(type_)
        if c_type is None:
            raise ValueError("Unexpected value of 'type_' parameter. Can not detect c type.")

        _Support.to_cache().c_vertex_array_pointer = _Support.list_to_c_array_no_conv(pointer, 0, c_type)

    _C_GL_1_1.glVertexPointer(size, type_, stride, _Support.to_cache().c_vertex_array_pointer)

def glNormalPointer(type_, stride, pointer):
    """
    type_           : int | SupportsInt
    stride          : int | SupportsInt
    pointer         : List[int | float] | Iterable[SupportsInt | SupportsFloat]
    """
    if not isinstance(type_, int):
        try:
            type_ = int(type_)
        except Exception as exception:
            raise ValueError("Value of 'type_' can not be converted to int.") from exception

    if not isinstance(stride, int):
        try:
            stride = int(stride)
        except Exception as exception:
            raise ValueError("Value of 'stride' can not be converted to int.") from exception

    if isinstance(pointer, bytes):
        _Support.to_cache().c_normal_array_pointer = pointer
    else:
        if stride != 0:
            raise ValueError("Value of 'stride' parameter can't be other than 0, when 'pointer' parameter type is not bytes.")

        py_type = _Support.gl_type_id_to_py_type(type_)
        if py_type is None:
            raise ValueError("Unexpected value of 'type_' parameter. Can not detect python type.")
            
        try:
            pointer = [py_type(item) for item in pointer]
        except:
            py_type_str = {
                int : "int",
                float : "float",
            }.get(py_type, "???")
            
            raise ValueError("Value of 'pointer' can not be converted to list of %ss." % py_type_str)

        c_type  = _Support.gl_type_id_to_c_type(type_)
        if c_type is None:
            raise ValueError("Unexpected value of 'type_' parameter. Can not detect c type.")

        _Support.to_cache().c_normal_array_pointer = _Support.list_to_c_array_no_conv(pointer, 0, c_type)

    _C_GL_1_1.glNormalPointer(type_, stride, _Support.to_cache().c_normal_array_pointer)

def glColorPointer(size, type_, stride, pointer):
    """
    size            : int | SupportsInt
    type_           : int | SupportsInt
    stride          : int | SupportsInt
    pointer         : List[int | float] | Iterable[SupportsInt | SupportsFloat]
    """
    if not isinstance(size, int):
        try:
            size = int(size)
        except Exception as exception:
            raise ValueError("Value of 'size' can not be converted to int.") from exception

    if not isinstance(type_, int):
        try:
            type_ = int(type_)
        except Exception as exception:
            raise ValueError("Value of 'type_' can not be converted to int.") from exception

    if not isinstance(stride, int):
        try:
            stride = int(stride)
        except Exception as exception:
            raise ValueError("Value of 'stride' can not be converted to int.") from exception

    if isinstance(pointer, bytes):
        _Support.to_cache().c_color_array_pointer = pointer
    else:
        if stride != 0:
            raise ValueError("Value of 'stride' parameter can't be other than 0, when 'pointer' parameter type is not bytes.")

        py_type = _Support.gl_type_id_to_py_type(type_)
        if py_type is None:
            raise ValueError("Unexpected value of 'type_' parameter. Can not detect python type.")
        
        try:
            pointer = [py_type(item) for item in pointer]
        except:
            py_type_str = {
                int : "int",
                float : "float",
            }.get(py_type, "???")
            
            raise ValueError("Value of 'pointer' can not be converted to list of %ss." % py_type_str)
        
        c_type  = _Support.gl_type_id_to_c_type(type_)
        if c_type is None:
            raise ValueError("Unexpected value of 'type_' parameter. Can not detect c type.")

        _Support.to_cache().c_color_array_pointer = _Support.list_to_c_array_no_conv(pointer, 0, c_type)

    _C_GL_1_1.glColorPointer(size, type_, stride, _Support.to_cache().c_color_array_pointer)

def glIndexPointer(type_, stride, pointer):
    """
    type_           : int | SupportsInt
    stride          : int | SupportsInt
    pointer         : List[int | float] | Iterable[SupportsInt | SupportsFloat]
    """
    if not isinstance(type_, int):
        try:
            type_ = int(type_)
        except Exception as exception:
            raise ValueError("Value of 'type_' can not be converted to int.") from exception

    if not isinstance(stride, int):
        try:
            stride = int(stride)
        except Exception as exception:
            raise ValueError("Value of 'stride' can not be converted to int.") from exception

    if isinstance(pointer, bytes):
        _Support.to_cache().c_index_array_pointer = pointer
    else:
        if stride != 0:
            raise ValueError("Value of 'stride' parameter can't be other than 0, when 'pointer' parameter type is not bytes.")

        py_type = _Support.gl_type_id_to_py_type(type_)
        if py_type is None:
            raise ValueError("Unexpected value of 'type_' parameter. Can not detect python type.")
            
        try:
            pointer = [py_type(item) for item in pointer]
        except:
            py_type_str = {
                int : "int",
                float : "float",
            }.get(py_type, "???")
            
            raise ValueError("Value of 'pointer' can not be converted to list of %ss." % py_type_str)
            
        c_type  = _Support.gl_type_id_to_c_type(type_)
        if c_type is None:
            raise ValueError("Unexpected value of 'type_' parameter. Can not detect c type.")

        _Support.to_cache().c_index_array_pointer = _Support.list_to_c_array_no_conv(pointer, 0, c_type)

    _C_GL_1_1.glIndexPointer(type_, stride, _Support.to_cache().c_index_array_pointer)

def glEdgeFlagPointer(stride, pointer):
    """
    stride          : int | SupportsInt
    pointer         : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(stride, int):
        try:
            stride = int(stride)
        except Exception as exception:
            raise ValueError("Value of 'stride' can not be converted to int.") from exception

    if isinstance(pointer, bytes):
        _Support.to_cache().c_edge_flag_array_pointer = pointer
    else:
        if stride != 0:
            raise ValueError("Value of 'stride' parameter can't be other than 0, when 'pointer' parameter type is not bytes.")
            
        try:
            pointer = [int(item) for item in pointer]
        except:
            raise ValueError("Value of 'pointer' can not be converted to list of ints.")

        _Support.to_cache().c_edge_flag_array_pointer = _Support.list_to_c_array_no_conv(pointer, 0, _C_GL_1_1.GLboolean)

    _C_GL_1_1.glEdgeFlagPointer(stride, _Support.to_cache().c_edge_flag_array_pointer)

def glTexCoordPointer(size, type_, stride, pointer):
    """
    size            : int | SupportsInt
    type_           : int | SupportsInt
    stride          : int | SupportsInt
    pointer         : List[int | float] | Iterable[SupportsInt | SupportsFloat]
    """
    if not isinstance(size, int):
        try:
            size = int(size)
        except Exception as exception:
            raise ValueError("Value of 'size' can not be converted to int.") from exception

    if not isinstance(type_, int):
        try:
            type_ = int(type_)
        except Exception as exception:
            raise ValueError("Value of 'type_' can not be converted to int.") from exception

    if not isinstance(stride, int):
        try:
            stride = int(stride)
        except Exception as exception:
            raise ValueError("Value of 'stride' can not be converted to int.") from exception

    if isinstance(pointer, bytes):
        _Support.to_cache().c_tex_coord_array_pointer = pointer
    else:
        if stride != 0:
            raise ValueError("Value of 'stride' parameter can't be other than 0, when 'pointer' parameter type is not bytes.")

        py_type = _Support.gl_type_id_to_py_type(type_)
        if py_type is None:
            raise ValueError("Unexpected value of 'type_' parameter. Can not detect python type.")
            
        try:
            pointer = [py_type(item) for item in pointer]
        except:
            py_type_str = {
                int : "int",
                float : "float",
            }.get(py_type, "???")
            
            raise ValueError("Value of 'pointer' can not be converted to list of %ss." % py_type_str)
            
        c_type  = _Support.gl_type_id_to_c_type(type_)
        if c_type is None:
            raise ValueError("Unexpected value of 'type_' parameter. Can not detect c type.")

        _Support.to_cache().c_tex_coord_array_pointer = _Support.list_to_c_array_no_conv(pointer, 0, c_type)

    _C_GL_1_1.glTexCoordPointer(size, type_, stride, _Support.to_cache().c_tex_coord_array_pointer)

def glEnableClientState(array):
    """
    array           : int | SupportsInt
    """
    if not isinstance(array, int):
        try:
            array = int(array)
        except Exception as exception:
            raise ValueError("Value of 'array' can not be converted to int.") from exception

    _C_GL_1_1.glEnableClientState(array)

def glDisableClientState(array):
    """
    array           : int | SupportsInt
    """
    if not isinstance(array, int):
        try:
            array = int(array)
        except Exception as exception:
            raise ValueError("Value of 'array' can not be converted to int.") from exception

    _C_GL_1_1.glDisableClientState(array)

def glArrayElement(i):
    """
    i               : int | SupportsInt
    """
    if not isinstance(i, int):
        try:
            i = int(i)
        except Exception as exception:
            raise ValueError("Value of 'i' can not be converted to int.") from exception

    _C_GL_1_1.glArrayElement(i)

# Drawing Commands

def glDrawArrays(mode, first, count):
    """
    mode            : int | SupportsInt
    first           : int | SupportsInt
    count           : int | SupportsInt
    """
    if not isinstance(mode, int):
        try:
            mode = int(mode)
        except Exception as exception:
            raise ValueError("Value of 'mode' can not be converted to int.") from exception

    if not isinstance(first, int):
        try:
            first = int(first)
        except Exception as exception:
            raise ValueError("Value of 'first' can not be converted to int.") from exception

    if not isinstance(count, int):
        try:
            count = int(count)
        except Exception as exception:
            raise ValueError("Value of 'count' can not be converted to int.") from exception

    _C_GL_1_1.glDrawArrays(mode, first, count)

def glDrawElements(mode, count, type_, indices):
    """
    mode            : int | SupportsInt
    count           : int | SupportsInt
    type_           : int | SupportsInt
    indices         : List[int | float] | Iterable[SupportsInt | SupportsFloat]
    """
    if not isinstance(mode, int):
        try:
            mode = int(mode)
        except Exception as exception:
            raise ValueError("Value of 'mode' can not be converted to int.") from exception

    if not isinstance(count, int):
        try:
            count = int(count)
        except Exception as exception:
            raise ValueError("Value of 'count' can not be converted to int.") from exception

    if not isinstance(type_, int):
        try:
            type_ = int(type_)
        except Exception as exception:
            raise ValueError("Value of 'type_' can not be converted to int.") from exception

    py_type = _Support.gl_type_id_to_py_type(type_)
    if py_type is None:
        raise ValueError("Unexpected value of 'type_' parameter. Can not detect python type.")
        
    try:
        indices = [py_type(item) for item in indices]
    except:
        py_type_str = {
            int : "int",
            float : "float",
        }.get(py_type, "???")
        
        raise ValueError("Value of 'indices' can not be converted to list of %ss." % py_type_str)
        
        
    c_type  = _Support.gl_type_id_to_c_type(type_)
    if c_type is None:
        raise ValueError("Unexpected value of 'type_' parameter. Can not detect c type.")

    c_indices = _Support.list_to_c_array_no_conv(indices, count, c_type)
    _C_GL_1_1.glDrawElements(mode, count, type_, c_indices)


def glInterleavedArrays(format_, stride, pointer):
    """
    format_         : int | SupportsInt
    stride          : int | SupportsInt
        Value can't be other than 0, when 'pointer' parameter type is not bytes.
    pointer         : bytes | List[int | Float] | Iterable[SupportsInt | SupportsFloat]
        Array of aggregate elements.
    """
    if not isinstance(format_, int):
        try:
            format_ = int(format_)
        except Exception as exception:
            raise ValueError("Value of 'format_' can not be converted to int.") from exception

    if not isinstance(stride, int):
        try:
            stride = int(stride)
        except Exception as exception:
            raise ValueError("Value of 'stride' can not be converted to int.") from exception

    if isinstance(pointer, bytes):
        c_pointer = pointer
    else:
        pointer = list(pointer) # it's actually not a pointer but a list

        _2F = (2, _C_GL_1_1.GLfloat, float)
        _3F = (3, _C_GL_1_1.GLfloat, float)
        _4F = (3, _C_GL_1_1.GLfloat, float)
        _4UB = (4, _C_GL_1_1.GLubyte, int)

        aggregate_formats = {
            GL_V2F                  : (_2F,), 
            GL_V3F                  : (_3F,), 
            GL_C4UB_V2F             : (_4UB, _2F),
            GL_C4UB_V3F             : (_4UB, _3F),
            GL_C3F_V3F              : (_3F, _3F),
            GL_N3F_V3F              : (_3F, _3F),
            GL_C4F_N3F_V3F          : (_4F, _3F, _3F),
            GL_T2F_V3F              : (_2F, _3F),
            GL_T4F_V4F              : (_4F, _4F),
            GL_T2F_C4UB_V3F         : (_2F, _4UB, _3F),
            GL_T2F_C3F_V3F          : (_2F, _3F, _3F),
            GL_T2F_N3F_V3F          : (_2F, _3F, _3F),
            GL_T2F_C4F_N3F_V3F      : (_2F, _4F, _3F, _3F),
            GL_T4F_C4F_N3F_V4F      : (_4F, _4F, _3F, _4F),
        }

        aggregate_format = aggregate_formats.get(format_, None)
        if aggregate_format is None:
            raise ValueError("Unexpected value of 'format_' parameter.")

        aggregae_size = 0
        aggregae_length = 0

        for length_c_type in aggregate_format:
            length, c_type, py_type = length_c_type

            aggregae_length += length
            aggregae_size   += _ctypes.sizeof(c_type) * length

        if stride != 0:
            raise ValueError("Value of 'stride' parameter can't be other than 0, when 'pointer' parameter type is not bytes.")

        if len(pointer) % aggregae_length != 0:
            raise ValueError("Wrong length of 'pointer' iterable parameter.")

        c_pointer_size = len(pointer) // aggregae_length * aggregae_size

        c_pointer = _Support.make_c_array(_C_GL_1_1.GLubyte, c_pointer_size)

        index = 0
        for base_offset in range(0, c_pointer_size, aggregae_size):
            offset = base_offset
            for length_c_type in aggregate_format:
                length, c_type, py_type = length_c_type
                size = _ctypes.sizeof(c_type)

                for _ in range(length):
                    try:
                        value = py_type(pointer[index])
                    except:
                        py_type_str = {
                            int : "int",
                            float : "float",
                        }.get(py_type, "???")
                    
                        raise ValueError("Value of 'pointer' can not be converted to list of %ss." % py_type_str)
                    
                    c_value_p = _ctypes.cast(_ctypes.addressof(c_pointer) + offset, _ctypes.POINTER(c_type))
                    c_value_p[0] = value

                    index += 1
                    offset += size

    _Support.to_cache().c_interleaved_array_pointer = c_pointer

    _C_GL_1_1.glInterleavedArrays(format_, stride, c_pointer)

### Rectangles, Matrices, Texture Coordinates ###

# Rectangles

def glRectd(x1, y1, x2, y2):
    """
    x1              : float | SupportsFloat
    y1              : float | SupportsFloat
    x2              : float | SupportsFloat
    y2              : float | SupportsFloat
    """
    if not isinstance(x1, float):
        try:
            x1 = float(x1)
        except Exception as exception:
            raise ValueError("Value of 'x1' can not be converted to float.") from exception

    if not isinstance(y1, float):
        try:
            y1 = float(y1)
        except Exception as exception:
            raise ValueError("Value of 'y1' can not be converted to float.") from exception

    if not isinstance(x2, float):
        try:
            x2 = float(x2)
        except Exception as exception:
            raise ValueError("Value of 'x2' can not be converted to float.") from exception

    if not isinstance(y2, float):
        try:
            y2 = float(y2)
        except Exception as exception:
            raise ValueError("Value of 'y2' can not be converted to float.") from exception

    _C_GL_1_1.glRectd(x1, y1, x2, y2)

def glRectdv(v1, v2):
    """
    v1              : List[float] | Iterable[SupportsFloat]
    v2              : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v1, list) or not all(isinstance(item, float) for item in v1):
        try:
            v1 = [float(item) for item in v1]
        except:
            raise ValueError("Value of 'v1' can not be converted to list of floats.")

    if not isinstance(v2, list) or not all(isinstance(item, float) for item in v2):
        try:
            v2 = [float(item) for item in v2]
        except:
            raise ValueError("Value of 'v2' can not be converted to list of floats.")
            
    c_v1 = _Support.list_part_to_c_array_no_conv(v1, 2, _C_GL_1_1.GLdouble)
    c_v2 = _Support.list_part_to_c_array_no_conv(v2, 2, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glRectdv(c_v1, c_v2)

def glRectf(x1, y1, x2, y2):
    """
    x1              : float | SupportsFloat
    y1              : float | SupportsFloat
    x2              : float | SupportsFloat
    y2              : float | SupportsFloat
    """
    if not isinstance(x1, float):
        try:
            x1 = float(x1)
        except Exception as exception:
            raise ValueError("Value of 'x1' can not be converted to float.") from exception

    if not isinstance(y1, float):
        try:
            y1 = float(y1)
        except Exception as exception:
            raise ValueError("Value of 'y1' can not be converted to float.") from exception

    if not isinstance(x2, float):
        try:
            x2 = float(x2)
        except Exception as exception:
            raise ValueError("Value of 'x2' can not be converted to float.") from exception

    if not isinstance(y2, float):
        try:
            y2 = float(y2)
        except Exception as exception:
            raise ValueError("Value of 'y2' can not be converted to float.") from exception

    _C_GL_1_1.glRectf(x1, y1, x2, y2)

def glRectfv(v1, v2):
    """
    v1              : List[float] | Iterable[SupportsFloat]
    v2              : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v1, list) or not all(isinstance(item, float) for item in v1):
        try:
            v1 = [float(item) for item in v1]
        except:
            raise ValueError("Value of 'v1' can not be converted to list of floats.")

    if not isinstance(v2, list) or not all(isinstance(item, float) for item in v2):
        try:
            v2 = [float(item) for item in v2]
        except:
            raise ValueError("Value of 'v2' can not be converted to list of floats.")

    c_v1 = _Support.list_part_to_c_array_no_conv(v1, 2, _C_GL_1_1.GLfloat)
    c_v2 = _Support.list_part_to_c_array_no_conv(v2, 2, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glRectfv(c_v1, c_v2)

def glRecti(x1, y1, x2, y2):
    """
    x1              : int | SupportsInt
    y1              : int | SupportsInt
    x2              : int | SupportsInt
    y2              : int | SupportsInt
    """
    if not isinstance(x1, int):
        try:
            x1 = int(x1)
        except Exception as exception:
            raise ValueError("Value of 'x1' can not be converted to int.") from exception

    if not isinstance(y1, int):
        try:
            y1 = int(y1)
        except Exception as exception:
            raise ValueError("Value of 'y1' can not be converted to int.") from exception

    if not isinstance(x2, int):
        try:
            x2 = int(x2)
        except Exception as exception:
            raise ValueError("Value of 'x2' can not be converted to int.") from exception

    if not isinstance(y2, int):
        try:
            y2 = int(y2)
        except Exception as exception:
            raise ValueError("Value of 'y2' can not be converted to int.") from exception

    _C_GL_1_1.glRecti(x1, y1, x2, y2)

def glRectiv(v1, v2):
    """
    v1              : List[int] | Iterable[SupportsInt]
    v2              : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v1, list) or not all(isinstance(item, int) for item in v1):
        try:
            v1 = [int(item) for item in v1]
        except:
            raise ValueError("Value of 'v1' can not be converted to list of ints.")

    if not isinstance(v2, list) or not all(isinstance(item, int) for item in v2):
        try:
            v2 = [int(item) for item in v2]
        except:
            raise ValueError("Value of 'v2' can not be converted to list of ints.")

    c_v1 = _Support.list_part_to_c_array_no_conv(v1, 2, _C_GL_1_1.GLint)
    c_v2 = _Support.list_part_to_c_array_no_conv(v2, 2, _C_GL_1_1.GLint)
    _C_GL_1_1.glRectiv(c_v1, c_v2)

def glRects(x1, y1, x2, y2):
    """
    x1              : int | SupportsInt
    y1              : int | SupportsInt
    x2              : int | SupportsInt
    y2              : int | SupportsInt
    """
    if not isinstance(x1, int):
        try:
            x1 = int(x1)
        except Exception as exception:
            raise ValueError("Value of 'x1' can not be converted to int.") from exception

    if not isinstance(y1, int):
        try:
            y1 = int(y1)
        except Exception as exception:
            raise ValueError("Value of 'y1' can not be converted to int.") from exception

    if not isinstance(x2, int):
        try:
            x2 = int(x2)
        except Exception as exception:
            raise ValueError("Value of 'x2' can not be converted to int.") from exception

    if not isinstance(y2, int):
        try:
            y2 = int(y2)
        except Exception as exception:
            raise ValueError("Value of 'y2' can not be converted to int.") from exception

    _C_GL_1_1.glRects(x1, y1, x2, y2)

def glRectsv(v1, v2):
    """
    v1              : List[int] | Iterable[SupportsInt]
    v2              : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v1, list) or not all(isinstance(item, int) for item in v1):
        try:
            v1 = [int(item) for item in v1]
        except:
            raise ValueError("Value of 'v1' can not be converted to list of ints.")

    if not isinstance(v2, list) or not all(isinstance(item, int) for item in v2):
        try:
            v2 = [int(item) for item in v2]
        except:
            raise ValueError("Value of 'v2' can not be converted to list of ints.")
            
    c_v1 = _Support.list_part_to_c_array_no_conv(v1, 2, _C_GL_1_1.GLshort)
    c_v2 = _Support.list_part_to_c_array_no_conv(v2, 2, _C_GL_1_1.GLshort)
    _C_GL_1_1.glRectsv(c_v1, c_v2)

# Matrices

def glMatrixMode(mode):
    """
    mode            : int | SupportsInt
    """
    if not isinstance(mode, int):
        try:
            mode = int(mode)
        except Exception as exception:
            raise ValueError("Value of 'mode' can not be converted to int.") from exception

    _C_GL_1_1.glMatrixMode(mode)

def glLoadMatrixd(m):
    """
    m               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(m, list) or not all(isinstance(item, float) for item in m):
        try:
            m = [float(item) for item in m]
        except:
            raise ValueError("Value of 'm' can not be converted to list of floats.")

    c_m = _Support.list_part_to_c_array_no_conv(m, 16, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glLoadMatrixd(c_m)

def glLoadMatrixf(m):
    """
    m               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(m, list) or not all(isinstance(item, float) for item in m):
        try:
            m = [float(item) for item in m]
        except:
            raise ValueError("Value of 'm' can not be converted to list of floats.")

    c_m = _Support.list_part_to_c_array_no_conv(m, 16, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glLoadMatrixf(c_m)

def glMultMatrixd(m):
    """
    m               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(m, list) or not all(isinstance(item, float) for item in m):
        try:
            m = [float(item) for item in m]
        except:
            raise ValueError("Value of 'm' can not be converted to list of floats.")

    c_m = _Support.list_part_to_c_array_no_conv(m, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glMultMatrixd(c_m)

def glMultMatrixf(m):
    """
    m               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(m, list) or not all(isinstance(item, float) for item in m):
        try:
            m = [float(item) for item in m]
        except:
            raise ValueError("Value of 'm' can not be converted to list of floats.")

    c_m = _Support.list_part_to_c_array_no_conv(m, 16, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glMultMatrixf(c_m)

def glLoadIdentity():
    _C_GL_1_1.glLoadIdentity()

def glRotated(angle, x, y, z):
    """
    angle           : float | SupportsFloat
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    z               : float | SupportsFloat
    """
    if not isinstance(angle, float):
        try:
            angle = float(angle)
        except Exception as exception:
            raise ValueError("Value of 'angle' can not be converted to float.") from exception

    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    if not isinstance(z, float):
        try:
            z = float(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to float.") from exception

    _C_GL_1_1.glRotated(angle, x, y, z)

def glRotatef(angle, x, y, z):
    """
    angle           : float | SupportsFloat
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    z               : float | SupportsFloat
    """
    if not isinstance(angle, float):
        try:
            angle = float(angle)
        except Exception as exception:
            raise ValueError("Value of 'angle' can not be converted to float.") from exception

    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    if not isinstance(z, float):
        try:
            z = float(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to float.") from exception

    _C_GL_1_1.glRotatef(angle, x, y, z)

def glTranslated(x, y, z):
    """
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    z               : float | SupportsFloat
    """
    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    if not isinstance(z, float):
        try:
            z = float(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to float.") from exception

    _C_GL_1_1.glTranslated(x, y, z)

def glTranslatef(x, y, z):
    """
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    z               : float | SupportsFloat
    """
    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    if not isinstance(z, float):
        try:
            z = float(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to float.") from exception

    _C_GL_1_1.glTranslatef(x, y, z)

def glScaled(x, y, z):
    """
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    z               : float | SupportsFloat
    """
    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    if not isinstance(z, float):
        try:
            z = float(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to float.") from exception

    _C_GL_1_1.glScaled(x, y, z)

def glScalef(x, y, z):
    """
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    z               : float | SupportsFloat
    """
    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    if not isinstance(z, float):
        try:
            z = float(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to float.") from exception

    _C_GL_1_1.glScalef(x, y, z)
def glFrustum(left, right, bottom, top, zNear, zFar):
    """
    left            : float | SupportsFloat
    right           : float | SupportsFloat
    bottom          : float | SupportsFloat
    top             : float | SupportsFloat
    zNear           : float | SupportsFloat
    zFar            : float | SupportsFloat
    """
    if not isinstance(left, float):
        try:
            left = float(left)
        except Exception as exception:
            raise ValueError("Value of 'left' can not be converted to float.") from exception

    if not isinstance(right, float):
        try:
            right = float(right)
        except Exception as exception:
            raise ValueError("Value of 'right' can not be converted to float.") from exception

    if not isinstance(bottom, float):
        try:
            bottom = float(bottom)
        except Exception as exception:
            raise ValueError("Value of 'bottom' can not be converted to float.") from exception

    if not isinstance(top, float):
        try:
            top = float(top)
        except Exception as exception:
            raise ValueError("Value of 'top' can not be converted to float.") from exception

    if not isinstance(zNear, float):
        try:
            zNear = float(zNear)
        except Exception as exception:
            raise ValueError("Value of 'zNear' can not be converted to float.") from exception

    if not isinstance(zFar, float):
        try:
            zFar = float(zFar)
        except Exception as exception:
            raise ValueError("Value of 'zFar' can not be converted to float.") from exception

    _C_GL_1_1.glFrustum(left, right, bottom, top, zNear, zFar)

def glOrtho(left, right, bottom, top, zNear, zFar):
    """
    left            : float | SupportsFloat
    right           : float | SupportsFloat
    bottom          : float | SupportsFloat
    top             : float | SupportsFloat
    zNear           : float | SupportsFloat
    zFar            : float | SupportsFloat
    """
    if not isinstance(left, float):
        try:
            left = float(left)
        except Exception as exception:
            raise ValueError("Value of 'left' can not be converted to float.") from exception

    if not isinstance(right, float):
        try:
            right = float(right)
        except Exception as exception:
            raise ValueError("Value of 'right' can not be converted to float.") from exception

    if not isinstance(bottom, float):
        try:
            bottom = float(bottom)
        except Exception as exception:
            raise ValueError("Value of 'bottom' can not be converted to float.") from exception

    if not isinstance(top, float):
        try:
            top = float(top)
        except Exception as exception:
            raise ValueError("Value of 'top' can not be converted to float.") from exception

    if not isinstance(zNear, float):
        try:
            zNear = float(zNear)
        except Exception as exception:
            raise ValueError("Value of 'zNear' can not be converted to float.") from exception

    if not isinstance(zFar, float):
        try:
            zFar = float(zFar)
        except Exception as exception:
            raise ValueError("Value of 'zFar' can not be converted to float.") from exception

    _C_GL_1_1.glOrtho(left, right, bottom, top, zNear, zFar)

def glPushMatrix():
    _C_GL_1_1.glPushMatrix()

def glPopMatrix():
    _C_GL_1_1.glPopMatrix()


# Generating Texture Coordinates

def glTexGend(coord, pname, param):
    """
    coord           : int | SupportsInt
    pname           : int | SupportsInt
    param           : float | SupportsFloat
    """
    if not isinstance(coord, int):
        try:
            coord = int(coord)
        except Exception as exception:
            raise ValueError("Value of 'coord' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, float):
        try:
            param = float(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to float.") from exception

    _C_GL_1_1.glTexGend(coord, pname, param)


def glTexGendv(coord, pname, params):
    """
    coord           : int | SupportsInt
    pname           : int | SupportsInt
    params          : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(coord, int):
        try:
            coord = int(coord)
        except Exception as exception:
            raise ValueError("Value of 'coord' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(params, list) or not all(isinstance(item, float) for item in params):
        try:
            params = [float(item) for item in params]
        except:
            raise ValueError("Value of 'params' can not be converted to list of floats.")

    n = _Support.get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname'.")
        
    c_params = _Support.list_part_to_c_array_no_conv(params, n, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glTexGendv(int(coord), int(pname), c_params)

def glTexGenf(coord, pname, param):
    """
    coord           : int | SupportsInt
    pname           : int | SupportsInt
    param           : float | SupportsFloat
    """
    if not isinstance(coord, int):
        try:
            coord = int(coord)
        except Exception as exception:
            raise ValueError("Value of 'coord' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, float):
        try:
            param = float(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to float.") from exception

    _C_GL_1_1.glTexGenf(coord, pname, param)

def glTexGenfv(coord, pname, params):
    """
    coord           : int | SupportsInt
    pname           : int | SupportsInt
    params          : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(coord, int):
        try:
            coord = int(coord)
        except Exception as exception:
            raise ValueError("Value of 'coord' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(params, list) or not all(isinstance(item, float) for item in params):
        try:
            params = [float(item) for item in params]
        except:
            raise ValueError("Value of 'params' can not be converted to list of floats.")

    n = _Support.get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname'.")
        
    c_params = _Support.list_part_to_c_array_no_conv(params, n, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glTexGenfv(int(coord), int(pname), c_params)

def glTexGeni(coord, pname, param):
    """
    coord           : int | SupportsInt
    pname           : int | SupportsInt
    param           : int | SupportsInt
    """
    if not isinstance(coord, int):
        try:
            coord = int(coord)
        except Exception as exception:
            raise ValueError("Value of 'coord' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, int):
        try:
            param = int(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to int.") from exception

    _C_GL_1_1.glTexGeni(coord, pname, param)

def glTexGeniv(coord, pname, params):
    """
    coord           : int | SupportsInt
    pname           : int | SupportsInt
    params          : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(coord, int):
        try:
            coord = int(coord)
        except Exception as exception:
            raise ValueError("Value of 'coord' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(params, list) or not all(isinstance(item, int) for item in params):
        try:
            params = [int(item) for item in params]
        except:
            raise ValueError("Value of 'params' can not be converted to list of ints.")
            

    n = _Support.get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname'.")
        
    c_params = _Support.list_part_to_c_array_no_conv(params, n, _C_GL_1_1.GLint)
    _C_GL_1_1.glTexGeniv(int(coord), int(pname), c_params)

### Viewport and Clipping ###

# Controlling the Viewport

def glDepthRange(zNear, zFar):
    """
    zNear           : float | SupportsFloat
    zFar            : float | SupportsFloat
    """
    if not isinstance(zNear, float):
        try:
            zNear = float(zNear)
        except Exception as exception:
            raise ValueError("Value of 'zNear' can not be converted to float.") from exception

    if not isinstance(zFar, float):
        try:
            zFar = float(zFar)
        except Exception as exception:
            raise ValueError("Value of 'zFar' can not be converted to float.") from exception

    _C_GL_1_1.glDepthRange(zNear, zFar)

def glViewport(x, y, width, height):
    """
    x               : int | SupportsInt
    y               : int | SupportsInt
    width           : int | SupportsInt
    height          : int | SupportsInt
    """
    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    if not isinstance(width, int):
        try:
            width = int(width)
        except Exception as exception:
            raise ValueError("Value of 'width' can not be converted to int.") from exception

    if not isinstance(height, int):
        try:
            height = int(height)
        except Exception as exception:
            raise ValueError("Value of 'height' can not be converted to int.") from exception

    _C_GL_1_1.glViewport(x, y, width, height)


# Clipping

def glClipPlane(plane, equation):
    """
    plane           : int | SupportsInt
    equation        : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(plane, int):
        try:
            plane = int(plane)
        except Exception as exception:
            raise ValueError("Value of 'plane' can not be converted to int.") from exception

    if not isinstance(equation, list) or not all(isinstance(item, float) for item in equation):
        try:
            equation = [float(item) for item in equation]
        except:
            raise ValueError("Value of 'equation' can not be converted to list of floats.")
            
    c_equation = _Support.list_part_to_c_array_no_conv(equation, 4, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glClipPlane(int(plane), c_equation)

def glGetClipPlane(plane):
    """
    plane           : int | SupportsInt
    Returns         : List[float]
        Corresponds to 'equation' parameter from OpenGL function specification.
    """
    if not isinstance(plane, int):
        try:
            plane = int(plane)
        except Exception as exception:
            raise ValueError("Value of 'plane' can not be converted to int.") from exception

    c_equation = _Support.make_c_array(_C_GL_1_1.GLdouble, 4)
    _C_GL_1_1.glGetClipPlane(plane, c_equation)
    return _Support.c_array_to_list(float, c_equation)

### Lighting and Color ###

# Lighting/ Lighting Parameter Specification

def glMaterialf(face, pname, param):
    """
    face            : int | SupportsInt
    pname           : int | SupportsInt
    param           : float | SupportsFloat
    """
    if not isinstance(face, int):
        try:
            face = int(face)
        except Exception as exception:
            raise ValueError("Value of 'face' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, float):
        try:
            param = float(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to float.") from exception

    _C_GL_1_1.glMaterialf(face, pname, param)

def glMaterialfv(face, pname, params):
    """
    face            : int | SupportsInt
    pname           : int | SupportsInt
    params          : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(face, int):
        try:
            face = int(face)
        except Exception as exception:
            raise ValueError("Value of 'face' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(params, list) or not all(isinstance(item, float) for item in params):
        try:
            params = [float(item) for item in params]
        except:
            raise ValueError("Value of 'params' can not be converted to list of floats.")

    c_params = _Support.list_to_c_array_no_conv(params, 1, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glMaterialfv(int(face), int(pname), c_params)

def glMateriali(face, pname, param):
    """
    face            : int | SupportsInt
    pname           : int | SupportsInt
    param           : int | SupportsInt
    """
    if not isinstance(face, int):
        try:
            face = int(face)
        except Exception as exception:
            raise ValueError("Value of 'face' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, int):
        try:
            param = int(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to int.") from exception

    _C_GL_1_1.glMateriali(face, pname, param)

def glMaterialiv(face, pname, params):
    """
    face            : int | SupportsInt
    pname           : int | SupportsInt
    params          : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(face, int):
        try:
            face = int(face)
        except Exception as exception:
            raise ValueError("Value of 'face' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(params, list) or not all(isinstance(item, int) for item in params):
        try:
            params = [int(item) for item in params]
        except:
            raise ValueError("Value of 'params' can not be converted to list of ints.")

    c_params = _Support.list_to_c_array_no_conv(params, 1, _C_GL_1_1.GLint)
    _C_GL_1_1.glMaterialiv(int(face), int(pname), c_params)


def glLightf(light, pname, param):
    """
    light           : int | SupportsInt
    pname           : int | SupportsInt
    param           : float | SupportsFloat
    """
    if not isinstance(light, int):
        try:
            light = int(light)
        except Exception as exception:
            raise ValueError("Value of 'light' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, float):
        try:
            param = float(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to float.") from exception

    _C_GL_1_1.glLightf(light, pname, param)

def glLightfv(light, pname, params):
    """
    light           : int | SupportsInt
    pname           : int | SupportsInt
    params          : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(light, int):
        try:
            light = int(light)
        except Exception as exception:
            raise ValueError("Value of 'light' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(params, list) or not all(isinstance(item, float) for item in params):
        try:
            params = [float(item) for item in params]
        except:
            raise ValueError("Value of 'params' can not be converted to list of floats.")

    c_params = _Support.list_to_c_array_no_conv(params, 1, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glLightfv(int(light), int(pname), c_params)

def glLighti(light, pname, param):
    """
    light           : int | SupportsInt
    pname           : int | SupportsInt
    param           : int | SupportsInt
    """
    if not isinstance(light, int):
        try:
            light = int(light)
        except Exception as exception:
            raise ValueError("Value of 'light' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, int):
        try:
            param = int(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to int.") from exception

    _C_GL_1_1.glLighti(light, pname, param)

def glLightiv(light, pname, params):
    """
    light           : int | SupportsInt
    pname           : int | SupportsInt
    params          : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(light, int):
        try:
            light = int(light)
        except Exception as exception:
            raise ValueError("Value of 'light' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(params, list) or not all(isinstance(item, int) for item in params):
        try:
            params = [int(item) for item in params]
        except:
            raise ValueError("Value of 'params' can not be converted to list of ints.")

    c_params = _Support.list_to_c_array_no_conv(params, 1, _C_GL_1_1.GLint)
    _C_GL_1_1.glLightiv(int(light), int(pname), c_params)


def glLightModelf(pname, param):
    """
    pname           : int | SupportsInt
    param           : float | SupportsFloat
    """
    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, float):
        try:
            param = float(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to float.") from exception

    _C_GL_1_1.glLightModelf(pname, param)

def glLightModelfv(pname, params):
    """
    pname           : int | SupportsInt
    params          : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(params, list) or not all(isinstance(item, float) for item in params):
        try:
            params = [float(item) for item in params]
        except:
            raise ValueError("Value of 'params' can not be converted to list of floats.")

    c_params = _Support.list_to_c_array_no_conv(params, 1, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glLightModelfv(int(pname), c_params)

def glLightModeli(pname, param):
    """
    pname           : int | SupportsInt
    param           : int | SupportsInt
    """
    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, int):
        try:
            param = int(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to int.") from exception

    _C_GL_1_1.glLightModeli(pname, param)

def glLightModeliv(pname, params):
    """
    pname           : int | SupportsInt
    params          : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(params, list) or not all(isinstance(item, int) for item in params):
        try:
            params = [int(item) for item in params]
        except:
            raise ValueError("Value of 'params' can not be converted to list of ints.")

    c_params = _Support.list_to_c_array_no_conv(params, 1, _C_GL_1_1.GLint)
    _C_GL_1_1.glLightModeliv(int(pname), c_params)


# ColorMaterial 

def glColorMaterial(face, mode):
    """
    face            : int | SupportsInt
    mode            : int | SupportsInt
    """
    if not isinstance(face, int):
        try:
            face = int(face)
        except Exception as exception:
            raise ValueError("Value of 'face' can not be converted to int.") from exception

    if not isinstance(mode, int):
        try:
            mode = int(mode)
        except Exception as exception:
            raise ValueError("Value of 'mode' can not be converted to int.") from exception

    _C_GL_1_1.glColorMaterial(face, mode)


# Flatshading

def glShadeModel(mode):
    """
    mode            : int | SupportsInt
    """
    if not isinstance(mode, int):
        try:
            mode = int(mode)
        except Exception as exception:
            raise ValueError("Value of 'mode' can not be converted to int.") from exception

    _C_GL_1_1.glShadeModel(mode)


# Queries

def glGetLightfv(light, pname):
    """
    light           : int | SupportsInt
    pname           : int | SupportsInt
    Returns         : List[float]
    """
    if not isinstance(light, int):
        try:
            light = int(light)
        except Exception as exception:
            raise ValueError("Value of 'light' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception
    
    if pname in [GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, GL_POSITION]:
        length = 4
    elif pname in [GL_SPOT_DIRECTION]:
        length = 3
    elif pname in [GL_SPOT_EXPONENT, GL_SPOT_CUTOFF, GL_CONSTANT_ATTENUATION, GL_LINEAR_ATTENUATION, GL_QUADRATIC_ATTENUATION]:
        length = 1
    else:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _Support.make_c_array(_C_GL_1_1.GLfloat, length)
    _C_GL_1_1.glGetLightfv(light, pname, c_params)
    return _Support.c_array_to_list(float, c_params)

def glGetLightiv(light, pname):
    """
    light           : int | SupportsInt
    pname           : int | SupportsInt
    Returns         : List[int]
    """
    if not isinstance(light, int):
        try:
            light = int(light)
        except Exception as exception:
            raise ValueError("Value of 'light' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception
    
    if pname in [GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, GL_POSITION]:
        length = 4
    elif pname in [GL_SPOT_DIRECTION]:
        length = 3
    elif pname in [GL_SPOT_EXPONENT, GL_SPOT_CUTOFF, GL_CONSTANT_ATTENUATION, GL_LINEAR_ATTENUATION, GL_QUADRATIC_ATTENUATION]:
        length = 1
    else:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _Support.make_c_array(_C_GL_1_1.GLint, length)
    _C_GL_1_1.glGetLightiv(light, pname, c_params)
    return _Support.c_array_to_list(int, c_params)

def glGetMaterialfv(face, pname):
    """
    face            : int | SupportsInt
    pname           : int | SupportsInt
    Returns         : List[float]
    """
    if not isinstance(face, int):
        try:
            face = int(face)
        except Exception as exception:
            raise ValueError("Value of 'face' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception
    
    if pname in [GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, GL_EMISSION]:
        length = 4
    elif pname in [GL_COLOR_INDEXES]:
        length = 3
    elif pname in [GL_SHININESS]:
        length = 1
    else:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _Support.make_c_array(_C_GL_1_1.GLfloat, length)
    _C_GL_1_1.glGetMaterialfv(face, pname, c_params)
    return _Support.c_array_to_list(float, c_params)

def glGetMaterialiv(face, pname):
    """
    face            : int | SupportsInt
    pname           : int | SupportsInt
    Returns         : List[int]
    """
    if not isinstance(face, int):
        try:
            face = int(face)
        except Exception as exception:
            raise ValueError("Value of 'face' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if pname in [GL_AMBIENT, GL_DIFFUSE, GL_SPECULAR, GL_EMISSION]:
        length = 4
    elif pname in [GL_COLOR_INDEXES]:
        length = 3
    elif pname in [GL_SHININESS]:
        length = 1
    else:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _Support.make_c_array(_C_GL_1_1.GLint, length)
    _C_GL_1_1.glGetMaterialiv(face, pname, c_params)
    return _Support.c_array_to_list(int, c_params)

### Rendering Control and Queries ###

# Current Raster Position

def glRasterPos2d(x, y):
    """
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    """
    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    _C_GL_1_1.glRasterPos2d(x, y)

def glRasterPos2dv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 2, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glRasterPos2dv(c_v)

def glRasterPos2f(x, y):
    """
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    """
    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    _C_GL_1_1.glRasterPos2f(x, y)

def glRasterPos2fv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 2, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glRasterPos2fv(c_v)

def glRasterPos2i(x, y):
    """
    x               : int | SupportsInt
    y               : int | SupportsInt
    """
    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    _C_GL_1_1.glRasterPos2i(x, y)

def glRasterPos2iv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 2, _C_GL_1_1.GLint)
    _C_GL_1_1.glRasterPos2iv(c_v)

def glRasterPos2s(x, y):
    """
    x               : int | SupportsInt
    y               : int | SupportsInt
    """
    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    _C_GL_1_1.glRasterPos2s(x, y)

def glRasterPos2sv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 2, _C_GL_1_1.GLshort)
    _C_GL_1_1.glRasterPos2sv(c_v)

def glRasterPos3d(x, y, z):
    """
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    z               : float | SupportsFloat
    """
    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    if not isinstance(z, float):
        try:
            z = float(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to float.") from exception

    _C_GL_1_1.glRasterPos3d(x, y, z)

def glRasterPos3dv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glRasterPos3dv(c_v)

def glRasterPos3f(x, y, z):
    """
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    z               : float | SupportsFloat
    """
    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    if not isinstance(z, float):
        try:
            z = float(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to float.") from exception

    _C_GL_1_1.glRasterPos3f(x, y, z)

def glRasterPos3fv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glRasterPos3fv(c_v)

def glRasterPos3i(x, y, z):
    """
    x               : int | SupportsInt
    y               : int | SupportsInt
    z               : int | SupportsInt
    """
    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    if not isinstance(z, int):
        try:
            z = int(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to int.") from exception

    _C_GL_1_1.glRasterPos3i(x, y, z)

def glRasterPos3iv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLint)
    _C_GL_1_1.glRasterPos3iv(c_v)

def glRasterPos3s(x, y, z):
    """
    x               : int | SupportsInt
    y               : int | SupportsInt
    z               : int | SupportsInt
    """
    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    if not isinstance(z, int):
        try:
            z = int(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to int.") from exception

    _C_GL_1_1.glRasterPos3s(x, y, z)

def glRasterPos3sv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 3, _C_GL_1_1.GLshort)
    _C_GL_1_1.glRasterPos3sv(c_v)

def glRasterPos4d(x, y, z, w):
    """
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    z               : float | SupportsFloat
    w               : float | SupportsFloat
    """
    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    if not isinstance(z, float):
        try:
            z = float(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to float.") from exception

    if not isinstance(w, float):
        try:
            w = float(w)
        except Exception as exception:
            raise ValueError("Value of 'w' can not be converted to float.") from exception

    _C_GL_1_1.glRasterPos4d(x, y, z, w)

def glRasterPos4dv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glRasterPos4dv(c_v)

def glRasterPos4f(x, y, z, w):
    """
    x               : float | SupportsFloat
    y               : float | SupportsFloat
    z               : float | SupportsFloat
    w               : float | SupportsFloat
    """
    if not isinstance(x, float):
        try:
            x = float(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to float.") from exception

    if not isinstance(y, float):
        try:
            y = float(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to float.") from exception

    if not isinstance(z, float):
        try:
            z = float(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to float.") from exception

    if not isinstance(w, float):
        try:
            w = float(w)
        except Exception as exception:
            raise ValueError("Value of 'w' can not be converted to float.") from exception

    _C_GL_1_1.glRasterPos4f(x, y, z, w)

def glRasterPos4fv(v):
    """
    v               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(v, list) or not all(isinstance(item, float) for item in v):
        try:
            v = [float(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of floats.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glRasterPos4fv(c_v)

def glRasterPos4i(x, y, z, w):
    """
    x               : int | SupportsInt
    y               : int | SupportsInt
    z               : int | SupportsInt
    w               : int | SupportsInt
    """
    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    if not isinstance(z, int):
        try:
            z = int(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to int.") from exception

    if not isinstance(w, int):
        try:
            w = int(w)
        except Exception as exception:
            raise ValueError("Value of 'w' can not be converted to int.") from exception

    _C_GL_1_1.glRasterPos4i(x, y, z, w)

def glRasterPos4iv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLint)
    _C_GL_1_1.glRasterPos4iv(c_v)

def glRasterPos4s(x, y, z, w):
    """
    x               : int | SupportsInt
    y               : int | SupportsInt
    z               : int | SupportsInt
    w               : int | SupportsInt
    """
    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    if not isinstance(z, int):
        try:
            z = int(z)
        except Exception as exception:
            raise ValueError("Value of 'z' can not be converted to int.") from exception

    if not isinstance(w, int):
        try:
            w = int(w)
        except Exception as exception:
            raise ValueError("Value of 'w' can not be converted to int.") from exception

    _C_GL_1_1.glRasterPos4s(x, y, z, w)

def glRasterPos4sv(v):
    """
    v               : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(v, list) or not all(isinstance(item, int) for item in v):
        try:
            v = [int(item) for item in v]
        except:
            raise ValueError("Value of 'v' can not be converted to list of ints.")

    c_v = _Support.list_part_to_c_array_no_conv(v, 4, _C_GL_1_1.GLshort)
    _C_GL_1_1.glRasterPos4sv(c_v)

### Rasterization ###

# Points

def glPointSize(size):
    """
    size            : float | SupportsFloat
    """
    if not isinstance(size, float):
        try:
            size = float(size)
        except Exception as exception:
            raise ValueError("Value of 'size' can not be converted to float.") from exception

    _C_GL_1_1.glPointSize(size)

# Line Segments

def glLineWidth(width):
    """
    width           : float | SupportsFloat
    """
    if not isinstance(width, float):
        try:
            width = float(width)
        except Exception as exception:
            raise ValueError("Value of 'width' can not be converted to float.") from exception

    _C_GL_1_1.glLineWidth(width)


# Other Line Segments Features

def glLineStipple(factor, pattern):
    """
    factor          : int | SupportsInt
    pattern         : int | SupportsInt
    """
    if not isinstance(factor, int):
        try:
            factor = int(factor)
        except Exception as exception:
            raise ValueError("Value of 'factor' can not be converted to int.") from exception

    if not isinstance(pattern, int):
        try:
            pattern = int(pattern)
        except Exception as exception:
            raise ValueError("Value of 'pattern' can not be converted to int.") from exception

    _C_GL_1_1.glLineStipple(factor, pattern)

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
    mode            : int | SupportsInt
    """
    if not isinstance(mode, int):
        try:
            mode = int(mode)
        except Exception as exception:
            raise ValueError("Value of 'mode' can not be converted to int.") from exception

    _C_GL_1_1.glFrontFace(mode)

def glCullFace(mode):
    """
    mode            : int | SupportsInt
    """
    if not isinstance(mode, int):
        try:
            mode = int(mode)
        except Exception as exception:
            raise ValueError("Value of 'mode' can not be converted to int.") from exception

    _C_GL_1_1.glCullFace(mode)

# Stippling


def glPolygonStipple(mask):
    """
    mask             : bytes
    """
    if not isinstance(mask, bytes):
        try:
            mask = bytes(mask)
        except Exception as exception:
            raise ValueError("Value of 'mask' can not be converted to bytes.") from exception
            
    size = 32 * 32 // 8
    c_mask = (_C_GL_1_1.GLubyte * size).from_buffer_copy(mask)
    _C_GL_1_1.glPolygonStipple(c_mask)

# Polygon Rasterization & Depth Offset

def glPolygonMode(face, mode):
    """
    face            : int | SupportsInt
    mode            : int | SupportsInt
    """
    if not isinstance(face, int):
        try:
            face = int(face)
        except Exception as exception:
            raise ValueError("Value of 'face' can not be converted to int.") from exception

    if not isinstance(mode, int):
        try:
            mode = int(mode)
        except Exception as exception:
            raise ValueError("Value of 'mode' can not be converted to int.") from exception

    _C_GL_1_1.glPolygonMode(face, mode)

def glPolygonOffset(factor, units):
    """
    factor          : float | SupportsFloat
    units           : float | SupportsFloat
    """
    if not isinstance(factor, float):
        try:
            factor = float(factor)
        except Exception as exception:
            raise ValueError("Value of 'factor' can not be converted to float.") from exception

    if not isinstance(units, float):
        try:
            units = float(units)
        except Exception as exception:
            raise ValueError("Value of 'units' can not be converted to float.") from exception

    _C_GL_1_1.glPolygonOffset(factor, units)

# Pixel Rectangles

def glPixelStoref(pname, param):
    """
    pname           : int | SupportsInt
    param           : float | SupportsFloat
    """
    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, float):
        try:
            param = float(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to float.") from exception

    _C_GL_1_1.glPixelStoref(pname, param)

def glPixelStorei(pname, param):
    """
    pname           : int | SupportsInt
    param           : int | SupportsInt
    """
    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, int):
        try:
            param = int(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to int.") from exception

    _C_GL_1_1.glPixelStorei(pname, param)


# Pixel Transfer Modes

def glPixelTransferf(pname, param):
    """
    pname           : int | SupportsInt
    param           : float | SupportsFloat
    """
    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, float):
        try:
            param = float(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to float.") from exception

    _C_GL_1_1.glPixelTransferf(pname, param)

def glPixelTransferi(pname, param):
    """
    pname           : int | SupportsInt
    param           : int | SupportsInt
    """
    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, int):
        try:
            param = int(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to int.") from exception

    _C_GL_1_1.glPixelTransferi(pname, param)


def glPixelMapfv(map_, values):
    """
    map_            : int | SupportsInt
    values          : bytes | List[float] | Iterable[SupportsFloat]
    
    Note: 'mapsize' is deduced form 'values'.
    """
    if not isinstance(map_, int):
        try:
            map_ = int(map_)
        except Exception as exception:
            raise ValueError("Value of 'map_' can not be converted to int.") from exception

    if isinstance(values, bytes):
        num_of_bytes = len(values)
        mapsize = num_of_bytes // 4 # div by size in bytes of single precision float 

        c_values_buffer = (_C_GL_1_1.GLubyte * num_of_bytes).from_buffer_copy(values)
        c_values = _ctypes.cast(c_values_buffer, _ctypes.POINTER(_C_GL_1_1.GLfloat))
    else:
        if not isinstance(values, list) or not all(isinstance(item, float) for item in values):
            try:
                values = [float(item) for item in values]
            except:
                raise ValueError("Value of 'values' can not be converted to list of floats.")

        mapsize = len(values)

        c_values = _Support.list_to_c_array(float, values, mapsize, _C_GL_1_1.GLfloat)

    _C_GL_1_1.glPixelMapfv(map_, mapsize, c_values)

def glPixelMapuiv(map_, values):
    """
    map_            : int | SupportsInt
    values          : bytes | List[int] | Iterable[SupportsInt]    
    
    Note: 'mapsize' is deduced form 'values'.
    """
    if not isinstance(map_, int):
        try:
            map_ = int(map_)
        except Exception as exception:
            raise ValueError("Value of 'map_' can not be converted to int.") from exception

    if isinstance(values, bytes):
        num_of_bytes = len(values)
        mapsize = num_of_bytes // 4 # div by size in bytes of single precision float 

        c_values_buffer = (_C_GL_1_1.GLubyte * num_of_bytes).from_buffer_copy(values)
        c_values = _ctypes.cast(c_values_buffer, _ctypes.POINTER(_C_GL_1_1.GLuint))
    else:
        if not isinstance(values, list) or not all(isinstance(item, int) for item in values):
            try:
                values = [int(item) for item in values]
            except:
                raise ValueError("Value of 'values' can not be converted to list of ints.")
            
        mapsize = len(values)

        c_values = _Support.list_to_c_array(int, values, mapsize, _C_GL_1_1.GLuint)

    _C_GL_1_1.glPixelMapuiv(map_, mapsize, c_values)

def glPixelMapusv(map_, values):
    """
    map_            : int | SupportsInt
    values          : List[int] | Iterable[SupportsInt]
    
    Note: 'mapsize' is deduced form 'values'.
    """
    if not isinstance(map_, int):
        try:
            map_ = int(map_)
        except Exception as exception:
            raise ValueError("Value of 'map_' can not be converted to int.") from exception

    if isinstance(values, bytes):
        num_of_bytes = len(values)
        mapsize = num_of_bytes // 2 # div by size in bytes of single precision float 

        c_values_buffer = (_C_GL_1_1.GLubyte * num_of_bytes).from_buffer_copy(values)
        c_values = _ctypes.cast(c_values_buffer, _ctypes.POINTER(_C_GL_1_1.GLushort))
    else:
        if not isinstance(values, list) or not all(isinstance(item, int) for item in values):
            try:
                values = [int(item) for item in values]
            except:
                raise ValueError("Value of 'values' can not be converted to list of ints.")
            
        mapsize = len(values)

        c_values = _Support.list_to_c_array(int, values, mapsize, _C_GL_1_1.GLushort)

    _C_GL_1_1.glPixelMapusv(map_, mapsize, c_values)


# Enumerated Queries

def glGetPixelMapfv(map_, is_return_bytes = False):
    """
    map_            : int | SupportsInt
    is_return_bytes : bool 
    Returns         : bytes | List[float]
        bytes, when 'is_return_bytes' is True.
        list of floats, when 'is_return_bytes' is False (default).

        Equivalent of 'data' from OpenGL function specification.
    """
    if not isinstance(map_, int):
        try:
            map_ = int(map_)
        except Exception as exception:
            raise ValueError("Value of 'map_' can not be converted to int.") from exception

    size_id = _Support.get_pixel_map_size_id(map_)
    if size_id is None:
        raise ValueError("Unexpected value of 'map_' parameter.")
    mapsize = glGetIntegerv(size_id)[0]
    c_data = _Support.make_c_array(_C_GL_1_1.GLfloat, mapsize)

    _C_GL_1_1.glGetPixelMapfv(map_, c_data)

    if is_return_bytes:
        return bytes(c_data)
    else:
        return _Support.c_array_to_list(float, c_data)

def glGetPixelMapuiv(map_, is_return_bytes = False):
    """
    map_            : int | SupportsInt
    is_return_bytes : bool 
    Returns         : bytes | List[int]
        bytes, when 'is_return_bytes' is True.
        list of ints, when 'is_return_bytes' is False (default).

        Equivalent of 'data' from OpenGL function specification.
    """
    if not isinstance(map_, int):
       try:
           map_ = int(map_)
       except Exception as exception:
           raise ValueError("Value of 'map_' can not be converted to int.") from exception

    size_id = _Support.get_pixel_map_size_id(map_)
    if size_id is None:
        raise ValueError("Unexpected value of 'map_' parameter.")
    mapsize = glGetIntegerv(size_id)[0]
    c_data = _Support.make_c_array(_C_GL_1_1.GLuint, mapsize)

    _C_GL_1_1.glGetPixelMapuiv(int(map_), c_data)

    if is_return_bytes:
        return bytes(c_data)
    else:
        return _Support.c_array_to_list(int, c_data)

def glGetPixelMapusv(map_, is_return_bytes = False):
    """
    map_            : int | SupportsInt
    Returns         : bytes | List[int]
        bytes, when 'is_return_bytes' is True.
        list of ints, when 'is_return_bytes' is False (default).

        Equivalent of 'data' from OpenGL function specification.
    """
    if not isinstance(map_, int):
        try:
            map_ = int(map_)
        except Exception as exception:
            raise ValueError("Value of 'map_' can not be converted to int.") from exception

    size_id = _Support.get_pixel_map_size_id(map_)
    if size_id is None:
        raise ValueError("Unexpected value of 'map_' parameter.")
    mapsize = glGetIntegerv(size_id)[0]
    c_data = _Support.make_c_array(_C_GL_1_1.GLushort, mapsize)

    _C_GL_1_1.glGetPixelMapusv(int(map_), c_data)

    if is_return_bytes:
        return bytes(c_data)
    else:
        return _Support.c_array_to_list(int, c_data)

# Rasterization of Pixel Rectangles

def glDrawPixels(width, height, format_, type_, pixels):
    """
    width           : int | SupportsInt
    height          : int | SupportsInt
    format_         : int | SupportsInt
    type_           : int | SupportsInt
    pixels          : bytes
    pixels          : List[float] | Iterable[SupportsFloat]
        Acceptable when 'type_' is GL_FLOAT and 'format_' is either GL_RGB or GL_RGBA.
        Each element of list 'pixels' represents single color channel or alpha channel.
    """
    if not isinstance(width, int):
        try:
            width = int(width)
        except Exception as exception:
            raise ValueError("Value of 'width' can not be converted to int.") from exception

    if not isinstance(height, int):
        try:
            height = int(height)
        except Exception as exception:
            raise ValueError("Value of 'height' can not be converted to int.") from exception

    if not isinstance(format_, int):
        try:
            format_ = int(format_)
        except Exception as exception:
            raise ValueError("Value of 'format_' can not be converted to int.") from exception

    if not isinstance(type_, int):
        try:
            type_ = int(type_)
        except Exception as exception:
            raise ValueError("Value of 'type_' can not be converted to int.") from exception
            
    if isinstance(pixels, bytes):
        c_pixels = pixels
    else:    
        if type_ == GL_FLOAT and format_ in [GL_RGB, GL_RGBA]:
            if not isinstance(pixels, list) or not all(isinstance(item, float) for item in pixels):
                try:
                    pixels = [float(item) for item in pixels]
                except:
                    raise ValueError("Value of 'pixels' can not be converted to list of floats.")
                    
            pixel_size  = 3 if format_ is GL_RGB else 4
            size        = int(width) * int(height) * pixel_size
            c_pixels    = _Support.list_part_to_c_array_no_conv(pixels, size, _C_GL_1_1.GLfloat)
        else:
            raise ValueError("Parameter 'pixels' can be accepted as list of integers or floats, only when 'type_' is GL_FLOAT and 'format_' is either GL_RGB or GL_RGBA.")

    _C_GL_1_1.glDrawPixels(width, height, format_, type_, c_pixels)

def glPixelZoom(xfactor, yfactor):
    """
    xfactor         : float | SupportsFloat
    yfactor         : float | SupportsFloat
    """
    if not isinstance(xfactor, float):
        try:
            xfactor = float(xfactor)
        except Exception as exception:
            raise ValueError("Value of 'xfactor' can not be converted to float.") from exception

    if not isinstance(yfactor, float):
        try:
            yfactor = float(yfactor)
        except Exception as exception:
            raise ValueError("Value of 'yfactor' can not be converted to float.") from exception

    _C_GL_1_1.glPixelZoom(xfactor, yfactor)

# Bitmaps

def glBitmap(width, height, xorig, yorig, xmove, ymove, bitmap):
    """
    width           : int | SupportsInt
    height          : int | SupportsInt
    xorig           : float | SupportsFloat
    yorig           : float | SupportsFloat
    xmove           : float | SupportsFloat
    ymove           : float | SupportsFloat
    bitmap          : bytes
    """
    if not isinstance(width, int):
        try:
            width = int(width)
        except Exception as exception:
            raise ValueError("Value of 'width' can not be converted to int.") from exception

    if not isinstance(height, int):
        try:
            height = int(height)
        except Exception as exception:
            raise ValueError("Value of 'height' can not be converted to int.") from exception

    if not isinstance(xorig, float):
        try:
            xorig = float(xorig)
        except Exception as exception:
            raise ValueError("Value of 'xorig' can not be converted to float.") from exception

    if not isinstance(yorig, float):
        try:
            yorig = float(yorig)
        except Exception as exception:
            raise ValueError("Value of 'yorig' can not be converted to float.") from exception

    if not isinstance(xmove, float):
        try:
            xmove = float(xmove)
        except Exception as exception:
            raise ValueError("Value of 'xmove' can not be converted to float.") from exception

    if not isinstance(ymove, float):
        try:
            ymove = float(ymove)
        except Exception as exception:
            raise ValueError("Value of 'ymove' can not be converted to float.") from exception
            
    if not isinstance(bitmap, bytes):
        try:
            bitmap = bytes(bitmap)
        except Exception as exception:
            raise ValueError("Value of 'bitmap' can not be converted to bytes.") from exception
    
    size = (width * height) // 8

    c_bitmap = (_C_GL_1_1.GLubyte * size).from_buffer_copy(bitmap)
    _C_GL_1_1.glBitmap(width, height, xorig, yorig, xmove, ymove, c_bitmap)

### Texturing ###

# Texture Image Specification

def glTexImage1D(target, level, internalformat, width, border, format_, type_, pixels):
    """
    target          : int | SupportsInt
    level           : int | SupportsInt
    internalformat  : int | SupportsInt
    width           : int | SupportsInt
    border          : int | SupportsInt
    format_         : int | SupportsInt
    type_           : int | SupportsInt
    pixels          : bytes 
    pixels          : Lists[float] | Iterable[SupportsFloat]
        Acceptable, when parameter 'type_' is GL_FLOAT and parameter 'format_' is either GL_RGB or GL_RGBA.
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(level, int):
        try:
            level = int(level)
        except Exception as exception:
            raise ValueError("Value of 'level' can not be converted to int.") from exception

    if not isinstance(internalformat, int):
        try:
            internalformat = int(internalformat)
        except Exception as exception:
            raise ValueError("Value of 'internalformat' can not be converted to int.") from exception

    if not isinstance(width, int):
        try:
            width = int(width)
        except Exception as exception:
            raise ValueError("Value of 'width' can not be converted to int.") from exception

    if not isinstance(border, int):
        try:
            border = int(border)
        except Exception as exception:
            raise ValueError("Value of 'border' can not be converted to int.") from exception

    if not isinstance(format_, int):
        try:
            format_ = int(format_)
        except Exception as exception:
            raise ValueError("Value of 'format_' can not be converted to int.") from exception

    if not isinstance(type_, int):
        try:
            type_ = int(type_)
        except Exception as exception:
            raise ValueError("Value of 'type_' can not be converted to int.") from exception

    n = _Support.get_tex_format_element_number(format_)
    if n is None:
        raise ValueError("Unexpected value of 'format_'.")

    md = _Support.get_tex_type_mul_div_size(type_)
    if md is None:
        raise ValueError("Unexpected value of 'type_'.")

    m, d = md

    expected_size = width           # in pixels
    single_item_size = (n * m // d) # in bytes
    
    if isinstance(pixels, bytes):
        size = len(pixels) // single_item_size

        if expected_size != size:
            raise ValueError("Unexpected size of 'pixels'. Should be %d pixels. It's %d pixels." % (expected_size, size))

        c_pixels = pixels
    else:
        if type_ != GL_FLOAT:
            raise ValueError("Unexpected value of 'type_'. For 'pixels' being a list of ints or floats, parameter 'type_' must be GL_FLOAT.")
        if format_ not in [GL_RGB, GL_RGBA]:
            raise ValueError("Unexpected value of 'format_'. For 'lists' being a list of ints or floats, parameter 'type_' must be either GL_RGB or GL_RGBA.")
        else:
            if not isinstance(pixels, list) or not all(isinstance(item, float) for item in pixels):
                try:
                    pixels = [float(item) for item in pixels]
                except:
                    raise ValueError("Value of 'pixels' can not be converted to list of floats.")
        
            # adjusted by size of single precision float
            size = len(pixels) * 4 // single_item_size  # in pixels

            if expected_size != size: 
                raise ValueError("Unexpected size of 'pixels'")

            c_pixels = _Support.list_to_c_array_no_conv(pixels, len(pixels), _C_GL_1_1.GLfloat)

    _C_GL_1_1.glTexImage1D(target, level, internalformat, width, border, format_, type_, c_pixels)

def glTexImage2D(target, level, internalformat, width, height, border, format_, type_, pixels):
    """
    target          : int | SupportsInt
    level           : int | SupportsInt
    internalformat  : int | SupportsInt
    width           : int | SupportsInt
    height          : int | SupportsInt
    border          : int | SupportsInt
    format_         : int | SupportsInt
    type_           : int | SupportsInt
    pixels          : bytes
    pixels          : Lists[float | Any]
        Acceptable, when parameter 'type_' is GL_FLOAT and parameter 'format_' is either GL_RGB or GL_RGBA.
        All items are converted to floats.
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(level, int):
        try:
            level = int(level)
        except Exception as exception:
            raise ValueError("Value of 'level' can not be converted to int.") from exception

    if not isinstance(internalformat, int):
        try:
            internalformat = int(internalformat)
        except Exception as exception:
            raise ValueError("Value of 'internalformat' can not be converted to int.") from exception

    if not isinstance(width, int):
        try:
            width = int(width)
        except Exception as exception:
            raise ValueError("Value of 'width' can not be converted to int.") from exception

    if not isinstance(height, int):
        try:
            height = int(height)
        except Exception as exception:
            raise ValueError("Value of 'height' can not be converted to int.") from exception

    if not isinstance(border, int):
        try:
            border = int(border)
        except Exception as exception:
            raise ValueError("Value of 'border' can not be converted to int.") from exception

    if not isinstance(format_, int):
        try:
            format_ = int(format_)
        except Exception as exception:
            raise ValueError("Value of 'format_' can not be converted to int.") from exception

    if not isinstance(type_, int):
        try:
            type_ = int(type_)
        except Exception as exception:
            raise ValueError("Value of 'type_' can not be converted to int.") from exception
            
    n = _Support.get_tex_format_element_number(format_)
    if n is None:
        raise ValueError("Unexpected value of 'format_'")

    md = _Support.get_tex_type_mul_div_size(type_)
    if md is None:
        raise ValueError("Unexpected value of 'type_'")

    m, d = md

    expected_size = width * height  # in pixels
    single_item_size = (n * m // d) # in bytes

    if isinstance(pixels, bytes):
        size = len(pixels) // single_item_size

        if expected_size != size:
            raise ValueError("Unexpected size of 'pixels'. Should be %d pixels. It's %d pixels." % (expected_size, size))

        c_pixels = pixels
        
    else:
        if type_ != GL_FLOAT:
            raise ValueError("Unexpected value of 'type_'. For 'pixels' being a list of ints or floats, 'type_' parameter must be GL_FLOAT.")
        if format_ not in [GL_RGB, GL_RGBA]:
            raise ValueError("Unexpected value of 'format_'. For 'lists' being a list of ints or floats, 'type_' parameter must be either GL_RGB or GL_RGBA.")
        else:
            if not isinstance(pixels, list) or not all(isinstance(item, float) for item in pixels):
                try:
                    pixels = [float(item) for item in pixels]
                except:
                    raise ValueError("Value of 'pixels' can not be converted to list of floats.")
                    
            # adjusted by size of single precision float
            size = len(pixels) * 4 // single_item_size # in pixels

            if expected_size != size: 
                raise ValueError("Unexpected size of 'pixels'")

            c_pixels = _Support.list_to_c_array_no_conv(pixels, len(pixels), _C_GL_1_1.GLfloat)

    _C_GL_1_1.glTexImage2D(target, level, internalformat, width, height, border, format_, type_, c_pixels)


# Alt. Texture Image Specification Commands 

def glCopyTexImage1D(target, level, internalFormat, x, y, width, border):
    """
    target          : int | SupportsInt
    level           : int | SupportsInt
    internalFormat  : int | SupportsInt
    x               : int | SupportsInt
    y               : int | SupportsInt
    width           : int | SupportsInt
    border          : int | SupportsInt
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(level, int):
        try:
            level = int(level)
        except Exception as exception:
            raise ValueError("Value of 'level' can not be converted to int.") from exception

    if not isinstance(internalFormat, int):
        try:
            internalFormat = int(internalFormat)
        except Exception as exception:
            raise ValueError("Value of 'internalFormat' can not be converted to int.") from exception

    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    if not isinstance(width, int):
        try:
            width = int(width)
        except Exception as exception:
            raise ValueError("Value of 'width' can not be converted to int.") from exception

    if not isinstance(border, int):
        try:
            border = int(border)
        except Exception as exception:
            raise ValueError("Value of 'border' can not be converted to int.") from exception

    _C_GL_1_1.glCopyTexImage1D(target, level, internalFormat, x, y, width, border)

def glCopyTexImage2D(target, level, internalFormat, x, y, width, height, border):
    """
    target          : int | SupportsInt
    level           : int | SupportsInt
    internalFormat  : int | SupportsInt
    x               : int | SupportsInt
    y               : int | SupportsInt
    width           : int | SupportsInt
    height          : int | SupportsInt
    border          : int | SupportsInt
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(level, int):
        try:
            level = int(level)
        except Exception as exception:
            raise ValueError("Value of 'level' can not be converted to int.") from exception

    if not isinstance(internalFormat, int):
        try:
            internalFormat = int(internalFormat)
        except Exception as exception:
            raise ValueError("Value of 'internalFormat' can not be converted to int.") from exception

    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    if not isinstance(width, int):
        try:
            width = int(width)
        except Exception as exception:
            raise ValueError("Value of 'width' can not be converted to int.") from exception

    if not isinstance(height, int):
        try:
            height = int(height)
        except Exception as exception:
            raise ValueError("Value of 'height' can not be converted to int.") from exception

    if not isinstance(border, int):
        try:
            border = int(border)
        except Exception as exception:
            raise ValueError("Value of 'border' can not be converted to int.") from exception

    _C_GL_1_1.glCopyTexImage2D(target, level, internalFormat, x, y, width, height, border)

def glTexSubImage1D(target, level, xoffset, width, format_, type_, pixels):
    """
    target          : int | SupportsInt
    level           : int | SupportsInt
    xoffset         : int | SupportsInt
    width           : int | SupportsInt
    format_         : int | SupportsInt
    type_           : int | SupportsInt
    pixels          : bytes
    pixels          : Lists[float | int]
        Acceptable, when parameter 'type_' is GL_FLOAT and parameter 'format_' is either GL_RGB or GL_RGBA.
        All elements of list are converted to floats
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(level, int):
        try:
            level = int(level)
        except Exception as exception:
            raise ValueError("Value of 'level' can not be converted to int.") from exception

    if not isinstance(xoffset, int):
        try:
            xoffset = int(xoffset)
        except Exception as exception:
            raise ValueError("Value of 'xoffset' can not be converted to int.") from exception

    if not isinstance(width, int):
        try:
            width = int(width)
        except Exception as exception:
            raise ValueError("Value of 'width' can not be converted to int.") from exception

    if not isinstance(format_, int):
        try:
            format_ = int(format_)
        except Exception as exception:
            raise ValueError("Value of 'format_' can not be converted to int.") from exception

    if not isinstance(type_, int):
        try:
            type_ = int(type_)
        except Exception as exception:
            raise ValueError("Value of 'type_' can not be converted to int.") from exception
    
    n = _Support.get_tex_format_element_number(format_)
    if n is None:
        raise ValueError("Unexpected value of 'format_'")

    md = _Support.get_tex_type_mul_div_size(type_)
    if md is None:
        raise ValueError("Unexpected value of 'type_'")

    m, d = md

    expected_size = width           # in pixels
    single_item_size = (n * m // d) # in bytes
    
    if isinstance(pixels, bytes):
        size = len(pixels) // single_item_size

        if expected_size != size:
            raise ValueError("Unexpected size of 'pixels'. Should be %d pixels. It's %d pixels." % (expected_size, size))

        c_pixels = pixels
    else:
        if type_ != GL_FLOAT:
            raise ValueError("Unexpected value of 'type_'. For 'pixels' being list of ints or floats, 'type_' must be GL_FLOAT.")
        if format_ not in [GL_RGB, GL_RGBA]:
            raise ValueError("Unexpected value of 'format_'. For 'lists' being list of ints or floats, 'type_' must be either GL_RGB or GL_RGBA.")
        else:
            if not isinstance(pixels, list) or not all(isinstance(item, float) for item in pixels):
                try:
                    pixels = [float(item) for item in pixels]
                except:
                    raise ValueError("Value of 'pixels' can not be converted to list of floats.")
                    
            # adjusted by size of single precision float
            size = len(pixels) * 4 // single_item_size  # in pixels

            if expected_size != size: 
                raise ValueError("Unexpected size of 'pixels'.")

            c_pixels = _Support.list_to_c_array_no_conv(pixels, len(pixels), _C_GL_1_1.GLfloat)

    _C_GL_1_1.glTexSubImage1D(target, level, xoffset, width, format_, type_, c_pixels)

def glTexSubImage2D(target, level, xoffset, yoffset, width, height, format_, type_, pixels):
    """
    target          : int | SupportsInt
    level           : int | SupportsInt
    xoffset         : int | SupportsInt
    yoffset         : int | SupportsInt
    width           : int | SupportsInt
    height          : int | SupportsInt
    format_         : int | SupportsInt
    type_           : int | SupportsInt
    pixels          : bytes
    pixels          : Lists[float | Any]
        Acceptable, when parameter 'type_' is GL_FLOAT and parameter 'format_' is either GL_RGB or GL_RGBA.
        All items are converted to floats.
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(level, int):
        try:
            level = int(level)
        except Exception as exception:
            raise ValueError("Value of 'level' can not be converted to int.") from exception

    if not isinstance(xoffset, int):
        try:
            xoffset = int(xoffset)
        except Exception as exception:
            raise ValueError("Value of 'xoffset' can not be converted to int.") from exception

    if not isinstance(yoffset, int):
        try:
            yoffset = int(yoffset)
        except Exception as exception:
            raise ValueError("Value of 'yoffset' can not be converted to int.") from exception

    if not isinstance(width, int):
        try:
            width = int(width)
        except Exception as exception:
            raise ValueError("Value of 'width' can not be converted to int.") from exception

    if not isinstance(height, int):
        try:
            height = int(height)
        except Exception as exception:
            raise ValueError("Value of 'height' can not be converted to int.") from exception

    if not isinstance(format_, int):
        try:
            format_ = int(format_)
        except Exception as exception:
            raise ValueError("Value of 'format_' can not be converted to int.") from exception

    if not isinstance(type_, int):
        try:
            type_ = int(type_)
        except Exception as exception:
            raise ValueError("Value of 'type_' can not be converted to int.") from exception
    
    n = _Support.get_tex_format_element_number(format_)
    if n is None:
        raise ValueError("Unexpected value of 'format_'")

    md = _Support.get_tex_type_mul_div_size(type_)
    if md is None:
        raise ValueError("Unexpected value of 'type_'")

    m, d = md

    expected_size = width * height  # in pixels
    single_item_size = (n * m // d) # in bytes

    if isinstance(pixels, bytes):
        size = len(pixels) // single_item_size

        if expected_size != size:
            raise ValueError("Unexpected size of 'pixels'. Should be %d pixels. It's %d pixels." % (expected_size, size))

        c_pixels = pixels
    else:
        if type_ != GL_FLOAT:
            raise ValueError("Unexpected value of 'type_'. For 'pixels' being list of ints or floats, 'type_' must be GL_FLOAT.")
        if format_ not in [GL_RGB, GL_RGBA]:
            raise ValueError("Unexpected value of 'format_'. For 'lists' being list of ints or floats, 'type_' must be either GL_RGB or GL_RGBA.")
        else:
            if not isinstance(pixels, list) or not all(isinstance(item, float) for item in pixels):
                try:
                    pixels = [float(item) for item in pixels]
                except:
                    raise ValueError("Value of 'pixels' can not be converted to list of floats.")
        
            # adjusted by size of single precision float
            size = len(pixels) * 4 // single_item_size # in pixels

            if expected_size != size: 
                raise ValueError("Unexpected size of 'pixels'.")

            c_pixels = _Support.list_to_c_array_no_conv(pixels, len(pixels), _C_GL_1_1.GLfloat)

    _C_GL_1_1.glTexSubImage2D(target, level, xoffset, yoffset, width, height, format_, type_, c_pixels)

def glCopyTexSubImage1D(target, level, xoffset, x, y, width):
    """
    target          : int | SupportsInt
    level           : int | SupportsInt
    xoffset         : int | SupportsInt
    x               : int | SupportsInt
    y               : int | SupportsInt
    width           : int | SupportsInt
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(level, int):
        try:
            level = int(level)
        except Exception as exception:
            raise ValueError("Value of 'level' can not be converted to int.") from exception

    if not isinstance(xoffset, int):
        try:
            xoffset = int(xoffset)
        except Exception as exception:
            raise ValueError("Value of 'xoffset' can not be converted to int.") from exception

    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    if not isinstance(width, int):
        try:
            width = int(width)
        except Exception as exception:
            raise ValueError("Value of 'width' can not be converted to int.") from exception

    _C_GL_1_1.glCopyTexSubImage1D(target, level, xoffset, x, y, width)

def glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height):
    """
    target          : int | SupportsInt
    level           : int | SupportsInt
    xoffset         : int | SupportsInt
    yoffset         : int | SupportsInt
    x               : int | SupportsInt
    y               : int | SupportsInt
    width           : int | SupportsInt
    height          : int | SupportsInt
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(level, int):
        try:
            level = int(level)
        except Exception as exception:
            raise ValueError("Value of 'level' can not be converted to int.") from exception

    if not isinstance(xoffset, int):
        try:
            xoffset = int(xoffset)
        except Exception as exception:
            raise ValueError("Value of 'xoffset' can not be converted to int.") from exception

    if not isinstance(yoffset, int):
        try:
            yoffset = int(yoffset)
        except Exception as exception:
            raise ValueError("Value of 'yoffset' can not be converted to int.") from exception

    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    if not isinstance(width, int):
        try:
            width = int(width)
        except Exception as exception:
            raise ValueError("Value of 'width' can not be converted to int.") from exception

    if not isinstance(height, int):
        try:
            height = int(height)
        except Exception as exception:
            raise ValueError("Value of 'height' can not be converted to int.") from exception

    _C_GL_1_1.glCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height)


# Texture Parameters

def glTexParameterf(target, pname, param):
    """
    target          : int | SupportsInt
    pname           : int | SupportsInt
    param           : float | SupportsFloat
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, float):
        try:
            param = float(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to float.") from exception

    _C_GL_1_1.glTexParameterf(target, pname, param)

def glTexParameterfv(target, pname, params):
    """
    target          : int | SupportsInt
    pname           : int | SupportsInt
    params          : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(params, list) or not all(isinstance(item, float) for item in params):
        try:
            params = [float(item) for item in params]
        except:
            raise ValueError("Value of 'params' can not be converted to list of floats.")
            
    length = _Support.get_tex_parameter_length(pname)
    if length is None:
        raise ValueError("Unexpected value of 'pname'.")
    elif length > len(params):
        raise ValueError("To small length of 'params'.")
    
    c_params = _Support.list_to_c_array_no_conv(params, length, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glTexParameterfv(target, pname, c_params)

def glTexParameteri(target, pname, param):
    """
    target          : int | SupportsInt
    pname           : int | SupportsInt
    param           : int | SupportsInt
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, int):
        try:
            param = int(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to int.") from exception

    _C_GL_1_1.glTexParameteri(target, pname, param)

def glTexParameteriv(target, pname, params):
    """
    target          : int | SupportsInt
    pname           : int | SupportsInt
    params          : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(params, list) or not all(isinstance(item, int) for item in params):
        try:
            params = [int(item) for item in params]
        except:
            raise ValueError("Value of 'params' can not be converted to list of ints.")
            
    length = _Support.get_tex_parameter_length(pname)
    if length is None:
        raise ValueError("Unexpected value of 'pname'.")
    elif length > len(params):
        raise ValueError("To small length of 'params'.")
    
    c_params = _Support.list_to_c_array_no_conv(params, length, _C_GL_1_1.GLint)
    _C_GL_1_1.glTexParameteriv(target, pname, c_params)

# Texture Objects

def glBindTexture(target, texture):
    """
    target          : int | SupportsInt
    texture         : int | SupportsInt

    Note: According to OpenGL specification of this function, 
    binding with 0 should generate GL_INVALID_VALUE, 
    because default texture is not generated by glGenTextures function.
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(texture, int):
        try:
            texture = int(texture)
        except Exception as exception:
            raise ValueError("Value of 'texture' can not be converted to int.") from exception

    _C_GL_1_1.glBindTexture(target, texture)

def glDeleteTextures(textures):
    """
    textures        : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(textures, list) or not all(isinstance(item, int) for item in textures):
        try:
            textures = [int(item) for item in textures]
        except:
            raise ValueError("Value of 'textures' can not be converted to list of ints.")
            
    n = len(textures)
    c_textures = _Support.list_to_c_array_no_conv(textures, n, _C_GL_1_1.GLuint)
    _C_GL_1_1.glDeleteTextures(n, c_textures)

def glGenTextures(n):
    """
    n               : int | SupportsInt
    Returns         : List[int]
        Refers to 'textures' parameter from OpenGL function specification. 
    """
    if not isinstance(n, int):
        try:
            n = int(n)
        except Exception as exception:
            raise ValueError("Value of 'n' can not be converted to int.") from exception
            
    c_textures = _Support.make_c_array(_C_GL_1_1.GLuint, n)
    _C_GL_1_1.glGenTextures(n, c_textures)
    return _Support.c_array_to_list(int, c_textures)

def glAreTexturesResident(textures, residences = None):
    """
    textures        : List[int] | SupportsInt
    residences      : List[bool] | None
    Returns         : bool
        True
            All textures are resident, and parameter 'residences' is untouched.
        False
            Not all textures are resident, and when parameter 'residences' is list,
            then it is set with residence information of each texture provided in parameter 'texture'.

    Note: glAreTexturesResident is deprecated. Information provided by this function might not be correct.
    """
    if not isinstance(textures, list) or not all(isinstance(item, int) for item in textures):
        try:
            textures = [int(item) for item in textures]
        except:
            raise ValueError("Value of 'textures' can not be converted to list of ints.")

    if (residences is not None) and (not isinstance(residences, list) or not all(isinstance(item, bool) for item in residences)):
            raise TypeError("Unexpected type of 'residences'.")
    
    n = len(textures)

    c_textures      = _Support.list_to_c_array_no_conv(textures, n, _C_GL_1_1.GLuint)
    c_residences    = _Support.make_c_array(_C_GL_1_1.GLboolean, n)

    is_all_resident = bool(_C_GL_1_1.glAreTexturesResident(n, c_textures, c_residences))
    if not is_all_resident and residences is not None:
        residences.clear()
        residences.extend(_Support.c_array_to_list(bool, c_residences))

    return is_all_resident

def glPrioritizeTextures(textures, priorities):
    """
    textures        : List[int] | Iterable[SupportsInt]
    priorities      : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(textures, list) or not all(isinstance(item, int) for item in textures):
        try:
            textures = [int(item) for item in textures]
        except:
            raise ValueError("Value of 'textures' can not be converted to list of ints.")

    if not isinstance(priorities, list) or not all(isinstance(item, float) for item in priorities):
        try:
            priorities = [float(item) for item in priorities]
        except:
            raise ValueError("Value of 'priorities' can not be converted to list of floats.")
    
    n = len(textures)

    c_textures      = _Support.list_to_c_array_no_conv(textures, n, _C_GL_1_1.GLuint)
    c_priorities    = _Support.list_to_c_array_no_conv(priorities, n, _C_GL_1_1.GLclampf)

    _C_GL_1_1.glPrioritizeTextures(n, c_textures, c_priorities)


# Texture Environments & Texture Functions 

def glTexEnvf(target, pname, param):
    """
    target          : int | SupportsInt
    pname           : int | SupportsInt
    param           : float | SupportsFloat
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, float):
        try:
            param = float(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to float.") from exception

    _C_GL_1_1.glTexEnvf(target, pname, param)

def glTexEnvfv(target, pname, params):
    """
    target          : int | SupportsInt
    pname           : int | SupportsInt
    params          : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(params, list) or not all(isinstance(item, float) for item in params):
        try:
            params = [float(item) for item in params]
        except:
            raise ValueError("Value of 'params' can not be converted to list of floats.")
            
    n = _Support.get_tex_env_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname'.")
    c_params = _Support.list_part_to_c_array_no_conv(params, n, _C_GL_1_1.GLfloat)

    _C_GL_1_1.glTexEnvfv(target, pname, c_params)

def glTexEnvi(target, pname, param):
    """
    target          : int | SupportsInt
    pname           : int | SupportsInt
    param           : int | SupportsInt
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, int):
        try:
            param = int(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to int.") from exception

    _C_GL_1_1.glTexEnvi(target, pname, param)

def glTexEnviv(target, pname, params):
    """
    target          : int | SupportsInt
    pname           : int | SupportsInt
    params          : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(params, list) or not all(isinstance(item, int) for item in params):
        try:
            params = [int(item) for item in params]
        except:
            raise ValueError("Value of 'params' can not be converted to list of ints.")
            
    n = _Support.get_tex_env_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname'.")
    c_params = _Support.list_part_to_c_array_no_conv(params, n, _C_GL_1_1.GLint)

    _C_GL_1_1.glTexEnviv(target, pname, c_params)


# Enumerated Queries

def glGetTexEnvfv(target, pname):
    """
    target          : int | SupportsInt
    pname           : int | SupportsInt
    Returns         : List[float]
        Corresponds to 'params' parameter from OpenGL function specification.
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    n = _Support.get_tex_env_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname'.")
    c_params = _Support.make_c_array(_C_GL_1_1.GLfloat, n)
    _C_GL_1_1.glGetTexEnvfv(target, pname, c_params)
    return _Support.c_array_to_list(float, c_params)

def glGetTexEnviv(target, pname):
    """
    target          : int | SupportsInt
    pname           : int | SupportsInt
    Returns         : List[int]
        Corresponds to 'params' parameter from OpenGL function specification. 
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception
            
    n = _Support.get_tex_env_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname'.")
    c_params = _Support.make_c_array(_C_GL_1_1.GLint, n)
    _C_GL_1_1.glGetTexEnviv(target, pname, c_params)
    return _Support.c_array_to_list(int, c_params)

def glGetTexGendv(coord, pname):
    """
    coord           : int | SupportsInt
    pname           : int | SupportsInt
    Returns         : List[float]
        Corresponds to 'params' parameter from OpenGL function specification. 
    """
    if not isinstance(coord, int):
        try:
            coord = int(coord)
        except Exception as exception:
            raise ValueError("Value of 'coord' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception
            
    n = _Support.get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname'.")
    c_params = _Support.make_c_array(_C_GL_1_1.GLdouble, n)
    _C_GL_1_1.glGetTexGendv(coord, pname, c_params)
    return _Support.c_array_to_list(float, c_params)

def glGetTexGenfv(coord, pname):
    """
    coord           : int | SupportsInt
    pname           : int | SupportsInt
    Returns         : List[float]
        Corresponds to 'params' parameter from OpenGL function specification. 
    """
    if not isinstance(coord, int):
        try:
            coord = int(coord)
        except Exception as exception:
            raise ValueError("Value of 'coord' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception
            
    n = _Support.get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname'.")
    c_params = _Support.make_c_array(_C_GL_1_1.GLfloat, n)
    _C_GL_1_1.glGetTexGenfv(coord, pname, c_params)
    return _Support.c_array_to_list(float, c_params)

def glGetTexGeniv(coord, pname):
    """
    coord           : int | SupportsInt
    pname           : int | SupportsInt
    Returns         : List[int]
        Corresponds to 'params' parameter from OpenGL function specification. 
    """
    if not isinstance(coord, int):
        try:
            coord = int(coord)
        except Exception as exception:
            raise ValueError("Value of 'coord' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception
            
    n = _Support.get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname'.")
    c_params = _Support.make_c_array(_C_GL_1_1.GLint, n)
    _C_GL_1_1.glGetTexGeniv(coord, pname, c_params)
    return _Support.c_array_to_list(int, c_params)

def glGetTexParameterfv(target, pname):
    """
    target          : int | SupportsInt
    pname           : int | SupportsInt
    Returns         : List[float]
        Equivalent of parameter 'params' from OpenGL functions specification.
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception
            
    length = _Support.get_tex_parameter_length(pname)
    if length is None:
        raise ValueError("Unexpected value of parameter 'pname'.")
    
    c_params = _Support.make_c_array(_C_GL_1_1.GLfloat, length)
    _C_GL_1_1.glGetTexParameterfv(target, pname, c_params)
    return _Support.c_array_to_list(float, c_params)

def glGetTexParameteriv(target, pname):
    """
    target          : int | SupportsInt
    pname           : int | SupportsInt
    Returns         : List[int]
        Equivalent of parameter 'params' from OpenGL functions specification.
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception
            
    length = _Support.get_tex_parameter_length(pname)
    if length is None:
        raise ValueError("Unexpected value of parameter 'pname'.")
    
    c_params = _Support.make_c_array(_C_GL_1_1.GLint, length)
    _C_GL_1_1.glGetTexParameteriv(target, pname, c_params)
    return _Support.c_array_to_list(int, c_params)

def glGetTexLevelParameterfv(target, level, pname):
    """
    target          : int | SupportsInt
    level           : int | SupportsInt
    pname           : int | SupportsInt
    Returns         : List[float]
        Corresponds to 'params' parameter from OpenGL functions specification.
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(level, int):
        try:
            level = int(level)
        except Exception as exception:
            raise ValueError("Value of 'level' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception
            
    n = _Support.get_tex_level_parameter_number(pname)
    c_params = _Support.make_c_array(_C_GL_1_1.GLfloat, n)
    _C_GL_1_1.glGetTexLevelParameterfv(target, level, pname, c_params)
    return _Support.c_array_to_list(float, c_params)

def glGetTexLevelParameteriv(target, level, pname):
    """
    target          : int | SupportsInt
    level           : int | SupportsInt
    pname           : int | SupportsInt
    Returns          : List[int]
        Corresponds to 'params' parameter from OpenGL functions specification.
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(level, int):
        try:
            level = int(level)
        except Exception as exception:
            raise ValueError("Value of 'level' can not be converted to int.") from exception

    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception
            
    n = _Support.get_tex_level_parameter_number(pname)
    c_params = _Support.make_c_array(_C_GL_1_1.GLint, n)
    _C_GL_1_1.glGetTexLevelParameteriv(target, level, pname, c_params)
    return _Support.c_array_to_list(int, c_params)

# Texture Queries

def glGetTexImage(target, level, format_, type_, is_return_list = False):
    """
    target          : int | SupportsInt
    level           : int | SupportsInt
    format_         : int | SupportsInt
        Any from expected values: GL_COLOR_INDEX, GL_STENCIL_INDEX, GL_DEPTH_COMPONENT, 
        GL_RED, GL_GREEN, GL_BLUE, GL_ALPHA, GL_RGB, GL_RGBA, GL_LUMINANCE, GL_LUMINANCE_ALPHA.
    type_           : int | SupportsInt
        Any from expected values: GL_UNSIGNED_BYTE, GL_BYTE, GL_UNSIGNED_SHORT, GL_SHORT, 
        GL_UNSIGNED_INT, GL_INT, GL_FLOAT.
    is_return_list  : bool
    Returns         : bytes | List[float]
        list of floats, when 'is_return_list' is True and 'type_' is GL_FLOAT and 'format_' is either GL_RGB or GL_RGBA.
        bytes, when 'is_return_list' is False.

        Corresponds to 'pixels' parameter from OpenGL functions specification.

    Exceptions
        ValueError 
            When any parameter have unexpected value.
        ValueError 
            When 'is_return_list' is True and 'type_' is not GL_FLOAT or 'format_' is neither GL_RGB nor GL_RGBA.
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(level, int):
        try:
            level = int(level)
        except Exception as exception:
            raise ValueError("Value of 'level' can not be converted to int.") from exception

    if not isinstance(format_, int):
        try:
            format_ = int(format_)
        except Exception as exception:
            raise ValueError("Value of 'format_' can not be converted to int.") from exception

    if not isinstance(type_, int):
        try:
            type_ = int(type_)
        except Exception as exception:
            raise ValueError("Value of 'type_' can not be converted to int.") from exception
            
    if target not in _Support.get_acceptable_tex_target_ids():
        raise ValueError("Unexpected value of 'target'.")

    width   = glGetTexLevelParameteriv(target, level, GL_TEXTURE_WIDTH)[0]
    height  = glGetTexLevelParameteriv(target, level, GL_TEXTURE_HEIGHT)[0]
    # depth # for OpengGL 2.1+ for sure

    n = _Support.get_tex_format_element_number(format_)
    if n is None:
        raise ValueError("Unexpected value of 'format_'.")

    md = _Support.get_tex_type_mul_div_size(type_)
    if md is None:
        raise ValueError("Unexpected value of 'type_'.")

    m, d = md

    if is_return_list:
        if type_ != GL_FLOAT:
            raise ValueError("Unexpected value of 'type_' for 'is_return_list' being True.")
        elif format_ not in [GL_RGB, GL_RGBA]:
            raise ValueError("Unexpected value of 'format_' for 'is_return_list' being True.")
        else:
            num_of_elements = _Support.get_tex_format_element_number(format_)

            length = width * height * num_of_elements
            c_pixels = _Support.make_c_array(_C_GL_1_1.GLfloat, length)

            _C_GL_1_1.glGetTexImage(target, level, format_, type_, _ctypes.cast(c_pixels, _ctypes.c_void_p))

            return _Support.c_array_to_list(float, c_pixels)
    else:
        single_item_size = (n * m // d)             # in bytes
        size = width * height * single_item_size    # in bytes
        c_pixels = _Support.make_c_array(_C_GL_1_1.GLubyte, size)

        _C_GL_1_1.glGetTexImage(target, level, format_, type_, _ctypes.cast(c_pixels, _ctypes.c_void_p))

        return bytes(c_pixels)


def glIsTexture(texture):
    """
    texture         : int | SupportsInt
    Returns         : bool
    """
    if not isinstance(texture, int):
        try:
            texture = int(texture)
        except Exception as exception:
            raise ValueError("Value of 'texture' can not be converted to int.") from exception

    return bool(_C_GL_1_1.glIsTexture(texture))


### Color Sum, Fog, and Hints  ###

# Fog

def glFogf(pname, param):
    """
    pname           : int | SupportsInt
    param           : float | SupportsFloat
    """
    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, float):
        try:
            param = float(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to float.") from exception

    _C_GL_1_1.glFogf(pname, param)

def glFogfv(pname, params):
    """
    pname           : int | SupportsInt
    params          : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(params, list) or not all(isinstance(item, float) for item in params):
        try:
            params = [float(item) for item in params]
        except:
            raise ValueError("Value of 'params' can not be converted to list of floats.")

    length = _Support.get_fog_params_length(pname)
    if length is None:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _Support.list_part_to_c_array_no_conv(params, length, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glFogfv(pname, c_params)

def glFogi(pname, param):
    """
    pname           : int | SupportsInt
    param           : int | SupportsInt
    """
    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(param, int):
        try:
            param = int(param)
        except Exception as exception:
            raise ValueError("Value of 'param' can not be converted to int.") from exception

    _C_GL_1_1.glFogi(pname, param)

def glFogiv(pname, params):
    """
    pname           : int | SupportsInt
    params          : List[int] | Iterable[SupportsInt]
    """
    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if not isinstance(params, list) or not all(isinstance(item, int) for item in params):
        try:
            params = [int(item) for item in params]
        except:
            raise ValueError("Value of 'params' can not be converted to list of ints.")

    length = _Support.get_fog_params_length(pname)
    if length is None:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _Support.list_part_to_c_array_no_conv(params, length, _C_GL_1_1.GLint)

    _C_GL_1_1.glFogiv(pname, c_params)


# Hints

def glHint(target, mode):
    """
    target          : int | SupportsInt
    mode            : int | SupportsInt
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(mode, int):
        try:
            mode = int(mode)
        except Exception as exception:
            raise ValueError("Value of 'mode' can not be converted to int.") from exception

    _C_GL_1_1.glHint(target, mode)


### Drawing, Reading, and Copying Pixels ###

# Reading Pixels

def glReadPixels(x, y, width, height, format_, type_):
    """
    x               : int | SupportsInt
    y               : int | SupportsInt
    width           : int | SupportsInt
    height          : int | SupportsInt
    format_         : int | SupportsInt
        Equivalent of 'format' parameter.
    type_           : int | SupportsInt
        Equivalent of 'type' parameter.

    Returns         : bytes | None
        Equivalent of 'pixels' parameter.
        If type of returned object is bytes, then returned object contains pixel data.
        If type of returned object is None, then computed size of pixels is below one byte (parameter 'width' or 'height' might be zero).
    """
    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    if not isinstance(width, int):
        try:
            width = int(width)
        except Exception as exception:
            raise ValueError("Value of 'width' can not be converted to int.") from exception

    if not isinstance(height, int):
        try:
            height = int(height)
        except Exception as exception:
            raise ValueError("Value of 'height' can not be converted to int.") from exception

    if not isinstance(format_, int):
        try:
            format_ = int(format_)
        except Exception as exception:
            raise ValueError("Value of 'format_' can not be converted to int.") from exception

    if not isinstance(type_, int):
        try:
            type_ = int(type_)
        except Exception as exception:
            raise ValueError("Value of 'type_' can not be converted to int.") from exception

    format_count = _Support.get_read_pixels_format_count(format_)
    if format_count is None:
        raise ValueError("Unexpected value of 'format_' parameter.")

    type_size = _Support.get_read_pixels_type_size(type_)
    if type_size is None:
        raise ValueError("Unexpected value of 'type_' parameter.")

    pixel_size  = int(format_count * type_size)
    size        = width * height * pixel_size

    if size > 0:
        c_pixels = _Support.make_c_array(_C_GL_1_1.GLubyte, size)
        _C_GL_1_1.glReadPixels(x, y, width, height, format_, type_, c_pixels)
        return bytes(c_pixels)
    else:
        _C_GL_1_1.glReadPixels(x, y, width, height, format_, type_, None)
        return None

def glReadBuffer(mode):
    """
    mode            : int | SupportsInt
    """
    if not isinstance(mode, int):
        try:
            mode = int(mode)
        except Exception as exception:
            raise ValueError("Value of 'mode' can not be converted to int.") from exception

    _C_GL_1_1.glReadBuffer(mode)


# Copying Pixels

def glCopyPixels(x, y, width, height, type_):
    """
    x               : int | SupportsInt
    y               : int | SupportsInt
    width           : int | SupportsInt
    height          : int | SupportsInt
    type_           : int | SupportsInt
    """
    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    if not isinstance(width, int):
        try:
            width = int(width)
        except Exception as exception:
            raise ValueError("Value of 'width' can not be converted to int.") from exception

    if not isinstance(height, int):
        try:
            height = int(height)
        except Exception as exception:
            raise ValueError("Value of 'height' can not be converted to int.") from exception

    if not isinstance(type_, int):
        try:
            type_ = int(type_)
        except Exception as exception:
            raise ValueError("Value of 'type_' can not be converted to int.") from exception

    _C_GL_1_1.glCopyPixels(x, y, width, height, type_)


### Per-Fragment Operations ###

# Scissor Test

def glScissor(x, y, width, height):
    """
    x               : int | SupportsInt
    y               : int | SupportsInt
    width           : int | SupportsInt
    height          : int | SupportsInt
    """
    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception as exception:
            raise ValueError("Value of 'x' can not be converted to int.") from exception

    if not isinstance(y, int):
        try:
            y = int(y)
        except Exception as exception:
            raise ValueError("Value of 'y' can not be converted to int.") from exception

    if not isinstance(width, int):
        try:
            width = int(width)
        except Exception as exception:
            raise ValueError("Value of 'width' can not be converted to int.") from exception

    if not isinstance(height, int):
        try:
            height = int(height)
        except Exception as exception:
            raise ValueError("Value of 'height' can not be converted to int.") from exception

    _C_GL_1_1.glScissor(x, y, width, height)


# Alpha Test

def glAlphaFunc(func, ref):
    """
    func            : int | SupportsInt
    ref             : float | SupportsFloat
    """
    if not isinstance(func, int):
        try:
            func = int(func)
        except Exception as exception:
            raise ValueError("Value of 'func' can not be converted to int.") from exception

    if not isinstance(ref, float):
        try:
            ref = float(ref)
        except Exception as exception:
            raise ValueError("Value of 'ref' can not be converted to float.") from exception

    _C_GL_1_1.glAlphaFunc(func, ref)


# Stencil Test

def glStencilFunc(func, ref, mask):
    """
    func            : int | SupportsInt
    ref             : int | SupportsInt
    mask            : int | SupportsInt
    """
    if not isinstance(func, int):
        try:
            func = int(func)
        except Exception as exception:
            raise ValueError("Value of 'func' can not be converted to int.") from exception

    if not isinstance(ref, int):
        try:
            ref = int(ref)
        except Exception as exception:
            raise ValueError("Value of 'ref' can not be converted to int.") from exception

    if not isinstance(mask, int):
        try:
            mask = int(mask)
        except Exception as exception:
            raise ValueError("Value of 'mask' can not be converted to int.") from exception

    _C_GL_1_1.glStencilFunc(func, ref, mask)

def glStencilOp(fail, zfail, zpass):
    """
    fail            : int | SupportsInt
    zfail           : int | SupportsInt
    zpass           : int | SupportsInt
    """
    if not isinstance(fail, int):
        try:
            fail = int(fail)
        except Exception as exception:
            raise ValueError("Value of 'fail' can not be converted to int.") from exception

    if not isinstance(zfail, int):
        try:
            zfail = int(zfail)
        except Exception as exception:
            raise ValueError("Value of 'zfail' can not be converted to int.") from exception

    if not isinstance(zpass, int):
        try:
            zpass = int(zpass)
        except Exception as exception:
            raise ValueError("Value of 'zpass' can not be converted to int.") from exception

    _C_GL_1_1.glStencilOp(fail, zfail, zpass)


# Depth Buffer Test

def glDepthFunc(func):
    """
    func            : int | SupportsInt
    """
    if not isinstance(func, int):
        try:
            func = int(func)
        except Exception as exception:
            raise ValueError("Value of 'func' can not be converted to int.") from exception

    _C_GL_1_1.glDepthFunc(func)


# Blending

def glBlendFunc(sfactor, dfactor):
    """
    sfactor         : int | SupportsInt
    dfactor         : int | SupportsInt
    """
    if not isinstance(sfactor, int):
        try:
            sfactor = int(sfactor)
        except Exception as exception:
            raise ValueError("Value of 'sfactor' can not be converted to int.") from exception

    if not isinstance(dfactor, int):
        try:
            dfactor = int(dfactor)
        except Exception as exception:
            raise ValueError("Value of 'dfactor' can not be converted to int.") from exception

    _C_GL_1_1.glBlendFunc(sfactor, dfactor)


# Logical Operation 

def glLogicOp(opcode):
    """
    opcode          : int | SupportsInt
    """
    if not isinstance(opcode, int):
        try:
            opcode = int(opcode)
        except Exception as exception:
            raise ValueError("Value of 'opcode' can not be converted to int.") from exception

    _C_GL_1_1.glLogicOp(opcode)


### Whole Framebuffer Operations ###

# Selecting a Buffer for Writing

def glDrawBuffer(mode):
    """
    mode            : int | SupportsInt
    """
    if not isinstance(mode, int):
        try:
            mode = int(mode)
        except Exception as exception:
            raise ValueError("Value of 'mode' can not be converted to int.") from exception

    _C_GL_1_1.glDrawBuffer(mode)



# Fine Control of Buffer Updates

def glIndexMask(mask):
    """
    mask            : int | SupportsInt
    """
    if not isinstance(mask, int):
        try:
            mask = int(mask)
        except Exception as exception:
            raise ValueError("Value of 'mask' can not be converted to int.") from exception

    _C_GL_1_1.glIndexMask(mask)

def glColorMask(red, green, blue, alpha):
    """
    red             : bool
    green           : bool
    blue            : bool
    alpha           : bool
    """
    if not isinstance(red, bool):
        try:
            red = bool(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to bool.") from exception

    if not isinstance(green, bool):
        try:
            green = bool(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to bool.") from exception

    if not isinstance(blue, bool):
        try:
            blue = bool(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to bool.") from exception

    if not isinstance(alpha, bool):
        try:
            alpha = bool(alpha)
        except Exception as exception:
            raise ValueError("Value of 'alpha' can not be converted to bool.") from exception

    _C_GL_1_1.glColorMask(red, green, blue, alpha)
    
def glDepthMask(flag):
    """
    flag            : bool
    """
    if not isinstance(flag, bool):
        try:
            flag = bool(flag)
        except Exception as exception:
            raise ValueError("Value of 'flag' can not be converted to bool.") from exception

    _C_GL_1_1.glDepthMask(flag)

def glStencilMask(mask):
    """
    mask            : int | SupportsInt
    """
    if not isinstance(mask, int):
        try:
            mask = int(mask)
        except Exception as exception:
            raise ValueError("Value of 'mask' can not be converted to int.") from exception

    _C_GL_1_1.glStencilMask(mask)

# Clearing the Buffers

def glClear(mask):
    """
    mask            : int | SupportsInt
    """
    if not isinstance(mask, int):
        try:
            mask = int(mask)
        except Exception as exception:
            raise ValueError("Value of 'mask' can not be converted to int.") from exception

    _C_GL_1_1.glClear(mask)

def glClearColor(red, green, blue, alpha):
    """
    red             : float | SupportsFloat
    green           : float | SupportsFloat
    blue            : float | SupportsFloat
    alpha           : float | SupportsFloat
    """
    if not isinstance(red, float):
        try:
            red = float(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to float.") from exception

    if not isinstance(green, float):
        try:
            green = float(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to float.") from exception

    if not isinstance(blue, float):
        try:
            blue = float(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to float.") from exception

    if not isinstance(alpha, float):
        try:
            alpha = float(alpha)
        except Exception as exception:
            raise ValueError("Value of 'alpha' can not be converted to float.") from exception

    _C_GL_1_1.glClearColor(red, green, blue, alpha)

def glClearIndex(c):
    """
    c               : float | SupportsFloat
    """
    if not isinstance(c, float):
        try:
            c = float(c)
        except Exception as exception:
            raise ValueError("Value of 'c' can not be converted to float.") from exception

    _C_GL_1_1.glClearIndex(c)

def glClearDepth(depth):
    """
    depth           : float | SupportsFloat
    """
    if not isinstance(depth, float):
        try:
            depth = float(depth)
        except Exception as exception:
            raise ValueError("Value of 'depth' can not be converted to float.") from exception

    _C_GL_1_1.glClearDepth(depth)

def glClearStencil(s):
    """
    s               : int | SupportsInt
    """
    if not isinstance(s, int):
        try:
            s = int(s)
        except Exception as exception:
            raise ValueError("Value of 's' can not be converted to int.") from exception

    _C_GL_1_1.glClearStencil(s)

def glClearAccum(red, green, blue, alpha):
    """
    red             : float | SupportsFloat
    green           : float | SupportsFloat
    blue            : float | SupportsFloat
    alpha           : float | SupportsFloat
    """
    if not isinstance(red, float):
        try:
            red = float(red)
        except Exception as exception:
            raise ValueError("Value of 'red' can not be converted to float.") from exception

    if not isinstance(green, float):
        try:
            green = float(green)
        except Exception as exception:
            raise ValueError("Value of 'green' can not be converted to float.") from exception

    if not isinstance(blue, float):
        try:
            blue = float(blue)
        except Exception as exception:
            raise ValueError("Value of 'blue' can not be converted to float.") from exception

    if not isinstance(alpha, float):
        try:
            alpha = float(alpha)
        except Exception as exception:
            raise ValueError("Value of 'alpha' can not be converted to float.") from exception

    _C_GL_1_1.glClearAccum(red, green, blue, alpha)


# Accumulation Buffer

def glAccum(op, value):
    """
    op              : int | SupportsInt
    value           : float | SupportsFloat
    """
    if not isinstance(op, int):
        try:
            op = int(op)
        except Exception as exception:
            raise ValueError("Value of 'op' can not be converted to int.") from exception

    if not isinstance(value, float):
        try:
            value = float(value)
        except Exception as exception:
            raise ValueError("Value of 'value' can not be converted to float.") from exception

    _C_GL_1_1.glAccum(op, value)


### Special Functions ###

# Evaluators

def glMap1d(target, u1, u2, points):
    """
    target          : int | SupportsInt
    u1              : float | SupportsFloat
    u2              : float | SupportsFloat
    points          : List[float] | Iterable[SupportsFloat]
        List (or iterable), which contains control points.
        Each control point is represented by one or more items in list (or iterable).
        Number of items in list (or iterable) per control point for target:
                4 - GL_MAP1_COLOR_4, 
                1 - GL_MAP1_INDEX, 
                3 - GL_MAP1_NORMAL, 
                1 - GL_MAP1_TEXTURE_COORD_1, 
                2 - GL_MAP1_TEXTURE_COORD_2, 
                3 - GL_MAP1_TEXTURE_COORD_3, 
                4 - GL_MAP1_TEXTURE_COORD_4, 
                3 - GL_MAP1_VERTEX_3, 
                4 - GL_MAP1_VERTEX_4.

    Note: Value of 'order' parameter (from OpenGL function specification) is deduced from length of 'points' parameter.
    Note: Value of 'stride' parameter (from OpenGL function specification) is deduced from 'target' parameter.
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(u1, float):
        try:
            u1 = float(u1)
        except Exception as exception:
            raise ValueError("Value of 'u1' can not be converted to float.") from exception

    if not isinstance(u2, float):
        try:
            u2 = float(u2)
        except Exception as exception:
            raise ValueError("Value of 'u2' can not be converted to float.") from exception

    if not isinstance(points, list) or not all(isinstance(item, float) for item in points):
        try:
            points = [float(item) for item in points]
        except:
            raise ValueError("Value of 'points' can not be converted to list of floats.")

    stride = _Support.get_map_1d_stride(target)
    if stride is None:
        raise ValueError("Unexpected value of 'target'.")

    if len(points) % stride != 0:
        raise ValueError("Number of items in 'points' must be multiply of %s (its stride)." % stride)

    order = len(points) // stride
    c_points = _Support.list_to_c_array_no_conv(points, len(points), _C_GL_1_1.GLdouble)

    _C_GL_1_1.glMap1d(target, u1, u2, stride, order, c_points)

def glMap1f(target, u1, u2, points):
    """
    target          : int | SupportsInt
    u1              : float | SupportsFloat
    u2              : float | SupportsFloat
    points          : List[float] | Iterable[SupportsFloat]
        List (or iterable), which contains control points.
        Each control point is represented by one or more items in list (or iterable).
        Number of items in list (or iterable) per control point for target:
                4 - GL_MAP1_COLOR_4, 
                1 - GL_MAP1_INDEX, 
                3 - GL_MAP1_NORMAL, 
                1 - GL_MAP1_TEXTURE_COORD_1, 
                2 - GL_MAP1_TEXTURE_COORD_2, 
                3 - GL_MAP1_TEXTURE_COORD_3, 
                4 - GL_MAP1_TEXTURE_COORD_4, 
                3 - GL_MAP1_VERTEX_3, 
                4 - GL_MAP1_VERTEX_4.

    Note: Value of 'order' parameter (from OpenGL function specification) is deduced from length of 'points' parameter.
    Note: Value of 'stride' parameter (from OpenGL function specification) is deduced from 'target' parameter.
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(u1, float):
        try:
            u1 = float(u1)
        except Exception as exception:
            raise ValueError("Value of 'u1' can not be converted to float.") from exception

    if not isinstance(u2, float):
        try:
            u2 = float(u2)
        except Exception as exception:
            raise ValueError("Value of 'u2' can not be converted to float.") from exception

    if not isinstance(points, list) or not all(isinstance(item, float) for item in points):
        try:
            points = [float(item) for item in points]
        except:
            raise ValueError("Value of 'points' can not be converted to list of floats.")

    stride = _Support.get_map_1d_stride(target)
    if stride is None:
        raise ValueError("Unexpected value of 'target'.")

    if len(points) % stride != 0:
        raise ValueError("Number of items in 'points' must be multiply of value from 'stride'.")

    order = len(points) // stride
    c_points = _Support.list_to_c_array_no_conv(points, len(points), _C_GL_1_1.GLfloat)

    _C_GL_1_1.glMap1f(target, u1, u2, stride, order, c_points)

def glMap2d(target, u1, u2, v1, v2, vorder, points):
    """
    target          : int | SupportsInt
    u1              : float | SupportsFloat
    u2              : float | SupportsFloat
    v1              : float | SupportsFloat
    v2              : float | SupportsFloat
    vorder          : int | SupportsInt
    points          : List[float] | Iterable[SupportsFloat]
        List (or iterable), which contains control points.
        Each control point is represented by one or more items in list (or iterable).
        Number of items in list (or iterable) per control point for target:
                4 - GL_MAP1_COLOR_4, 
                1 - GL_MAP1_INDEX, 
                3 - GL_MAP1_NORMAL, 
                1 - GL_MAP1_TEXTURE_COORD_1, 
                2 - GL_MAP1_TEXTURE_COORD_2, 
                3 - GL_MAP1_TEXTURE_COORD_3, 
                4 - GL_MAP1_TEXTURE_COORD_4, 
                3 - GL_MAP1_VERTEX_3, 
                4 - GL_MAP1_VERTEX_4.

    Note: Value of 'uorder' parameter (from OpenGL function specification) is deduced from length of 'points' parameter.
    Note: Values of 'ustride' parameter and 'vstride' parameter (from OpenGL function specification) is deduced from 'target' parameter.
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(u1, float):
        try:
            u1 = float(u1)
        except Exception as exception:
            raise ValueError("Value of 'u1' can not be converted to float.") from exception

    if not isinstance(u2, float):
        try:
            u2 = float(u2)
        except Exception as exception:
            raise ValueError("Value of 'u2' can not be converted to float.") from exception

    if not isinstance(v1, float):
        try:
            v1 = float(v1)
        except Exception as exception:
            raise ValueError("Value of 'v1' can not be converted to float.") from exception

    if not isinstance(v2, float):
        try:
            v2 = float(v2)
        except Exception as exception:
            raise ValueError("Value of 'v2' can not be converted to float.") from exception

    if not isinstance(vorder, int):
        try:
            vorder = int(vorder)
        except Exception as exception:
            raise ValueError("Value of 'vorder' can not be converted to int.") from exception

    if not isinstance(points, list) or not all(isinstance(item, float) for item in points):
        try:
            points = [float(item) for item in points]
        except:
            raise ValueError("Value of 'points' can not be converted to list of floats.")

    ustride = _Support.get_map_2d_stride(target)
    if ustride is None:
        raise ValueError("Unexpected value of 'target' parameter.")

    if len(points) % ustride != 0:
        raise ValueError("Number of items in 'points' parameter must be multiply of %d." % ustride)

    uorder = len(points) // (ustride * vorder)
    vstride = ustride * uorder

    c_points = _Support.list_to_c_array_no_conv(points, len(points), _C_GL_1_1.GLdouble)

    _C_GL_1_1.glMap2d(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, c_points)

def glMap2f(target, u1, u2, v1, v2, vorder, points):
    """
    target          : int | SupportsInt
    u1              : float | SupportsFloat
    u2              : float | SupportsFloat
    v1              : float | SupportsFloat
    v2              : float | SupportsFloat
    vorder          : int | SupportsInt
    points          : List[float] | Iterable[SupportsFloat]
        List (or iterable), which contains control points.
        Each control point is represented by one or more items in list (or iterable).
        Number of items in list (or iterable) per control point for target:
                4 - GL_MAP1_COLOR_4, 
                1 - GL_MAP1_INDEX, 
                3 - GL_MAP1_NORMAL, 
                1 - GL_MAP1_TEXTURE_COORD_1, 
                2 - GL_MAP1_TEXTURE_COORD_2, 
                3 - GL_MAP1_TEXTURE_COORD_3, 
                4 - GL_MAP1_TEXTURE_COORD_4, 
                3 - GL_MAP1_VERTEX_3, 
                4 - GL_MAP1_VERTEX_4.
                
    Note: Value of 'uorder' parameter (from OpenGL function specification) is deduced from length of 'points' parameter.
    Note: Values of 'ustride' parameter and 'vstride' parameter (from OpenGL function specification) is deduced from 'target' parameter.
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(u1, float):
        try:
            u1 = float(u1)
        except Exception as exception:
            raise ValueError("Value of 'u1' can not be converted to float.") from exception

    if not isinstance(u2, float):
        try:
            u2 = float(u2)
        except Exception as exception:
            raise ValueError("Value of 'u2' can not be converted to float.") from exception

    if not isinstance(v1, float):
        try:
            v1 = float(v1)
        except Exception as exception:
            raise ValueError("Value of 'v1' can not be converted to float.") from exception

    if not isinstance(v2, float):
        try:
            v2 = float(v2)
        except Exception as exception:
            raise ValueError("Value of 'v2' can not be converted to float.") from exception

    if not isinstance(vorder, int):
        try:
            vorder = int(vorder)
        except Exception as exception:
            raise ValueError("Value of 'vorder' can not be converted to int.") from exception

    if not isinstance(points, list) or not all(isinstance(item, float) for item in points):
        try:
            points = [float(item) for item in points]
        except:
            raise ValueError("Value of 'points' can not be converted to list of floats.")

    ustride = _Support.get_map_2d_stride(target)
    if ustride is None:
        raise ValueError("Unexpected value of 'target'.")

    if len(points) % ustride != 0:
        raise ValueError("Number of items in 'points' must be multiply of %d." % ustride)

    uorder = len(points) // (ustride * vorder)
    vstride = ustride * uorder

    c_points = _Support.list_to_c_array(float, points, len(points), _C_GL_1_1.GLfloat)

    _C_GL_1_1.glMap2f(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, c_points)


def glEvalCoord1d(u):
    """
    u               : float | SupportsFloat
    """
    if not isinstance(u, float):
        try:
            u = float(u)
        except Exception as exception:
            raise ValueError("Value of 'u' can not be converted to float.") from exception

    _C_GL_1_1.glEvalCoord1d(u)

def glEvalCoord1dv(u):
    """
    u               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(u, list) or not all(isinstance(item, float) for item in u):
        try:
            u = [float(item) for item in u]
        except:
            raise ValueError("Value of 'u' can not be converted to list of floats.")
            
    c_u = _Support.list_part_to_c_array_no_conv(u, 1, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glEvalCoord1dv(c_u)

def glEvalCoord1f(u):
    """
    u               : float | SupportsFloat
    """
    if not isinstance(u, float):
        try:
            u = float(u)
        except Exception as exception:
            raise ValueError("Value of 'u' can not be converted to float.") from exception

    _C_GL_1_1.glEvalCoord1f(u)

def glEvalCoord1fv(u):
    """
    u               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(u, list) or not all(isinstance(item, float) for item in u):
        try:
            u = [float(item) for item in u]
        except:
            raise ValueError("Value of 'u' can not be converted to list of floats.")

    c_u = _Support.list_part_to_c_array_no_conv(u, 1, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glEvalCoord1fv(c_u)

def glEvalCoord2d(u, v):
    """
    u               : float | SupportsFloat
    v               : float | SupportsFloat
    """
    if not isinstance(u, float):
        try:
            u = float(u)
        except Exception as exception:
            raise ValueError("Value of 'u' can not be converted to float.") from exception

    if not isinstance(v, float):
        try:
            v = float(v)
        except Exception as exception:
            raise ValueError("Value of 'v' can not be converted to float.") from exception

    _C_GL_1_1.glEvalCoord2d(u, v)

def glEvalCoord2dv(u):
    """
    u               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(u, list) or not all(isinstance(item, float) for item in u):
        try:
            u = [float(item) for item in u]
        except:
            raise ValueError("Value of 'u' can not be converted to list of floats.")
            
    c_u = _Support.list_part_to_c_array_no_conv(u, 2, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glEvalCoord2dv(c_u)

def glEvalCoord2f(u, v):
    """
    u               : float | SupportsFloat
    v               : float | SupportsFloat
    """
    if not isinstance(u, float):
        try:
            u = float(u)
        except Exception as exception:
            raise ValueError("Value of 'u' can not be converted to float.") from exception

    if not isinstance(v, float):
        try:
            v = float(v)
        except Exception as exception:
            raise ValueError("Value of 'v' can not be converted to float.") from exception

    _C_GL_1_1.glEvalCoord2f(u, v)

def glEvalCoord2fv(u):
    """
    u               : List[float] | Iterable[SupportsFloat]
    """
    if not isinstance(u, list) or not all(isinstance(item, float) for item in u):
        try:
            u = [float(item) for item in u]
        except:
            raise ValueError("Value of 'u' can not be converted to list of floats.")
            
    c_u = _Support.list_part_to_c_array_no_conv(u, 2, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glEvalCoord2fv(c_u)

def glMapGrid1d(un, u1, u2):
    """
    un              : int | SupportsInt
    u1              : float | SupportsFloat
    u2              : float | SupportsFloat
    """
    if not isinstance(un, int):
        try:
            un = int(un)
        except Exception as exception:
            raise ValueError("Value of 'un' can not be converted to int.") from exception

    if not isinstance(u1, float):
        try:
            u1 = float(u1)
        except Exception as exception:
            raise ValueError("Value of 'u1' can not be converted to float.") from exception

    if not isinstance(u2, float):
        try:
            u2 = float(u2)
        except Exception as exception:
            raise ValueError("Value of 'u2' can not be converted to float.") from exception

    _C_GL_1_1.glMapGrid1d(un, u1, u2)

def glMapGrid1f(un, u1, u2):
    """
    un              : int | SupportsInt
    u1              : float | SupportsFloat
    u2              : float | SupportsFloat
    """
    if not isinstance(un, int):
        try:
            un = int(un)
        except Exception as exception:
            raise ValueError("Value of 'un' can not be converted to int.") from exception

    if not isinstance(u1, float):
        try:
            u1 = float(u1)
        except Exception as exception:
            raise ValueError("Value of 'u1' can not be converted to float.") from exception

    if not isinstance(u2, float):
        try:
            u2 = float(u2)
        except Exception as exception:
            raise ValueError("Value of 'u2' can not be converted to float.") from exception

    _C_GL_1_1.glMapGrid1f(un, u1, u2)

def glMapGrid2d(un, u1, u2, vn, v1, v2):
    """
    un              : int | SupportsInt
    u1              : float | SupportsFloat
    u2              : float | SupportsFloat
    vn              : int | SupportsInt
    v1              : float | SupportsFloat
    v2              : float | SupportsFloat
    """
    if not isinstance(un, int):
        try:
            un = int(un)
        except Exception as exception:
            raise ValueError("Value of 'un' can not be converted to int.") from exception

    if not isinstance(u1, float):
        try:
            u1 = float(u1)
        except Exception as exception:
            raise ValueError("Value of 'u1' can not be converted to float.") from exception

    if not isinstance(u2, float):
        try:
            u2 = float(u2)
        except Exception as exception:
            raise ValueError("Value of 'u2' can not be converted to float.") from exception

    if not isinstance(vn, int):
        try:
            vn = int(vn)
        except Exception as exception:
            raise ValueError("Value of 'vn' can not be converted to int.") from exception

    if not isinstance(v1, float):
        try:
            v1 = float(v1)
        except Exception as exception:
            raise ValueError("Value of 'v1' can not be converted to float.") from exception

    if not isinstance(v2, float):
        try:
            v2 = float(v2)
        except Exception as exception:
            raise ValueError("Value of 'v2' can not be converted to float.") from exception

    _C_GL_1_1.glMapGrid2d(un, u1, u2, vn, v1, v2)

def glMapGrid2f(un, u1, u2, vn, v1, v2):
    """
    un              : int | SupportsInt
    u1              : float | SupportsFloat
    u2              : float | SupportsFloat
    vn              : int | SupportsInt
    v1              : float | SupportsFloat
    v2              : float | SupportsFloat
    """
    if not isinstance(un, int):
        try:
            un = int(un)
        except Exception as exception:
            raise ValueError("Value of 'un' can not be converted to int.") from exception

    if not isinstance(u1, float):
        try:
            u1 = float(u1)
        except Exception as exception:
            raise ValueError("Value of 'u1' can not be converted to float.") from exception

    if not isinstance(u2, float):
        try:
            u2 = float(u2)
        except Exception as exception:
            raise ValueError("Value of 'u2' can not be converted to float.") from exception

    if not isinstance(vn, int):
        try:
            vn = int(vn)
        except Exception as exception:
            raise ValueError("Value of 'vn' can not be converted to int.") from exception

    if not isinstance(v1, float):
        try:
            v1 = float(v1)
        except Exception as exception:
            raise ValueError("Value of 'v1' can not be converted to float.") from exception

    if not isinstance(v2, float):
        try:
            v2 = float(v2)
        except Exception as exception:
            raise ValueError("Value of 'v2' can not be converted to float.") from exception

    _C_GL_1_1.glMapGrid2f(un, u1, u2, vn, v1, v2)


def glEvalMesh1(mode, i1, i2):
    """
    mode            : int | SupportsInt
    i1              : int | SupportsInt
    i2              : int | SupportsInt
    """
    if not isinstance(mode, int):
        try:
            mode = int(mode)
        except Exception as exception:
            raise ValueError("Value of 'mode' can not be converted to int.") from exception

    if not isinstance(i1, int):
        try:
            i1 = int(i1)
        except Exception as exception:
            raise ValueError("Value of 'i1' can not be converted to int.") from exception

    if not isinstance(i2, int):
        try:
            i2 = int(i2)
        except Exception as exception:
            raise ValueError("Value of 'i2' can not be converted to int.") from exception

    _C_GL_1_1.glEvalMesh1(mode, i1, i2)

def glEvalMesh2(mode, i1, i2, j1, j2):
    """
    mode            : int | SupportsInt
    i1              : int | SupportsInt
    i2              : int | SupportsInt
    j1              : int | SupportsInt
    j2              : int | SupportsInt
    """
    if not isinstance(mode, int):
        try:
            mode = int(mode)
        except Exception as exception:
            raise ValueError("Value of 'mode' can not be converted to int.") from exception

    if not isinstance(i1, int):
        try:
            i1 = int(i1)
        except Exception as exception:
            raise ValueError("Value of 'i1' can not be converted to int.") from exception

    if not isinstance(i2, int):
        try:
            i2 = int(i2)
        except Exception as exception:
            raise ValueError("Value of 'i2' can not be converted to int.") from exception

    if not isinstance(j1, int):
        try:
            j1 = int(j1)
        except Exception as exception:
            raise ValueError("Value of 'j1' can not be converted to int.") from exception

    if not isinstance(j2, int):
        try:
            j2 = int(j2)
        except Exception as exception:
            raise ValueError("Value of 'j2' can not be converted to int.") from exception

    _C_GL_1_1.glEvalMesh2(mode, i1, i2, j1, j2)


def glEvalPoint1(i):
    """
    i               : int | SupportsInt
    """
    if not isinstance(i, int):
        try:
            i = int(i)
        except Exception as exception:
            raise ValueError("Value of 'i' can not be converted to int.") from exception

    _C_GL_1_1.glEvalPoint1(i)

def glEvalPoint2(i, j):
    """
    i               : int | SupportsInt
    j               : int | SupportsInt
    """
    if not isinstance(i, int):
        try:
            i = int(i)
        except Exception as exception:
            raise ValueError("Value of 'i' can not be converted to int.") from exception

    if not isinstance(j, int):
        try:
            j = int(j)
        except Exception as exception:
            raise ValueError("Value of 'j' can not be converted to int.") from exception

    _C_GL_1_1.glEvalPoint2(i, j)


# Enumerated Query

def glGetMapdv(target, query):
    """
    target          : int | SupportsInt
    query           : int | SupportsInt
    Returns         : List[float]
        Corresponds to 'v' parameter from OpenGL function specification.
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(query, int):
        try:
            query = int(query)
        except Exception as exception:
            raise ValueError("Value of 'query' can not be converted to int.") from exception

    if query == GL_COEFF:
        stride = _Support.get_map_stride(target)
        if stride is None:
            ValueError("Unexpected value of 'target' parameter.")

        if _Support.is_map_1d_target(target):
            c_order = _C_GL_1_1.GLint()
            _C_GL_1_1.glGetMapiv(target, GL_ORDER, _ctypes.byref(c_order))
            order = c_order.value

            length = stride * order
        else:
            c_order = _Support.make_c_array(_C_GL_1_1.GLint, 2)
            _C_GL_1_1.glGetMapiv(target, GL_ORDER, c_order)
            uorder = c_order[0]
            vorder = c_order[1]
            
            length = stride * uorder * vorder

        c_v = _Support.make_c_array(_C_GL_1_1.GLdouble, length)

    elif query == GL_ORDER:
        length = 1 if _Support.is_map_1d_target(target) else 2
        c_v = _Support.make_c_array(_C_GL_1_1.GLdouble, length)

    elif query == GL_DOMAIN:
        length = 2 if _Support.is_map_1d_target(target) else 4
        c_v = _Support.make_c_array(_C_GL_1_1.GLdouble, length)

    _C_GL_1_1.glGetMapdv(target, query, c_v)
    return _Support.c_array_to_list(float, c_v)


def glGetMapfv(target, query):
    """
    target          : int | SupportsInt
    query           : int | SupportsInt
    Returns         : List[float]
        Corresponds to 'v' parameter from OpenGL function specification.
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(query, int):
        try:
            query = int(query)
        except Exception as exception:
            raise ValueError("Value of 'query' can not be converted to int.") from exception

    if query == GL_COEFF:
        stride = _Support.get_map_stride(target)
        if stride is None:
            ValueError("Unexpected value of 'target' parameter.")

        if _Support.is_map_1d_target(target):
            c_order = _C_GL_1_1.GLint()
            _C_GL_1_1.glGetMapiv(target, GL_ORDER, _ctypes.byref(c_order))
            order = c_order.value
            length = stride * order
        else:
            c_order = _Support.make_c_array(_C_GL_1_1.GLint, 2)
            _C_GL_1_1.glGetMapiv(target, GL_ORDER, c_order)
            uorder = c_order[0]
            vorder = c_order[1]

            length = stride * uorder * vorder

        c_v = _Support.make_c_array(_C_GL_1_1.GLfloat, length)

    elif query == GL_ORDER:
        length = 1 if _Support.is_map_1d_target(target) else 2
        c_v = _Support.make_c_array(_C_GL_1_1.GLfloat, length)

    elif query == GL_DOMAIN:
        length = 2 if _Support.is_map_1d_target(target) else 4
        c_v = _Support.make_c_array(_C_GL_1_1.GLfloat, length)

    _C_GL_1_1.glGetMapfv(target, query, c_v)
    return _Support.c_array_to_list(float, c_v)

def glGetMapiv(target, query):
    """
    target          : int | SupportsInt
    query           : int | SupportsInt
    Returns         : List[int]
        Corresponds to 'v' parameter from OpenGL function specification.
    """
    if not isinstance(target, int):
        try:
            target = int(target)
        except Exception as exception:
            raise ValueError("Value of 'target' can not be converted to int.") from exception

    if not isinstance(query, int):
        try:
            query = int(query)
        except Exception as exception:
            raise ValueError("Value of 'query' can not be converted to int.") from exception

    if query == GL_COEFF:
        stride = _Support.get_map_stride(target)
        if stride is None:
            ValueError("Unexpected value of 'target' parameter.")

        if _Support.is_map_1d_target(target):
            c_order = _C_GL_1_1.GLint()
            _C_GL_1_1.glGetMapiv(target, GL_ORDER, _ctypes.byref(c_order))
            order = c_order.value

            length = stride * order
        else:
            c_order = _Support.make_c_array(_C_GL_1_1.GLint, 2)
            _C_GL_1_1.glGetMapiv(target, GL_ORDER, c_order)
            uorder = c_order[0]
            vorder = c_order[1]

            length = stride * uorder * vorder

        c_v = _Support.make_c_array(_C_GL_1_1.GLint, length)

    elif query == GL_ORDER:
        length = 1 if _Support.is_map_1d_target(target) else 2
        c_v = _Support.make_c_array(_C_GL_1_1.GLint, length)

    elif query == GL_DOMAIN:
        length = 2 if _Support.is_map_1d_target(target) else 4
        c_v = _Support.make_c_array(_C_GL_1_1.GLint, length)

    _C_GL_1_1.glGetMapiv(target, query, c_v)
    return _Support.c_array_to_list(int, c_v)

# Selection

def glInitNames():
    _C_GL_1_1.glInitNames()

def glPopName():
    _C_GL_1_1.glPopName()

def glPushName(name):
    """
    name            : int | SupportsInt
    """
    if not isinstance(name, int):
        try:
            name = int(name)
        except Exception as exception:
            raise ValueError("Value of 'name' can not be converted to int.") from exception

    _C_GL_1_1.glPushName(name)

def glLoadName(name):
    """
    name            : int | SupportsInt
    """
    if not isinstance(name, int):
        try:
            name = int(name)
        except Exception as exception:
            raise ValueError("Value of 'name' can not be converted to int.") from exception

    _C_GL_1_1.glLoadName(name)

def glRenderMode(mode):
    """
    mode            : int | SupportsInt
    Returns         : int
    """
    if not isinstance(mode, int):
        try:
            mode = int(mode)
        except Exception as exception:
            raise ValueError("Value of 'mode' can not be converted to int.") from exception

    return int(_C_GL_1_1.glRenderMode(mode))

#def glSelectBuffer(size, buffer):
#    """
#    size            : int | SupportsInt
#    buffer          : List[int] | Iterable[SupportsInt]
#    """
#    if not isinstance(size, int):
#        try:
#            size = int(size)
#        except Exception as exception:
#            raise ValueError("Value of 'size' can not be converted to int.") from exception
#
#    if not isinstance(buffer, list) or not all(isinstance(item, int) for item in buffer):
#        try:
#            buffer = [int(item) for item in buffer]
#        except:
#            raise ValueError("Value of 'buffer' can not be converted to list of ints.")
#
#    _C_GL_1_1.glSelectBuffer(size, buffer)


# Feedback

#def glFeedbackBuffer(size, type_, buffer):
#    """
#    size            : int | SupportsInt
#    type_           : int | SupportsInt
#    buffer          : List[float] | Iterable[SupportsFloat]
#    """
#    if not isinstance(size, int):
#        try:
#            size = int(size)
#        except Exception as exception:
#            raise ValueError("Value of 'size' can not be converted to int.") from exception
#
#    if not isinstance(type_, int):
#        try:
#            type_ = int(type_)
#        except Exception as exception:
#            raise ValueError("Value of 'type_' can not be converted to int.") from exception
#
#    if not isinstance(buffer, list) or not all(isinstance(item, float) for item in buffer):
#        try:
#            buffer = [float(item) for item in buffer]
#        except:
#            raise ValueError("Value of 'buffer' can not be converted to list of floats.")
#
#    _C_GL_1_1.glFeedbackBuffer(size, type_, buffer)

def glPassThrough(token):
    """
    token           : float | SupportsFloat
    """
    if not isinstance(token, float):
        try:
            token = float(token)
        except Exception as exception:
            raise ValueError("Value of 'token' can not be converted to float.") from exception

    _C_GL_1_1.glPassThrough(token)


# Display Lists

def glNewList(list_, mode):
    """
    list_           : int | SupportsInt
    mode            : int | SupportsInt
    """
    if not isinstance(list_, int):
        try:
            list_ = int(list_)
        except Exception as exception:
            raise ValueError("Value of 'list_' can not be converted to int.") from exception

    if not isinstance(mode, int):
        try:
            mode = int(mode)
        except Exception as exception:
            raise ValueError("Value of 'mode' can not be converted to int.") from exception

    _C_GL_1_1.glNewList(list_, mode)

def glEndList():
    _C_GL_1_1.glEndList()

def glCallList(list_):
    """
    list_           : int | SupportsInt
    """
    if not isinstance(list_, int):
        try:
            list_ = int(list_)
        except Exception as exception:
            raise ValueError("Value of 'list_' can not be converted to int.") from exception

    _C_GL_1_1.glCallList(list_)

def glCallLists(type_, lists):
    """
    type_           : int | SupportsInt
    lists           : List[int | float] | Iterable[SupportsInt | SupportsFloat]
    lists           : bytes
        Acceptable when parameter 'type_' is  GL_UNSIGNED_BYTE.
    lists           : str
        Acceptable when parameter 'type_' is  GL_UNSIGNED_INT.
    """
    if not isinstance(type_, int):
        try:
            type_ = int(type_)
        except Exception as exception:
            raise ValueError("Value of 'type_' can not be converted to int.") from exception

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
        c_type      = _Support.get_call_lists_c_type(type_)
        if c_type is None:
            raise ValueError("Unexpected value of 'type_'.")
            
        py_types    = _Support.get_call_lists_py_type(type_)
        if py_types is None:
            raise ValueError("Unexpected value of 'type_'.")
        
        if not isinstance(lists, list) or not all(isinstance(item, py_types) for item in lists):
            try:
                lists = [py_types(item) for item in lists]
            except:
                py_type_str = "float" if py_type is float else "int"
                
                raise ValueError("Value of 'lists' can not be converted to list of %ss." % (py_type_str))
                
        n = len(lists)
        if type_ == GL_2_BYTES:     n //= 2
        elif type_ == GL_3_BYTES:   n //= 3
        elif type_ == GL_4_BYTES:   n //= 4

        c_lists = _Support.list_part_to_c_array_no_conv(lists, len(lists), c_type)
        _C_GL_1_1.glCallLists(n, type_, c_lists)

def glListBase(base):
    """
    base            : int | SupportsInt
    """
    if not isinstance(base, int):
        try:
            base = int(base)
        except Exception as exception:
            raise ValueError("Value of 'base' can not be converted to int.") from exception

    _C_GL_1_1.glListBase(base)

def glGenLists(range_):
    """
    range_          : int | SupportsInt
    Returns         : int
    """
    if not isinstance(range_, int):
        try:
            range_ = int(range_)
        except Exception as exception:
            raise ValueError("Value of 'range_' can not be converted to int.") from exception

    return int(_C_GL_1_1.glGenLists(range_))

def glIsList(list_):
    """
    list_           : int | SupportsInt
    Returns         : bool
    """
    if not isinstance(list_, int):
        try:
            list_ = int(list_)
        except Exception as exception:
            raise ValueError("Value of 'list_' can not be converted to int.") from exception

    return bool(_C_GL_1_1.glIsList(list_))

def glDeleteLists(list_, range_):
    """
    list_           : int | SupportsInt
    range_          : int | SupportsInt
    """
    if not isinstance(list_, int):
        try:
            list_ = int(list_)
        except Exception as exception:
            raise ValueError("Value of 'list_' can not be converted to int.") from exception

    if not isinstance(range_, int):
        try:
            range_ = int(range_)
        except Exception as exception:
            raise ValueError("Value of 'range_' can not be converted to int.") from exception

    _C_GL_1_1.glDeleteLists(list_, range_)


### Synchronization ###

# Flush and Finish 

def glFlush():
    _C_GL_1_1.glFlush()

def glFinish():
    _C_GL_1_1.glFinish()


### State and State Requests  ###

def glDisable(cap):
    """
    cap             : int | SupportsInt
    """
    if not isinstance(cap, int):
        try:
            cap = int(cap)
        except Exception as exception:
            raise ValueError("Value of 'cap' can not be converted to int.") from exception

    _C_GL_1_1.glDisable(cap)

def glEnable(cap):
    """
    cap             : int | SupportsInt
    """
    if not isinstance(cap, int):
        try:
            cap = int(cap)
        except Exception as exception:
            raise ValueError("Value of 'cap' can not be converted to int.") from exception

    _C_GL_1_1.glEnable(cap)


# Simple Queries

def glGetBooleanv(pname):
    """
    pname            : int
    Returns          : List[bool]
        Equivalent of 'params'.
    """
    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception
            
    num = _Support.get_num_of_get_values(pname)
    if num is None:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _Support.make_c_array(_C_GL_1_1.GLboolean, num)
    _C_GL_1_1.glGetBooleanv(pname, c_params)
    return _Support.c_array_to_list(bool, c_params)

def glGetIntegerv(pname):
    """
    pname           : int
    Returns         : List[int]
        Equivalent of 'params'.
    """
    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    num = _Support.get_num_of_get_values(pname)
    if num is None:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _Support.make_c_array(_C_GL_1_1.GLint, num)
    _C_GL_1_1.glGetIntegerv(pname, c_params)
    return _Support.c_array_to_list(int, c_params)

def glGetFloatv(pname):
    """
    pname           : int
    Returns         : List[float]
        Equivalent of 'params'.
    """
    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception
            
    num = _Support.get_num_of_get_values(pname)
    if num is None:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _Support.make_c_array(_C_GL_1_1.GLfloat, num)
    _C_GL_1_1.glGetFloatv(pname, c_params)
    return _Support.c_array_to_list(float, c_params)


def glGetDoublev(pname):
    """
    pname           : int
    Returns         : List[float]
        Equivalent of 'params'.
    """
    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception
            
    num = _Support.get_num_of_get_values(pname)
    if num is None:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _Support.make_c_array(_C_GL_1_1.GLdouble, num)
    _C_GL_1_1.glGetDoublev(pname, c_params)
    return _Support.c_array_to_list(float, c_params)

def glIsEnabled(cap):
    """
    cap             : int | SupportsInt
    Returns         : bool
    """
    if not isinstance(cap, int):
        try:
            cap = int(cap)
        except Exception as exception:
            raise ValueError("Value of 'cap' can not be converted to int.") from exception

    return bool(_C_GL_1_1.glIsEnabled(cap))

# Pointer and String Queries 

def glGetPointerv(pname):
    """
    pname           : int | SupportsInt
    Returns         : bytes | List[int | float]
        Bytes or list of all array elements (depends on what was type of object provided to 'pointer' parameter in gl{Vertex|Color|...}Pointer function).
        Equivalent of 'params' parameter from OpenGl function specification.
    Exceptions
        CacheMismatch
            When cashed array mismatch actual array pointer. 
            To get actual array pointer, use function 'PyTrivialOpenGL.C_GL.glGetPointerv'.
    """
    if not isinstance(pname, int):
        try:
            pname = int(pname)
        except Exception as exception:
            raise ValueError("Value of 'pname' can not be converted to int.") from exception

    if pname in [GL_FEEDBACK_BUFFER_POINTER, GL_SELECTION_BUFFER_POINTER]:
        raise ValueError("Unsupported value of 'pname'.")

    c_array = {
        # Note: Commented elements are (most likely) from OpenGL above 1.1 or unsupported by this package.

        GL_COLOR_ARRAY_POINTER              : _Support.to_cache().c_color_array_pointer, 
        GL_EDGE_FLAG_ARRAY_POINTER          : _Support.to_cache().c_edge_flag_array_pointer, 
        # GL_FOG_COORD_ARRAY_POINTER          : _support.to_cache().???, 
        # GL_FEEDBACK_BUFFER_POINTER          : _support.to_cache().???, 
        GL_INDEX_ARRAY_POINTER              : _Support.to_cache().c_index_array_pointer, 
        GL_NORMAL_ARRAY_POINTER             : _Support.to_cache().c_normal_array_pointer, 
        # GL_SECONDARY_COLOR_ARRAY_POINTER    : _support.to_cache().???, 
        # GL_SELECTION_BUFFER_POINTER         : _support.to_cache().???, 
        GL_TEXTURE_COORD_ARRAY_POINTER      : _Support.to_cache().c_tex_coord_array_pointer,
        GL_VERTEX_ARRAY_POINTER             : _Support.to_cache().c_vertex_array_pointer,
    }.get(pname, None)

    if isinstance(c_array, bytes):
        return c_array

    if pname is None:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _ctypes.c_void_p(None)
    _C_GL_1_1.glGetPointerv(pname, _ctypes.byref(c_params))

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
    name            : int | SupportsInt
    Returns         : str
    """
    if not isinstance(name, int):
        try:
            name = int(name)
        except Exception as exception:
            raise ValueError("Value of 'name' can not be converted to int.") from exception
            
    return _ctypes.cast(_C_GL_1_1.glGetString(name), _ctypes.c_char_p).value.decode()

# Saving and Restoring State

def glPushAttrib(mask):
    """
    mask            : int | SupportsInt
    """
    if not isinstance(mask, int):
        try:
            mask = int(mask)
        except Exception as exception:
            raise ValueError("Value of 'mask' can not be converted to int.") from exception

    _C_GL_1_1.glPushAttrib(mask)

def glPushClientAttrib(mask):
    """
    mask            : int | SupportsInt
    """
    if not isinstance(mask, int):
        try:
            mask = int(mask)
        except Exception as exception:
            raise ValueError("Value of 'mask' can not be converted to int.") from exception

    _C_GL_1_1.glPushClientAttrib(mask)

def glPopAttrib():
    _C_GL_1_1.glPopAttrib()

def glPopClientAttrib():
    _C_GL_1_1.glPopClientAttrib()

