import ctypes as _ctypes
from . import C_WinApi as _C_WinApi
from ..Area import Area
from ..Size import Size
from ..Point import Point

__all__ = []

class WindowAreaCorrector:
    """
    Corrects window coordinates and size to match position and size of visible part of window.
    """
    def __init__(self):
        pass

    def get_correction(self, window_handle):
        """
        window_handle : HWND
        Returns (Area).
        """
        window_rect = _C_WinApi.RECT()
        _C_WinApi.GetWindowRect(window_handle, _ctypes.byref(window_rect))

        actual_window_rect = _C_WinApi.RECT()

        # Note: To return correct values, must be called after ShowWindow(window_handle, SW_SHOW).
        _C_WinApi.DwmGetWindowAttribute(window_handle, _C_WinApi.DWMWA_EXTENDED_FRAME_BOUNDS, _ctypes.byref(actual_window_rect), _ctypes.sizeof(_C_WinApi.RECT))

        # frame thickness
        left      = actual_window_rect.left   - window_rect.left
        top       = actual_window_rect.top    - window_rect.top
        right     = window_rect.right         - actual_window_rect.right
        bottom    = window_rect.bottom        - actual_window_rect.bottom

        return Area(-left, -top, left + right, top + bottom)

    def add_invisible_frame_to_area(self, area, window_handle):
        """
        area            : TrivialOpenGL.Area
        window_handle   : HWND
        Returns (TrivialOpenGL.Area).
        """
        correction = self.get_correction(window_handle)
        return Area(
            area.x      + correction.x,
            area.y      + correction.y,
            area.width  + correction.width,
            area.height + correction.height
        )

    def add_invisible_frame_to_size(self, size, window_handle):
        """
        size            : TrivialOpenGL.Size
        window_handle   : HWND
        Returns (TrivialOpenGL.Size).
        """
        correction = self.get_correction(window_handle)
        return Size(
            size.width  + correction.width,
            size.height + correction.height
        )

    def add_invisible_frame_to_pos(self, pos, window_handle):
        """
        pos             : TrivialOpenGL.Point
        window_handle   : HWND
        Returns (TrivialOpenGL.Point).
        """
        correction = self.get_correction(window_handle)
        return Point(
            pos.x       + correction.x,
            pos.y       + correction.y,
        )

    def remove_invisible_frame_from_area(self, area, window_handle):
        """
        area            : TrivialOpenGL.Area
        window_handle   : HWND
        Returns (TrivialOpenGL.Area).
        """
        correction = self.get_correction(window_handle)
        return Area(
            area.x      - correction.x,
            area.y      - correction.y,
            area.width  - correction.width,
            area.height - correction.height
        )

    def remove_invisible_frame_from_size(self, size, window_handle):
        """
        size            : TrivialOpenGL.Size
        window_handle   : HWND
        Returns (TrivialOpenGL.Size).
        """
        correction = self.get_correction(window_handle)
        return Size(
            size.width  - correction.width,
            size.height - correction.height
        )

    def remove_invisible_frame_from_pos(self, pos, window_handle):
        """
        pos             : TrivialOpenGL.Point
        window_handle   : HWND
        Returns (TrivialOpenGL.Point).
        """
        correction = self.get_correction(window_handle)
        return Point(
            pos.x       - correction.x,
            pos.y       - correction.y,
        )