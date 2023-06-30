import ctypes as _ctypes
import enum as _enum
from . import _C_WinApi

from ._SingletonGuardian    import _SingletonGuardian
from ._WindowAreaCorrector  import _WindowAreaCorrector
from .Area                  import Area
from .Utility               import *
from .Log                   import *
from .SpecialDebug          import *

from . import _Basics
from ._Basics import clamp as _clamp
from ._Basics import _MIN_I32, _MAX_I32, _MAX_U16, _MIN_U16


__all__ = [
    "WindowStyleBit",
    "WindowStateId",
    "WindowOptionId",
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

class WindowStateId(_enum.IntEnum):
    NORMAL                  = _enum.auto()
    MAXIMIZED               = _enum.auto()
    MINIMIZED               = _enum.auto()
    WINDOWED_FULL_SCREENED  = _enum.auto()

class WindowOptionId(_enum.IntEnum):
    AUTO_SLEEP_MODE = _enum.auto()

class _WindowAreaPartId(_enum.Enum):
    POSITION            = _enum.auto()
    POSITION_OFFSET     = _enum.auto()
    SIZE                = _enum.auto()
    ALL                 = _enum.auto()

class Window:
    """
    _window_name                : str
    _window_class_name          : str

    _area                       : Area | Tuple[int, int, int, int] | None
    _style                      : int 
    _opengl_version             : OpenGL_Version | None
    _icon_file_name             : str
    _icon_resource_id           : int
    _timer_time_interval        : int
    _is_auto_sleep_blocked      : bool

    
    _instance_handle            : _C_WinApi.HINSTANCE
    _window_handle              : _C_WinApi.HWND
    _device_context_handle      : _C_WinApi.HDC
    _rendering_context_handle   : _C_WinApi.HGLRC

    _window_style               : int
    _window_extended_style      : int

    _is_active                  : bool
    _is_visible                 : bool
    _is_frame                   : bool

    _state                      : WindowStateId
    _prev_state                 : WindowStateId

    _is_apply_fake_width              : bool 
    _is_enable_do_on_resize           : bool  
    _is_enable_change_state_at_resize : bool  
    _is_in_draw                       : bool

    _is_enable_do_on_resize_stack              : List[bool]
    _is_enable_change_state_at_resize_stack    : List[bool]

    _do_on_create               : Callable[[], NoneType]
    _do_on_create               : Callable[[], NoneType]

    _draw                       : Callable[[], NoneType]


    """
    _WIDTH_CORRECTION_TO_FAKE = 1

    _singleton_guardian = _SingletonGuardian("Window")


    def __init__(self):
        self._singleton_guardian.count_as_created_instance()

        self._DEFAULT_TIMER_ID              = 1001

        self._window_name                   = ""
        self._window_class_name             = ""

        self._area                          = Area(0, 0, 0, 0)
        self._style                         = 0
        self._opengl_version                = OpenGL_Version(0, 0)
        self._icon_file_name                = ""
        self._timer_time_interval           = 0
        self._is_auto_sleep_blocked         = False

        self._window_area_corrector         = _WindowAreaCorrector()

        self._instance_handle               = None
        self._window_handle                 = None
        self._device_context_handle         = None
        self._rendering_context_handle      = None

        self._window_style                  = 0
        self._window_extended_style         = 0

        self._is_active                     = False
        self._is_visible                    = False
        self._is_frame                      = True

        self._state_id                      = WindowStateId.NORMAL
        self._prev_state_id                 = self._state_id

        self._is_apply_fake_width               = False
        self._is_enable_do_on_resize            = True
        self._is_enable_change_state_at_resize  = True
        self._is_in_draw                        = False

        self._is_enable_do_on_resize_stack              = []
        self._is_enable_change_state_at_resize_stack    = []

        ### callbacks ###

        self._do_on_create                  = None
        self._do_on_destory                 = None

        self._draw                          = None

        # TODO:
        # do_on_key
        # do_on_char
        # do_on_char_utf16
        # do_on_char_utf32
        # 
        # do_on_mouse_wheel_roll
        # do_on_mouse_move
        # 
        # do_on_resize
        # 
        # do_on_state_change
        # do_on_show
        # do_on_hide
        # do_on_foreground
        # 
        # do_on_time

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
        timer_time_interval     : int
        is_auto_sleep_blocked   : bool

        do_on_create            : Callable[[], NoneType]
        do_on_create            : Callable[[], NoneType]

        draw                    : Callable[[], NoneType]
        """
        self._window_name               = window_name

        if area is None:
            self._area = None

        elif isinstance(area, tuple):
            if len(area) == 4:
                area = Area(area[0], area[1], area[2], area[3])
                try:
                    _Basics.check_area_i32_u16(area)
                except ValueError as e:
                    raise ValueError("Wrong value range in parameter 'area'.") from e
                self._area = area
            else:
                raise ValueError("Tuple 'area' needs to contain four variables (x, y, width, height), either ints or floats.")

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
        wc.lpfnWndProc      = _c_window_proc
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

        if self._timer_time_interval > 0:
            result = _C_WinApi.SetTimer(self._window_handle, self._DEFAULT_TIMER_ID, self._timer_time_interval, _C_WinApi.TIMERPROC(0))
            if result == 0:
               log_fatal_error("Can not set timer. (windows error code: %d)" % _C_WinApi.GetLastError())


        _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_SHOW)
        _C_WinApi.SetForegroundWindow(self._window_handle)
        _C_WinApi.SetFocus(self._window_handle)

        self._change_area(self._area)

        if self._do_on_create is not None:
            self._do_on_create()

        _C_WinApi.UpdateWindow(self._window_handle)

        result = self._execute_main_loop()
  
        if _C_WinApi.UnregisterClassW(self._window_class_name, self._instance_handle):
            log_debug("Unregistered window class.")
        else:
            log_fatal_error("Can not unregister window class.")

        return result

    def request_close(self):
        _C_WinApi.DestroyWindow(self._window_handle)

    def request_draw(self):
        _C_WinApi.InvalidateRect(self._window_handle, _C_WinApi.NULL, _C_WinApi.FALSE)

    def draw_now(self):
        if not self._is_in_draw:
            self._is_in_draw = True

            if to_special_debug().is_notify_draw_call:
                log_debug("Window Draw Call")

            if self._draw:
                self._draw()

            _C_WinApi.SwapBuffers(self._device_context_handle);
            
            self._is_in_draw = False

    ###

    def set_option(self, window_option_id, is_enabled):
        """
        window_option_id : WindowOptionId
        is_enabled : bool
        """
        if window_option_id == WindowOptionId.AUTO_SLEEP_MODE:
            self._is_auto_sleep_blocked = not is_enabled

    def is_enabled(self, window_option_id):
        """
        window_option_id : WindowOptionId
        is_enabled : bool
        """
        if window_option_id == WindowOptionId.AUTO_SLEEP_MODE:
            return not self._is_auto_sleep_blocked
        
        raise RuntimeError("Unexpected window option id '%s'." % window_option_id.name)

    ###

    def move_to(self, x = None, y = None, pos = None, is_draw_area = False):
        # TODO: Check x, y, pos value range.
        if pos is not None:
            area = Area(pos.x, pos.y, 0, 0)

        elif (x is not None) and (y is not None):
            area = Area(x, y, 0, 0)

        else:
            if is_draw_area:
                pos = self.get_draw_area_pos()
            else:
                pos = self.get_pos()

            if x is None:
                x = pos.x

            if y is None:
                y = pos.y

            area = Area(x, y, 0, 0)

        self._set_area(area, _WindowAreaPartId.POSITION, is_draw_area)

    # TODO:
    # MoveTo
    # MoveBy
    # Resize
    # SetArea / Reshape
    # Center

    ###

    def get_pos(self):
        """
        Returns (Point).
        """
        return self.get_area().get_pos()

    def get_size(self):
        """
        Returns (Size).
        """
        return self.get_area().get_size()

    def get_area(self):
        """
        Returns (Area).
        """
        if self._state_id == WindowStateId.MINIMIZED:
            return Area(0, 0, 0, 0)

        area = _get_window_area(self._window_handle)

        # Workaround to problems with full screen.
        if self.is_windowed_full_screen():
           area.width -= self._WIDTH_CORRECTION_TO_FAKE

        return self._window_area_corrector.remove_invisible_frame_from_area(area, self._window_handle)

    def get_draw_area_pos(self):
        """
        Returns (Point) window draw area position in screen coordinates system.
        """
        return self.get_draw_area().get_pos()

    def get_draw_area_size(self):
        """
        Returns (Size).
        """
        return self.get_draw_area().get_size()


    def get_draw_area(self):
        if self._state_id == WindowStateId.MINIMIZED:
            return Area(0, 0, 0, 0)

        rect    = _C_WinApi.RECT()
        rect_p  = _ctypes.byref(rect)
        pos1_p  = _ctypes.cast(rect_p, _C_WinApi.LPPOINT)
        pos2_p  = _ctypes.cast(_ctypes.byref(rect.right), _C_WinApi.LPPOINT)

        if (    _C_WinApi.GetClientRect(self._window_handle, rect_p) and 
                _C_WinApi.ClientToScreen(self._window_handle, pos1_p) and 
                _C_WinApi.ClientToScreen(self._window_handle, pos2_p)
                ):
            area = _make_area_from_rect(rect)
        
            # Workaround to problems with full screen.
            if self.is_windowed_full_screen():
               area.width -= self._WIDTH_CORRECTION_TO_FAKE
        
            return area
        
        return Area(0, 0, 0, 0)

    ###

    # TODO:
    # Hide
    # Show
    # IsVisible

    ###

    # TODO:
    # Minimize
    # Maximize
    # GoWindowedFullScreen

    ###

    def get_state_id(self):
        """
        Returns (WindowStateId).
        """
        return self._state_id

    def is_normal(self):
        """
        Returns (bool).
        """
        return self.get_state_id() == WindowStateId.NORMAL

    def is_minimized(self):
        """
        Returns (bool).
        """
        return self.get_state_id() == WindowStateId.MINIMIZED

    def is_maximized(self):
        """
        Returns (bool).
        """
        return self.get_state_id() == WindowStateId.MAXIMIZED

    def is_windowed_full_screen(self):
        """
        Returns (bool).
        """
        return self.get_state_id() == WindowStateId.WINDOWED_FULL_SCREENED

    ###

    # TODO:
    # GoForeground
    # IsForeground

    ###
    
    # TODO:
    # GetStyle
    # GetCursorPosInDrawArea
    # GetOpenGL_Version

    ### Private ###

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
                    self.draw_now()
                    

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

    def _change_area(self, area):
        """
        area : Area
        """
        self._set_area(self._generate_window_area(area), _WindowAreaPartId.ALL, self._style & WindowStyleBit.DRAW_AREA_ONLY)
    

    def _generate_window_area(self, area):
        """
        area : Area
        Returns (Area).
        """
        window_area = Area(0, 0, 0, 0)

        is_default = (area is None)

        # --- Size --- #

        desktop_area = get_desctop_area_no_task_bar()

        window_area.width   = (desktop_area.width / 2) if is_default else area.width
        window_area.height  = (desktop_area.height / 2) if is_default else area.height

        # In a case of unreasonable values.
        if window_area.width < 0:
            window_area.width = 0
        if window_area.height < 1:
            window_area.height = 1

        if (self._style & WindowStyleBit.DRAW_AREA_SIZE) and not (self._style & WindowStyleBit.DRAW_AREA_ONLY):
            window_area_with_invisible_frame = _get_window_area_from_draw_area(window_area, self._window_style)

            window_area = self._window_area_corrector.remove_invisible_frame_from_area(window_area_with_invisible_frame, self._window_handle);

        # --- Position --- #

        if self._style & WindowStyleBit.CENTERED:
            window_area.x = (desktop_area.width - window_area.width) / 2
            window_area.y = (desktop_area.height - window_area.height) / 2
        else:
            window_area.x = ((desktop_area.width - window_area.width) / 2)     if is_default else area.x
            window_area.y = ((desktop_area.height - window_area.height) / 2)   if is_default else area.y

        # No need for additional adjustment for invisible window frame. 
        # Already done for both position and size in 'Size' section.

        # ---
        
        return window_area

    def _set_area(self, area, area_part_id, is_draw_area):
        """
        area            : Area
        area_part_id    : _AreaPartId
        is_draw_area    : bool
        """
        def get_flags(area_part_id):
            if area_part_id == _WindowAreaPartId.POSITION:
                return _C_WinApi.SWP_NOSIZE
            if area_part_id == _WindowAreaPartId.POSITION_OFFSET:
                return _C_WinApi.SWP_NOSIZE
            if area_part_id == _WindowAreaPartId.SIZE:
                return _C_WinApi.SWP_NOMOVE
            if area_part_id == _WindowAreaPartId.ALL:
                return 0
            return 0

        is_skip = _C_WinApi.IsMinimized(self._window_handle) and (area_part_id == _WindowAreaPartId.POSITION_OFFSET)

        if not is_skip:
            if not self._is_visible:
                _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_SHOW)

            self._restore()
        
            raw_area = Area(0, 0, 0, 0)
        
            if area_part_id == _WindowAreaPartId.POSITION_OFFSET:
                raw_area = _get_window_area(self._window_handle)
                raw_area.x += area.x
                raw_area.y += area.y
            elif is_draw_area:
                raw_area = _get_window_area_from_draw_area(area, self._window_style);
            else:
                raw_area = self._window_area_corrector.add_invisible_frame_to_area(area, self._window_handle)

            _C_WinApi.SetWindowPos(
                self._window_handle, 
                _C_WinApi.HWND_TOP, 
                _clamp(int(raw_area.x), _MIN_I32, _MAX_I32), 
                _clamp(int(raw_area.y), _MIN_I32, _MAX_I32), 
                _clamp(int(raw_area.width), _MIN_U16, _MAX_U16), 
                _clamp(int(raw_area.height), _MIN_U16, _MAX_U16), 
                get_flags(area_part_id) | _C_WinApi.SWP_SHOWWINDOW
            )
        
    def _restore(self):
        if _C_WinApi.IsMaximized(self._window_handle):
            if self._prev_state_id == WindowStateId.WINDOWED_FULL_SCREENED:
                self._push_is_enable_do_on_resize(False)
                self._push_is_enable_change_state_at_resize(False)

                _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_RESTORE)

                self._pop_is_enable_do_on_resize()
                self._pop_is_enable_change_state_at_resize()
            else:
                _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_RESTORE)

        if _C_WinApi.IsMinimized(self._window_handle):
            _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_RESTORE)
        
        if self._state_id == WindowStateId.WINDOWED_FULL_SCREENED:
            self._push_is_enable_do_on_resize(False)
            self._push_is_enable_change_state_at_resize(False)
        
            _C_WinApi.SetWindowLongPtrW(self._window_handle, _C_WinApi.GWL_STYLE,   self._window_style);
            _C_WinApi.SetWindowLongPtrW(self._window_handle, _C_WinApi.GWL_EXSTYLE, self._window_extended_style);
            _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_NORMAL);
        
            self._pop_is_enable_do_on_resize()
            self._pop_is_enable_change_state_at_resize()
        
    def _push_is_enable_do_on_resize(self, new_value):
        """
        new_value : bool
        """
        self._is_enable_do_on_resize_stack.append(self._is_enable_do_on_resize)
        self._is_enable_do_on_resize = new_value

    def _pop_is_enable_do_on_resize(self):
        if len(self._is_enable_do_on_resize_stack) > 0:
            self._is_enable_do_on_resize = self._is_enable_do_on_resize_stack.pop()

    def _push_is_enable_change_state_at_resize(self, new_value):
        """
        new_value : bool
        """
        self._is_enable_change_state_at_resize_stack.append(self._is_enable_change_state_at_resize)
        self._is_enable_change_state_at_resize = new_value

    def _pop_is_enable_change_state_at_resize(self):
        if len(self._is_enable_change_state_at_resize_stack) > 0:
            self._is_enable_change_state_at_resize = self._is_enable_change_state_at_resize_stack.pop()

    def _window_proc(self, window_handle, window_message, w_param, l_param):
        """
        window_handle   : HWND
        window_message  : UINT
        w_param         : WPARAM
        l_param         : LPARAM
        """

        # TODO: log_all_window_messages()

        ### Draw ###

        if window_message == _C_WinApi.WM_PAINT:
            return 0

        elif window_message == _C_WinApi.WM_ERASEBKGND:
            # Tells DefWindowProc to not erase background. It's unnecessary since background is handled by OpenGL.
            return 1

        ### Mouse ###

        # TODO:
        # WM_MOUSEMOVE
        # WM_MOUSEWHEEL
        # WM_LBUTTONDOWN
        # WM_LBUTTONUP
        # WM_RBUTTONDOWN
        # WM_RBUTTONUP
        # WM_MBUTTONDOWN
        # WM_MBUTTONUP
        # WM_XBUTTONDOWN
        # WM_XBUTTONUP
        
        ### Keyboard ###

        # TODO:
        # WM_KEYDOWN
        # WM_KEYUP
        # WM_SYSKEYDOWN
        # WM_SYSKEYUP
        # WM_CHAR
        
        ### Window ###

        # TODO:
        # WM_SIZING
        # WM_SIZE
        
        ### Timer ###

        # TODO:
        # WM_TIMER
        
        ### State ###

        # TODO:
        # WM_SHOWWINDOW
        # WM_ACTIVATE
        # WM_ACTIVATEAPP
        # WM_SYSCOMMAND
        
        ### Focus ###

        # TODO:
        # WM_SETFOCUS
        # WM_KILLFOCUS

        ### Create, Close, Destroy ###

        elif window_message == _C_WinApi.WM_CREATE:
            return 0

        elif window_message == _C_WinApi.WM_CLOSE:
            _C_WinApi.DestroyWindow(window_handle)
            return 0

        elif window_message == _C_WinApi.WM_DESTROY:
            if self._do_on_destroy is not None:
                self._do_on_destroy()

            _C_WinApi.PostQuitMessage(0)
            return 0

        return _C_WinApi.DefWindowProcW(window_handle, window_message, w_param, l_param)

_window = Window()

def to_window():
    """
    Returns (Window).
    """
    return _window

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

def _make_area_from_rect(rect):
    """
    rect : _C_WinApi.RECT
    """
    return Area(rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top)


def _get_window_area(window_handle):
    """
    window_handle : _C_WinApi.HWND
    Returns (Area).
    """
    rect = _C_WinApi.RECT()

    if _C_WinApi.GetWindowRect(window_handle, _ctypes.byref(rect)):
        return _make_area_from_rect(rect)
    
    return Area(0, 0, 0, 0)

def _get_window_area_from_draw_area(draw_area, window_style):
    """
    draw_area : Area
    window_style : int
    Returns (Area).
    """
    rect = _C_WinApi.RECT(
        draw_area.x,
        draw_area.y,
        draw_area.x + draw_area.width,
        draw_area.y + draw_area.height
    )

    _C_WinApi.AdjustWindowRect(_ctypes.byref(rect), window_style, _C_WinApi.FALSE)

    return _make_area_from_rect(rect)

def _window_proc(window_handle, window_message, w_param, l_param):
    return to_window()._window_proc(window_handle, window_message, w_param, l_param)

_c_window_proc = _C_WinApi.WNDPROC(_window_proc)
