from .Point         import Point
from .Size          import Size
from .Area          import Area
from ._Private      import C_WinApi as _C_WinApi
from .GL._Private   import Support as _gl_support

import ctypes as _ctypes

__all__ = [
    "MIN_U16",
    "MAX_U16",
    "MIN_I32",
    "MAX_I32",
    "OpenGL_Version",
    "get_work_area",
    "get_screen_size",
    "get_cursor_pos_in_screen",
    "run_question_box",
    "is_defined_in_gl",
    "is_defined_in_c_gl",
    "get_gl_error_str",
]

################################################################################

MIN_U16 = 0
MAX_U16 = 2**31 - 1

MIN_I32 = -(2**31)
MAX_I32 = 2**31 - 1

################################################################################

class OpenGL_Version:
    """
    major : int
    minor : int
    """
    def __init__(self, major, minor):
        """
        major : int | SupportsInt
        minor : int | SupportsInt
        """
        self.major = major
        self.minor = minor

    def __setattr__(self, name, value):
        if isinstance(value, int):
            self.__dict__[name] = value
        else:
            try:
                value = int(value)
            except:
                raise TypeError("Value of '%s' can not be converted to int." % (name))

            self.__dict__[name] = value

    def __str__(self):
        return "%d.%d" % (self.major, self.minor)

    def __repr__(self):
        return self.__str__()

################################################################################

def get_work_area():
    """
    Returns : Area
        Desktop area without task bar.
    """
    rc = _C_WinApi.RECT()
    _C_WinApi.SystemParametersInfoW(_C_WinApi.SPI_GETWORKAREA, 0, _ctypes.byref(rc), 0)
    return Area(rc.left, rc.top, rc.right - rc.left, rc.bottom - rc.top)


def get_work_area():
    """
    Returns : Area
    """
    rc = _C_WinApi.RECT()
    _C_WinApi.SystemParametersInfoW(_C_WinApi.SPI_GETWORKAREA, 0, _ctypes.byref(rc), 0)
    return Area(rc.left, rc.top, rc.right - rc.left, rc.bottom - rc.top)

def get_screen_size():
    """
    Returns : Size
    """
    width   = _C_WinApi.GetSystemMetrics(_C_WinApi.SM_CXSCREEN)
    height  = _C_WinApi.GetSystemMetrics(_C_WinApi.SM_CYSCREEN)
    return Size(width, height)

def get_cursor_pos_in_screen():
    """
    Returns : Point
    """
    pt = _C_WinApi.POINT()
    if _C_WinApi.GetCursorPos(_ctypes.byref(pt)):
        return Point(pt.x, pt.y)
    return Point(0, 0)

################################################################################

def run_question_box(title = None, message = None):
    """
    Run question box and waits for answer.
    title   : str | Any | None
    message : str | Any | None
    Returns : bool
        True, when 'Yes' was pressed. 
        False, when 'No' was pressed.
    """
    if title is None:
        title = ""
    elif not isinstance(title, str):
        try:
            title = str(title)
        except Exception as exception:
            raise ValueError("Value of 'title' is not convertible to str.") from exception

    if message is None:
        message = ""
    elif not isinstance(message, str):
        try:
            message = str(message)
        except Exception as exception:
            raise ValueError("Value of 'message' is not convertible to str.") from exception

    result = _C_WinApi.OwnerlessMessageBox_FromNewThreadWithWait(message, title, _C_WinApi.MB_ICONQUESTION | _C_WinApi.MB_YESNO)

    return result == _C_WinApi.IDYES

################################################################################

def is_defined_in_gl(target):
    """
    target  : str | Any
        OpenGl extension name or OpenGL core version name.
    Returns : bool
        True, when constants and functions for target are defined in GL module.

    Note: Even if constants and functions are defined, GPU vendor might not provide them.
    """
    if not isinstance(target, str):
        try:
            target = str(target)
        except Exception as exception:
            raise ValueError("Value of 'target' is not convertible to str.") from exception

    return target in set(
        "GL_VERSION_1_0",
        "GL_VERSION_1_1",
    )

def is_defined_in_c_gl(target):
    """
    target  : str | Any
        OpenGl extension name or OpenGL core version name.
    Returns : bool
        True, when constants and functions for target are defined in C_GL module.

    Note: Even if constants and functions are defined, GPU vendor might not provide them.
    """
    if not isinstance(target, str):
        try:
            target = str(target)
        except Exception as exception:
            raise ValueError("Value of 'target' is not convertible to str.") from exception

    return target in set(
        "GL_VERSION_1_0",
        "GL_VERSION_1_1",
    )

def get_gl_error_str(gl_error_code):
    """
    gl_error_code  : int | SupportsInt
        Value returned by glGetError().
    Returns : str
    """
    if not isinstance(gl_error_code, int):
        try:
            gl_error_code = int(gl_error_code)
        except Exception as exception:
            raise ValueError("Value of 'gl_error_code' is not convertible to int.") from exception

    return _gl_support.get_gl_error_str(gl_error_code)