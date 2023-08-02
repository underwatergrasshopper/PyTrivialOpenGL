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
    n = _Support.get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _Support.list_part_to_c_array(float, params, n, _C_GL_1_1.GLdouble)
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
    n = _Support.get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _Support.list_part_to_c_array(float, params, n, _C_GL_1_1.GLfloat)
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
    n = _Support.get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _Support.list_part_to_c_array(int, params, n, _C_GL_1_1.GLint)
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
    c_equation = _Support.list_part_to_c_array(float, equation, 4, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glClipPlane(int(plane), c_equation)

def glGetClipPlane(plane):
    """
    plane           : int
    Returns         : List[float]
        Corresponds to 'equation' parameter from OpenGL function specification.
    """
    c_equation = _Support.make_c_array(_C_GL_1_1.GLdouble, 4)
    _C_GL_1_1.glGetClipPlane(int(plane), c_equation)
    return _Support.c_array_to_list(float, c_equation)

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
    c_params = _Support.list_to_c_array(float, params, 1, _C_GL_1_1.GLfloat)
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
    c_params = _Support.list_to_c_array(int, params, 1, _C_GL_1_1.GLint)
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
    c_params = _Support.list_to_c_array(float, params, 1, _C_GL_1_1.GLfloat)
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
    c_params = _Support.list_to_c_array(int, params, 1, _C_GL_1_1.GLint)
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
    c_params = _Support.list_to_c_array(float, params, 1, _C_GL_1_1.GLfloat)
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
    c_params = _Support.list_to_c_array(int, params, 1, _C_GL_1_1.GLint)
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

    c_params = _Support.make_c_array(_C_GL_1_1.GLfloat, length)
    _C_GL_1_1.glGetLightfv(int(light), int(pname), c_params)
    return _Support.c_array_to_list(float, c_params)

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

    c_params = _Support.make_c_array(_C_GL_1_1.GLint, length)
    _C_GL_1_1.glGetLightiv(int(light), int(pname), c_params)
    return _Support.c_array_to_list(int, c_params)

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

    c_params = _Support.make_c_array(_C_GL_1_1.GLfloat, length)
    _C_GL_1_1.glGetMaterialfv(int(face), int(pname), c_params)
    return _Support.c_array_to_list(float, c_params)

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

    c_params = _Support.make_c_array(_C_GL_1_1.GLint, length)
    _C_GL_1_1.glGetMaterialiv(int(face), int(pname), c_params)
    return _Support.c_array_to_list(int, c_params)

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
    c_v = _Support.list_part_to_c_array(float, v, 2, _C_GL_1_1.GLdouble)
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
    c_v = _Support.list_part_to_c_array(float, v, 2, _C_GL_1_1.GLfloat)
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
    c_v = _Support.list_part_to_c_array(int, v, 2, _C_GL_1_1.GLint)
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
    c_v = _Support.list_part_to_c_array(int, v, 2, _C_GL_1_1.GLshort)
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
    c_v = _Support.list_part_to_c_array(float, v, 3, _C_GL_1_1.GLdouble)
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
    c_v = _Support.list_part_to_c_array(float, v, 3, _C_GL_1_1.GLfloat)
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
    c_v = _Support.list_part_to_c_array(int, v, 3, _C_GL_1_1.GLint)
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
    c_v = _Support.list_part_to_c_array(int, v, 3, _C_GL_1_1.GLshort)
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
    c_v = _Support.list_part_to_c_array(float, v, 4, _C_GL_1_1.GLdouble)
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
    c_v = _Support.list_part_to_c_array(float, v, 4, _C_GL_1_1.GLfloat)
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
    c_v = _Support.list_part_to_c_array(int, v, 4, _C_GL_1_1.GLint)
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
    c_v = _Support.list_part_to_c_array(int, v, 4, _C_GL_1_1.GLshort)
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


def glPixelMapfv(map_, values):
    """
    map_             : int
    values           : List[float]
    """
    map_ = int(map_) 

    if isinstance(values, bytes):
        num_of_bytes = len(values)
        mapsize = num_of_bytes // 4 # div by size in bytes of single precision float 

        c_values_buffer = (_C_GL_1_1.GLubyte * num_of_bytes).from_buffer_copy(values)
        c_values = _ctypes.cast(c_values_buffer, _ctypes.POINTER(_C_GL_1_1.GLfloat))
    else:
        values = list(values)
        mapsize = len(values)

        c_values = _Support.list_to_c_array(float, values, mapsize, _C_GL_1_1.GLfloat)

    _C_GL_1_1.glPixelMapfv(map_, mapsize, c_values)

def glPixelMapuiv(map_, values):
    """
    map_             : int
    values           : List[int]
    """
    map_ = int(map_) 

    if isinstance(values, bytes):
        num_of_bytes = len(values)
        mapsize = num_of_bytes // 4 # div by size in bytes of single precision float 

        c_values_buffer = (_C_GL_1_1.GLubyte * num_of_bytes).from_buffer_copy(values)
        c_values = _ctypes.cast(c_values_buffer, _ctypes.POINTER(_C_GL_1_1.GLuint))
    else:
        values = list(values)
        mapsize = len(values)

        c_values = _Support.list_to_c_array(int, values, mapsize, _C_GL_1_1.GLuint)

    _C_GL_1_1.glPixelMapuiv(map_, mapsize, c_values)

def glPixelMapusv(map_, values):
    """
    map_             : int
    values           : List[int]
    """
    map_ = int(map_) 

    if isinstance(values, bytes):
        num_of_bytes = len(values)
        mapsize = num_of_bytes // 2 # div by size in bytes of single precision float 

        c_values_buffer = (_C_GL_1_1.GLubyte * num_of_bytes).from_buffer_copy(values)
        c_values = _ctypes.cast(c_values_buffer, _ctypes.POINTER(_C_GL_1_1.GLushort))
    else:
        values = list(values)
        mapsize = len(values)

        c_values = _Support.list_to_c_array(int, values, mapsize, _C_GL_1_1.GLushort)

    _C_GL_1_1.glPixelMapusv(map_, mapsize, c_values)


# Enumerated Queries

def glGetPixelMapfv(map_, is_return_bytes = False):
    """
    map_            : int
    is_return_bytes : bool 
    Returns         : bytes | List[float]
        bytes, when 'is_return_bytes' is True.
        list of floats, when 'is_return_bytes' is False (default).

        Equivalent of 'data' from OpenGL function specification.
    """
    map_ = int(map_)
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
    map_            : int
    is_return_bytes : bool 
    Returns         : bytes | List[int]
        bytes, when 'is_return_bytes' is True.
        list of ints, when 'is_return_bytes' is False (default).

        Equivalent of 'data' from OpenGL function specification.
    """
    map_ = int(map_)
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
    map_            : int
    Returns         : bytes | List[int]
        bytes, when 'is_return_bytes' is True.
        list of ints, when 'is_return_bytes' is False (default).

        Equivalent of 'data' from OpenGL function specification.
    """
    map_ = int(map_)
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
            c_pixels    = _Support.list_part_to_c_array(float, pixels, size, _C_GL_1_1.GLfloat)
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
    n = _Support.get_tex_format_element_number(format_)
    if n is None:
        raise ValueError("Unexpected value of 'format_' parameter")

    md = _Support.get_tex_type_mul_div_size(type_)
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

            c_pixels = _Support.list_to_c_array(float, pixels, len(pixels), _C_GL_1_1.GLfloat)
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
    n = _Support.get_tex_format_element_number(format_)
    if n is None:
        raise ValueError("Unexpected value of 'format_' parameter")

    md = _Support.get_tex_type_mul_div_size(type_)
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

            c_pixels = _Support.list_to_c_array(float, pixels, len(pixels), _C_GL_1_1.GLfloat)
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
    n = _Support.get_tex_format_element_number(format_)
    if n is None:
        raise ValueError("Unexpected value of 'format_' parameter")

    md = _Support.get_tex_type_mul_div_size(type_)
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

            c_pixels = _Support.list_to_c_array(float, pixels, len(pixels), _C_GL_1_1.GLfloat)
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
    n = _Support.get_tex_format_element_number(format_)
    if n is None:
        raise ValueError("Unexpected value of 'format_' parameter")

    md = _Support.get_tex_type_mul_div_size(type_)
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

            c_pixels = _Support.list_to_c_array(float, pixels, len(pixels), _C_GL_1_1.GLfloat)
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
    length = _Support.get_tex_parameter_length(pname)
    if length is None:
        raise ValueError("Unexpected value of parameter 'pname'.")
    elif length > len(params):
        raise ValueError("To small length of parameter 'params'.")
    
    c_params = _Support.list_to_c_array(float, params, length, _C_GL_1_1.GLfloat)
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
    length = _Support.get_tex_parameter_length(pname)
    if length is None:
        raise ValueError("Unexpected value of parameter 'pname'.")
    elif length > len(params):
        raise ValueError("To small length of parameter 'params'.")
    
    c_params = _Support.list_to_c_array(int, params, length, _C_GL_1_1.GLint)
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
    c_textures = _Support.list_to_c_array(int, textures, n, _C_GL_1_1.GLuint)
    _C_GL_1_1.glDeleteTextures(n, c_textures)

def glGenTextures(n):
    """
    n               : int
    Returns         : List[int]
        Refers to 'textures' parameter from OpenGL function specification. 
    """
    n = int(n)
    c_textures = _Support.make_c_array(_C_GL_1_1.GLuint, n)
    _C_GL_1_1.glGenTextures(n, c_textures)
    return _Support.c_array_to_list(int, c_textures)

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

    c_textures      = _Support.list_to_c_array(int, textures, n, _C_GL_1_1.GLuint)
    c_residences    = _Support.make_c_array(_C_GL_1_1.GLboolean, n)

    is_all_resident = bool(_C_GL_1_1.glAreTexturesResident(n, c_textures, c_residences))
    if not is_all_resident and residences is not None:
        residences.clear()
        residences.extend(_Support.c_array_to_list(bool, c_residences))

    return is_all_resident

def glPrioritizeTextures(textures, priorities):
    """
    textures         : List[int]
    priorities       : List[float]
    """
    n = len(textures)

    c_textures      = _Support.list_to_c_array(int, textures, n, _C_GL_1_1.GLuint)
    c_priorities    = _Support.list_to_c_array(float, priorities, n, _C_GL_1_1.GLclampf)

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
    n = _Support.get_tex_env_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _Support.list_part_to_c_array(float, params, n, _C_GL_1_1.GLfloat)

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
    n = _Support.get_tex_env_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _Support.list_part_to_c_array(int, params, n, _C_GL_1_1.GLint)

    _C_GL_1_1.glTexEnviv(int(target), int(pname), c_params)


# Enumerated Queries

def glGetTexEnvfv(target, pname):
    """
    target          : int | SupportsInt
    pname           : int | SupportsInt
    Returns         : List[float]
        Corresponds to 'params' parameter from OpenGL function specification.
    """
    n = _Support.get_tex_env_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _Support.make_c_array(_C_GL_1_1.GLfloat, n)
    _C_GL_1_1.glGetTexEnvfv(int(target), int(pname), c_params)
    return _Support.c_array_to_list(float, c_params)

def glGetTexEnviv(target, pname):
    """
    target          : int | SupportsInt
    pname           : int | SupportsInt
    Returns         : List[int]
        Corresponds to 'params' parameter from OpenGL function specification. 
    """
    n = _Support.get_tex_env_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _Support.make_c_array(_C_GL_1_1.GLint, n)
    _C_GL_1_1.glGetTexEnviv(int(target), int(pname), c_params)
    return _Support.c_array_to_list(int, c_params)

def glGetTexGendv(coord, pname):
    """
    coord           : int
    pname           : int
    Returns         : List[float]
        Corresponds to 'params' parameter from OpenGL function specification. 
    """
    n = _Support.get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _Support.make_c_array(_C_GL_1_1.GLdouble, n)
    _C_GL_1_1.glGetTexGendv(int(coord), int(pname), c_params)
    return _Support.c_array_to_list(float, c_params)

def glGetTexGenfv(coord, pname):
    """
    coord           : int
    pname           : int
    Returns         : List[float]
        Corresponds to 'params' parameter from OpenGL function specification. 
    """
    n = _Support.get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _Support.make_c_array(_C_GL_1_1.GLfloat, n)
    _C_GL_1_1.glGetTexGenfv(int(coord), int(pname), c_params)
    return _Support.c_array_to_list(float, c_params)

def glGetTexGeniv(coord, pname):
    """
    coord            : int
    pname            : int
    Returns         : List[int]
        Corresponds to 'params' parameter from OpenGL function specification. 
    """
    n = _Support.get_tex_gen_params_length(pname)
    if n is None:
        raise ValueError("Unexpected value of 'pname' parameter.")
    c_params = _Support.make_c_array(_C_GL_1_1.GLint, n)
    _C_GL_1_1.glGetTexGeniv(int(coord), int(pname), c_params)
    return _Support.c_array_to_list(int, c_params)

def glGetTexParameterfv(target, pname):
    """
    target          : int
    pname           : int
    Returns         : List[float]
        Equivalent of parameter 'params' from OpenGL functions specification.
    """
    length = _Support.get_tex_parameter_length(pname)
    if length is None:
        raise ValueError("Unexpected value of parameter 'pname'.")
    
    c_params = _Support.make_c_array(_C_GL_1_1.GLfloat, length)
    _C_GL_1_1.glGetTexParameterfv(int(target), int(pname), c_params)
    return _Support.c_array_to_list(float, c_params)

def glGetTexParameteriv(target, pname):
    """
    target          : int
    pname           : int
    Returns         : List[int]
        Equivalent of parameter 'params' from OpenGL functions specification.
    """
    length = _Support.get_tex_parameter_length(pname)
    if length is None:
        raise ValueError("Unexpected value of parameter 'pname'.")
    
    c_params = _Support.make_c_array(_C_GL_1_1.GLint, length)
    _C_GL_1_1.glGetTexParameteriv(int(target), int(pname), c_params)
    return _Support.c_array_to_list(int, c_params)

def glGetTexLevelParameterfv(target, level, pname):
    """
    target           : int
    level            : int
    pname            : int
    Returns          : List[float]
        Corresponds to 'params' parameter from OpenGL functions specification.
    """
    n = _Support.get_tex_level_parameter_number(pname)
    c_params = _Support.make_c_array(_C_GL_1_1.GLfloat, n)
    _C_GL_1_1.glGetTexLevelParameterfv(int(target), int(level), int(pname), c_params)
    return _Support.c_array_to_list(float, c_params)

def glGetTexLevelParameteriv(target, level, pname):
    """
    target           : int
    level            : int
    pname            : int
    Returns          : List[int]
        Corresponds to 'params' parameter from OpenGL functions specification.
    """
    n = _Support.get_tex_level_parameter_number(pname)
    c_params = _Support.make_c_array(_C_GL_1_1.GLint, n)
    _C_GL_1_1.glGetTexLevelParameteriv(int(target), int(level), int(pname), c_params)
    return _Support.c_array_to_list(int, c_params)

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
    if target not in _Support.get_acceptable_tex_target_ids():
        raise ValueError("Unexpected value of 'target' parameter")

    width   = glGetTexLevelParameteriv(target, level, GL_TEXTURE_WIDTH)[0]
    height  = glGetTexLevelParameteriv(target, level, GL_TEXTURE_HEIGHT)[0]
    # depth # for OpengGL 2.1+ for sure

    format_ = int(format_)
    type_   = int(type_)

    n = _Support.get_tex_format_element_number(format_)
    if n is None:
        raise ValueError("Unexpected value of 'format_' parameter.")

    md = _Support.get_tex_type_mul_div_size(type_)
    if md is None:
        raise ValueError("Unexpected value of 'type_' parameter.")

    m, d = md

    if is_return_list:
        if type_ == GL_FLOAT and format_ in [GL_RGB, GL_RGBA]:
            num_of_elements = _Support.get_tex_format_element_number(format_)

            length = width * height * num_of_elements
            c_pixels = _Support.make_c_array(_C_GL_1_1.GLfloat, length)

            _C_GL_1_1.glGetTexImage(int(target), int(level), format_, type_, _ctypes.cast(c_pixels, _ctypes.c_void_p))

            return _Support.c_array_to_list(float, c_pixels)
        else:
            raise ValueError("Unexpected value of 'type_' and/or 'format_' parameters when 'is_return_list' parameter is True.")
    else:
        single_item_size = (n * m // d)             # in bytes
        size = width * height * single_item_size    # in bytes
        c_pixels = _Support.make_c_array(_C_GL_1_1.GLubyte, size)

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

def glFogfv(pname, params):
    """
    pname            : int
    params           : List[float] | Iterable[SupportFloat]
    """
    pname = int(pname)

    length = _Support.get_fog_params_length(pname)
    if length is None:
        raise ValueError("Unexpected value of 'pname' parameter.")

    c_params = _Support.list_part_to_c_array(float, params, length, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glFogfv(pname, c_params)

def glFogi(pname, param):
    """
    pname            : int
    param            : int
    """
    _C_GL_1_1.glFogi(int(pname), int(param))

def glFogiv(pname, params):
    """
    pname            : int
    params           : List[int] | Iterable[SupportInt]
    """
    pname = int(pname)

    length = _Support.get_fog_params_length(pname)
    if length is None:
        raise ValueError("Unexpected value of 'pname' parameter.")

    c_params = _Support.list_part_to_c_array(int, params, length, _C_GL_1_1.GLint)

    _C_GL_1_1.glFogiv(pname, c_params)


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

    format_count = _Support.get_read_pixels_format_count(format_)
    if format_count is None:
        raise ValueError("Unexpected value of 'format_' parameter.")

    type_size = _Support.get_read_pixels_type_size(type_)
    if type_size is None:
        raise ValueError("Unexpected value of 'type_' parameter.")

    width       = int(width)
    height      = int(height)
    pixel_size  = int(format_count * type_size)
    size        = width * height * pixel_size

    if size > 0:
        c_pixels = _Support.make_c_array(_C_GL_1_1.GLubyte, size)
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

def glMap1d(target, u1, u2, points):
    """
    target           : int
    u1               : float
    u2               : float
    points           : List[float]
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
    stride = int(stride)
    points = list(points)

    stride = _Support.get_map_1d_stride(target)
    if stride is None:
        raise ValueError("Unexpected value of 'target' parameter.")

    if len(points) % stride != 0:
        raise ValueError("Number of items in 'points' parameter must be multiply of %s (its stride)." % stride)

    order = len(points) // stride
    c_points = _Support.list_to_c_array(float, points, len(points), _C_GL_1_1.GLdouble)

    _C_GL_1_1.glMap1d(int(target), float(u1), float(u2), stride, order, c_points)

def glMap1f(target, u1, u2, points):
    """
    target           : int
    u1               : float
    u2               : float
    stride           : int
    points           : List[float]
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
    points = list(points)

    stride = _Support.get_map_1d_stride(target)
    if stride is None:
        raise ValueError("Unexpected value of 'target' parameter.")

    if len(points) % stride != 0:
        raise ValueError("Number of items in 'points' parameter must be multiply of value from 'stride' parameter.")

    order = len(points) // stride
    c_points = _Support.list_to_c_array(float, points, len(points), _C_GL_1_1.GLfloat)

    _C_GL_1_1.glMap1f(int(target), float(u1), float(u2), stride, order, c_points)

def glMap2d(target, u1, u2, v1, v2, vorder, points):
    """
    target           : int
    u1               : float
    u2               : float
    v1               : float
    v2               : float
    vorder           : int
    points           : List[float]
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
    points = list(points)

    ustride = _Support.get_map_2d_stride(target)
    if ustride is None:
        raise ValueError("Unexpected value of 'target' parameter.")

    if len(points) % ustride != 0:
        raise ValueError("Number of items in 'points' parameter must be multiply of %d." % ustride)

    uorder = len(points) // (ustride * vorder)
    vstride = ustride * uorder

    c_points = _Support.list_to_c_array(float, points, len(points), _C_GL_1_1.GLdouble)

    _C_GL_1_1.glMap2d(int(target), float(u1), float(u2), ustride, uorder, float(v1), float(v2), vstride, vorder, c_points)

def glMap2f(target, u1, u2, v1, v2, vorder, points):
    """
    target           : int
    u1               : float
    u2               : float
    v1               : float
    v2               : float
    vorder           : int
    points           : List[float]
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
    points = list(points)

    ustride = _Support.get_map_2d_stride(target)
    if ustride is None:
        raise ValueError("Unexpected value of 'target' parameter.")

    if len(points) % ustride != 0:
        raise ValueError("Number of items in 'points' parameter must be multiply of %d." % ustride)

    uorder = len(points) // (ustride * vorder)
    vstride = ustride * uorder

    c_points = _Support.list_to_c_array(float, points, len(points), _C_GL_1_1.GLfloat)

    _C_GL_1_1.glMap2f(int(target), float(u1), float(u2), ustride, uorder, float(v1), float(v2), vstride, vorder, c_points)


def glEvalCoord1d(u):
    """
    u                : float
    """
    _C_GL_1_1.glEvalCoord1d(float(u))

def glEvalCoord1dv(u):
    """
    u                : List[float]
    """
    c_u = _Support.list_part_to_c_array(float, u, 1, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glEvalCoord1dv(c_u)

def glEvalCoord1f(u):
    """
    u                : float
    """
    _C_GL_1_1.glEvalCoord1f(float(u))

def glEvalCoord1fv(u):
    """
    u                : List[float]
    """
    c_u = _Support.list_part_to_c_array(float, u, 1, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glEvalCoord1fv(c_u)

def glEvalCoord2d(u, v):
    """
    u                : float
    v                : float
    """
    _C_GL_1_1.glEvalCoord2d(float(u), float(v))

def glEvalCoord2dv(u):
    """
    u                : List[float]
    """
    c_u = _Support.list_part_to_c_array(float, u, 2, _C_GL_1_1.GLdouble)
    _C_GL_1_1.glEvalCoord2dv(c_u)

def glEvalCoord2f(u, v):
    """
    u                : float
    v                : float
    """
    _C_GL_1_1.glEvalCoord2f(float(u), float(v))

def glEvalCoord2fv(u):
    """
    u                : List[float]
    """
    c_u = _Support.list_part_to_c_array(float, u, 2, _C_GL_1_1.GLfloat)
    _C_GL_1_1.glEvalCoord2fv(c_u)

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

def glGetMapdv(target, query):
    """
    target          : int 
    query           : int
    Returns         : List[float]
        Corresponds to 'v' parameter from OpenGL function specification.
    """
    target = int(target)
    query = int(query)

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
    target          : int
    query           : int
    Returns         : List[float]
        Corresponds to 'v' parameter from OpenGL function specification.
    """
    target = int(target)
    query = int(query)

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
    target          : int
    query           : int
    Returns         : List[int]
        Corresponds to 'v' parameter from OpenGL function specification.
    """
    target = int(target)
    query = int(query)

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

        c_type      = _Support.get_call_lists_c_type(type_)
        py_types    = _Support.get_call_lists_py_type(type_)

        c_lists = _Support.list_part_to_c_array(py_types, lists, len(lists), c_type)
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
    num = _Support.get_num_of_get_values(pname)
    if num is None:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _Support.make_c_array(_C_GL_1_1.GLboolean, num)
    _C_GL_1_1.glGetBooleanv(int(pname), c_params)
    return _Support.c_array_to_list(bool, c_params)

def glGetIntegerv(pname):
    """
    pname           : int
    ReturnType      : List[int]
        Equivalent of 'params'.
    """
    num = _Support.get_num_of_get_values(pname)
    if num is None:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _Support.make_c_array(_C_GL_1_1.GLint, num)
    _C_GL_1_1.glGetIntegerv(int(pname), c_params)
    return _Support.c_array_to_list(int, c_params)

def glGetFloatv(pname):
    """
    pname            : int
    ReturnType       : List[float]
        Equivalent of 'params'.
    """
    num = _Support.get_num_of_get_values(pname)
    if num is None:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _Support.make_c_array(_C_GL_1_1.GLfloat, num)
    _C_GL_1_1.glGetFloatv(int(pname), c_params)
    return _Support.c_array_to_list(float, c_params)


def glGetDoublev(pname):
    """
    pname            : int
    n                : int
        Number of floats to get.
    ReturnType       : List[float]
        Equivalent of 'params'.
    """
    num = _Support.get_num_of_get_values(pname)
    if num is None:
        raise ValueError("Unexpected value of 'pname'.")

    c_params = _Support.make_c_array(_C_GL_1_1.GLdouble, num)
    _C_GL_1_1.glGetDoublev(int(pname), c_params)
    return _Support.c_array_to_list(float, c_params)

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
    Returns         : bytes | List[int | float]
        Bytes or list of all array elements (depends on what was type of object provided to 'pointer' parameter in gl{Vertex|Color|...}Pointer function).
        Equivalent of 'params' parameter from OpenGl function specification.
    Exceptions
        CacheMismatch
            When cashed array mismatch actual array pointer. 
            To get actual array pointer, use function 'PyTrivialOpenGL.C_GL.glGetPointerv'.
    """

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

