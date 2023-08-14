import ctypes   as _ctypes
import enum     as _enum
import os       as _os
import logging  as _logging
import re       as _re

from copy import deepcopy as _deepcopy

from ._Private import C_WinApi as _C_WinApi
from ._Private import C_WGL as _C_WGL
from . import C_GL          as _C_GL

from ._Private.SingletonGuardian    import SingletonGuardian as _SingletonGuardian
from ._Private.WindowAreaCorrector  import WindowAreaCorrector as _WindowAreaCorrector
from .Point                 import Point
from .Size                  import Size
from .Area                  import Area
from .Utility               import *
from .Log                   import *
from .SpecialDebug          import *
from .Key                   import *
from ._Private              import KeySupport as _KeySupport

from ._Private import Basics as _Basics
from ._Private.Basics import clamp      as _clamp
from ._Private.Basics import is_i32     as _is_i32
from ._Private.Basics import is_u16     as _is_u16
from ._Private.Basics import MIN_I32    as _MIN_I32
from ._Private.Basics import MAX_I32    as _MAX_I32
from ._Private.Basics import MAX_U16    as _MAX_U16
from ._Private.Basics import MIN_U16    as _MIN_U16

from ._Private.Debug import wm_to_str as _wm_to_str

from .GL._Private import Support as _gl_support


__all__ = [
    "WindowStyleBit",
    "window_style_bitfield_to_str",
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

def window_style_bitfield_to_str(style):
    """
    style   : int
        Bitfield made from values of WindowStyleBit or 0.
    Returns : str
    """
    names = []

    if style & WindowStyleBit.NO_RESIZE:                    names += ["NO_RESIZE"]
    if style & WindowStyleBit.NO_MAXIMIZE:                  names += ["NO_MAXIMIZE"]
    if style & WindowStyleBit.CENTERED:                     names += ["CENTERED"]
    if style & WindowStyleBit.DRAW_AREA_SIZE:               names += ["DRAW_AREA_SIZE"]
    if style & WindowStyleBit.DRAW_AREA_ONLY:               names += ["DRAW_AREA_ONLY"]
    if style & WindowStyleBit.REDRAW_ON_CHANGE_OR_REQUEST:  names += ["REDRAW_ON_CHANGE_OR_REQUEST"]

    return " | ".join(names)

class WindowStateId(_enum.IntEnum):
    NORMAL                  = _enum.auto()
    MAXIMIZED               = _enum.auto()
    MINIMIZED               = _enum.auto()
    WINDOWED_FULL_SCREENED  = _enum.auto()

class WindowOptionId(_enum.IntEnum):
    AUTO_SLEEP_MODE = _enum.auto()

class WindowCreateData:
    """
    width               : int
        Width of window draw area in pixels.
    height              : int
        Height of window draw area in pixels.
    is_visible          : bool
    is_foreground       : bool
    state_id            : WindowStateId
    """
    def __init__(self, width, height, is_visible, is_foreground, state_id):
        self.width              = width
        self.height             = height
        self.is_visible         = is_visible
        self.is_foreground      = is_foreground
        self.state_id           = state_id

class _WindowAreaPartId(_enum.Enum):
    POSITION            = _enum.auto()
    POSITION_OFFSET     = _enum.auto()
    SIZE                = _enum.auto()
    ALL                 = _enum.auto()

class Window:
    """
    _window_name                    : str
    _window_class_name              : str
    _style                          : int
    _opengl_version                 : OpenGL_Version
    _icon_file_name                 : str
    _icon_resource_id               : int
    _timer_time_interval            : int
    _is_auto_sleep_blocked          : bool

    _instance_handle                : int | None
    _window_handle                  : int | None
    _device_context_handle          : int | None
    _rendering_context_handle       : int | None

    _window_style                   : int
    _window_extended_style          : int

    _is_active                      : bool
    _is_visible                     : bool

    _state                          : WindowStateId
    _prev_state                     : WindowStateId

    _is_apply_fake_width                    : bool 
    _is_enable_do_on_resize                 : bool  
    _is_enable_do_on_hide_show              : bool  
    _is_enable_do_on_foreground             : bool  
    _is_enable_change_state_at_resize       : bool  
    _is_in_draw                             : bool

    _is_enable_do_on_resize_stack           : List[bool]
    _is_enable_do_on_hide_show_stack        : List[bool]
    _is_enable_do_on_foreground_stack       : List[bool]
    _is_enable_change_state_at_resize_stack : List[bool]

    _is_shift_down                  : bool
    _is_alt_down                    : bool
    _is_ctrl_down                   : bool

    _is_left_shift_down             : bool
    _is_left_alt_down               : bool
    _is_left_ctrl_down              : bool

    _is_right_shift_down            : bool
    _is_right_alt_down              : bool
    _is_right_ctrl_down             : bool

    _is_during_do_on_create         : bool

    _is_requested_close             : bool

    _dbg_code_utf32                 : int
    _code_utf32                     : int
    _is_two_utf16_code_units        : bool
    _is_decode_fail                 : bool

    _do_on_create                   : Callable[[WindowCreateData], None]
    _do_on_close                    : Callable[[], bool]
    _do_on_destroy                  : Callable[[], None]
    _draw                           : Callable[[], None]
    _do_on_key                      : Callable[[KeyId, bool, KeyExtra], None | bool]
    _do_on_text                     : Callable[[str, bool], None]
    _do_on_mouse_wheel_roll         : Callable[[int, int, int], None]
    _do_on_mouse_move               : Callable[[int, int], None]
    _do_on_resize                   : Callable[[], None]
    _do_on_state_change             : Callable[[WindowStateId], None]
    _do_on_show                     : Callable[[], None]
    _do_on_hide                     : Callable[[], None]
    _do_on_foreground               : Callable[[bool], None]
    _do_on_time                     : Callable[[int], None]
    """
    _WIDTH_CORRECTION_TO_FAKE       = 1
    _DEFAULT_TIMER_ID               = 1001

    _singleton_guardian = _SingletonGuardian("Window") # shared

    def __init__(self):
        self._singleton_guardian.count_as_created_instance()
        self._reset()

    def create_and_run(    
            self,
            window_name             = "Window",
            area                    = None,
            style                   = 0,
            state_id                = WindowStateId.NORMAL,
            is_hidden               = False,
            opengl_version          = None,
            icon_file_name          = "",
            timer_time_interval     = 0,
            is_auto_sleep_blocked   = False,

            do_on_create            = None,
            do_on_close             = None,
            do_on_destroy           = None,

            draw                    = None,

            do_on_key               = None,
            do_on_text              = None,
            
            do_on_mouse_wheel_roll  = None,
            do_on_mouse_move        = None,
            
            do_on_resize            = None,
            
            do_on_state_change      = None,
            do_on_show              = None,
            do_on_hide              = None,
            do_on_foreground        = None,
            
            do_on_time              = None,
            ):
        """
        window_name             : str | Any
        area                    : Area | Tuple[int | SupportsInt, int | SupportsInt, int | SupportsInt, int | SupportsInt] | Tuple[int | SupportsInt, int | SupportsInt] | None
            Position and size of created window. 

            When Area, then:
                Values area.x and area.y corresponds to left-top corner of window in screen coordinate system.
                Values area.width and area.height corresponds to window size or draw area size if style is DRAW_AREA_SIZE.
                All values must be int type or convertible to int.
            
            When Tuple[int | SupportsInt, int | SupportsInt, int | SupportsInt, int | SupportsInt], then:
                Values area[0] and area[0] corresponds to left-top corner of window in screen coordinate system,
                Values area[1] and area[2] corresponds to window size or draw area size if style is DRAW_AREA_SIZE.

            When Tuple[int | SupportsInt, int | SupportsInt], then:
                Values area[0] and area[0] corresponds to window size or draw area size if style is DRAW_AREA_SIZE.
                Window is centered to middle of work area (desktop area without task bar).

            When None, then:
                Window have one fourth size of work area (desktop area without task bar)
                and it is centered to middle of work area.

        style                   : int | SupportsInt
            Bitfield made of value from WindowStyleBit or 0.

        opengl_version          : OpenGL_Version | Tuple[int | SupportsInt, int | SupportsInt] | None
            Request creating rendering context with minimal version of OpenGL. 

            When Tuple[int | SupportsInt, int | SupportsInt], then:
                Value opengl_version[0] corresponds to major version.
                Value opengl_version[1] corresponds to minor version.
            When None, then it's OpenGL 1.1.

        icon_file_name          : str | Any
            File name of icon file to be loaded.
            If loaded successfully, then will displayed on title bar and task bar.

        timer_time_interval     : int | SupportsInt
            Time interval in milliseconds for do_on_time callback.

        is_auto_sleep_blocked   : bool | Any
            If True, then prevents system from going to sleep mode while window is running.

        do_on_create            : Callable[[WindowCreateData], None]
            Argument name convention: do_on_create(data).
            This is the first callback called.
            Called right after window is created.

        do_on_close                    : Callable[[], bool]
            Called when window is about to be destroyed. Caused by pressing window close button or calling request_close method.
            If returns True, then window is destroyed.
            If returns False, then window destroy is aborted, and window continues running.

        do_on_destroy           : Callable[[], None]
            This is the last callback called.
            Called right before window is destroyed.

        draw                    : Callable[[], None]
            Called each time when window content needs to be redrawn.

        do_on_key               : Callable[[KeyId, bool, KeyExtra], None | bool]
            Argument name convention: do_on_key(key_id, is_down, extra).
            Called when window receive keyboard key message or mouse button message.
            is_down
                True when key is down, False when key is up.
            extra 
                Contains additional key informations, like: 
                cursor position in draw area (extra.x, extra.y), 
                indicator if pressed key is left or right or doesn't matter (extra.keyboard_side_id).
            If do not returns any value, then received key message is discarded from further system interpretation.
            If returns True, then received key message is discarded from further system interpretation.
            If returns False, then received key message is NOT discarded from further system interpretation (useful for Alt+F4).

        do_on_text              : Callable[[str, bool], None]
            Argument name convention: do_on_text(text, is_correct).
            Called when window receive text message from keyboard (single key or key combination).
            text  
                Text received from keyboard. At least one character.
            is_correct 
                True when there was no decoding error.

        do_on_mouse_wheel_roll  : Callable[[int, int, int], None]
            Argument name convention: do_on_mouse_wheel_roll(step_count, x, y).
            Called when mouse wheel is rolled.
            step_count
                Number of wheel rotation steps. 
                Positive number if away from user. 
                Negative number if towards user.
            x, y
                Cursor position in draw area.

        do_on_mouse_move        : Callable[[int, int], None]
            Argument name convention: do_on_mouse_move(x, y).
            Called when cursor change position in draw area.
            x, y
                Cursor position in draw area.

        do_on_resize            : Callable[[int, int], None]
            Argument name convention: do_on_resize(width, height).
            Called each time window resize.
            width
                Width of draw area.
            height
                Height of draw area.

        do_on_state_change      : Callable[[WindowStateId], None]
            Argument name convention: do_on_state_change(state_id).
            Called each time when window state changes.

        do_on_show              : Callable[[], None]
            Called when window change to be visible.

        do_on_hide              : Callable[[], None]
            Called when window change to not be visible.

        do_on_foreground        : Callable[[bool], None]
            Argument name convention: do_on_foreground(is_gain).
            Called when window gains foreground position (gain keyboard focus or is activated) or leaves foreground position.
            is_gain    
                True, when window gains foreground position.
                False, when window leaves foreground position.

        do_on_time              : Callable[[int], None]
            Argument name convention: do_on_time(time_interval).
            Called periodically. Each call is delayed by time_interval. 
            Value of time_interval argument is taken form timer_time_interval argument.
            time_interval
                Time in milliseconds.

        Exceptions
            ValueError
                When either area.x, area.y, area[0] or area[1] is not in range <-2^31, 2^31-1>. 
                When either area.width, area.height, area[2] or area[3] is not in range <0, 2^31-1>.
                When area is tuple with length other than 2 or 4.
                When opengl_verion is tuple with length other than 2.
            TypeError
                When any value of area is not int type.
                When type of area is unexpected.
                When type of opengl_version is unexpected.
                When any of do_on_... parameter is not callable.
            RunTimeError
                When this method is called while window already running.
        """
        if self._is_running:
            raise RuntimeError("Window is already running.")
        self._reset()

        self._is_running = True

        if isinstance(window_name, str):
            self._window_name = window_name
        else:
            try:
                self._window_name = str(window_name)
            except Exception as exception:
                raise ValueError("Value of 'window_name' is not convertible to str.") from exception

        if isinstance(area, tuple):
            try:
                area = tuple(int(item) for item in area)
            except Exception as esception:
                raise ValueError("At least one value from 'area' is not convertible to int.") from esception

            if len(area) == 4:
                area = Area(area[0], area[1], area[2], area[3])
            elif len(area) == 2:
                style |= WindowStyleBit.CENTERED
                area = Area(0, 0, area[0], area[1])
            else:
                raise ValueError("Tuple 'area' needs to contain four variables (x, y, width, height) or two variables (width, height), either ints or convertible to ints.")

            try:
                _Basics.check_area_i32_u16(area)
            except ValueError as exception:
                raise ValueError("Wrong value range in parameter 'area'.") from exception

        elif isinstance(area, Area):
            try:
                _Basics.check_area_i32_u16(area)
            except ValueError as exception:
                raise ValueError("Wrong value range in parameter 'area'.") from exception
            area = _deepcopy(area)

        else:
            raise TypeError("Wrong type of parameter 'area'.")

        if isinstance(style, int):
             self._style = style
        else:
            try:
                 self._style = int(style)
            except Exception as exception:
                raise ValueError("Value of 'style' is not convertible to int.") from exception


        if not isinstance(state_id, WindowStateId):
            raise TypeError("Wrong type of parameter 'state_id'.")

        if not isinstance(is_auto_sleep_blocked, bool):
            try:
                is_hidden = bool(is_hidden)
            except Exception as exception:
                raise ValueError("Value of 'is_hidden' is not convertible to bool.") from exception

        if opengl_version is None:
            self._opengl_version = OpenGL_Version(0, 0)
        elif isinstance(opengl_version, OpenGL_Version):
            self._opengl_version = _deepcopy(opengl_version)
        elif isinstance(opengl_version, tuple):
            try:
                opengl_version = tuple(int(item) for item in opengl_version)
            except Exception as esception:
                raise ValueError("At least one value from 'opengl_version' is not convertible to int.") from esception

            if len(opengl_version) == 2:
                self._opengl_version = OpenGL_Version(opengl_version[0], opengl_version[1])
            else:
                raise ValueError("Wrong number of values in parameter 'opengl_version'. Should be 2.") 
        else:
            TypeError("Wrong type of parameter 'opengl_version'. Should be 'Tuple[int, int]' or 'OpenGL_Version'.")

        if isinstance(icon_file_name, str):
            self._icon_file_name = icon_file_name
        else:
            try:
                self._icon_file_name = str(icon_file_name)
            except Exception as exception:
                raise ValueError("Value of 'icon_file_name' is not convertible to str.") from exception

        if isinstance(timer_time_interval, int):
            self._timer_time_interval = timer_time_interval
        else:
            try:
                self._timer_time_interval = int(timer_time_interval)
            except Exception as exception:
                raise ValueError("Value of 'timer_time_interval' is not convertible to int.") from exception

        if isinstance(is_auto_sleep_blocked, bool):
            self._is_auto_sleep_blocked = is_auto_sleep_blocked
        else:
            try:
                self._is_auto_sleep_blocked = bool(is_auto_sleep_blocked)
            except Exception as exception:
                raise ValueError("Value of 'is_auto_sleep_blocked' is not convertible to bool.") from exception

        ### callbacks ###

        def is_wrong(callback):
            return (callback is not None) and (not callable(callback))

        if is_wrong(do_on_create):              raise TypeError("Parameter 'do_on_create' is not callable.")
        if is_wrong(do_on_close):               raise TypeError("Parameter 'do_on_close' is not callable.")
        if is_wrong(do_on_destroy):             raise TypeError("Parameter 'do_on_destroy' is not callable.")

        if is_wrong(draw):                      raise TypeError("Parameter 'draw' is not callable.")

        if is_wrong(do_on_key):                 raise TypeError("Parameter 'do_on_key' is not callable.")
        if is_wrong(do_on_text):                raise TypeError("Parameter 'do_on_text' is not callable.")

        if is_wrong(do_on_mouse_wheel_roll):    raise TypeError("Parameter 'do_on_mouse_wheel_roll' is not callable.")
        if is_wrong(do_on_mouse_move):          raise TypeError("Parameter 'do_on_mouse_move' is not callable.")

        if is_wrong(do_on_resize):              raise TypeError("Parameter 'do_on_resize' is not callable.")

        if is_wrong(do_on_state_change):        raise TypeError("Parameter 'do_on_state_change' is not callable.")
        if is_wrong(do_on_show):                raise TypeError("Parameter 'do_on_show' is not callable.")
        if is_wrong(do_on_hide):                raise TypeError("Parameter 'do_on_hide' is not callable.")
        if is_wrong(do_on_foreground):          raise TypeError("Parameter 'do_on_foreground' is not callable.")

        if is_wrong(do_on_time):                raise TypeError("Parameter 'do_on_time' is not callable.")

        self._do_on_create              = do_on_create
        self._do_on_close               = do_on_close
        self._do_on_destroy             = do_on_destroy

        self._draw                      = draw

        self._do_on_key                 = do_on_key
        self._do_on_text                = do_on_text            
        
        self._do_on_mouse_wheel_roll    = do_on_mouse_wheel_roll
        self._do_on_mouse_move          = do_on_mouse_move      
        
        self._do_on_resize              = do_on_resize          
        
        self._do_on_state_change        = do_on_state_change    
        self._do_on_show                = do_on_show            
        self._do_on_hide                = do_on_hide            
        self._do_on_foreground          = do_on_foreground      
        
        self._do_on_time                = do_on_time        
        
        ###

        self._instance_handle = _C_WinApi.GetModuleHandleW(_C_WinApi.NULL)

        self._window_class_name = self._window_name + " WINDOW CLASS"

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

        self._push_is_enable_change_state_at_resize(False)
        self._push_is_enable_do_on_hide_show(False)
        self._push_is_enable_do_on_foreground(False)
        self._push_is_enable_do_on_resize(False)

        if self._window_handle:
            log_debug("Created window.")
        else:
            log_fatal_error("Can not create window.")

        if state_id == WindowStateId.NORMAL:
            self._solve_and_set_area(area)

        elif state_id == WindowStateId.MINIMIZED:
            self._solve_and_set_area(area)
            self.minimize()

        elif state_id == WindowStateId.MAXIMIZED:
            self.maximize()

        elif state_id == WindowStateId.WINDOWED_FULL_SCREENED:
            self.go_windowed_full_screen()

        if is_hidden:
            _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_HIDE)
        elif self._state_id != WindowStateId.MINIMIZED:
            _C_WinApi.SetForegroundWindow(self._window_handle)
            _C_WinApi.SetFocus(self._window_handle)

        self._pop_is_enable_change_state_at_resize()
        self._pop_is_enable_do_on_hide_show()
        self._pop_is_enable_do_on_foreground()
        self._pop_is_enable_do_on_resize()

        if self._do_on_create is not None:
            size = self.get_draw_area_size()
            data = WindowCreateData(size.width, size.height, self._is_visible, self._is_active, self._state_id)

            self._is_during_do_on_create = True
            self._do_on_create(data)
            self._is_during_do_on_create = False

        if self._timer_time_interval > 0:
            result = _C_WinApi.SetTimer(self._window_handle, self._DEFAULT_TIMER_ID, self._timer_time_interval, _C_WinApi.TIMERPROC(0))
            if result == 0:
               log_fatal_error("Can not set timer. (windows error code: %d)" % _C_WinApi.GetLastError())

        _C_WinApi.UpdateWindow(self._window_handle)

        result = self._execute_main_loop()
  
        if _C_WinApi.UnregisterClassW(self._window_class_name, self._instance_handle):
            log_debug("Unregistered window class.")
        else:
            log_fatal_error("Can not unregister window class.")

        self._is_running = False

        return result

    def is_running(self):
        """
        Returns : bool
        """
        return self._is_running

    def request_close(self):
        """
        Should be called from inside of do_on... callback function (except do_on_close and do_on_destroy).
        Window will be closed after processing current do_on... callback function.
        """
        self._is_requested_close = True

    def request_draw(self):
        """
        Content of draw area will be re-rendered after processing current do_on... callback function.
        """
        _C_WinApi.InvalidateRect(self._window_handle, _C_WinApi.NULL, _C_WinApi.FALSE)

    def draw_now(self):
        """
        Force re-render of draw area right now.
        """
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
            AUTO_SLEEP_MODE
                No going into sleep mode by system while window is running.
        is_enabled : bool | Any
            When True, then enables option.
            When False, then disables option.
        """
        if not isinstance(window_option_id, WindowOptionId):
            raise TypeError("Unexpected type of 'window_option_id'.")

        if not isinstance(is_enabled, bool):
            try:
                is_enabled = bool(is_enabled)
            except Exception as exception:
                raise TypeError("Value of 'is_enabled' is not convertible to bool.") from exception

        if window_option_id == WindowOptionId.AUTO_SLEEP_MODE:
            self._is_auto_sleep_blocked = not is_enabled

    def is_enabled(self, window_option_id):
        """
        window_option_id    : WindowOptionId
        Returns             : bool
            True, when option is enabled.
            False, when option is disabled.
        """
        if not isinstance(window_option_id, WindowOptionId):
            raise TypeError("Unexpected type of 'window_option_id'.")

        if window_option_id == WindowOptionId.AUTO_SLEEP_MODE:
            return not self._is_auto_sleep_blocked

        return False
    ###

    def move_to(self, x = None, y = None, pos = None, is_draw_area = False):
        """
        Moves window to new position.

        Calling convention:
            move_to(10, 30)                                     - Moves to new position.
            move_to(x = 10)                                     - Moves to new position only at X axis.
            move_to(y = 10)                                     - Moves to new position only at Y axis.
            move_to(10, 30, is_draw_area = True)                - Moves left-top corner of draw area to new position. 
            move_to(pos = Point(10, 30))                        - Moves to new position.
            move_to(pos = (10, 30))                             - Moves to new position.
            move_to(pos = Point(10, 30), is_draw_area = True)   - Moves left-top corner of draw area to new position. 

        x               : int | SupportInt | None
            New position in screen coordinate system in X axis.
        y               : int | SupportInt | None
            New position in screen coordinate system in Y axis.
        pos             : Point | Tuple[int | SupportInt, int | SupportInt] | None
            New position in screen coordinate system.
        is_draw_area    : bool | Any
            If True, then new position of window corresponding to left-top corner of draw area.
            (default) If False, then new position of window corresponding to left-top corner of window.

        Assignment to at least one of 'x', 'y' or 'pos' needs to be present.
        When assignment to 'pos' is present then assignment to either 'x' or 'y' can not be present.

        Exceptions:
            TypeError
                When pos type is other than expected.
                When unexpected combination of arguments.
            ValueError
                When either x, y, pos.x, pos.y is not in range of <-2^31, 2^31-1>.
        """
        if not isinstance(is_draw_area, bool):
            try:
                is_draw_area = bool(is_draw_area)
            except Exception as exception:
                raise ValueError("Value of 'is_draw_area' is not convertible to bool.") from exception

        if pos is not None:
            if x is not None:
                raise TypeError("Unexpected combination of arguments. Assignment to 'x' shouldn't be present when assignment to 'pos' is present.")
            if y is not None:
                raise TypeError("Unexpected combination of arguments. Assignment to 'y' shouldn't be present when assignment to 'pos' is present.")

            if isinstance(pos, tuple):
                if len(pos) != 2:
                    raise TypeError("Length of tuple 'pos' is not 2.")

                try:
                    pos = tuple(int(item) for item in pos)
                except Exception as exception:
                    raise ValueError("At least one value from 'pos' is not convertible to int.") from exception

                if not _is_i32(pos[0]):
                    raise ValueError("First value of 'pos' is out of range for 32 bit integer.")
                if not _is_i32(pos[1]):
                    raise ValueError("Second value of 'pos' is out of range for 32 bit integer.")

                area = Area(pos[0], pos[1], 0, 0)

            elif isinstance(pos, Point):
                if not _is_i32(pos.x):
                    raise ValueError("Value of 'x' from 'pos' is out of range for 32 bit integer.")
                if not _is_i32(pos.y):
                    raise ValueError("Value of 'y' from 'pos' is out of range for 32 bit integer.")

                area = Area(pos.x, pos.y, 0, 0)
            else:
                raise TypeError("Unexpected type of 'pos'.")

        elif (x is not None) or (y is not None):
            if (x is None) or (y is None):
                if is_draw_area:
                    current_pos = self.get_draw_area_pos()
                else:
                    current_pos = self.get_pos()

            if x is not None:
                if not isinstance(x, int):
                    try:
                        x = int(x)
                    except Exception as exception:
                        raise ValueError("Value of 'x' is not convertible to int.") from exception

                if not _is_i32(x):
                    raise ValueError("Value of 'x' is out of range for 32 bit integer.")
            else:
                x = current_pos.x

            if y is not None:
                if not isinstance(y, int):
                    try:
                        y = int(y)
                    except Exception as exception:
                        raise ValueError("Value of 'y' is not convertible to int.") from exception

                if not _is_i32(y):
                    raise ValueError("Value of 'y' is out of range for 32 bit integer.")
            else:
                y = current_pos.y

            area = Area(x, y, 0, 0)

        else:
            raise TypeError("Unexpected combination of arguments. Assignment to at least one of 'x', 'y' or 'pos' should be present.")

        self._set_area(area, _WindowAreaPartId.POSITION, is_draw_area)

    def move_by(self, offset_x = None, offset_y = None, offset = None):
        """
        Moves window by offset.
        Won't work when window is minimized.

        Calling convention:
            move_by(10, 30)                                     - Moves by (10, 30). 
            move_by(offset_x = 10)                              - Moves by 10 only on X axis.
            move_by(offset_y = 10)                              - Moves by 10 only on Y axis.
            move_by(offset = Point(10, 30))                     - Moves by (10, 30). 
            move_by(offset = (10, 30))                          - Moves by (10, 30). 

        offset_x    : int | SupportsInt | None
            Offset in screen coordinate system at X axis.
        offset_y    : int | SupportsInt | None
            Offset in screen coordinate system at Y axis.
        offset      : Point | Tuple[int | SupportsInt, int | SupportsInt] | None
            Offset in screen coordinate system.

        Assignment to at least one of 'offset_x', 'offset_y' or 'offset' needs to be present.
        When assignment to 'offset' is present then assignment to either 'offset_x' or 'offset_y' can not be present.

        Exceptions
            TypeError
                When offset type is other than expected.
            ValueError
                When either offset_x, offset_y, offset.x, offset.y is not in range of <-2^31, 2^31-1>.
        """
        if offset is not None:
            if offset_x is not None:
                raise TypeError("Unexpected combination of arguments. Assignment to 'offset_x' shouldn't be present when assignment to 'offset' is present.")
            if offset_y is not None:
                raise TypeError("Unexpected combination of arguments. Assignment to 'offset_x' shouldn't be present when assignment to 'offset' is present.")

            if isinstance(offset, tuple):
                if len(offset) != 2:
                    raise TypeError("Length of tuple 'offset' is not 2.")

                try:
                    offset = tuple(int(item) for item in offset)
                except Exception as exception:
                    raise ValueError("At least one value from 'offset' is not convertible to int.") from exception

                if not _is_i32(offset[0]):
                    raise ValueError("First value of 'offset' is out of range for 32 bit integer.")
                if not _is_i32(offset[1]):
                    raise ValueError("Second value of 'offset' is out of range for 32 bit integer.")

                area = Area(offset[0], offset[1], 0, 0)

            elif isinstance(offset, Point):
                if not _is_i32(offset.x):
                    raise ValueError("Value of 'x' from 'offset' is out of range for 32 bit integer.")
                if not _is_i32(offset.y):
                    raise ValueError("Value of 'y' from 'offset' is out of range for 32 bit integer.")

                area = Area(offset.x, offset.y, 0, 0)
            else:
                raise TypeError("Unexpected type of 'offset'.")

        elif (offset_x is not None) or (offset_y is not None):
            if offset_x is not None:
                if not isinstance(offset_x, int):
                    try:
                        offset_x = int(offset_x)
                    except Exception as exception:
                        raise ValueError("Value of 'offset_x' is not convertible to int.") from exception

                if not _is_i32(offset_x):
                    raise ValueError("Value of 'offset_x' is out of range for 32 bit integer.")
            else:
                offset_x = 0

            if offset_y is not None:
                if not isinstance(offset_y, int):
                    try:
                        offset_y = int(offset_y)
                    except Exception as exception:
                        raise ValueError("Value of 'offset_y' is not convertible to int.") from exception

                if not _is_i32(offset_y):
                    raise ValueError("Value of 'offset_y' is out of range for 32 bit integer.")
            else:
                offset_y = 0

            area = Area(offset_x, offset_y, 0, 0)

        else:
            raise TypeError("Unexpected combination of arguments. Assignment to at least one of 'offset_x', 'offset_y' or 'offset' should be present.")

        self._set_area(area, _WindowAreaPartId.POSITION_OFFSET, False)

    def resize(self, width = None, height = None, size = None, is_draw_area = False):
        """
        Changes size of window.

        Calling convention:
            resize(100, 300)                                    - Changes both width and height of window.
            resize(width = 100)                                 - Changes only width of window.
            resize(height = 100)                                - Changes only height of window.
            resize(100, 300, is_draw_area = True)               - Changes both width and height of window's draw area.
            resize(size = Size(100, 300))                       - Changes both width and height of window.
            resize(size = (100, 300))                           - Changes both width and height of window.
            resize(size = Size(100, 300), is_draw_area = True)  - Changes both width and height of window's draw area.

        width           : int | SupportsInt | None
            New width in screen coordinate system.
        height          : int | SupportsInt | None
            New height in screen coordinate system.
        size            : Size | Tuple[int | SupportsInt, int | SupportsInt] | None
            New size in screen coordinate system.
        is_draw_area    : bool | Any
            If True, then draw area of window is resized.
            (default) If False, then window is resized.


        Assignment to at least one of 'width', 'height' or 'size' needs to be present.
        When assignment to 'size' is present then assignment to either 'width' or 'height' can not be present.

        Exceptions
            TypeError
                When size type is other than expected.
            ValueError
                When either width, height, size.width, size.height is not in range of <0, 2^31-1>.
        """
        if not isinstance(is_draw_area, bool):
            try:
                is_draw_area = bool(is_draw_area)
            except Exception as exception:
                raise ValueError("Value of 'is_draw_area' is not convertible to bool.") from exception

        if size is not None:
            if width is not None:
                raise TypeError("Unexpected combination of arguments. Assignment to 'width' shouldn't be present when assignment to 'size' is present.")
            if height is not None:
                raise TypeError("Unexpected combination of arguments. Assignment to 'height' shouldn't be present when assignment to 'size' is present.")

            if isinstance(size, tuple):
                if len(size) != 2:
                    raise TypeError("Length of tuple 'size' is not 2.")

                try:
                    size = tuple(int(item) for item in size)
                except Exception as exception:
                    raise ValueError("At least one value from 'size' is not convertible to int.") from exception

                if not _is_u16(size[0]):
                    raise ValueError("First value of 'size' is out of range for 16 bit unsigned integer.")
                if not _is_u16(size[1]):
                    raise ValueError("Second value of 'size' is out of range for 16 bit unsigned integer.")

                area = Area(0, 0, size[0], size[1])

            elif isinstance(size, Size):
                if not _is_u16(size.width):
                    raise ValueError("Value of 'width' from 'size' is out of range for 16 bit unsigned integer.")
                if not _is_u16(size.height):
                    raise ValueError("Value of 'height' from 'size' is out of range for 16 bit unsigned integer.")

                area = Area(0, 0, size.width, size.height)
            else:
                raise TypeError("Unexpected type of 'size'.")

        elif (width is not None) or (height is not None):
            if (width is None) or (height is None):
                if is_draw_area:
                    current_size = self.get_draw_area_size()
                else:
                    current_size = self.get_size()

            if width is not None:
                if not isinstance(width, int):
                    try:
                        width = int(width)
                    except Exception as exception:
                        raise ValueError("Value of 'width' is not convertible to int.") from exception

                if not _is_u16(width):
                    raise ValueError("Value of 'width' is out of range for 16 bit unsigned integer.")
            else:
                width = current_size.width

            if height is not None:
                if not isinstance(height, int):
                    try:
                        height = int(height)
                    except Exception as exception:
                        raise ValueError("Value of 'height' is not convertible to int.") from exception

                if not _is_u16(height):
                    raise ValueError("Value of 'height' is out of range for 16 bit unsigned integer.")
            else:
                height = current_size.height

            area = Area(0, 0, width, height)

        else:
            raise TypeError("Unexpected combination of arguments. Assignment to at least one of 'width', 'height' or 'size' should be present.")

        self._set_area(area, _WindowAreaPartId.SIZE, is_draw_area)

    def reshape(self, x = None, y = None, width = None, height = None, area = None, is_draw_area = False):
        """
        Changes position and size of window.

        Calling convention:
            reshape(10, 20, 100, 300)                           - Reshapes area of window.
            reshape(x = 10)                                     - Changes only x of window.
            reshape(y = 20)                                     - Changes only y of window.
            reshape(width = 100)                                - Changes only width of window.
            reshape(height = 100)                               - Changes only height of window.
            reshape(10, 20, 100, 300, is_draw_area = True)      - Reshapes area of window. Coordinates corresponds to draw area.
            reshape(area = (10, 20, 100, 300))                          - Reshapes area of window.
            reshape(area = Area(10, 20, 100, 300))                      - Reshapes area of window.
            reshape(area = Area(10, 20, 100, 300), is_draw_area = True) - Reshapes area of window. Coordinates corresponds to draw area.

        x               : int | SupportsInt | None
            New position in screen coordinate system in X axis.
        y               : int | SupportsInt | None
            New position in screen coordinate system in Y axis.
        width           : int | SupportsInt | None
            New width in screen coordinate system.
        height          : int | SupportsInt | None
            New height in screen coordinate system.
        area            : Area | Tuple[int | SupportsInt, int | SupportsInt, int | SupportsInt, int | SupportsInt] | None
            New size in screen coordinate system.
        is_draw_area    : bool | Any
            If True, then draw area of window is reshaped.
            (default) If False, then window is reshaped.

        Assignment to at least one of 'x', 'y', 'width', 'height' or 'area' needs to be present.
        When assignment to 'area' is present then assignment to any of 'x', 'y', 'width' or 'height' can not be present.

        Exceptions
            TypeError
                When area type is other than expected.
            ValueError
                When either x, y, area.x, area.y is not in range of <-2^31, 2^31-1>.
                When either width, height, area.width, area.height is not in range of <0, 2^31-1>.
        """
        if not isinstance(is_draw_area, bool):
            try:
                is_draw_area = bool(is_draw_area)
            except Exception as exception:
                raise ValueError("Value of 'is_draw_area' is not convertible to bool.") from exception

        if area is not None:
            if x is not None:
                raise TypeError("Unexpected combination of arguments. Assignment to 'x' shouldn't be present when assignment to 'area' is present.")
            if y is not None:
                raise TypeError("Unexpected combination of arguments. Assignment to 'y' shouldn't be present when assignment to 'area' is present.")
            if width is not None:
                raise TypeError("Unexpected combination of arguments. Assignment to 'width' shouldn't be present when assignment to 'area' is present.")
            if height is not None:
                raise TypeError("Unexpected combination of arguments. Assignment to 'height' shouldn't be present when assignment to 'area' is present.")

            if isinstance(area, tuple):
                if len(area) != 4:
                    raise TypeError("Length of tuple 'area' is not 4.")

                try:
                    area = tuple(int(item) for item in area)
                except Exception as exception:
                    raise ValueError("At least one value from 'area' is not convertible to int.") from exception

                if not _is_i32(area[0]):
                    raise ValueError("First value of 'area' is out of range for 32 bit integer.")
                if not _is_i32(area[1]):
                    raise ValueError("Second value of 'area' is out of range for 32 bit integer.")
                if not _is_u16(area[2]):
                    raise ValueError("Third value of 'area' is out of range for 16 bit unsigned integer.")
                if not _is_u16(area[3]):
                    raise ValueError("Fourth value of 'area' is out of range for 16 bit unsigned integer.")

                new_area = Area(area[0], area[1], area[2], area[3])

            elif isinstance(area, Area):
                if not _is_i32(area.x):
                    raise ValueError("Value of 'x' from 'area' is out of range for 32 bit integer.")
                if not _is_i32(area.y):
                    raise ValueError("Value of 'y' from 'area' is out of range for 32 bit integer.")
                if not _is_u16(area.width):
                    raise ValueError("Value of 'width' from 'area' is out of range for 16 bit unsigned integer.")
                if not _is_u16(area.height):
                    raise ValueError("Value of 'height' from 'area' is out of range for 16 bit unsigned integer.")

                new_area = _deepcopy(area)
            else:
                raise TypeError("Unexpected type of 'area'.")

        elif (x is not None) or (y is not None) or (width is not None) or (height is not None):
            if (x is None) or (y is None) or (width is None) or (height is None):
                if is_draw_area:
                    current_area = self.get_draw_area()
                else:
                    current_area = self.get_area()

            if x is not None:
                if not isinstance(x, int):
                    try:
                        x = int(x)
                    except Exception as exception:
                        raise ValueError("Value of 'x' is not convertible to int.") from exception

                if not _is_i32(x):
                    raise ValueError("Value of 'x' is out of range for 32 bit integer.")
            else:
                x = current_area.x

            if y is not None:
                if not isinstance(y, int):
                    try:
                        y = int(y)
                    except Exception as exception:
                        raise ValueError("Value of 'y' is not convertible to int.") from exception

                if not _is_i32(y):
                    raise ValueError("Value of 'y' is out of range for 32 bit integer.")
            else:
                y = current_area.y

            if width is not None:
                if not isinstance(width, int):
                    try:
                        width = int(width)
                    except Exception as exception:
                        raise ValueError("Value of 'width' is not convertible to int.") from exception

                if not _is_u16(width):
                    raise ValueError("Value of 'width' is out of range for 16 bit unsigned integer.")
            else:
                width = current_area.width

            if height is not None:
                if not isinstance(height, int):
                    try:
                        height = int(height)
                    except Exception as exception:
                        raise ValueError("Value of 'height' is not convertible to int.") from exception

                if not _is_u16(height):
                    raise ValueError("Value of 'height' is out of range for 16 bit unsigned integer.")
            else:
                height = current_area.height

            new_area = Area(x, y, width, height)

        else:
            raise TypeError("Unexpected combination of arguments. Assignment to at least one of 'x', 'y', 'width', 'height' or 'area' should be present.")

        self._set_area(new_area, _WindowAreaPartId.ALL, is_draw_area)

    def center(self, width = None, height = None, size = None, is_draw_area_size = False):
        """
        Centers window in middle of work area (desktop area excluding task bar).

        Calling convention:
            center(400, 300)                            - Changes window size to (400, 300) and centers window.
            center(size = Size(400, 300))               - Changes window size to (400, 300) and centers window.
            center(size = (400, 300))                   - Changes window size to (400, 300) and centers window.
            center(width = 400)                         - Changes only window width to 400 and centers window.
            center(height = 300)                        - Changes only window height to 300 and centers window.
            center(400, 300, is_draw_area_size = True)  - Changes draw area size to (400, 300) and centers window.

        width               : int | SupportsInt | None
            New width of window when 'is_draw_area_size' is False.
            New width of draw area when 'is_draw_area_size' is True.

        height              : int | SupportsInt | None
            New height of window when 'is_draw_area_size' is False.
            New height of draw area when 'is_draw_area_size' is True.

        size                : Size | SupportsInt | None
            New size of window when 'is_draw_area_size' is False.
            New size of draw area when 'is_draw_area_size' is True.

        is_draw_area_size   : bool | Any
            True - width and height (or size if not None) applies to window draw area.

        Draw area is place in window when OpenGL draws in.

        Exceptions
            TypeError
                When size type is other than expected.
            ValueError
                When either width, height, size.width, size.height is not in range of <0, 2^31-1>.
        """
        if not isinstance(is_draw_area_size, bool):
            try:
                is_draw_area_size = bool(is_draw_area_size)
            except Exception as exception:
                raise ValueError("Value of 'is_draw_area_size' is not convertible to bool.") from exception

        if size is not None:
            if isinstance(size, tuple):
                if len(size) != 2:
                    raise TypeError("Length of tuple 'size' is not 2.")

                try:
                    size = tuple(int(item) for item in size)
                except Exception as exception:
                    raise ValueError("At least one value from 'size' is not convertible to int.") from exception

                if not _is_u16(size[0]):
                    raise ValueError("First value of 'size' is out of range for 16 bit unsigned integer.")
                if not _is_u16(size[1]):
                    raise ValueError("Second value of 'size' is out of range for 16 bit unsigned integer.")

                window_area = Area(0, 0, size[0], size[1])

            elif isinstance(size, Size):
                if not _is_u16(size.width):
                    raise ValueError("Value of 'width' from 'size' is out of range for 16 bit unsigned integer.")
                if not _is_u16(size.height):
                    raise ValueError("Value of 'height' from 'size' is out of range for 16 bit unsigned integer.")

                window_area = Area(0, 0, size.width, size.height)
            else:
                raise TypeError("Unexpected type of 'size'.")

        elif (width is not None) or (height is not None):
            if (width is None) or (height is None):
                if is_draw_area_size:
                    current_size = self.get_draw_area_size()
                else:
                    current_size = self.get_size()

            if width is not None:
                if not isinstance(width, int):
                    try:
                        width = int(width)
                    except Exception as exception:
                        raise ValueError("Value of 'width' is not convertible to int.") from exception

                if not _is_u16(width):
                    raise ValueError("Value of 'width' is out of range for 16 bit unsigned integer.")
            else:
                width = current_size.width

            if height is not None:
                if not isinstance(height, int):
                    try:
                        height = int(height)
                    except Exception as exception:
                        raise ValueError("Value of 'height' is not convertible to int.") from exception

                if not _is_u16(height):
                    raise ValueError("Value of 'height' is out of range for 16 bit unsigned integer.")
            else:
                height = current_size.height

            window_area = Area(0, 0, width, height)

        else:
            if is_draw_area_size:
                current_size = self.get_draw_area_size()
            else:
                current_size = self.get_size()

            window_area = Area(0, 0, current_size.width, current_size.height)

        work_area = get_work_area()

        self._restore()

        if is_draw_area_size:
            window_area = _get_window_area_from_draw_area(window_area, self._window_style)
            window_area = self._window_area_corrector.remove_invisible_frame_from_area(window_area, self._window_handle)

        window_area.x = (work_area.width - window_area.width) / 2 + work_area.x
        window_area.y = (work_area.height - window_area.height) / 2 + work_area.y
        
        self.reshape(area = window_area)

    ###

    def get_x(self):
        """
        Returns : int 
            Position in screen X axis of left-top corner of window.
        """
        return self.get_area().x

    def get_y(self):
        """
        Returns : int
            Position in screen Y axis of left-top corner of window.
        """
        return self.get_area().y

    def get_width(self):
        """
        Returns : int
            Width of window.
        """
        return self.get_area().width

    def get_height(self):
        """
        Returns : int
            Height of window.
        """
        return self.get_area().height

    def get_pos(self):
        """
        Returns : Point
            Position in screen of left-top corner of window.
        """
        return self.get_area().get_pos()

    def get_size(self):
        """
        Returns : Size
            Size of window.
        """
        return self.get_area().get_size()

    def get_area(self):
        """
        Returns : Area
            Area of window.
        """
        if self._state_id == WindowStateId.MINIMIZED:
            return Area(0, 0, 0, 0)

        area = _get_window_area(self._window_handle)

        # Workaround to problems with full screen.
        if self.is_windowed_full_screened():
           area.width -= self._WIDTH_CORRECTION_TO_FAKE

        return self._window_area_corrector.remove_invisible_frame_from_area(area, self._window_handle)

    def get_draw_area_x(self):
        """
        Returns : int
            Position in screen X axis of left-top corner of draw area.
        """
        return self.get_draw_area().x

    def get_draw_area_y(self):
        """
        Returns : int 
            Position in screen Y axis of left-top corner of draw area.
        """
        return self.get_draw_area().y

    def get_draw_area_width(self):
        """
        Returns : int
            Width of draw area.
        """
        return self.get_draw_area().width

    def get_draw_area_height(self):
        """
        Returns : int
            Height of draw area.
        """
        return self.get_draw_area().height

    def get_draw_area_pos(self):
        """
        Returns : Point
            Position in screen of left-top corner of draw area.
        """
        return self.get_draw_area().get_pos()

    def get_draw_area_size(self):
        """
        Returns : Size
            Size of draw area.
        """
        return self.get_draw_area().get_size()

    def get_draw_area(self):
        """
        Returns : Area
            Area of draw area.
        """
        if self._state_id == WindowStateId.MINIMIZED:
            return Area(0, 0, 0, 0)

        rect    = _C_WinApi.RECT()
        rect_p  = _ctypes.byref(rect)
        pos1_p  = _ctypes.cast(rect_p, _C_WinApi.LPPOINT)
        pos2_p  = _ctypes.cast(_ctypes.byref(pos1_p[1]), _C_WinApi.LPPOINT)

        if (    _C_WinApi.GetClientRect(self._window_handle, rect_p) and 
                _C_WinApi.ClientToScreen(self._window_handle, pos1_p) and 
                _C_WinApi.ClientToScreen(self._window_handle, pos2_p)
                ):
            area = _make_area_from_rect(rect)
        
            # Workaround to problems with full screen.
            if self.is_windowed_full_screened():
               area.width -= self._WIDTH_CORRECTION_TO_FAKE
        
            return area
        
        return Area(0, 0, 0, 0)

    ###

    def show(self):
        _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_SHOW)

    def hide(self):
        _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_HIDE)

    def is_visible(self):
        return self._is_visible

    ###

    def minimize(self):
        if self._state_id == WindowStateId.WINDOWED_FULL_SCREENED:
            self._push_is_enable_do_on_resize(False)
            self._push_is_enable_change_state_at_resize(False)

            _C_WinApi.SetWindowLongPtrW(self._window_handle, _C_WinApi.GWL_STYLE, self._window_style)
            _C_WinApi.SetWindowLongPtrW(self._window_handle, _C_WinApi.GWL_EXSTYLE, self._window_extended_style)
            _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_NORMAL);

            self._pop_is_enable_change_state_at_resize()
            self._pop_is_enable_do_on_resize()

        elif self._state_id == WindowStateId.MAXIMIZED:
            self._push_is_enable_do_on_resize(False)
            self._push_is_enable_change_state_at_resize(False)

            _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_RESTORE)

            self._pop_is_enable_change_state_at_resize()
            self._pop_is_enable_do_on_resize()

        _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_MINIMIZE)

    def maximize(self):
        if not self._is_visible:
            _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_SHOW)

        if self._state_id == WindowStateId.WINDOWED_FULL_SCREENED:
            self._push_is_enable_do_on_resize(False)
            self._push_is_enable_change_state_at_resize(False)

            _C_WinApi.SetWindowLongPtrW(self._window_handle, _C_WinApi.GWL_STYLE, self._window_style)
            _C_WinApi.SetWindowLongPtrW(self._window_handle, _C_WinApi.GWL_EXSTYLE, self._window_extended_style)

            self._pop_is_enable_change_state_at_resize()
            self._pop_is_enable_do_on_resize()

        elif self._state_id == WindowStateId.MINIMIZED:
            _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_RESTORE)

        if self._style & WindowStyleBit.DRAW_AREA_ONLY:
            work_area = get_work_area()

            self._push_is_enable_change_state_at_resize(False)

            _C_WinApi.SetWindowPos(self._window_handle, _C_WinApi.HWND_TOP, work_area.x, work_area.y, work_area.width, work_area.height, _C_WinApi.SWP_SHOWWINDOW)

            self._pop_is_enable_change_state_at_resize()

            self._set_state(WindowStateId.MAXIMIZED)
        else:
            _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_MAXIMIZE)

    def go_windowed_full_screen(self):
        if not self._is_visible:
            _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_SHOW)
        
        self._push_is_enable_do_on_resize(False)
        self._push_is_enable_change_state_at_resize(False)

        _C_WinApi.SetWindowLongPtrW(self._window_handle, _C_WinApi.GWL_STYLE, _get_window_style_draw_area_only())
        _C_WinApi.SetWindowLongPtrW(self._window_handle, _C_WinApi.GWL_EXSTYLE, _get_window_extended_style_draw_area_only())

        self._pop_is_enable_change_state_at_resize()
        self._pop_is_enable_do_on_resize()

        # Workaround.
        # In Windows 7, if window is borderless and covers exactly whole screen then alt+tab is not working. 
        # To omit that, size of window is extended beyond borders of screen, internally.
        # Library provides size of window without this internal adjustment.
        screen_size = get_screen_size()
        screen_rect = _C_WinApi.RECT(0, 0, screen_size.width, screen_size.height)
        _C_WinApi.AdjustWindowRectEx(_ctypes.byref(screen_rect), _get_window_style_draw_area_only(), _C_WinApi.FALSE, _get_window_extended_style_draw_area_only())
        screen_area = _make_area_from_rect(screen_rect)

        self._push_is_enable_change_state_at_resize(False)
        self._is_apply_fake_width = True

        _C_WinApi.SetWindowPos(self._window_handle, _C_WinApi.HWND_TOP, screen_area.x, screen_area.y, screen_area.width + self._WIDTH_CORRECTION_TO_FAKE, screen_area.height, _C_WinApi.SWP_SHOWWINDOW)

        self._is_apply_fake_width = False
        self._pop_is_enable_change_state_at_resize()

        self._set_state(WindowStateId.WINDOWED_FULL_SCREENED)

    ###

    def get_state_id(self):
        """
        Returns : WindowStateId
        """
        return self._state_id

    def get_previous_state_id(self):
        """
        Returns : WindowStateId
        """
        return self._previous_state_id

    def is_normal(self):
        """
        Returns : bool
        """
        return self.get_state_id() == WindowStateId.NORMAL

    def is_minimized(self):
        """
        Returns : bool
        """
        return self.get_state_id() == WindowStateId.MINIMIZED

    def is_maximized(self):
        """
        Returns : bool
        """
        return self.get_state_id() == WindowStateId.MAXIMIZED

    def is_windowed_full_screened(self):
        """
        Returns : bool
        """
        return self.get_state_id() == WindowStateId.WINDOWED_FULL_SCREENED

    ###

    def go_foreground(self):
        _C_WinApi.SetForegroundWindow(self._window_handle)

    def is_foreground(self):
        """
        Returns : bool
        """
        return _C_WinApi.GetForegroundWindow() == self._window_handle

    ###
    
    def get_style(self):
        """
        Returns : int
            Bitfield made of values from WindowStyleBit or 0.
        """
        return self._style

    def get_cursor_pos_in_draw_area(self):
        """
        Returns : Point
        """
        pos = _C_WinApi.POINT()
        if _C_WinApi.GetCursorPos(_ctypes.byref(pos)) and _C_WinApi.ScreenToClient(self._window_handle, _ctypes.byref(pos)):
            return Point(pos.x, pos.y)
        return Point(0, 0)

    def get_opengl_version(self):
        """
        Returns : OpenGL_Version
        """
        return _deepcopy(self._opengl_version)

    ### Private ###

    def _reset(self):
        self._is_running                    = False 

        self._window_name                   = ""
        self._window_class_name             = ""

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

        self._state_id                      = WindowStateId.NORMAL
        self._previous_state_id             = WindowStateId.NORMAL

        self._is_apply_fake_width               = False
        self._is_enable_do_on_resize            = True
        self._is_enable_do_on_hide_show         = True
        self._is_enable_do_on_foreground        = True
        self._is_enable_change_state_at_resize  = True
        self._is_in_draw                        = False

        self._is_enable_do_on_resize_stack              = []
        self._is_enable_do_on_hide_show_stack           = []
        self._is_enable_do_on_foreground_stack          = []
        self._is_enable_change_state_at_resize_stack    = []

        self._is_shift_down                 = False
        self._is_alt_down                   = False
        self._is_ctrl_down                  = False

        self._is_left_shift_down            = False
        self._is_left_alt_down              = False
        self._is_left_ctrl_down             = False

        self._is_right_shift_down           = False
        self._is_right_alt_down             = False
        self._is_right_ctrl_down            = False

        self._is_during_do_on_create        = False

        self._is_requested_close            = False

        # character decoding
        self._dbg_code_utf32                = 0
        self._code_utf32                    = 0
        self._is_two_utf16_code_units       = False
        self._is_decode_fail                = False

        ### callbacks ###

        self._do_on_create                  = None
        self._do_on_close                   = None
        self._do_on_destory                 = None

        self._draw                          = None
                        
        self._do_on_key                     = None
        self._do_on_text                    = None
        
        self._do_on_mouse_wheel_roll        = None
        self._do_on_mouse_move              = None
        
        self._do_on_resize                  = None
        
        self._do_on_state_change            = None
        self._do_on_show                    = None
        self._do_on_hide                    = None
        self._do_on_foreground              = None
        
        self._do_on_time                    = None

    def _execute_main_loop(self):
        """
        Returns : int
        """
        msg = _C_WinApi.MSG()

        if self._style & WindowStyleBit.REDRAW_ON_CHANGE_OR_REQUEST:

            while _C_WinApi.GetMessageW(_ctypes.byref(msg), _C_WinApi.NULL, 0, 0):
                _C_WinApi.TranslateMessage(_ctypes.byref(msg))
                _C_WinApi.DispatchMessageW(_ctypes.byref(msg))

                if self._is_requested_close:
                    self._is_requested_close = False
                    self._close()
            
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

                    if self._is_requested_close:
                        self._is_requested_close = False
                        self._close()
                else:
                    self.draw_now()
                    

        return _C_WinApi.EXIT_FAILURE


    def _try_load_icon(self):
        """
        Returns : C_WinApi.HICON
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

    def _solve_and_set_area(self, area):
        # Position of window is always in screen coordinate system and correspond to left-top corner of window.
        # Area's width and height correspond to window or draw area.

        _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_SHOW)

        # Note: Faster solution.
        self._set_area(self._solve_window_area(area), _WindowAreaPartId.ALL, self._style & WindowStyleBit.DRAW_AREA_ONLY)

        # Note: More readable solution.
        #if self._style & WindowStyleBit.CENTERED:
        #    self.center(area.width, area.height, is_draw_area_size = self._style & WindowStyleBit.DRAW_AREA_SIZE)
        #else:
        #    self.move_to(area.x, area.y)
        #    self.resize(area.width, area.height, is_draw_area = self._style & WindowStyleBit.DRAW_AREA_SIZE)

    def _solve_window_area(self, area):
        """
        area    : Area
        Returns : Area
        """
        window_area = Area(0, 0, 0, 0)

        is_default = (area is None)

        # --- Size --- #

        work_area = get_work_area()

        window_area.width   = (work_area.width / 2) if is_default else area.width
        window_area.height  = (work_area.height / 2) if is_default else area.height

        # In a case of unreasonable values.
        if window_area.width < 0:
            window_area.width = 0
        if window_area.height < 1:
            window_area.height = 1

        if (self._style & WindowStyleBit.DRAW_AREA_SIZE) and not (self._style & WindowStyleBit.DRAW_AREA_ONLY):
            window_area_with_invisible_frame = _get_window_area_from_draw_area(window_area, self._window_style)
     
            window_area = self._window_area_corrector.remove_invisible_frame_from_area(window_area_with_invisible_frame, self._window_handle)

        # --- Position --- #

        if self._style & WindowStyleBit.CENTERED:
            window_area.x = (work_area.width - window_area.width) / 2 + work_area.x
            window_area.y = (work_area.height - window_area.height) / 2 + work_area.y
        else:
            window_area.x = ((work_area.width - window_area.width) / 2 + work_area.x)     if is_default else area.x
            window_area.y = ((work_area.height - window_area.height) / 2 + work_area.y)   if is_default else area.y

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
            if self._previous_state_id == WindowStateId.WINDOWED_FULL_SCREENED:
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

    def _push_is_enable_do_on_hide_show(self, new_value):
        """
        new_value : bool
        """
        self._is_enable_do_on_hide_show_stack.append(self._is_enable_do_on_hide_show)
        self._is_enable_do_on_hide_show = new_value

    def _pop_is_enable_do_on_hide_show(self):
        if len(self._is_enable_do_on_hide_show_stack) > 0:
            self._is_enable_do_on_hide_show = self._is_enable_do_on_hide_show_stack.pop()

    def _push_is_enable_do_on_foreground(self, new_value):
        """
        new_value : bool
        """
        self._is_enable_do_on_foreground_stack.append(self._is_enable_do_on_foreground)
        self._is_enable_do_on_foreground = new_value

    def _pop_is_enable_do_on_foreground(self):
        if len(self._is_enable_do_on_foreground_stack) > 0:
            self._is_enable_do_on_foreground = self._is_enable_do_on_foreground_stack.pop()

    def _push_is_enable_change_state_at_resize(self, new_value):
        """
        new_value : bool
        """
        self._is_enable_change_state_at_resize_stack.append(self._is_enable_change_state_at_resize)
        self._is_enable_change_state_at_resize = new_value

    def _pop_is_enable_change_state_at_resize(self):
        if len(self._is_enable_change_state_at_resize_stack) > 0:
            self._is_enable_change_state_at_resize = self._is_enable_change_state_at_resize_stack.pop()

    def _handle_do_on_mouse_key(self, window_message, w_param, l_param):
        """
        window_message  : int
        w_param         : int
        l_param         : int
        Returns         : bool
        """
        is_discard = True

        is_down = _KeySupport.is_mouse_button_down(window_message)

        if self._do_on_key:
            key_id = _KeySupport.get_mouse_key_id(window_message, w_param);

            extra = KeyExtra(
                count               = 1,
                x                   = _C_WinApi.GET_X_LPARAM(l_param).value,
                y                   = _C_WinApi.GET_Y_LPARAM(l_param).value,
                keyboard_side_id    = KeyboardSideId.NONE
            )

            extra.is_shift_down         = self._is_shift_down
            extra.is_alt_down           = self._is_alt_down
            extra.is_ctrl_down          = self._is_ctrl_down
            extra.is_left_shift_down    = self._is_left_shift_down
            extra.is_left_alt_down      = self._is_left_alt_down
            extra.is_left_ctrl_down     = self._is_left_ctrl_down
            extra.is_right_shift_down   = self._is_right_shift_down
            extra.is_right_alt_down     = self._is_right_alt_down
            extra.is_right_ctrl_down    = self._is_right_ctrl_down   

            is_discard = self._do_on_key(key_id, is_down, extra)
            if is_discard is None: 
                is_discard = True
        
        # Tracks mouse button up message when mouse button is down and cursor leave window draw (client) area.
        if is_down:
            _C_WinApi.SetCapture(self._window_handle)
        elif _C_WinApi.GetCapture() == self._window_handle:
            _C_WinApi.ReleaseCapture()

        return is_discard

    def _handle_do_on_keybard_key(self, is_down, w_param, l_param):
        """
        is_down : bool
        w_param : int
        l_param : int
        Returns : bool
        """
        is_discard = True

        if self._do_on_key:
            vk_data = _KeySupport.VirtualKeyData(l_param)
            key_id = _KeySupport.vk_code_to_key_id(w_param)

            pos = self.get_cursor_pos_in_draw_area()

            extra = KeyExtra(
                count               = vk_data.count,
                x                   = pos.x,
                y                   = pos.y,
                keyboard_side_id    = _KeySupport.get_keyboard_side_id(key_id, vk_data),
            )

            if key_id == KeyId.SHIFT:
                if is_down:
                    if extra.keyboard_side_id == KeyboardSideId.LEFT:
                        self._is_left_shift_down = True
                    elif extra.keyboard_side_id == KeyboardSideId.RIGHT:
                        self._is_right_shift_down = True
                else:
                    if extra.keyboard_side_id == KeyboardSideId.LEFT:
                        self._is_left_shift_down = False
                    elif extra.keyboard_side_id == KeyboardSideId.RIGHT:
                        self._is_right_shift_down = False

                self._is_shift_down = self._is_left_shift_down or self._is_right_shift_down

            elif key_id == KeyId.ALT:
                if is_down:
                    if extra.keyboard_side_id == KeyboardSideId.LEFT:
                        self._is_left_alt_down = True
                    elif extra.keyboard_side_id == KeyboardSideId.RIGHT:
                        self._is_right_alt_down = True
                else:
                    if extra.keyboard_side_id == KeyboardSideId.LEFT:
                        self._is_left_alt_down = False
                    elif extra.keyboard_side_id == KeyboardSideId.RIGHT:
                        self._is_right_alt_down = False

                self._is_alt_down = self._is_left_alt_down or self._is_right_alt_down

            elif key_id == KeyId.CONTROL:
                if is_down:
                    if extra.keyboard_side_id == KeyboardSideId.LEFT:
                        self._is_left_ctrl_down = True
                    elif extra.keyboard_side_id == KeyboardSideId.RIGHT:
                        self._is_right_ctrl_down = True
                else:
                    if extra.keyboard_side_id == KeyboardSideId.LEFT:
                        self._is_left_ctrl_down = False
                    elif extra.keyboard_side_id == KeyboardSideId.RIGHT:
                        self._is_right_ctrl_down = False

                self._is_ctrl_down = self._is_left_ctrl_down or self._is_right_ctrl_down

            extra.is_shift_down         = self._is_shift_down
            extra.is_alt_down           = self._is_alt_down
            extra.is_ctrl_down          = self._is_ctrl_down
            extra.is_left_shift_down    = self._is_left_shift_down
            extra.is_left_alt_down      = self._is_left_alt_down
            extra.is_left_ctrl_down     = self._is_left_ctrl_down
            extra.is_right_shift_down   = self._is_right_shift_down
            extra.is_right_alt_down     = self._is_right_alt_down
            extra.is_right_ctrl_down    = self._is_right_ctrl_down   

            is_discard = self._do_on_key(key_id, is_down, extra)
            if is_discard is None: 
                is_discard = True

        return is_discard

    def _set_state(self, state_id):
        """
        state_id : WindowStateId
        """
        self._previous_state_id = self._state_id
        self._state_id = state_id

        if (self._state_id != self._previous_state_id) and self._do_on_state_change:
           self._do_on_state_change(state_id)

    def _create(self, window_handle):
        """
        window_handle : C_WinApi.HWND
        """
        pfd = _C_WinApi.PIXELFORMATDESCRIPTOR()
        pfd.nSize           = _ctypes.sizeof(_C_WinApi.PIXELFORMATDESCRIPTOR)
        pfd.nVersion        = 1
        pfd.dwFlags         = _C_WinApi.PFD_DRAW_TO_WINDOW | _C_WinApi.PFD_SUPPORT_OPENGL | _C_WinApi.PFD_DOUBLEBUFFER
        pfd.iPixelType      = _C_WinApi.PFD_TYPE_RGBA
        pfd.cColorBits      = 24
        pfd.cAlphaBits      = 8
        pfd.cDepthBits      = 32
        pfd.cStencilBits    = 8
        pfd.iLayerType      = _C_WinApi.PFD_MAIN_PLANE

        self._device_context_handle = _C_WinApi.GetDC(window_handle)
        if not self._device_context_handle:
           log_fatal_error("Can not get device context.")

        pfi = _C_WinApi.ChoosePixelFormat(self._device_context_handle, _ctypes.byref(pfd))
        if not pfi:
           log_fatal_error("Can not choose pixel format. (windows error code: %d)" % _C_WinApi.GetLastError())

        result = _C_WinApi.SetPixelFormat(self._device_context_handle, pfi, _ctypes.byref(pfd))
        if not result:
            log_fatal_error("Can not set pixel format. (windows error code: %d))" % _C_WinApi.GetLastError())

        # --- Displaying Format Info --- #

        if is_log_level_at_least(LogLevel.INFO):
            pfd = _C_WinApi.PIXELFORMATDESCRIPTOR()
            max_pfi = _C_WinApi.DescribePixelFormat(self._device_context_handle, pfi, _ctypes.sizeof(_C_WinApi.PIXELFORMATDESCRIPTOR), _ctypes.byref(pfd))
            if not max_pfi:
               log_fatal_error("Can not get pixel format. (windows error code: %d)" % _C_WinApi.GetLastError())

            log_info("OpenGL Pixel Format: Red:%d Green:%d Blue:%d Alpha:%d Depth:%d Stencil:%d." % (pfd.cRedBits, pfd.cGreenBits, pfd.cBlueBits, pfd.cAlphaBits, pfd.cDepthBits, pfd.cStencilBits))

        # --- Creates OpenGL Rendering Context --- #

        self._rendering_context_handle = _C_WGL.wglCreateContext(self._device_context_handle)
        if not self._rendering_context_handle:
           log_fatal_error("Can not create OpenGl Rendering Context. (windows error code: %d))" % _C_WinApi.GetLastError())

        if not _C_WGL.wglMakeCurrent(self._device_context_handle, self._rendering_context_handle):
            log_fatal_error("Can not set created OpenGl Rendering Context to be current.")

        # --- Creates OpenGL Rendering Context with required minimum version --- #

        if self._opengl_version.major != 0 and self._opengl_version.minor != 0:
            wglCreateContextAttribsARB = _C_WGL.PFNWGLCREATECONTEXTATTRIBSARBPROC(_C_WGL.wglGetProcAddress(b"wglCreateContextAttribsARB"))
            if not wglCreateContextAttribsARB:
                log_fatal_error("Can not load wglCreateContextAttribsARB function.")

            attribute_list = [
                _C_WGL.WGL_CONTEXT_MAJOR_VERSION_ARB, self._opengl_version.major,
                _C_WGL.WGL_CONTEXT_MINOR_VERSION_ARB, self._opengl_version.minor,
                _C_WGL.WGL_CONTEXT_PROFILE_MASK_ARB, _C_WGL.WGL_CONTEXT_COMPATIBILITY_PROFILE_BIT_ARB,
                0
            ]
            attribute_list = (_ctypes.c_int * len(attribute_list))(*(attribute for attribute in attribute_list))

            rendering_context_handle = wglCreateContextAttribsARB(self._device_context_handle, 0, attribute_list)
            if not rendering_context_handle:
                log_fatal_error("Can not create OpenGl Rendering Context for version %d.%d (error code = %d)." % (self._opengl_version.major, self._opengl_version.minor, _C_WinApi.GetLastError()))
            

            if not _C_WGL.wglMakeCurrent(self._device_context_handle, rendering_context_handle):
                log_fatal_error( "Can not set created OpenGl Rendering Context for version %d.%d to be current." % (self._opengl_version.major, self._opengl_version.minor))
            
            self._rendering_context_handle = rendering_context_handle

        # --- Fetch OpenGL Versions --- #

        major = _ctypes.c_int()
        minor = _ctypes.c_int()
        
        # From OpenGl v3.0
        GL_MAJOR_VERSION = 0x821B
        GL_MINOR_VERSION = 0x821C
        
        _C_GL.glGetIntegerv(GL_MAJOR_VERSION, _ctypes.byref(major))
        gl_error_code = _C_GL.glGetError()
        
        if gl_error_code == _C_GL.GL_NO_ERROR:
            _C_GL.glGetIntegerv(GL_MINOR_VERSION, _ctypes.byref(minor));
            gl_error_code = _C_GL.glGetError()

        if gl_error_code == _C_GL.GL_NO_ERROR:
            self._opengl_version = OpenGL_Version(major.value, minor.value)

        elif gl_error_code == _C_GL.GL_INVALID_ENUM:
            version_text = _ctypes.cast(_C_GL.glGetString(_C_GL.GL_VERSION), _ctypes.c_char_p).value.decode()

            result = _re.search(r"^([1-9][0-9]*)\.([0-9]+).*$", version_text)
            if result and result.lastindex == 2:
                self._opengl_version = OpenGL_Version(int(result.group(1)), int(result.group(2)))
            else:
                log_fatal_error("Can not receive OpenGL version from string.")
        else:
            log_fatal_error("Can not receive OpenGL version.")

        if is_log_level_at_least(LogLevel.INFO):
            version_text = _ctypes.cast(_C_GL.glGetString(_C_GL.GL_VERSION), _ctypes.c_char_p).value.decode()
            log_info("OpenGl Version: %s." % version_text)

    def _close(self):
        """
        Returns : bool
            False, when window destroy is aborted.
        """
        if self._do_on_close:
            is_abort = not self._do_on_close()
        else:
            is_abort = False

        if not is_abort:
            _C_WinApi.DestroyWindow(self._window_handle)
           
        return not is_abort

    def _destroy(self):
        if self._do_on_destroy:
            self._do_on_destroy()

        _gl_support.to_cache().clear()

        _C_WGL.wglMakeCurrent(_C_WinApi.NULL, _C_WinApi.NULL)
        _C_WGL.wglDeleteContext(self._rendering_context_handle)
        self._rendering_context_handle = _C_WinApi.NULL

        _C_WinApi.ReleaseDC(self._window_handle, self._device_context_handle);
        self._device_context_handle = _C_WinApi.NULL

        _C_WinApi.PostQuitMessage(0)


    def _window_proc(self, window_handle, window_message, w_param, l_param):
        """
        window_handle   : C_WinApi.HWND
        window_message  : C_WinApi.UINT
        w_param         : C_WinApi.WPARAM
        l_param         : C_WinApi.LPARAM
        """

        ### Draw ###

        if window_message == _C_WinApi.WM_PAINT:
            if True or to_special_debug().is_notify_remaining_messages:
                log_debug("WM_PAINT")

            self.draw_now()
            _C_WinApi.ValidateRect(self._window_handle, _C_WinApi.NULL)
            return 0
        
        elif window_message == _C_WinApi.WM_ERASEBKGND:
            if to_special_debug().is_notify_remaining_messages:
                log_debug("WM_ERASEBKGND")
            # Tells DefWindowProc to not erase background. It's unnecessary since background is handled by OpenGL.
            return 1
        
        ### Mouse ###
        
        elif window_message == _C_WinApi.WM_MOUSEMOVE:
            if to_special_debug().is_notify_mouse_move:
                wm_text = "WM_MOUSEMOVE"
                x       = _C_WinApi.GET_X_LPARAM(l_param).value
                y       = _C_WinApi.GET_Y_LPARAM(l_param).value
        
                log_debug("%-20s: %d %d" % (wm_text, x, y))
        
            if self._do_on_mouse_move:
                self._do_on_mouse_move(_C_WinApi.GET_X_LPARAM(l_param).value, _C_WinApi.GET_Y_LPARAM(l_param).value)
        
            return 0
        
        elif window_message == _C_WinApi.WM_MOUSEWHEEL:
            if is_log_level_at_least(LogLevel.DEBUG):
                wm_text = "WM_MOUSEWHEEL"
                delta   = _C_WinApi.GET_WHEEL_DELTA_WPARAM(w_param).value
                x       = _C_WinApi.GET_X_LPARAM(l_param).value # in screen coordinates system
                y       = _C_WinApi.GET_Y_LPARAM(l_param).value # in screen coordinates system
        
                pos = _C_WinApi.POINT(x, y)
                _C_WinApi.ScreenToClient(self._window_handle, _ctypes.byref(pos)) # in window client (draw area) coordinates system
        
                mk_text = _mk_to_str(_C_WinApi.LOWORD(w_param).value)
        
                log_debug("%-20s: %d (%d %d) %d %d %s" % (wm_text, delta, x, y, pos.x, pos.y, mk_text))
        
            if self._do_on_mouse_wheel_roll:
                step_count = _C_WinApi.GET_WHEEL_DELTA_WPARAM(w_param).value // 120
        
                pos = _C_WinApi.POINT(_C_WinApi.GET_X_LPARAM(l_param), _C_WinApi.GET_Y_LPARAM(l_param))
                _C_WinApi.ScreenToClient(self._window_handle, _ctypes.byref(pos))
        
                self._do_on_mouse_wheel_roll(step_count, pos.x, pos.y)
        
            return 0
        
        elif _KeySupport.is_mw_mouse_button(window_message):
            if is_log_level_at_least(LogLevel.DEBUG):
                wm_text = _wm_to_str(window_message)
        
                xb_text = ""
                if _KeySupport.is_mw_mouse_button_x(window_message):
                    if      _C_WinApi.HIWORD(w_param).value == _C_WinApi.XBUTTON1: xb_text = " XBUTTON1"
                    elif    _C_WinApi.HIWORD(w_param).value == _C_WinApi.XBUTTON2: xb_text = " XBUTTON2"
        
                x       = _C_WinApi.GET_X_LPARAM(l_param).value 
                y       = _C_WinApi.GET_Y_LPARAM(l_param).value 
                mk_text = _mk_to_str(_C_WinApi.LOWORD(w_param).value)
        
                log_debug("%-20s:%s %d %d %s" % (wm_text, xb_text, x, y, mk_text))
        
            is_discard = self._handle_do_on_mouse_key(window_message, w_param, l_param)
            if is_discard:
                return 0
        
        ### Keyboard ###
        
        elif window_message in [_C_WinApi.WM_KEYDOWN, _C_WinApi.WM_KEYUP, _C_WinApi.WM_SYSKEYDOWN, _C_WinApi.WM_SYSKEYUP]:
            if to_special_debug().is_notify_key_message:
                wm_text = _wm_to_str(window_message)
                vk_text = _KeySupport.vk_code_to_str(w_param)
                vk_data = _KeySupport.VirtualKeyData(l_param)
        
                log_debug("%-20s: %-13s %s" % (wm_text, vk_text, vk_data))
        
            is_down = window_message in [_C_WinApi.WM_KEYDOWN, _C_WinApi.WM_SYSKEYDOWN]
        
            is_discard = self._handle_do_on_keybard_key(is_down, w_param, l_param)
            if is_discard:
                return 0
        
        elif window_message == _C_WinApi.WM_CHAR:
            if to_special_debug().is_notify_character_message:
                wm_text = "WM_CHAR"
                vk_data = _KeySupport.VirtualKeyData(l_param)
                
                code = w_param
        
                if (0xDC00 & code) == 0xDC00: # second utf-16 code unit
                    self._dbg_code_utf32 += (code & 0x000003FF) + 0x00010000
                    code_text = "cu2=%04Xh, cp=%Xh(%d), chr='%s'" % (code, self._dbg_code_utf32, self._dbg_code_utf32, chr(self._dbg_code_utf32))
        
                elif (0xD800 & code) == 0xD800: # first utf-16 code unit
                    self._dbg_code_utf32 = (code & 0x000003FF) << 10
                    code_text = "cu1=%04Xh" % (code)
        
                else: # ascii or single utf-16 code unit
                    code_text = "cp=%Xh(%d), chr='%s'" % (code, code, chr(code))
        
                log_debug("%-20s: %s, %s" % (wm_text, code_text, vk_data))
        
            if self._do_on_text:
                code = w_param
        
                if (0xDC00 & code) == 0xDC00: # second utf-16 code unit
                    if not self._is_two_utf16_code_units:
                        self._is_decode_fail = True
        
                    self._code_utf32 += (code & 0x000003FF) + 0x00010000
                    self._do_on_text(chr(self._code_utf32), not self._is_decode_fail)
        
                    self._is_decode_fail = False
                    self._is_two_utf16_code_units = False
        
                elif (0xD800 & code) == 0xD800: # first utf-16 code unit
                    if self._is_two_utf16_code_units:
                        self._is_decode_fail = True
        
                    self._code_utf32 = (code & 0x000003FF) << 10
        
                    self._is_two_utf16_code_units = True
        
                else: # ascii or single utf-16 code unit
                    if self._is_two_utf16_code_units:
                        self._is_decode_fail = True
                        self._is_two_utf16_code_units = False
        
                    self._do_on_text(chr(code), not self._is_decode_fail)
        
                    self._is_decode_fail = False
            return 0
        
        ### Window ###
        
        elif window_message == _C_WinApi.WM_SIZING:
            if is_log_level_at_least(LogLevel.DEBUG):
                wm_text = "WM_SIZING"
        
                def get_edge_name(edge_id):
                    if edge_id == _C_WinApi.WMSZ_LEFT:          return "WMSZ_LEFT"         
                    if edge_id == _C_WinApi.WMSZ_RIGHT:         return "WMSZ_RIGHT"        
                    if edge_id == _C_WinApi.WMSZ_TOP:           return "WMSZ_TOP"         
                    if edge_id == _C_WinApi.WMSZ_TOPLEFT:       return "WMSZ_TOPLEFT"
                    if edge_id == _C_WinApi.WMSZ_TOPRIGHT:      return "WMSZ_TOPRIGHT"
                    if edge_id == _C_WinApi.WMSZ_BOTTOM:        return "WMSZ_BOTTOM"   
                    if edge_id == _C_WinApi.WMSZ_BOTTOMLEFT:    return "WMSZ_BOTTOMLEFT"
                    if edge_id == _C_WinApi.WMSZ_BOTTOMRIGHT:   return "WMSZ_BOTTOMRIGHT"
                    return "(%d)" % edge_id
                edge_name = get_edge_name(w_param)
        
                rect_p = _ctypes.cast(l_param, _C_WinApi.LPRECT)
                drag_rect_text = "drag_rect=%d %d %d %d" % (rect_p[0].left, rect_p[0].top, rect_p[0].right, rect_p[0].bottom)
        
                log_debug("%-20s: %s, %s" % (wm_text, edge_name, drag_rect_text))
        
            return _C_WinApi.TRUE
        
        elif window_message == _C_WinApi.WM_SIZE:
            if is_log_level_at_least(LogLevel.DEBUG):
                wm_text     = "WM_SIZE"
                width       = _C_WinApi.LOWORD(l_param).value
                height      = _C_WinApi.HIWORD(l_param).value
        
                def get_request_nama(request_id):
                    if request_id == _C_WinApi.SIZE_MAXHIDE:    return "SIZE_MAXHIDE"
                    if request_id == _C_WinApi.SIZE_MAXIMIZED:  return "SIZE_MAXIMIZED"
                    if request_id == _C_WinApi.SIZE_MAXSHOW:    return "SIZE_MAXSHOW"
                    if request_id == _C_WinApi.SIZE_MINIMIZED:  return "SIZE_MINIMIZED"
                    if request_id == _C_WinApi.SIZE_RESTORED:   return "SIZE_RESTORED"
                    return "(%d)" % request_id
                request_name = get_request_nama(w_param)
        
                additional = ""
                if self._is_apply_fake_width:
                    additional += ", fake_width=%d" % self._WIDTH_CORRECTION_TO_FAKE
                if not self._is_enable_do_on_resize:
                    additional += ", without:do_on_resize"
        
                log_debug("%-20s: %d %d, %s%s" % (wm_text, width, height, request_name, additional))
        
            self._is_visible = True
        
            if self._do_on_resize:
                if self._is_enable_do_on_resize:
                    width = _C_WinApi.LOWORD(l_param).value
                    height = _C_WinApi.HIWORD(l_param).value
                    if self._is_apply_fake_width:
                        self._do_on_resize(width - self._WIDTH_CORRECTION_TO_FAKE, height)
                    else:
                        self._do_on_resize(width, height)
        
            if self._is_enable_change_state_at_resize:
                if w_param == _C_WinApi.SIZE_MAXIMIZED:  
                    self._set_state(WindowStateId.MAXIMIZED)
                elif w_param == _C_WinApi.SIZE_MINIMIZED:    
                    self._set_state(WindowStateId.MINIMIZED)
                elif w_param == _C_WinApi.SIZE_RESTORED:    
                    self._set_state(WindowStateId.NORMAL)
               
            return 0
        
        ## Timer ###

        elif window_message == _C_WinApi.WM_TIMER:
            if to_special_debug().is_notify_timer:
                wm_text         = "WM_TIMER"
                timer_id        = w_param
                callback_addr   = l_param
                log_debug("%-20s: id=%d, callback_addr=%d" % (wm_text, timer_id, callback_addr))

            if w_param == self._DEFAULT_TIMER_ID:
                if self._do_on_time:
                   self._do_on_time(self._timer_time_interval)

            return 0
        
        ### State ###

        elif window_message == _C_WinApi.WM_SHOWWINDOW:
            if is_log_level_at_least(LogLevel.DEBUG):
                wm_text = "WM_SHOWWINDOW"

                visibility_text = "SHOW" if w_param == _C_WinApi.TRUE else "HIDE"

                def get_status_name(status_id):
                    if status_id == _C_WinApi.SW_OTHERUNZOOM:    return "SW_OTHERUNZOOM"
                    if status_id == _C_WinApi.SW_OTHERZOOM:      return "SW_OTHERZOOM"
                    if status_id == _C_WinApi.SW_PARENTCLOSING:  return "SW_PARENTCLOSING"
                    if status_id == _C_WinApi.SW_PARENTOPENING:  return "SW_PARENTOPENING"
                    return "(%d)" % status_id

                if l_param:
                    status_name = get_status_name(l_param)
                else:
                    status_name = ""

                if not self._is_enable_do_on_hide_show:
                    if visibility_text == "SHOW":
                        status_name += " without:do_on_show"
                    else:
                        status_name += " without:do_on_hide"

                log_debug("%-20s: %s %s" % (wm_text, visibility_text, status_name))

            is_visible = (w_param == _C_WinApi.TRUE)

            if is_visible != self._is_visible:
                self._is_visible = is_visible

                if self._is_visible and self._do_on_show:
                    if self._is_enable_do_on_hide_show:
                        self._do_on_show()
                elif (not self._is_visible) and self._do_on_hide:
                    if self._is_enable_do_on_hide_show:
                        self._do_on_hide()

            return 0
        
        elif window_message == _C_WinApi.WM_ACTIVATE:
            is_active = _C_WinApi.LOWORD(w_param).value != _C_WinApi.WA_INACTIVE

            if is_log_level_at_least(LogLevel.DEBUG):
                wm_text = "WM_ACTIVATE"

                is_minimized = _C_WinApi.HIWORD(w_param).value

                if is_minimized:
                    minimized_text = " MINIMIZED"
                else:
                    minimized_text = ""

                def get_activation_state_name(state_id):
                    if state_id == _C_WinApi.WA_ACTIVE:         return "WA_ACTIVE"
                    elif state_id == _C_WinApi.WA_CLICKACTIVE:  return "WA_CLICKACTIVE"
                    elif state_id == _C_WinApi.WA_INACTIVE:     return "WA_INACTIVE"
                    return "(%d)" % state_id
                activation_state_name = get_activation_state_name(_C_WinApi.LOWORD(w_param).value)

                if is_active != self._is_active:
                    transition_text = " active->inactive" if self._is_active else " inactive->active"
                else:
                    transition_text = ""

                if not self._is_enable_do_on_foreground:
                    transition_text += " without:do_on_foreground"

                log_debug("%-20s:%s %s%s" % (wm_text, minimized_text, activation_state_name, transition_text))

            if is_active != self._is_active:
                self._is_active = is_active

                if self._do_on_foreground:
                    if self._is_enable_do_on_foreground:
                        self._do_on_foreground(is_active)

            return 0

        elif window_message == _C_WinApi.WM_SYSCOMMAND:
            if to_special_debug().is_notify_remaining_messages:
                wm_text = "WM_SYSCOMMAND"

                def get_system_command_name(cmd_id):        
                    if cmd_id == _C_WinApi.SC_SIZE:         return "SC_SIZE"        
                    if cmd_id == _C_WinApi.SC_MOVE:         return "SC_MOVE"
                    if cmd_id == _C_WinApi.SC_MINIMIZE:     return "SC_MINIMIZE"
                    if cmd_id == _C_WinApi.SC_MAXIMIZE:     return "SC_MAXIMIZE"
                    if cmd_id == _C_WinApi.SC_NEXTWINDOW:   return "SC_NEXTWINDOW"
                    if cmd_id == _C_WinApi.SC_PREVWINDOW:   return "SC_PREVWINDOW"
                    if cmd_id == _C_WinApi.SC_CLOSE:        return "SC_CLOSE"
                    if cmd_id == _C_WinApi.SC_VSCROLL:      return "SC_VSCROLL"
                    if cmd_id == _C_WinApi.SC_HSCROLL:      return "SC_HSCROLL"
                    if cmd_id == _C_WinApi.SC_MOUSEMENU:    return "SC_MOUSEMENU"
                    if cmd_id == _C_WinApi.SC_KEYMENU:      return "SC_KEYMENU"
                    if cmd_id == _C_WinApi.SC_ARRANGE:      return "SC_ARRANGE"
                    if cmd_id == _C_WinApi.SC_RESTORE:      return "SC_RESTORE"
                    if cmd_id == _C_WinApi.SC_TASKLIST:     return "SC_TASKLIST"
                    if cmd_id == _C_WinApi.SC_SCREENSAVE:   return "SC_SCREENSAVE"
                    if cmd_id == _C_WinApi.SC_HOTKEY:       return "SC_HOTKEY"
                    if cmd_id == _C_WinApi.SC_DEFAULT:      return "SC_DEFAULT"
                    if cmd_id == _C_WinApi.SC_MONITORPOWER: return "SC_MONITORPOWER"
                    if cmd_id == _C_WinApi.SC_CONTEXTHELP:  return "SC_CONTEXTHELP"
                    if cmd_id == _C_WinApi.SC_SEPARATOR:    return "SC_SEPARATOR"
                    return "(%d)" % cmd_id
                system_command_name = get_system_command_name(w_param)

                # if not used, both might be 0
                x = _C_WinApi.GET_X_LPARAM(l_param).value # screen coordinates
                y = _C_WinApi.GET_X_LPARAM(l_param).value # screen coordinates

                log_debug("%-20s: %d %d %s" % (wm_text, x, y, system_command_name))

            if self._is_auto_sleep_blocked:
                system_command_id = w_param

                if system_command_id == _C_WinApi.SC_SCREENSAVE: 
                    # Blocks screen saver.
                    return 0
                elif system_command_id == _C_WinApi.SC_MONITORPOWER: 
                    # Blocks entering to power save mode.
                    return 0

        ### Focus ###

        elif window_message == _C_WinApi.WM_SETFOCUS:
            if is_log_level_at_least(LogLevel.DEBUG):
                log_debug("WM_SETFOCUS")

            return 0

        elif window_message == _C_WinApi.WM_KILLFOCUS:
            if is_log_level_at_least(LogLevel.DEBUG):
                log_debug("WM_KILLFOCUS")

            return 0

        ### Create, Close, Destroy ###

        elif window_message == _C_WinApi.WM_CREATE:
            if is_log_level_at_least(LogLevel.DEBUG):
                log_debug("WM_CREATE")

            self._create(window_handle)
            return 0

        elif window_message == _C_WinApi.WM_CLOSE:
            if is_log_level_at_least(LogLevel.DEBUG):
                log_debug("WM_CLOSE")

            self._close()
            return 0

        elif window_message == _C_WinApi.WM_DESTROY:
            if is_log_level_at_least(LogLevel.DEBUG):
                log_debug("WM_DESTROY")

            self._destroy()
            return 0

        else:
            if to_special_debug().is_notify_remaining_messages:
                log_debug(_wm_to_str(window_message))

        return _C_WinApi.DefWindowProcW(window_handle, window_message, w_param, l_param)

_window = Window()

def to_window():
    """
    Returns : Window
    """
    return _window

def _get_window_style_draw_area_only():
    """
    Returns : int
    """
    return _C_WinApi.WS_POPUP | _C_WinApi.WS_CLIPSIBLINGS | _C_WinApi.WS_CLIPCHILDREN

def _get_window_extended_style_draw_area_only():
    """
    Returns : int
    """
    return _C_WinApi.WS_EX_APPWINDOW

def _make_area_from_rect(rect):
    """
    rect : C_WinApi.RECT
    """
    return Area(rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top)


def _get_window_area(window_handle):
    """
    window_handle   : C_WinApi.HWND
    Returns         : Area
    """
    rect = _C_WinApi.RECT()

    if _C_WinApi.GetWindowRect(window_handle, _ctypes.byref(rect)):
        return _make_area_from_rect(rect)
    
    return Area(0, 0, 0, 0)

def _get_window_area_from_draw_area(draw_area, window_style):
    """
    draw_area       : Area
    window_style    : int
    Returns         : Area
    """
    draw_area = draw_area.get_area_i()
    rect = _C_WinApi.RECT(
        draw_area.x,
        draw_area.y,
        draw_area.x + draw_area.width,
        draw_area.y + draw_area.height
    )

    _C_WinApi.AdjustWindowRect(_ctypes.byref(rect), window_style, _C_WinApi.FALSE)

    return _make_area_from_rect(rect)

def _mk_to_str(mk_code):
    """
    mk_code : int
    Returns : str
    """
    text = ""
    if mk_code & _C_WinApi.MK_LBUTTON:  text += "MK_LBUTTON "
    if mk_code & _C_WinApi.MK_RBUTTON:  text += "MK_RBUTTON "
    if mk_code & _C_WinApi.MK_SHIFT:    text += "MK_SHIFT "
    if mk_code & _C_WinApi.MK_CONTROL:  text += "MK_CONTROL "
    if mk_code & _C_WinApi.MK_MBUTTON:  text += "MK_MBUTTON "
    if mk_code & _C_WinApi.MK_XBUTTON1: text += "MK_XBUTTON1 "
    if mk_code & _C_WinApi.MK_XBUTTON2: text += "MK_XBUTTON2 "
    if len(text) > 0: text = text[:-1]
    return text

def _window_proc(window_handle, window_message, w_param, l_param):
    try:
        return to_window()._window_proc(window_handle, window_message, w_param, l_param)
    except SystemExit as e:
        if to_special_debug().is_full_exit_track_in_callback:
            _logging.exception("From _window_proc callback.")
        else:
            print("SystemExit: %d" % e.code)
        _os._exit(e.code)
    except Exception as e:
        _logging.exception("")
        _os._exit(1)

_c_window_proc = _C_WinApi.WNDPROC(_window_proc)
