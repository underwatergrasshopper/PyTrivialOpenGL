from .Point import Point
from .Size  import Size
from .Area  import Area
from .      import _C_WinApi

import ctypes as _ctypes

__all__ = [
    "MIN_U16",
    "MAX_U16",
    "MIN_I32",
    "MAX_I32",
    "OpenGL_Version",
    "get_desktop_area_no_task_bar",
    "get_desktop_size_no_task_bar",
    "get_screen_size",
    "get_cursor_pos_in_screen",
]

################################################################################

MIN_U16 = 0
MAX_U16 = 2**31 - 1

MIN_I32 = -(2**31)
MAX_I32 = 2**31 - 1

################################################################################

class OpenGL_Version:
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor

################################################################################

def get_desktop_area_no_task_bar():
    """
    Returns (PyTrivialOpenGL.Area).
    """
    rc = _C_WinApi.RECT()
    _C_WinApi.SystemParametersInfoW(_C_WinApi.SPI_GETWORKAREA, 0, _ctypes.byref(rc), 0)
    return Area(rc.left, rc.top, rc.right - rc.left, rc.bottom - rc.top)

def get_desktop_size_no_task_bar():
    """
    Returns (PyTrivialOpenGL.Size).
    """
    return get_desktop_area_no_task_bar().get_size()

def get_screen_size():
    """
    Returns (PyTrivialOpenGL.Size).
    """
    width   = _C_WinApi.GetSystemMetrics(_C_WinApi.SM_CXSCREEN)
    height  = _C_WinApi.GetSystemMetrics(_C_WinApi.SM_CYSCREEN)
    return Size(width, height)

def get_cursor_pos_in_screen():
    """
    Returns (PyTrivialOpenGL.Point).
    """
    pt = _C_WinApi.POINT()
    if _C_WinApi.GetCursorPos(_ctypes.byref(pt)):
        return Point(pt.x, pt.y)
    return Point(0, 0)
