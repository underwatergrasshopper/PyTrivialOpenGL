import ctypes as _ctypes
from . import _C_WinApi

from ._SingletonGuardian    import _SingletonGuardian
from .Area                  import Area
from .Utility               import *
from .Log                   import *

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
    """
    _window_name            : str
    _area                   : Area | Tuple[int, int, int, int] | None
    _style                  : int 
    _opengl_version         : OpenGL_Version | None
    _icon_file_name         : str
    _icon_resource_id       : int
    _timer_time_interval    : int
    _is_auto_sleep_blocked  : bool

    _do_on_create           : Callable[[], NoneType]
    _do_on_create           : Callable[[], NoneType]

    _draw                   : Callable[[], NoneType]

    _window_class_name      : str
    _instance_handle        : _C_WinApi.HANDLE
    _window_style           : int
    _window_extended_style  : int
    _window_handle          : _C_WinApi.HWND
    """
    _singleton_guardian = _SingletonGuardian("Window")

    def __init__(self):
        self._singleton_guardian.count_as_created_instance()

        self._window_name           = ""
        self._window_class_name     = ""

        self._area                  = Area(0, 0, 0, 0)
        self._style                 = 0
        self._opengl_version        = OpenGL_Version(0, 0)
        self._icon_file_name        = ""
        self._timer_time_interval   = 0
        self._is_auto_sleep_blocked = False

        self._instance_handle       = None
        self._window_handle         = None

        self._window_style          = 0
        self._window_extended_style = 0

        self._do_on_create          = None
        self._do_on_create          = None

        self._draw                  = None

    def create_and_run(    
            self,
            window_name              = "Window",
            area                     = None,
            style                    = 0,
            opengl_version           = None,
            icon_file_name           = "",
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
        self._window_name               = window_name

        if not area:
            self._area = _get_def_window_area()

        elif isinstance(area, tuple):
            area = Area(area[0], area[1], area[2], area[3])
            try:
                _Basics.check_area_i32_u16(area)
            except ValueError as e:
                raise ValueError("Wrong value range in parameter 'area'.") from e
            self._area = area

        elif isinstance(area, Area):
            try:
                _Basics.check_area_i32_u16(area)
            except ValueError as e:
                raise ValueError("Wrong value range in parameter 'area'.") from e
            self._area = area

        else:
            raise TypeError("Wrong type of parameter 'area'.")

        self._style                     = style
        self._opengl_version            = opengl_version          if opengl_version   else OpenGL_Version(1, 1) 
        self._icon_file_name            = icon_file_name
        self._timer_time_interval       = timer_time_interval
        self._is_auto_sleep_blocked     = is_auto_sleep_blocked

        self._do_on_create              = do_on_create
        self._do_on_destroy             = do_on_destroy
        self._draw                      = draw

        self._instance_handle = _C_WinApi.GetModuleHandleW(_C_WinApi.NULL);

        self._window_class_name = window_name + " WINDOW CLASS"

        wc = _C_WinApi.WNDCLASSEXW()
        wc.cbSize           = _ctypes.sizeof(_C_WinApi.WNDCLASSEXW)
        wc.style            = _C_WinApi.CS_OWNDC | _C_WinApi.CS_HREDRAW | _C_WinApi.CS_VREDRAW
        wc.lpfnWndProc      = _C_WindowProc
        wc.cbClsExtra       = 0
        wc.cbWndExtra       = 0
        wc.hInstance        = self._instance_handle
        wc.hIcon            = self._try_load_icon()
        wc.hCursor          = _C_WinApi.LoadCursorW(_C_WinApi.NULL, _C_WinApi.IDC_ARROW)
        wc.hbrBackground    = _C_WinApi.NULL
        wc.lpszMenuName     = _C_WinApi.NULL
        wc.lpszClassName    = self._window_class_name
        wc.hIconSm          = _C_WinApi.NULL

        if _C_WinApi.RegisterClassExW(_ctypes.byref(wc)):
            log_debug("Registered window class.")
        else:
            log_fatal_error("Can not register window class.")

        self._window_style = _C_WinApi.WS_OVERLAPPEDWINDOW;
        if style & WindowStyleBit.NO_RESIZE:
            self._window_style &= ~_C_WinApi.WS_THICKFRAME
        if style & WindowStyleBit.NO_MAXIMIZE:
            self._window_style &= ~_C_WinApi.WS_MAXIMIZEBOX
        if style & WindowStyleBit.DRAW_AREA_ONLY:
            self._window_style          = _get_window_style_draw_area_only()
            self._window_extended_style = _get_window_extended_style_draw_area_only()
        
        self._window_handle = _C_WinApi.CreateWindowExW(
            self._window_extended_style,
            self._window_class_name,
            self._window_name,
            self._window_style,
            _C_WinApi.CW_USEDEFAULT, _C_WinApi.CW_USEDEFAULT, _C_WinApi.CW_USEDEFAULT, _C_WinApi.CW_USEDEFAULT,
            _C_WinApi.NULL,
            _C_WinApi.NULL,
            self._instance_handle,
            _C_WinApi.NULL
        )

        if self._window_handle:
            log_debug("Created window.")
        else:
            log_fatal_error("Can not create window.")

        _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_SHOW)
        _C_WinApi.SetForegroundWindow(self._window_handle)
        _C_WinApi.SetFocus(self._window_handle)

        result = self._execute_main_loop()
  
        if _C_WinApi.UnregisterClassW(self._window_class_name, self._instance_handle):
            log_debug("Unregistered window class.")
        else:
            log_fatal_error("Can not unregister window class.")

        return result

    def _execute_main_loop(self):
        msg = _C_WinApi.MSG()

        if self._style & WindowStyleBit.REDRAW_ON_CHANGE_OR_REQUEST:

            while _C_WinApi.GetMessageW(_ctypes.byref(msg), _C_WinApi.NULL, 0, 0):
                _C_WinApi.TranslateMessage(_ctypes.byref(msg))
                _C_WinApi.DispatchMessageW(_ctypes.byref(msg))
            
            if msg.message == _C_WinApi.WM_QUIT:
                self._window_handle = _C_WinApi.NULL
                log_debug("Destroyed window.")
                return int(msg.wParam)

        else:
            while True:
                if _C_WinApi.PeekMessageW(_ctypes.byref(msg), _C_WinApi.NULL, 0, 0, _C_WinApi.PM_REMOVE):
                    if msg.message == _C_WinApi.WM_QUIT:
                        m_window_handle = _C_WinApi.NULL
                        log_debug("Destroyed window.")
                        return int(msg.wParam)

                    _C_WinApi.TranslateMessage(_ctypes.byref(msg))
                    _C_WinApi.DispatchMessageW(_ctypes.byref(msg))
                else:
                    pass
                    # TODO: DrawNow()

        return _C_WinApi.EXIT_FAILURE;

    def _try_load_icon(self):
        """
        Returns (HICON).
        """
        if len(self._icon_file_name) != 0:
            icon_handle = _C_WinApi.LoadImageW(
                _C_WinApi.NULL,
                self._icon_file_name,
                _C_WinApi.IMAGE_ICON,
                0, 0,
                _C_WinApi.LR_LOADFROMFILE | _C_WinApi.LR_DEFAULTSIZE | _C_WinApi.LR_SHARED
            )
            if icon_handle:
                log_debug("Loaded icon image from '%s' file." % (self._icon_file_name))
            else:
                log_warning("Can not load icon image from '%s' file." % self._icon_file_name)
            return icon_handle
        else:
            return _C_WinApi.NULL

_window = Window()

def to_window():
    """
    Returns (Window).
    """
    return _window

def _get_def_window_area():
    """
    Returns (Area).
    """
    size    = get_desctop_size_no_task_bar() // 2

    x       = size.width // 2
    y       = size.height // 2

    return Area(x, y, size.width, size.height)

def _get_window_style_draw_area_only():
    """
    Returns (int).
    """
    return _C_WinApi.WS_POPUP | _C_WinApi.WS_CLIPSIBLINGS | _C_WinApi.WS_CLIPCHILDREN

def _get_window_extended_style_draw_area_only():
    """
    Returns (int).
    """
    return _C_WinApi.WS_EX_APPWINDOW

def _WindowProc(window_handle, window_message, w_param, l_param):
    """
    window_handle   : HWND
    window_message  : UINT
    w_param         : WPARAM
    l_param         : LPARAM
    """

    if window_message == _C_WinApi.WM_PAINT:
        return 0

    elif window_message == _C_WinApi.WM_CLOSE:
        _C_WinApi.DestroyWindow(window_handle)
        return 0

    elif window_message == _C_WinApi.WM_DESTROY:
        _C_WinApi.PostQuitMessage(0)
        return 0

    return _C_WinApi.DefWindowProcW(window_handle, window_message, w_param, l_param)

_C_WindowProc = _C_WinApi.WNDPROC(_WindowProc)
