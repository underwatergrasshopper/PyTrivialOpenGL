"""
Contains selected macros and functions of WinApi.
And also type and macro dependent constants.
"""

import sys      as _sys
import ctypes   as _ctypes

# This module and modules imported below are logically part of one module.
from .Constants     import *
from .Types         import *

### Libraries ###

_Kernel32   = _ctypes.windll.Kernel32
_User32     = _ctypes.windll.User32
_Dwmapi     = _ctypes.windll.Dwmapi
_Gdi32      = _ctypes.windll.Gdi32

###

_IS_64_BIT = _sys.maxsize > 2**32

### Constants - type dependent  ###

# SetWindowPos, hWndInsertAfter
HWND_TOP                = HWND(0)
HWND_BOTTOM             = HWND(1)
HWND_TOPMOST            = HWND(-1)
HWND_NOTOPMOST          = HWND(-2)

### Macros ###

def MAKEINTRESOURCEW(i):
    return LPWSTR(ULONG_PTR(WORD(i).value).value)

def LOWORD(l):
    return WORD(DWORD_PTR(l).value & 0xFFFF)

def HIWORD(l):
    return WORD((DWORD_PTR(l).value >> 16) & 0xFFFF)

def GET_X_LPARAM(lp):
    return _ctypes.c_int(_ctypes.c_short(LOWORD(lp).value).value)

def GET_Y_LPARAM(lp):
    return _ctypes.c_int(_ctypes.c_short(HIWORD(lp).value).value)

def GET_WHEEL_DELTA_WPARAM(wParam):
    return _ctypes.c_short(HIWORD(wParam).value)

def GET_KEYSTATE_WPARAM(wParam):
    return LOWORD(wParam)

def IsMinimized(hwnd):
    return IsIconic(hwnd)

def IsMaximized(hwnd):
    return IsZoomed(hwnd)

### Constants - macro dependent  ###

IDC_ARROW               = MAKEINTRESOURCEW(32512)

### Functions ###

GetLastError            = _ctypes.WINFUNCTYPE(DWORD)(
    ("GetLastError", _Kernel32), 
    ()
)

GetModuleHandleW        = _ctypes.WINFUNCTYPE(HMODULE, LPCWSTR)(
    ("GetModuleHandleW", _Kernel32), 
    ((1, "lpModuleName"), )
)

GetSystemMetrics        = _ctypes.WINFUNCTYPE(_ctypes.c_int, _ctypes.c_int)(
    ("GetSystemMetrics", _User32), 
    ((1, "nIndex"), )
)

SystemParametersInfoW   = _ctypes.WINFUNCTYPE(BOOL, UINT, UINT, PVOID, UINT)(
    ("SystemParametersInfoW", _User32), 
    ((1, "uiAction"), (1, "uiParam"), (1, "pvParam"), (1, "fWinIni"))
)

### Functions - Window ###

GetForegroundWindow     = _ctypes.WINFUNCTYPE(HWND)(
    ("GetForegroundWindow", _User32), 
    ()
)

SetForegroundWindow     = _ctypes.WINFUNCTYPE(BOOL, HWND)(
    ("SetForegroundWindow", _User32), 
    ((1, "hWnd"),)
)

SetFocus                = _ctypes.WINFUNCTYPE(HWND, HWND)(
    ("SetFocus", _User32), 
    ((1, "hWnd"),)
)

FindWindowW             = _ctypes.WINFUNCTYPE(HWND, LPCWSTR, LPCWSTR)(
    ("FindWindowW", _User32), 
    ((1, "lpClassName", None), (1, "lpWindowName", None))
)

GetActiveWindow         = _ctypes.WINFUNCTYPE(HWND)(
    ("GetActiveWindow", _User32), 
    ()
)

GetWindow               = _ctypes.WINFUNCTYPE(HWND, HWND, UINT)(
    ("GetWindow", _User32), 
    ((1, "hWnd"), (1, "uCmd"))
)

GetWindowTextLengthW    = _ctypes.WINFUNCTYPE(_ctypes.c_int, HWND)(
    ("GetWindowTextLengthW", _User32), 
    ((1, "hWnd"),)
)

GetWindowTextW          = _ctypes.WINFUNCTYPE(_ctypes.c_int, HWND, LPWSTR, _ctypes.c_int)(
    ("GetWindowTextW", _User32), 
    ((1, "hWnd"), (1, "lpString"), (1, "nMaxCount"))
)

GetWindowRect           = _ctypes.WINFUNCTYPE(BOOL, HWND, LPRECT)(
    ("GetWindowRect", _User32), 
    ((1, "hWnd"), (1, "lpRect"))
)

GetClientRect           = _ctypes.WINFUNCTYPE(BOOL, HWND, LPRECT)(
    ("GetClientRect", _User32), 
    ((1, "hWnd"), (1, "lpRect"))
)

DwmGetWindowAttribute   = _ctypes.WINFUNCTYPE(HRESULT, HWND, DWORD, PVOID, DWORD)(
    ("DwmGetWindowAttribute", _Dwmapi), 
    ((1, "hwnd"), (1, "dwAttribute"), (1, "pvAttribute"), (1, "cbAttribute"))
)

ClientToScreen          = _ctypes.WINFUNCTYPE(BOOL, HWND, LPPOINT)(
    ("ClientToScreen", _User32), 
    ((1, "hWnd"), (1, "lpPoint"))
)

ScreenToClient          = _ctypes.WINFUNCTYPE(BOOL, HWND, LPPOINT)(
    ("ScreenToClient", _User32), 
    ((1, "hWnd"), (1, "lpPoint"))
)

SetWindowLongW          = _ctypes.WINFUNCTYPE(LONG, HWND, _ctypes.c_int, LONG)(
    ("SetWindowLongW", _User32), 
    ((1, "hWnd"), (1, "nIndex"), (1, "dwNewLong"))
)

if _IS_64_BIT:
    SetWindowLongPtrW   = _ctypes.WINFUNCTYPE(LONG_PTR, HWND, _ctypes.c_int, LONG_PTR)(
        ("SetWindowLongPtrW", _User32), 
        ((1, "hWnd"), (1, "nIndex"), (1, "dwNewLong"))
    )
else:
    SetWindowLongPtrW = SetWindowLongW 

SetWindowLongW          = _ctypes.WINFUNCTYPE(LONG, HWND, _ctypes.c_int, LONG)(
    ("SetWindowLongW", _User32), 
    ((1, "hWnd"), (1, "nIndex"), (1, "dwNewLong"))
)

SetWindowPos            = _ctypes.WINFUNCTYPE(BOOL, HWND, HWND, _ctypes.c_int, _ctypes.c_int, _ctypes.c_int, _ctypes.c_int, UINT)(
    ("SetWindowPos", _User32), 
    ((1, "hWnd"), (1, "hWndInsertAfter"), (1, "X"), (1, "Y"), (1, "cx"), (1, "cy"), (1, "uFlags"))
)

AdjustWindowRectEx      = _ctypes.WINFUNCTYPE(BOOL, LPRECT, DWORD, BOOL, DWORD)(
    ("AdjustWindowRectEx", _User32), 
    ((1, "lpRect"), (1, "dwStyle"), (1, "bMenu"), (1, "dwExStyle"))
)

AdjustWindowRect        = _ctypes.WINFUNCTYPE(BOOL, LPRECT, DWORD, BOOL)(
    ("AdjustWindowRect", _User32), 
    ((1, "lpRect"), (1, "dwStyle"), (1, "bMenu"))
)

IsZoomed                = _ctypes.WINFUNCTYPE(BOOL, HWND)(
    ("IsZoomed", _User32), 
    ((1, "hWnd"),)
)

IsIconic                = _ctypes.WINFUNCTYPE(BOOL, HWND)(
    ("IsIconic", _User32), 
    ((1, "hWnd"),)
)

ShowWindow              = _ctypes.WINFUNCTYPE(BOOL, HWND, _ctypes.c_int)(
    ("ShowWindow", _User32), 
    ((1, "hWnd"), (1, "nCmdShow"))
)

LoadCursorW             = _ctypes.WINFUNCTYPE(HCURSOR, HINSTANCE, LPCWSTR)(
    ("LoadCursorW", _User32), 
    ((1, "hInstance"), (1, "lpCursorName"))
)

LoadImageW             = _ctypes.WINFUNCTYPE(HANDLE, HINSTANCE, LPCWSTR, UINT, _ctypes.c_int, _ctypes.c_int, UINT)(
    ("LoadImageW", _User32), 
    ((1, "hInst"), (1, "name"), (1, "_type"), (1, "cx"), (1, "cy"), (1, "fuLoad"))
)

MessageBoxW            = _ctypes.WINFUNCTYPE(_ctypes.c_int, HWND, LPCWSTR, LPCWSTR, UINT)(
    ("MessageBoxW", _User32), 
    ((1, "hWnd", NULL), (1, "lpText", ""), (1, "lpCaption", ""), (1, "uType", 0))
)

# NOTE: This is not WinApi function! It's custom made function for purpose of _C_WinApi module.
def OwnerlessMessageBox_FromNewThreadWithWait(lpText, lpCaption, uType):
    """
    Function works 'pretty much' same as MessageBoxW. 
    In addition, is called from separate thread, and window handle of owner (hWnd) is ignored.
    Will wait until message box is closed (until thread finish).

    Warning! If called withing window message procedure, 
    then new messages (which are coming to the callee window) still can be stacked in the message queue, 
    even when current thread waits to this function to finish. 
    Their dispatching resumes after this function finish.
    
    lpText          : LPCWSTR
    lpCaption       : LPCWSTR
    uType           : UINT
    Returns (ctypes.c_int). Same result values as MessageBoxW. 
    """
    class ParameterPack(_ctypes.Structure):
        _fields_ = [
            ("lpText",      LPCWSTR),
            ("lpCaption",   LPCWSTR),
            ("uType",       UINT),
            ("iResult",     _ctypes.c_int),
        ]

    def ThreadFunction(param):
        pack = _ctypes.cast(param, _ctypes.POINTER(ParameterPack))[0]

        pack.iResult = MessageBoxW(NULL, pack.lpText, pack.lpCaption, pack.uType)
        return 0
    ThreadFunction = LPTHREAD_START_ROUTINE(ThreadFunction)

    pack = ParameterPack(lpText, lpCaption, uType, 0)

    thread_handle = CreateThread(NULL, 0, ThreadFunction, _ctypes.byref(pack), 0, NULL)
    WaitForSingleObject(thread_handle, INFINITE)

    return pack.iResult

###

RegisterClassExW        = _ctypes.WINFUNCTYPE(ATOM, _ctypes.POINTER(WNDCLASSEXW))(
    ("RegisterClassExW", _User32), 
    ((1, "lpwcx"), )
)

UnregisterClassW        = _ctypes.WINFUNCTYPE(BOOL, LPCWSTR, HINSTANCE)(
    ("UnregisterClassW", _User32), 
    ((1, "lpClassName"), (1, "hInstance"))
)

CreateWindowExW         = _ctypes.WINFUNCTYPE(HWND, DWORD, LPCWSTR, LPCWSTR, DWORD, _ctypes.c_int, _ctypes.c_int, _ctypes.c_int, _ctypes.c_int, HWND, HMENU, HINSTANCE, LPVOID)(
    ("CreateWindowExW", _User32), 
    (
        (1, "dwExStyle", 0), 
        (1, "lpClassName"), 
        (1, "lpWindowName"), 
        (1, "dwStyle", 0), 
        (1, "X", CW_USEDEFAULT), (1, "Y", CW_USEDEFAULT), (1, "nWidth", CW_USEDEFAULT), (1, "nHeight", CW_USEDEFAULT), 
        (1, "hWndParent", None), 
        (1, "hMenu", None), 
        (1, "hInstance"), 
        (1, "lpParam", 0)
    )
)

DestroyWindow           = _ctypes.WINFUNCTYPE(BOOL, HWND)(
    ("DestroyWindow", _User32), 
    ((1, "hWnd"), )
)

CloseWindow             = _ctypes.WINFUNCTYPE(BOOL, HWND)(
    ("CloseWindow", _User32), 
    ((1, "hWnd"), )
)

UpdateWindow            = _ctypes.WINFUNCTYPE(BOOL, HWND)(
    ("UpdateWindow", _User32), 
    ((1, "hWnd"), )
)

DefWindowProcW          = _ctypes.WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)(
    ("DefWindowProcW", _User32), 
    ((1, "hWnd"), (1, "Msg"), (1, "wParam"), (1, "lParam"))
)

GetMessageW             = _ctypes.WINFUNCTYPE(BOOL, _ctypes.POINTER(MSG), HWND, UINT, UINT)(
    ("GetMessageW", _User32), 
    ((1, "lpMsg"), (1, "hWnd"), (1, "wMsgFilterMin"), (1, "wMsgFilterMax"))
)

PeekMessageW            = _ctypes.WINFUNCTYPE(BOOL, _ctypes.POINTER(MSG), HWND, UINT, UINT, UINT)(
    ("PeekMessageW", _User32), 
    ((1, "lpMsg"), (1, "hWnd"), (1, "wMsgFilterMin"), (1, "wMsgFilterMax"), (1, "wRemoveMsg"))
)

TranslateMessage        = _ctypes.WINFUNCTYPE(BOOL, _ctypes.POINTER(MSG))(
    ("TranslateMessage", _User32), 
    ((1, "lpMsg"), )
)

DispatchMessageW        = _ctypes.WINFUNCTYPE(LRESULT, _ctypes.POINTER(MSG))(
    ("DispatchMessageW", _User32), 
    ((1, "lpMsg"), )
)

PostQuitMessage        = _ctypes.WINFUNCTYPE(None, _ctypes.c_int)(
    ("PostQuitMessage", _User32), 
    ((1, "nExitCode"), )
)

PostMessageW            = _ctypes.WINFUNCTYPE(BOOL, HWND, UINT, WPARAM, LPARAM)(
    ("PostMessageW", _User32), 
    ((1, "hWnd"), (1, "Msg"), (1, "wParam"), (1, "lParam"))
)

SendMessageW            = _ctypes.WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)(
    ("SendMessageW", _User32), 
    ((1, "hWnd"), (1, "Msg"), (1, "wParam"), (1, "lParam"))
)

GetQueueStatus          = _ctypes.WINFUNCTYPE(DWORD, UINT)(
    ("GetQueueStatus", _User32), 
    ((1, "flags"), )
)

WaitForSingleObject = _ctypes.WINFUNCTYPE(DWORD, HANDLE, DWORD)(
    ("WaitForSingleObject", _Kernel32), 
    ((1, "hHandle"), (1, "dwMilliseconds"))
)

MsgWaitForMultipleObjectsEx = _ctypes.WINFUNCTYPE(DWORD, DWORD, _ctypes.POINTER(HANDLE), DWORD, DWORD, DWORD)(
    ("MsgWaitForMultipleObjectsEx", _User32), 
    ((1, "nCount"), (1, "pHandles"), (1, "dwMilliseconds"), (1, "dwWakeMask"), (1, "dwFlags"))
)

InSendMessage           = _ctypes.WINFUNCTYPE(BOOL)(
    ("InSendMessage", _User32), 
    ()
)

ReplyMessage            = _ctypes.WINFUNCTYPE(BOOL, LRESULT)(
    ("ReplyMessage", _User32), 
    ((1, "lResult"), )
)

SetTimer                = _ctypes.WINFUNCTYPE(UINT_PTR, HWND, UINT_PTR, UINT, TIMERPROC)(
    ("SetTimer", _User32), 
    ((1, "hWnd"), (1, "nIDEvent"), (1, "uElapse"), (1, "lpTimerFunc"))
)

### Functions - Mouse ###

GetCursorPos            = _ctypes.WINFUNCTYPE(BOOL, LPPOINT)(
    ("GetCursorPos", _User32), 
    ((1, "lpPoint"),)
)

SetCapture              = _ctypes.WINFUNCTYPE(HWND, HWND)(
    ("SetCapture", _User32), 
    ((1, "hWnd"),)
)

GetCapture              = _ctypes.WINFUNCTYPE(HWND)(
    ("GetCapture", _User32), 
    ()
)

ReleaseCapture          = _ctypes.WINFUNCTYPE(HWND)(
    ("ReleaseCapture", _User32), 
    ()
)

### Function - Keyboard ###

GetKeyState             = _ctypes.WINFUNCTYPE(SHORT, _ctypes.c_int)(
    ("GetKeyState", _User32), 
    ((1, "nVirtKey"),)
)

GetAsyncKeyState        = _ctypes.WINFUNCTYPE(SHORT, _ctypes.c_int)(
    ("GetAsyncKeyState", _User32), 
    ((1, "vKey"),)
)

MapVirtualKeyA          = _ctypes.WINFUNCTYPE(UINT, UINT, UINT)(
    ("MapVirtualKeyA", _User32), 
    ((1, "uCode"), (1, "uMapType"))
)

### Functions - Thread ###

CREATE_SUSPENDED                    = 0x00000004
STACK_SIZE_PARAM_IS_A_RESERVATION   = 0x00010000

class SECURITY_ATTRIBUTES(_ctypes.Structure):
    _fields_ = [
        ("nLength",                 DWORD),
        ("lpSecurityDescriptor",    LPVOID),
        ("bInheritHandle",          BOOL)
    ]

LPSECURITY_ATTRIBUTES   = _ctypes.POINTER(SECURITY_ATTRIBUTES)
LPTHREAD_START_ROUTINE  = _ctypes.WINFUNCTYPE(DWORD, LPVOID)


CreateThread            = _ctypes.WINFUNCTYPE(HANDLE, LPSECURITY_ATTRIBUTES, SIZE_T, LPTHREAD_START_ROUTINE, LPVOID, DWORD, LPDWORD)(
    ("CreateThread", _Kernel32), 
    (
        (1, "lpThreadAttributes"), 
        (1, "dwStackSize"), 
        (1, "lpStartAddress"), 
        (1, "lpParameter"), 
        (1, "dwCreationFlags"), 
        (1, "lpThreadId")
    )
)

### Functions - Rendering Context, Device Context ###

GetDC                   = _ctypes.WINFUNCTYPE(HDC, HWND)(
    ("GetDC", _User32), 
    ((1, "hWnd"), )
)

ReleaseDC               = _ctypes.WINFUNCTYPE(_ctypes.c_int, HWND, HDC)(
    ("ReleaseDC", _User32), 
    ((1, "hWnd"), (1, "hDC"), )
)

SwapBuffers             = _ctypes.WINFUNCTYPE(BOOL, HDC)(
    ("SwapBuffers", _Gdi32), 
    ((1, "hdc"),)
)

InvalidateRect          = _ctypes.WINFUNCTYPE(BOOL, HDC, LPRECT, BOOL)(
    ("InvalidateRect", _User32), 
    ((1, "hWnd"), (1, "lpRect"), (1, "bErase"))
)

ValidateRect            = _ctypes.WINFUNCTYPE(BOOL, HDC, LPRECT)(
    ("ValidateRect", _User32), 
    ((1, "hWnd"), (1, "lpRect"))
)

ChoosePixelFormat       = _ctypes.WINFUNCTYPE(_ctypes.c_int, HDC, _ctypes.POINTER(PIXELFORMATDESCRIPTOR))(
    ("ChoosePixelFormat", _Gdi32), 
    ((1, "hdc"), (1, "ppfd"), )
)

SetPixelFormat          = _ctypes.WINFUNCTYPE(BOOL, HDC, _ctypes.c_int, _ctypes.POINTER(PIXELFORMATDESCRIPTOR))(
    ("SetPixelFormat", _Gdi32), 
    ((1, "hdc"), (1, "_format"), (1, "ppfd"), )
)

DescribePixelFormat     = _ctypes.WINFUNCTYPE(_ctypes.c_int, HDC, _ctypes.c_int, UINT, _ctypes.POINTER(PIXELFORMATDESCRIPTOR))(
    ("DescribePixelFormat", _Gdi32), 
    ((1, "hdc"), (1, "iPixelFormat"), (1, "nBytes"), (1, "ppfd"), )
)

### Functions - Object ###

SelectObject            = _ctypes.WINFUNCTYPE(HGDIOBJ, HDC, HGDIOBJ)(
    ("SelectObject", _Gdi32), 
    ((1, "hdc"), (1, "h"))
)


DeleteObject            = _ctypes.WINFUNCTYPE(BOOL, HGDIOBJ)(
    ("DeleteObject", _Gdi32), 
    ((1, "ho"),)
)

### Functions - Font ###

CreateFontW             = _ctypes.WINFUNCTYPE(
    HFONT, 
    _ctypes.c_int, _ctypes.c_int, _ctypes.c_int, _ctypes.c_int, _ctypes.c_int, 
    DWORD, DWORD, DWORD, DWORD, DWORD, DWORD, DWORD, DWORD,
    LPCWSTR)(
    ("CreateFontW", _Gdi32), 
    (
        (1, "cHeight"), 
        (1, "cWidth"), 
        (1, "cEscapement"), 
        (1, "cOrientation"), 
        (1, "cWeight"), 
        (1, "bItalic"), 
        (1, "bUnderline"), 
        (1, "bStrikeOut"), 
        (1, "iCharSet"), 
        (1, "iOutPrecision"), 
        (1, "iClipPrecision"), 
        (1, "iQuality"), 
        (1, "iPitchAndFamily"), 
        (1, "pszFaceName"), 
    )
)

SetTextAlign            = _ctypes.WINFUNCTYPE(UINT, HDC, UINT)(
    ("SetTextAlign", _Gdi32), 
    ((1, "hdc"), (1, "align"))
)

SetMapMode              = _ctypes.WINFUNCTYPE(_ctypes.c_int, HDC, _ctypes.c_int)(
    ("SetMapMode", _Gdi32), 
    ((1, "hdc"), (1, "iMode"))
)

GetTextMetricsW         = _ctypes.WINFUNCTYPE(BOOL, HDC, LPTEXTMETRICW)(
    ("GetTextMetricsW", _Gdi32), 
    ((1, "hdc"), (1, "lptm"))
)

GetFontUnicodeRanges    = _ctypes.WINFUNCTYPE(DWORD, HDC, LPGLYPHSET)(
    ("GetFontUnicodeRanges", _Gdi32), 
    ((1, "hdc"), (1, "lpgs"))
)

GetTextExtentPoint32W    = _ctypes.WINFUNCTYPE(BOOL, HDC, LPCWSTR, _ctypes.c_int, LPSIZE)(
    ("GetTextExtentPoint32W", _Gdi32), 
    ((1, "hdc"), (1, "lpString"), (1, "c"), (1, "psizl"))
)