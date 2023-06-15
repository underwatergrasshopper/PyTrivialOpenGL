import ctypes           as _ct
import ctypes.wintypes  as _wt

### WinApi Libraries ###

_Kernel32   = _ct.windll.Kernel32
_User32     = _ct.windll.User32
_Dwmapi     = _ct.windll.Dwmapi
_Gdi32      = _ct.windll.Gdi32

_IS_64_BIT  = _ct.sizeof(_ct.c_void_p) == 8

### WinApi Constants ###

# Window Styles
WS_OVERLAPPED           = 0x00000000
WS_POPUP                = 0x80000000
WS_CHILD                = 0x40000000
WS_MINIMIZE             = 0x20000000
WS_VISIBLE              = 0x10000000
WS_DISABLED             = 0x08000000
WS_CLIPSIBLINGS         = 0x04000000
WS_CLIPCHILDREN         = 0x02000000
WS_MAXIMIZE             = 0x01000000
WS_BORDER               = 0x00800000
WS_DLGFRAME             = 0x00400000
WS_CAPTION              = WS_BORDER | WS_DLGFRAME
WS_VSCROLL              = 0x00200000
WS_HSCROLL              = 0x00100000
WS_SYSMENU              = 0x00080000
WS_THICKFRAME           = 0x00040000
WS_GROUP                = 0x00020000
WS_TABSTOP              = 0x00010000
WS_MINIMIZEBOX          = 0x00020000
WS_MAXIMIZEBOX          = 0x00010000
                   
WS_TILED                = WS_OVERLAPPED
WS_ICONIC               = WS_MINIMIZE
WS_SIZEBOX              = WS_THICKFRAME

WS_OVERLAPPEDWINDOW     = (
    WS_OVERLAPPED     | 
    WS_CAPTION        | 
    WS_SYSMENU        | 
    WS_THICKFRAME     | 
    WS_MINIMIZEBOX    | 
    WS_MAXIMIZEBOX
)

WS_TILEDWINDOW          = WS_OVERLAPPEDWINDOW

WS_POPUPWINDOW          = (
    WS_POPUP          | 
    WS_BORDER         | 
    WS_SYSMENU
)

WS_CHILDWINDOW          = (
    WS_CHILD
)

# Extended Window Styles
WS_EX_DLGMODALFRAME         = 0x00000001
WS_EX_NOPARENTNOTIFY        = 0x00000004
WS_EX_TOPMOST               = 0x00000008
WS_EX_ACCEPTFILES           = 0x00000010
WS_EX_TRANSPARENT           = 0x00000020
WS_EX_MDICHILD              = 0x00000040
WS_EX_TOOLWINDOW            = 0x00000080
WS_EX_WINDOWEDGE            = 0x00000100
WS_EX_CLIENTEDGE            = 0x00000200
WS_EX_CONTEXTHELP           = 0x00000400
WS_EX_RIGHT                 = 0x00001000
WS_EX_LEFT                  = 0x00000000
WS_EX_RTLREADING            = 0x00002000
WS_EX_LTRREADING            = 0x00000000
WS_EX_LEFTSCROLLBAR         = 0x00004000
WS_EX_RIGHTSCROLLBAR        = 0x00000000
WS_EX_CONTROLPARENT         = 0x00010000
WS_EX_STATICEDGE            = 0x00020000
WS_EX_APPWINDOW             = 0x00040000
WS_EX_OVERLAPPEDWINDOW      = (WS_EX_WINDOWEDGE | WS_EX_CLIENTEDGE)
WS_EX_PALETTEWINDOW         = (WS_EX_WINDOWEDGE | WS_EX_TOOLWINDOW | WS_EX_TOPMOST)
WS_EX_LAYERED               = 0x00080000
WS_EX_NOINHERITLAYOUT       = 0x00100000
WS_EX_NOREDIRECTIONBITMAP   = 0x00200000
WS_EX_LAYOUTRTL             = 0x00400000
WS_EX_COMPOSITED            = 0x02000000
WS_EX_NOACTIVATE            = 0x08000000

# Window Class Styles
CS_VREDRAW              = 0x0001
CS_HREDRAW              = 0x0002
CS_DBLCLKS              = 0x0008
CS_OWNDC                = 0x0020
CS_CLASSDC              = 0x0040
CS_PARENTDC             = 0x0080
CS_NOCLOSE              = 0x0200
CS_SAVEBITS             = 0x0800
CS_BYTEALIGNCLIENT      = 0x1000
CS_BYTEALIGNWINDOW      = 0x2000
CS_GLOBALCLASS          = 0x4000
CS_IME                  = 0x00010000
CS_DROPSHADOW           = 0x00020000

# GetSystemMetrics, nIndex
SM_CXSCREEN             = 0
SM_CYSCREEN             = 1

# SystemParametersInfo, uiAction
SPI_GETWORKAREA         = 0x0030

# DwmGetWindowAttribute, dwAttribute
DWMWA_EXTENDED_FRAME_BOUNDS = 9

# GetWindow, uCmd
GW_HWNDFIRST            = 0
GW_HWNDLAST             = 1
GW_HWNDNEXT             = 2
GW_HWNDPREV             = 3
GW_OWNER                = 4
GW_CHILD                = 5
GW_ENABLEDPOPUP         = 6

# SetWindowLongPtrW, nIndex
GWL_EXSTYLE             = -20
GWL_STYLE               = -16

# SetWindowPos, uFlags
SWP_NOSIZE              = 0x0001
SWP_NOMOVE              = 0x0002
SWP_NOZORDER            = 0x0004
SWP_NOREDRAW            = 0x0008
SWP_NOACTIVATE          = 0x0010
SWP_FRAMECHANGED        = 0x0020  
SWP_SHOWWINDOW          = 0x0040
SWP_HIDEWINDOW          = 0x0080
SWP_NOCOPYBITS          = 0x0100
SWP_NOOWNERZORDER       = 0x0200  
SWP_NOSENDCHANGING      = 0x0400 
SWP_DRAWFRAME           = SWP_FRAMECHANGED
SWP_NOREPOSITION        = SWP_NOOWNERZORDER
SWP_DEFERERASE          = 0x2000 
SWP_ASYNCWINDOWPOS      = 0x4000 

# ShowWindow, nCmdShow
SW_HIDE                 = 0
SW_SHOWNORMAL           = 1
SW_NORMAL               = 1
SW_SHOWMINIMIZED        = 2
SW_SHOWMAXIMIZED        = 3
SW_MAXIMIZE             = 3
SW_SHOWNOACTIVATE       = 4
SW_SHOW                 = 5
SW_MINIMIZE             = 6
SW_SHOWMINNOACTIVE      = 7
SW_SHOWNA               = 8
SW_RESTORE              = 9
SW_SHOWDEFAULT          = 10
SW_FORCEMINIMIZE        = 11
SW_MAX                  = 11

# Errors
ERROR_INVALID_PARAMETER = 0x57

# Other
WHEEL_DELTA             = 120

### WinApi Types ###

BYTE                    = _wt.BYTE
WORD                    = _wt.WORD
DWORD                   = _wt.DWORD
CHAR                    = _wt.CHAR
WCHAR                   = _wt.WCHAR
UINT                    = _wt.UINT
INT                     = _wt.INT
DOUBLE                  = _wt.DOUBLE
FLOAT                   = _wt.FLOAT
BOOLEAN                 = _wt.BOOLEAN
BOOL                    = _wt.BOOL

ULONG                   = _wt.ULONG
LONG                    = _wt.LONG
USHORT                  = _wt.USHORT
SHORT                   = _wt.SHORT
LARGE_INTEGER           = _wt.LARGE_INTEGER
ULARGE_INTEGER          = _wt.ULARGE_INTEGER

LPWSTR                  = _wt.LPWSTR
LPCWSTR                 = _wt.LPCWSTR
LPSTR                   = _wt.LPSTR
LPCSTR                  = _wt.LPCSTR
PVOID                   = _ct.c_void_p
LPVOID                  = _wt.LPVOID
LPCVOID                 = _wt.LPCVOID

if _IS_64_BIT:
    ULONG_PTR               = _ct.c_size_t
    LONG_PTR                = _ct.c_ssize_t 
    UINT_PTR                = _ct.c_size_t
    INT_PTR                 = _ct.c_ssize_t 
else:
    ULONG_PTR               = _ct.c_ulong
    LONG_PTR                = _ct.c_long 
    UINT_PTR                = _ct.c_uint
    INT_PTR                 = _ct.c_int 

DWORD_PTR               = ULONG_PTR

ATOM                    = _wt.WORD

HANDLE                  = _wt.HANDLE
HBRUSH                  = _wt.HBRUSH
HFONT                   = _wt.HFONT
HICON                   = _wt.HICON
HINSTANCE               = _wt.HINSTANCE
HMODULE                 = _wt.HMODULE

HWND                    = _wt.HWND
HDC                     = _wt.HDC

WPARAM                  = _wt.WPARAM
LPARAM                  = _wt.LPARAM

HRESULT                 = _ct.c_long

### WinApi Structures ###

POINT                   = _wt.POINT
SIZE                    = _wt.SIZE
RECT                    = _wt.RECT

LPPOINT                 = _wt.LPPOINT
LPSIZE                  = _wt.LPSIZE
LPRECT                  = _wt.LPRECT

MSG                     = _wt.MSG

# SetWindowPos, hWndInsertAfter
HWND_TOP                = HWND(0)
HWND_BOTTOM             = HWND(1)
HWND_TOPMOST            = HWND(-1)
HWND_NOTOPMOST          = HWND(-2)

### WinApi Macros ###

def MAKEINTRESOURCEW(i):
    return LPWSTR(ULONG_PTR(WORD(i).value).value)

def LOWORD(l):
    return WORD(DWORD_PTR(l).value & 0xFFFF)

def HIWORD(l):
    return WORD((DWORD_PTR(l).value >> 16) & 0xFFFF)

def GET_X_LPARAM(lp):
    return _ct.c_int(_ct.c_short(LOWORD(lp).value).value)

def GET_Y_LPARAM(lp):
    return _ct.c_int(_ct.c_short(HIWORD(lp).value).value)

def GET_WHEEL_DELTA_WPARAM(wParam):
    return _ct.c_short(HIWORD(wParam).value)

def GET_KEYSTATE_WPARAM(wParam):
    return LOWORD(wParam)

def IsMinimized(hwnd):
    return IsIconic(hwnd)

def IsMaximized(hwnd):
    return IsZoomed(hwnd)

### WinApi Functions ###

GetLastError            = _ct.WINFUNCTYPE(DWORD)(
    ("GetLastError", _Kernel32), 
    ()
)

GetSystemMetrics        = _ct.WINFUNCTYPE(_ct.c_int, _ct.c_int)(
    ("GetSystemMetrics", _User32), 
    ((1, "nIndex"),)
)

SystemParametersInfoW   = _ct.WINFUNCTYPE(BOOL, UINT, UINT, PVOID, UINT)(
    ("SystemParametersInfoW", _User32), 
    ((1, "uiAction"), (1, "uiParam"), (1, "pvParam"), (1, "fWinIni"))
)

### WinApi Functions - Window ###

GetForegroundWindow     = _ct.WINFUNCTYPE(HWND)(
    ("GetForegroundWindow", _User32), 
    ()
)

SetForegroundWindow     = _ct.WINFUNCTYPE(BOOL, HWND)(
    ("SetForegroundWindow", _User32), 
    ((1, "hWnd"),)
)

SetFocus                = _ct.WINFUNCTYPE(HWND, HWND)(
    ("SetFocus", _User32), 
    ((1, "hWnd"),)
)

FindWindowW             = _ct.WINFUNCTYPE(HWND, LPCWSTR, LPCWSTR)(
    ("FindWindowW", _User32), 
    ((1, "lpClassName", None), (1, "lpWindowName", None))
)

GetActiveWindow         = _ct.WINFUNCTYPE(HWND)(
    ("GetActiveWindow", _User32), 
    ()
)

GetWindow               = _ct.WINFUNCTYPE(HWND, HWND, UINT)(
    ("GetWindow", _User32), 
    ((1, "hWnd"), (1, "uCmd"))
)

GetWindowTextLengthW    = _ct.WINFUNCTYPE(_ct.c_int, HWND)(
    ("GetWindowTextLengthW", _User32), 
    ((1, "hWnd"),)
)

GetWindowTextW          = _ct.WINFUNCTYPE(_ct.c_int, HWND, LPWSTR, _ct.c_int)(
    ("GetWindowTextW", _User32), 
    ((1, "hWnd"), (1, "lpString"), (1, "nMaxCount"))
)

GetWindowRect           = _ct.WINFUNCTYPE(BOOL, HWND, LPRECT)(
    ("GetWindowRect", _User32), 
    ((1, "hWnd"), (1, "lpRect"))
)

GetClientRect           = _ct.WINFUNCTYPE(BOOL, HWND, LPRECT)(
    ("GetClientRect", _User32), 
    ((1, "hWnd"), (1, "lpRect"))
)

DwmGetWindowAttribute   = _ct.WINFUNCTYPE(HRESULT, HWND, DWORD, PVOID, DWORD)(
    ("DwmGetWindowAttribute", _Dwmapi), 
    ((1, "hwnd"), (1, "dwAttribute"), (1, "pvAttribute"), (1, "cbAttribute"))
)

ClientToScreen          = _ct.WINFUNCTYPE(BOOL, HWND, LPPOINT)(
    ("ClientToScreen", _User32), 
    ((1, "hWnd"), (1, "lpPoint"))
)

ScreenToClient          = _ct.WINFUNCTYPE(BOOL, HWND, LPPOINT)(
    ("ScreenToClient", _User32), 
    ((1, "hWnd"), (1, "lpPoint"))
)

SetWindowLongW          = _ct.WINFUNCTYPE(LONG, HWND, _ct.c_int, LONG)(
    ("SetWindowLongW", _User32), 
    ((1, "hWnd"), (1, "nIndex"), (1, "dwNewLong"))
)

if _IS_64_BIT:
    SetWindowLongPtrW   = _ct.WINFUNCTYPE(LONG_PTR, HWND, _ct.c_int, LONG_PTR)(
        ("SetWindowLongPtrW", _User32), 
        ((1, "hWnd"), (1, "nIndex"), (1, "dwNewLong"))
    )
else:
    SetWindowLongPtrW = SetWindowLongW 

SetWindowLongW          = _ct.WINFUNCTYPE(LONG, HWND, _ct.c_int, LONG)(
    ("SetWindowLongW", _User32), 
    ((1, "hWnd"), (1, "nIndex"), (1, "dwNewLong"))
)

SetWindowPos            = _ct.WINFUNCTYPE(BOOL, HWND, HWND, _ct.c_int, _ct.c_int, _ct.c_int, _ct.c_int, UINT)(
    ("SetWindowPos", _User32), 
    ((1, "hWnd"), (1, "hWndInsertAfter"), (1, "X"), (1, "Y"), (1, "cx"), (1, "cy"), (1, "uFlags"))
)

AdjustWindowRectEx      = _ct.WINFUNCTYPE(BOOL, LPRECT, DWORD, BOOL, DWORD)(
    ("AdjustWindowRectEx", _User32), 
    ((1, "lpRect"), (1, "dwStyle"), (1, "bMenu"), (1, "dwExStyle"))
)

AdjustWindowRect        = _ct.WINFUNCTYPE(BOOL, LPRECT, DWORD, BOOL)(
    ("AdjustWindowRect", _User32), 
    ((1, "lpRect"), (1, "dwStyle"), (1, "bMenu"))
)

IsZoomed                = _ct.WINFUNCTYPE(BOOL, HWND)(
    ("IsZoomed", _User32), 
    ((1, "hWnd"),)
)

IsIconic                = _ct.WINFUNCTYPE(BOOL, HWND)(
    ("IsIconic", _User32), 
    ((1, "hWnd"),)
)

ShowWindow              = _ct.WINFUNCTYPE(BOOL, HWND, _ct.c_int)(
    ("ShowWindow", _User32), 
    ((1, "hWnd"), (1, "nCmdShow"))
)

### WinApi Functions - Cursor ###

GetCursorPos            = _ct.WINFUNCTYPE(BOOL, LPPOINT)(
    ("GetCursorPos", _User32), 
    ((1, "lpPoint"),)
)

### WinApi Functions - Device Context ###

SwapBuffers             = _ct.WINFUNCTYPE(BOOL, HDC)(
    ("SwapBuffers", _Gdi32), 
    ((1, "hdc"),)
)

InvalidateRect          = _ct.WINFUNCTYPE(BOOL, HDC, LPRECT, BOOL)(
    ("InvalidateRect", _User32), 
    ((1, "hWnd"), (1, "lpRect"), (1, "bErase"))
)

ValidateRect            = _ct.WINFUNCTYPE(BOOL, HDC, LPRECT)(
    ("ValidateRect", _User32), 
    ((1, "hWnd"), (1, "lpRect"))
)
