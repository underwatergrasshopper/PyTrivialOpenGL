import ctypes           as _ct
import ctypes.wintypes  as _wt

### WinApi Libraries ###

#_Kernel32   = _ct.windll.Kernel32
#_User32     = _ct.windll.User32
#_Dwmapi     = _ct.windll.Dwmapi

_Kernel32   = _ct.windll.LoadLibrary("C:\\Windows\\SysWOW64\\Kernel32.dll")
_User32     = _ct.windll.LoadLibrary("C:\\Windows\\SysWOW64\\User32.dll")
_Dwmapi     = _ct.windll.LoadLibrary("C:\\Windows\\SysWOW64\\Dwmapi.dll")


### WinApi Constants ###

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

# Errors
ERROR_INVALID_PARAMETER = 0x57

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

ATOM                    = _wt.WORD

HANDLE                  = _wt.HANDLE
HBRUSH                  = _wt.HBRUSH
HFONT                   = _wt.HFONT
HICON                   = _wt.HICON
HINSTANCE               = _wt.HINSTANCE
HMODULE                 = _wt.HMODULE
HWND                    = _wt.HWND

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

### Window ###

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
