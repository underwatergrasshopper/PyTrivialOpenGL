import ctypes   as _ctypes
import enum     as _enum
import os       as _os
import logging  as _logging
import re       as _re

from . import _C_WinApi
from . import _C_WGL
from . import _C_GL
from . import Key

from ._SingletonGuardian    import _SingletonGuardian
from ._WindowAreaCorrector  import _WindowAreaCorrector
from .Point                 import Point
from .Size                  import Size
from .Area                  import Area
from .Utility               import *
from .Log                   import *
from .SpecialDebug          import *
from .Key                   import *
from .Key                   import _VirtualKeyData, _vk_code_to_key_id, _vk_code_to_str, _is_mouse_button_down, _get_keyboard_side_id, _get_mouse_key_id, _is_mw_mouse_button, _is_mw_mouse_button_x

from . import _Basics
from ._Basics import clamp as _clamp
from ._Basics import is_i32 as _is_i32
from ._Basics import is_u16 as _is_u16
from ._Basics import _MIN_I32, _MAX_I32, _MAX_U16, _MIN_U16

from ._Debug import _wm_to_str


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

    _dbg_code_utf32             : int
    _code_utf32                 : int
    _is_two_utf16_code_units    : bool
    _is_decode_fail             : bool

    _do_on_create               : Callable[[], NoneType]
        Called right after window is created.

    _do_on_create               : Callable[[], NoneType]
        Called right before window is closed.

    _draw                       : Callable[[], NoneType]
        Called each time when window content needs to be redrawn.

    _do_on_key                  : Callable[[KeyId, bool, KeyExtra], NoneType]
        Call naming convention: do_on_key(key_id, is_down, extra).
        Called when window receive keyboard key or mouse button message.
        is_down          - true when key is down, false when key is up.
        extra            - Contains additional informations, like: 
                           cursor position in draw area (extra.x, extra.y), 
                           indicator if pressed key is left or right or doesn't matter (extra.keyboard_side_id).

    _do_on_text                 : Callable[[str, bool], NoneType]
        Call naming convention: do_on_text(text, is_correct).
        Called when window receive character message (from keyboard single key or key combination).
        text            - Text received from keyboard. At least one character.
        is_correct      - True - if there was no decoding error.

    _do_on_mouse_wheel_roll     : Callable[[int, int, int], NoneType]
        Call naming convention: do_on_mouse_wheel_roll(step_count, x, y).
        Called when mouse wheel is rolled.
        step_count      - Number of wheel rotation steps. 
                          Positive number if away from user. 
                          Negative number if towards user.
        x, y            - Cursor position in draw area.

    _do_on_mouse_move           : Callable[[int, int], NoneType]
        Call naming convention: do_on_mouse_move(x, y).
        Called when cursor change position in draw area.
        x, y            - Cursor position in draw area.

    _do_on_resize               : Callable[[], NoneType]
        Call naming convention: do_on_resize(width, height).
        Called each time window resize.
        width           - Width of draw area.
        height          - Height of draw area.

    _do_on_state_change         : Callable[[WindowStateId], NoneType]
        Call naming convention: do_on_state_change(state_id).
        Called each time when window state change.

    _do_on_show                 : Callable[[], NoneType]
        Called when window is about to show.

    _do_on_hide                 : Callable[[], NoneType]
        Called when window is about to hide.

    _do_on_foreground           : Callable[[bool], NoneType]
        Call naming convention: do_on_foreground(is_gain).
        Called when window goes to foreground (gain keyboard focus or is activated).
        is_gain         - True  - when window goes to foreground,
                          False - when window loses foreground position.

    _do_on_time                 : Callable[[int], NoneType]
        Call naming convention: do_on_time(time_interval).
        Called periodically. Call delay is taken from timer_time_interval variable and is provided as time_interval parameter.
        time_interval   - in milliseconds
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

        # character decoding
        self._dbg_code_utf32                = 0
        self._code_utf32                    = 0
        self._is_two_utf16_code_units       = False
        self._is_decode_fail                = False

        ### callbacks ###

        self._do_on_create                  = None
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

            do_on_key                = None,
            do_on_text               = None,
            
            do_on_mouse_wheel_roll   = None,
            do_on_mouse_move         = None,
            
            do_on_resize             = None,
            
            do_on_state_change       = None,
            do_on_show               = None,
            do_on_hide               = None,
            do_on_foreground         = None,
            
            do_on_time               = None,
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

        do_on_create                : Callable[[], NoneType]
            Called right after window is created.

        do_on_create                : Callable[[], NoneType]
            Called right before window is closed.

        draw                        : Callable[[], NoneType]
            Called each time when window content needs to be redrawn.

        do_on_key                   : Callable[[KeyId, bool, KeyExtra], NoneType]
            Call naming convention: do_on_key(key_id, is_down, extra).
            Called when window receive keyboard key or mouse button message.
            is_down          - true when key is down, false when key is up.
            extra            - Contains additional informations, like: 
                               cursor position in draw area (extra.x, extra.y), 
                               indicator if pressed key is left or right or doesn't matter (extra.keyboard_side_id).

        do_on_text                  : Callable[[str, bool], NoneType]
            Call naming convention: do_on_text(text, is_correct).
            Called when window receive character message (from keyboard single key or key combination).
            text            - Text received from keyboard. At least one character.
            is_correct      - True - if there was no decoding error.

        do_on_mouse_wheel_roll      : Callable[[int, int, int], NoneType]
            Call naming convention: do_on_mouse_wheel_roll(step_count, x, y).
            Called when mouse wheel is rolled.
            step_count      - Number of wheel rotation steps. 
                              Positive number if away from user. 
                              Negative number if towards user.
            x, y            - Cursor position in draw area.

        do_on_mouse_move            : Callable[[int, int], NoneType]
            Call naming convention: do_on_mouse_move(x, y).
            Called when cursor change position in draw area.
            x, y            - Cursor position in draw area.

        do_on_resize                : Callable[[], NoneType]
            Call naming convention: do_on_resize(width, height).
            Called each time window resize.
            width           - Width of draw area.
            height          - Height of draw area.

        do_on_state_change          : Callable[[WindowStateId], NoneType]
            Call naming convention: do_on_state_change(state_id).
            Called each time when window state change.

        do_on_show                  : Callable[[], NoneType]
            Called when window is about to show.

        do_on_hide                  : Callable[[], NoneType]
            Called when window is about to hide.

        do_on_foreground            : Callable[[bool], NoneType]
            Call naming convention: do_on_foreground(is_gain).
            Called when window goes to foreground (gain keyboard focus or is activated).
            is_gain         - True  - when window goes to foreground,
                              False - when window loses foreground position.

        do_on_time                  : Callable[[int], NoneType]
            Call naming convention: do_on_time(time_interval).
            Called periodically. Call delay is taken from timer_time_interval variable and is provided as time_interval parameter.
            time_interval   - in milliseconds
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

        if opengl_version is None:
            self._opengl_version = OpenGL_Version(1, 1)
        elif isinstance(opengl_version, OpenGL_Version):
            self._opengl_version = opengl_version
        elif isinstance(opengl_version, tuple):
            if len(opengl_version) == 2:
                self._opengl_version = OpenGL_Version(opengl_version[0], opengl_version[1])
            else:
                raise ValueError("Wrong number of values in parameter 'opengl_version'. Should be 2.") 
        else:
            TypeError("Wrong type of parameter 'opengl_version'. Should be 'Tuple[int, int]' or 'OpenGL_Version'.")

        self._icon_file_name            = icon_file_name
        self._timer_time_interval       = timer_time_interval
        self._is_auto_sleep_blocked     = is_auto_sleep_blocked

        ### callbacks ###

        self._do_on_create              = do_on_create
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

        _C_WinApi.ShowWindow(self._window_handle, _C_WinApi.SW_SHOW)
        _C_WinApi.SetForegroundWindow(self._window_handle)
        _C_WinApi.SetFocus(self._window_handle)

        self._change_area(self._area)

        if self._do_on_create is not None:
            self._do_on_create()

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
        """
        Moves window to new position.
        Calling convention:
            move_to(10, 30)                                     - Moves to new position.
            move_to(x = 10)                                     - Moves to new position only at X axis.
            move_to(y = 10)                                     - Moves to new position only at Y axis.
            move_to(10, 30, is_draw_area = True)                - Moves left-top corner of draw area to new position. 
            move_to(pos = Point(10, 30))                        - Moves to new position.
            move_to(pos = Point(10, 30), is_draw_area = True)   - Moves left-top corner of draw area to new position. 

        x               : int | None
            New position in screen coordinate system in X axis.
        y               : int | None
            New position in screen coordinate system in Y axis.
        pos             : Point | None
            New position in screen coordinate system.
        is_draw_area    : bool
            If True, then new position of window corresponding to left-top corner of draw area.
            (default) If False, then new position of window corresponding to left-top corner of window.
        """
        if x is not None and not _is_i32(x):
            raise ValueError("Argument 'x' is out of range for 32 bit integer.")
        if y is not None and not _is_i32(y):
            raise ValueError("Argument 'y' is out of range for 32 bit integer.")
        if pos is not None:
            if not isinstance(pos, Point):
                raise TypeError("Type of argument 'pos' is not 'Point'.")
            if not _is_i32(pos.x):
                raise ValueError("Value 'x' of argument 'pos' is out of range for 32 bit integer.")
            if not _is_i32(pos.y):
                raise ValueError("Value 'y' of argument 'pos' is out of range for 32 bit integer.")

        if pos is not None:
            area = Area(pos.x, pos.y, 0, 0)

        elif (x is not None) and (y is not None):
            area = Area(x, y, 0, 0)

        else:
            if is_draw_area:
                pos = self.get_draw_area_pos()
            else:
                pos = self.get_pos()

            if x is None: x = pos.x
            if y is None: y = pos.y

            area = Area(x, y, 0, 0)

        self._set_area(area, _WindowAreaPartId.POSITION, is_draw_area)

    def move_by(self, offset_x = None, offset_y = None, offset = None):
        """
        Moves window by offset
        Calling convention:
            move_by(10, 30)                                     - Moves by (10, 30). 
            move_by(offset_x = 10)                              - Moves by 10 only on X axis.
            move_by(offset_y = 10)                              - Moves by 10 only on Y axis.
            move_by(offset = Point(10, 30))                     - Moves by (10, 30). 
        offset_x    : int | None
            Offset in screen coordinate system at X axis.
        offset_y    : int | None
            Offset in screen coordinate system at Y axis.
        offset      : Point | None
            Offset in screen coordinate system.
        """
        if offset_x is not None and not _is_i32(offset_x):
            raise ValueError("Argument 'offset_x' is out of range for 32 bit integer.")
        if offset_y is not None and not _is_i32(offset_y):
            raise ValueError("Argument 'offset_y' is out of range for 32 bit integer.")
        if offset is not None:
            if not isinstance(offset, Point):
                raise TypeError("Type of argument 'offset' is not 'Point'.")
            if not _is_i32(offset.x):
                raise ValueError("Value 'x' of argument 'offset' is out of range for 32 bit integer.")
            if not _is_i32(offset.y):
                raise ValueError("Value 'y' of argument 'offset' is out of range for 32 bit integer.")

        if offset is not None:
            area = Area(offset.x, offset.y, 0, 0)

        elif (offset_x is not None) and (offset_y is not None):
            area = Area(offset_x, offset_y, 0, 0)

        else:
            if offset_x is None: offset_x = 0
            if offset_y is None: offset_y = 0

            area = Area(offset_x, offset_y, 0, 0)

        self._set_area(area, _WindowAreaPartId.POSITION_OFFSET, False)

    def resize(self, width = None, height = None, size = None, is_draw_area = False):
        """
        Moves window to new position.
        Calling convention:
            resize(100, 300)                                    - Changes both width and height of window.
            resize(width = 100)                                 - Changes only width of window.
            resize(height = 100)                                - Changes only height of window.
            resize(100, 300, is_draw_area = True)               - Changes both width and height of window's draw area.
            resize(size = Size(100, 300))                       - Changes both width and height of window.
            resize(size = Size(100, 300), is_draw_area = True)  - Changes both width and height of window's draw area.
        width           : int | None
            New width in screen coordinate system.
        height          : int | None
            New height in screen coordinate system.
        size            : Point | None
            New size in screen coordinate system.
        is_draw_area    : bool
            If True, then draw area of window is resized.
            (default) If False, then window is resized.
        """
        if width is not None and not _is_u16(width):
            raise ValueError("Argument 'width' is out of range for 16 bit unsigned integer.")
        if height is not None and not _is_u16(height):
            raise ValueError("Argument 'height' is out of range for 16 bit unsigned integer.")
        if size is not None:
            if not isinstance(size, Size):
                raise TypeError("Type of argument 'size' is not 'Size'.")
            if not _is_u16(size.width):
                raise ValueError("Value 'width' of argument 'size' is out of range for 16 bit unsigned integer.")
            if not _is_u16(size.height):
                raise ValueError("Value 'height' of argument 'size' is out of range for 16 bit unsigned integer.")

        if size is not None:
            area = Area(0, 0, size.width, size.height)

        elif (width is not None) and (height is not None):
            area = Area(0, 0, width, height)

        else:
            if is_draw_area:
                size = self.get_draw_area_size()
            else:
                size = self.get_size()

            if width is None:   width   = size.width
            if height is None:  height  = size.height

            area = Area(0, 0, width, height)

        self._set_area(area, _WindowAreaPartId.SIZE, is_draw_area)

    # TODO:
    # Resize
    # SetArea / Reshape
    # Center

    ###

    def get_x(self):
        """
        Returns (int).
        """
        return self.get_area().x

    def get_y(self):
        """
        Returns (int).
        """
        return self.get_area().y

    def get_width(self):
        """
        Returns (int).
        """
        return self.get_area().width

    def get_height(self):
        """
        Returns (int).
        """
        return self.get_area().height

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

    def get_draw_area_x(self):
        """
        Returns (int).
        """
        return self.get_draw_area().x

    def get_draw_area_y(self):
        """
        Returns (int).
        """
        return self.get_draw_area().y

    def get_draw_area_width(self):
        """
        Returns (int).
        """
        return self.get_draw_area().width

    def get_draw_area_height(self):
        """
        Returns (int).
        """
        return self.get_draw_area().height

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
        """
        Returns (Area).
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
            if self.is_windowed_full_screen():
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

    def get_cursor_pos_in_draw_area(self):
        pos = _C_WinApi.POINT()
        if _C_WinApi.GetCursorPos(_ctypes.byref(pos)) and _C_WinApi.ScreenToClient(self._window_handle, _ctypes.byref(pos)):
            return Point(pos.x, pos.y)
        return Point(0, 0)

    # TODO:
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
                    

        return _C_WinApi.EXIT_FAILURE


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

            window_area = self._window_area_corrector.remove_invisible_frame_from_area(window_area_with_invisible_frame, self._window_handle);

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

    def _handle_do_on_mouse_key(self, window_message, w_param, l_param):
        """
        window_message  : int
        w_param         : int
        l_param         : int
        """
        is_down = _is_mouse_button_down(window_message)

        if self._do_on_key:
            key_id = _get_mouse_key_id(window_message, w_param);

            extra = KeyExtra(
                count               = 1,
                x                   = _C_WinApi.GET_X_LPARAM(l_param).value,
                y                   = _C_WinApi.GET_Y_LPARAM(l_param).value,
                keyboard_side_id    = KeyboardSideId.NONE
            )
            self._do_on_key(key_id, is_down, extra);
        
        # Tracks mouse button up message when mouse button is down and cursor leave window draw (client) area.
        if is_down:
            _C_WinApi.SetCapture(self._window_handle)
        elif _C_WinApi.GetCapture() == self._window_handle:
            _C_WinApi.ReleaseCapture()

    def _handle_do_on_keybard_key(self, is_down, w_param, l_param):
        """
        is_down : bool
        w_param : int
        l_param : int
        """
        if self._do_on_key:
            vk_data = _VirtualKeyData(l_param)
            key_id = _vk_code_to_key_id(w_param)

            pos = self.get_cursor_pos_in_draw_area()

            extra = KeyExtra(
                count = vk_data.count,
                x = pos.x,
                y = pos.y,
                keyboard_side_id = _get_keyboard_side_id(key_id, vk_data),
            )
            self._do_on_key(key_id, is_down, extra)

    def _set_state(self, state_id):
        """
        state_id : WindowStateId
        """
        self._prev_state_id = self._state_id
        self._state_id      = state_id

        if (self._state_id != self._prev_state_id) and self._do_on_state_change:
           self._do_on_state_change(state_id)

    def _create(self, window_handle):
        """
        window_handle : _C_WinApi.HWND
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
                _C_WGL.WGL_CONTEXT_FLAGS_ARB, _C_WGL.WGL_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB,
                0
            ]
            attribute_list = (_ctypes.c_int * len(attribute_list))(*(attribute for attribute in attribute_list))

            rendering_context_handle = wglCreateContextAttribsARB(self._device_context_handle, 0, attribute_list)
            if not rendering_context_handle:
                log_fatal_error("Can not create OpenGl Rendering Context for version %d.%d." % (self._opengl_version.major, self._opengl_version.minor))
            

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
            self._opengl_version = OpenGL_Version(major, minor)

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

    def _destroy(self):
        if self._do_on_destroy:
            self._do_on_destroy()

        _C_WGL.wglMakeCurrent(_C_WinApi.NULL, _C_WinApi.NULL)
        _C_WGL.wglDeleteContext(self._rendering_context_handle)
        self._rendering_context_handle = _C_WinApi.NULL

        _C_WinApi.ReleaseDC(self._window_handle, self._device_context_handle);
        self._device_context_handle = _C_WinApi.NULL

        _C_WinApi.PostQuitMessage(0)


    def _window_proc(self, window_handle, window_message, w_param, l_param):
        """
        window_handle   : HWND
        window_message  : UINT
        w_param         : WPARAM
        l_param         : LPARAM
        """

        ### Draw ###

        if window_message == _C_WinApi.WM_PAINT:
            if to_special_debug().is_notify_any_message:
                log_debug("WM_PAINT")

            self.draw_now()
            _C_WinApi.ValidateRect(self._window_handle, _C_WinApi.NULL)
            return 0
        
        elif window_message == _C_WinApi.WM_ERASEBKGND:
            if to_special_debug().is_notify_any_message:
                log_debug("WM_ERASEBKGND")
            # Tells DefWindowProc to not erase background. It's unnecessary since background is handled by OpenGL.
            return 1
        
        ## Mouse ###
        
        elif window_message == _C_WinApi.WM_MOUSEMOVE:
            if to_special_debug().is_notify_mouse_move or to_special_debug().is_notify_any_message:
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
        
        elif _is_mw_mouse_button(window_message):
            if is_log_level_at_least(LogLevel.DEBUG):
                wm_text = _wm_to_str(window_message)
        
                xb_text = ""
                if _is_mw_mouse_button_x(window_message):
                    if      _C_WinApi.HIWORD(w_param).value == _C_WinApi.XBUTTON1: xb_text = " XBUTTON1"
                    elif    _C_WinApi.HIWORD(w_param).value == _C_WinApi.XBUTTON2: xb_text = " XBUTTON2"
        
                x       = _C_WinApi.GET_X_LPARAM(l_param).value 
                y       = _C_WinApi.GET_Y_LPARAM(l_param).value 
                mk_text = _mk_to_str(_C_WinApi.LOWORD(w_param).value)
        
                log_debug("%-20s:%s %d %d %s" % (wm_text, xb_text, x, y, mk_text))
        
            self._handle_do_on_mouse_key(window_message, w_param, l_param)
            return 0
        
        ### Keyboard ###
        
        elif window_message in [_C_WinApi.WM_KEYDOWN, _C_WinApi.WM_KEYUP, _C_WinApi.WM_SYSKEYDOWN, _C_WinApi.WM_SYSKEYUP]:
            if to_special_debug().is_notify_key_message or to_special_debug().is_notify_any_message:
                wm_text = _wm_to_str(window_message)
                vk_text = _vk_code_to_str(w_param)
                vk_data = _VirtualKeyData(l_param)
        
                log_debug("%-20s: %-13s %s" % (wm_text, vk_text, vk_data))
        
            is_down = window_message in [_C_WinApi.WM_KEYDOWN, _C_WinApi.WM_SYSKEYDOWN]
        
            self._handle_do_on_keybard_key(is_down, w_param, l_param)
            return 0
        
        elif window_message == _C_WinApi.WM_CHAR:
            if to_special_debug().is_notify_character_message or to_special_debug().is_notify_any_message:
                wm_text = "WM_CHAR"
                vk_data = _VirtualKeyData(l_param)
                
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
            if to_special_debug().is_notify_timer or to_special_debug().is_notify_any_message:
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

                log_debug("%-20s: %s %s" % (wm_text, visibility_text, status_name))

            is_visible = (w_param == _C_WinApi.TRUE)

            if is_visible != self._is_visible:
                self._is_visible = is_visible

                if self._is_visible and self._do_on_show:
                    self._do_on_show()
                elif (not self._is_visible) and self._do_on_hide:
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

                log_debug("%-20s:%s %s%s" % (wm_text, minimized_text, activation_state_name, transition_text))

            if is_active != self._is_active:
                self._is_active = is_active

                if self._do_on_foreground:
                    self._do_on_foreground(is_active)

            return 0

        elif window_message == _C_WinApi.WM_SYSCOMMAND:
            if is_log_level_at_least(LogLevel.DEBUG):
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

        elif window_message == _C_WinApi.WM_CLOSE:
            if is_log_level_at_least(LogLevel.DEBUG):
                log_debug("WM_CLOSE")

            _C_WinApi.DestroyWindow(window_handle)
            return 0

        elif window_message == _C_WinApi.WM_DESTROY:
            if is_log_level_at_least(LogLevel.DEBUG):
                log_debug("WM_DESTROY")

            self._destroy()
            return 0

        else:
            if to_special_debug().is_notify_any_message:
                log_debug(_wm_to_str(window_message))

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
    draw_area       : Area
    window_style    : int
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

def _mk_to_str(mk_code):
    """
    mk_code : int
    Returns (str).
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
