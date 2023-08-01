from msilib.schema import Icon
from PyTrivialOpenGL._Private.C_WinApi import *
from PyTrivialOpenGL._Private.C_WGL import *
from PyTrivialOpenGL.C_GL import *
from PyTrivialOpenGL.Utility import *
from PyTrivialOpenGL.Key import *
from PyTrivialOpenGL._Private.KeySupport import *
from PyTrivialOpenGL._Private.Debug import wm_to_str as _wm_to_str
from PyTrivialOpenGL._Private.WindowAreaCorrector import WindowAreaCorrector as _WindowAreaCorrector

from ctypes import *
from ..utility.ExampleManager import ExampleManager
import time
import os
import re

__all__ = ["run"]

def run(name, options):
    def rect_to_str(r):
        return "%d %d %d %d" % (r.left, r.top, r.right, r.bottom)

    def rect_diff(a, b):
        return RECT(a.left - b.left, a.top - b.top, a.right - b.right, a.bottom - b.bottom)

    ### Window Function Scenarios ####
    width   = GetSystemMetrics(SM_CXSCREEN)
    height  = GetSystemMetrics(SM_CYSCREEN)
    print(width, height)

    rc = RECT()
    if not SystemParametersInfoW(SPI_GETWORKAREA, 0, byref(rc), 0):
        print("Error Code: %d" % GetLastError())
    print(rc.left, rc.top, rc.right, rc.bottom)

    NOT_WORKING_CODE = 11111111
    if not SystemParametersInfoW(NOT_WORKING_CODE, 0, None, 0):
        print("Error Code: %d" % GetLastError())
        print(FormatError(GetLastError()))
        

    window_handle = GetForegroundWindow()
    print(window_handle)

    window_rect = RECT()
    GetWindowRect(window_handle, byref(window_rect))
    print(rect_to_str(window_rect))

    actual_window_rect = RECT()
    DwmGetWindowAttribute(window_handle, DWMWA_EXTENDED_FRAME_BOUNDS, byref(actual_window_rect), sizeof(RECT))
    print(rect_to_str(actual_window_rect))
    print(rect_to_str(rect_diff(actual_window_rect, window_rect)))

    client_rect = RECT()
    GetClientRect(window_handle, byref(client_rect))
    print(rect_to_str(client_rect))

    points = cast(byref(client_rect), LPPOINT)

    ClientToScreen(window_handle, points)
    ClientToScreen(window_handle, byref(points[1]))

    print(rect_to_str(client_rect))

    ScreenToClient(window_handle, points)
    ScreenToClient(window_handle, byref(points[1]))

    print(rect_to_str(client_rect))

    ### get window name ###

    num_of_chars = GetWindowTextLengthW(window_handle)
    length = num_of_chars + 1
    buffer = (c_wchar * length)()
    GetWindowTextW(window_handle, buffer, length)

    window_name = cast(buffer, c_wchar_p).value
    print(window_name)

    this_window_handle = window_handle

    ### 

    window_handle = FindWindowW(None, "Untitled - Notepad")
    if window_handle:
        if not SetForegroundWindow(window_handle):
            print(FormatError(GetLastError()))
        
        print("Window 'Untitled - Notepad' moved to foreground.")

    window_handle = FindWindowW(None, "*Untitled - Notepad")
    if window_handle:
        if not SetForegroundWindow(window_handle):
            print(FormatError(GetLastError()))
        
        print("Focused on '*Untitled - Notepad'.")

    if not SetWindowLongPtrW(window_handle, GWL_STYLE, WS_POPUPWINDOW):
        print(FormatError(GetLastError()))

    pos = POINT()
    GetCursorPos(byref(pos))
    print("%d %d" % (pos.x, pos.y))

    SetWindowPos(this_window_handle, HWND_TOP, 0, 0, 1200, 600, SWP_NOMOVE)

    ###

    if "min_max" in options:
        assert IsMaximized(this_window_handle) == False
        assert IsMinimized(this_window_handle) == False

        ShowWindow(this_window_handle, SW_MINIMIZE)

        assert IsMaximized(this_window_handle) == False
        assert IsMinimized(this_window_handle) == True

        time.sleep(0.2)

        ShowWindow(this_window_handle, SW_MAXIMIZE)

        assert IsMaximized(this_window_handle) == True
        assert IsMinimized(this_window_handle) == False

        time.sleep(0.2)

        ShowWindow(this_window_handle, SW_SHOWNORMAL)
    
        assert IsMaximized(this_window_handle) == False
        assert IsMinimized(this_window_handle) == False

    ### Macro Check ###
    if sizeof(c_void_p) == 4:
        assert ULONG is ULONG_PTR
    else:
        assert ULONG is not ULONG_PTR

    i = MAKEINTRESOURCEW(0x12345678)
    p = cast(byref(i), POINTER(c_short))
    assert p[0] == 0x5678

    assert HIWORD(0x12345678).value == 0x1234
    assert LOWORD(0x12345678).value == 0x5678

    assert GET_X_LPARAM(0xFF12FF34).value == -204
    assert GET_Y_LPARAM(0xFF12FF34).value == -238

    assert GET_WHEEL_DELTA_WPARAM(0xFF12FF34).value == -238
    assert GET_KEYSTATE_WPARAM(0x12345678).value == 0x5678

    ###

    print("Work Area: %s" % get_work_area())
    print("Screen Size: %s" % get_screen_size())
    print("Cursor Pos. in Screen: %s" % get_cursor_pos_in_screen())

    ###

    print("is caps lock toggled:", is_key_toggled(KeyId.CAPS_LOCK))
    print("is insert toggled:", is_key_toggled(KeyId.INSERT))



    return 0