from tkinter.ttk import Style
from xml.dom.expatbuilder import DOCUMENT_NODE
from ._SingletonGuardian    import _SingletonGuardian
from .Area                  import Area

__all__ = [
    "WindowStyleBit",
    "OpenGL_Version",
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

class OpenGL_Version:
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor

class Window:
    _singleton_guardian = _SingletonGuardian("Window")

    def __init__(self):
        self._singleton_guardian.count_as_created_instance()

    def run(    self,
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
        return 0

_window = Window()

def to_window():
    return _window