from ._SingletonGuardian    import _SingletonGuardian
from .Area                  import Area
from .Utility               import *

from . import _Basics

__all__ = [
    "WindowStyleBit",
    "Window",
    "to_window",
]

class WindowStyleBit:
    NO_RESIZE                   = 0x0001
    NO_MAXIMIZE                 = 0x0002
    CENTERED                    = 0x0004
    DRAW_AREA_SIZE              = 0x0008
    DRAW_AREA_ONLY              = 0x0010
    REDRAW_ON_CHANGE_OR_REQUEST = 0x0020

class Window:
    _singleton_guardian = _SingletonGuardian("Window")

    def __init__(self):
        self._singleton_guardian.count_as_created_instance()

    def create_and_run(    
            self,
            window_name              = "",
            area                     = None,
            style                    = 0,
            opengl_version           = None,
            icon_file_name           = "",
            icon_resource_id         = 0,
            timer_time_interval      = 0,
            is_auto_sleep_blocked    = False,

            do_on_create             = None,
            do_on_destroy            = None,

            draw                     = None,
            ):
        """
        window_name             : str
        area                    : Area | Tuple[int, int, int, int] | None
        style                   : int 
            Bitfield of WindowStyleBit values.
        opengl_version          : OpenGL_Version | None
        icon_file_name          : str
        icon_resource_id        : int
        timer_time_interval     : int
        is_auto_sleep_blocked   : bool

        do_on_create            : Callable[[], NoneType]
        do_on_create            : Callable[[], NoneType]

        draw                    : Callable[[], NoneType]
        """

        self.window_name              = window_name
        self.area                     = area                    if area             else _get_def_window_area()
        self.style                    = style
        self.opengl_version           = opengl_version          if opengl_version   else OpenGL_Version(1, 1) 
        self.icon_file_name           = icon_file_name
        self.icon_resource_id         = icon_resource_id
        self.timer_time_interval      = timer_time_interval
        self.is_auto_sleep_blocked    = is_auto_sleep_blocked

        self.do_on_create             = do_on_create
        self.do_on_destroy            = do_on_destroy
        self.draw                     = draw

        _Basics.check_area_i32_u16(self.area)



        return 0

_window = Window()

def to_window():
    return _window

def _get_def_window_area():
    """
    Returns (Area).
    """
    size    = get_desctop_size_no_task_bar() // 2

    x       = size.width // 2
    y       = size.height // 2

    return Area(x, y, size.width, size.height)
