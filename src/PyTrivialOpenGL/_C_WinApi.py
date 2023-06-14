import ctypes           as _ct
import ctypes.wintypes  as _wt

### WinApi Libraries ###

_Kernel32   = _ct.windll.Kernel32
_User32     = _ct.windll.User32

### WinApi Constants ###

# GetSystemMetrics, nIndex
SM_CXSCREEN             = 0
SM_CYSCREEN             = 1

# SystemParametersInfo, uiAction
SPI_GETWORKAREA         = 0x0030

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

### WinApi Structures ###

POINT                   = _wt.POINT
SIZE                    = _wt.SIZE
RECT                    = _wt.RECT

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
