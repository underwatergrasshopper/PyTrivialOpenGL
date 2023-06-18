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

# MessageBoxW, uType
MB_OK                   = 0x00000000
MB_OKCANCEL             = 0x00000001
MB_ABORTRETRYIGNORE     = 0x00000002
MB_YESNOCANCEL          = 0x00000003
MB_YESNO                = 0x00000004
MB_RETRYCANCEL          = 0x00000005
MB_CANCELTRYCONTINUE    = 0x00000006
MB_ICONHAND             = 0x00000010
MB_ICONQUESTION         = 0x00000020
MB_ICONEXCLAMATION      = 0x00000030
MB_ICONASTERISK         = 0x00000040
MB_USERICON             = 0x00000080
MB_ICONWARNING          = MB_ICONEXCLAMATION
MB_ICONERROR            = MB_ICONHAND
MB_ICONINFORMATION      = MB_ICONASTERISK
MB_ICONSTOP             = MB_ICONHAND
MB_DEFBUTTON1           = 0x00000000
MB_DEFBUTTON2           = 0x00000100
MB_DEFBUTTON3           = 0x00000200
MB_DEFBUTTON4           = 0x00000300
MB_APPLMODAL            = 0x00000000
MB_SYSTEMMODAL          = 0x00001000
MB_TASKMODAL            = 0x00002000
MB_HELP                 = 0x00004000 
MB_NOFOCUS              = 0x00008000
MB_SETFOREGROUND        = 0x00010000
MB_DEFAULT_DESKTOP_ONLY = 0x00020000
MB_TOPMOST              = 0x00040000
MB_RIGHT                = 0x00080000
MB_RTLREADING           = 0x00100000

# MessageBoxW, return
IDOK                    = 1
IDCANCEL                = 2
IDABORT                 = 3
IDRETRY                 = 4
IDIGNORE                = 5
IDYES                   = 6
IDNO                    = 7
IDCLOSE                 = 8
IDHELP                  = 9
IDTRYAGAIN              = 10
IDCONTINUE              = 11
IDTIMEOUT               = 32000

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

# Window Messages
WM_NULL                 = 0x0000
                        
WM_CREATE               = 0x0001
WM_DESTROY              = 0x0002

WM_CLOSE                = 0x0010
WM_QUIT                 = 0x0012

WM_PAINT                = 0x000F
WM_ERASEBKGND           = 0x0014

WM_MOVE                 = 0x0003
WM_SIZE                 = 0x0005
WM_SIZING               = 0x0214
WM_MOVING               = 0x0216

WM_ENTERSIZEMOVE        = 0x0231
WM_EXITSIZEMOVE         = 0x0232  

WM_TIMER                = 0x0113

WM_SHOWWINDOW           = 0x0018

WM_ACTIVATE             = 0x0006
WM_ACTIVATEAPP          = 0x001C

WM_SYSCOMMAND           = 0x0112

WM_SETFOCUS             = 0x0007
WM_KILLFOCUS            = 0x0008

WM_KEYDOWN              = 0x0100
WM_KEYUP                = 0x0101
WM_SYSKEYDOWN           = 0x0104
WM_SYSKEYUP             = 0x0105
WM_CHAR                 = 0x0102

WM_LBUTTONDOWN          = 0x0201
WM_LBUTTONUP            = 0x0202
WM_RBUTTONDOWN          = 0x0204
WM_RBUTTONUP            = 0x0205
WM_MBUTTONDOWN          = 0x0207
WM_MBUTTONUP            = 0x0208
WM_XBUTTONDOWN          = 0x020B
WM_XBUTTONUP            = 0x020C

WM_MOUSEMOVE            = 0x0200
WM_MOUSEWHEEL           = 0x020A

WM_USER                 = 0x0400

# LoadImage, _type
IMAGE_BITMAP            = 0
IMAGE_ICON              = 1
IMAGE_CURSOR            = 2

# LoadImage, fuLoad
LR_DEFAULTCOLOR         = 0x00000000
LR_MONOCHROME           = 0x00000001
LR_COLOR                = 0x00000002
LR_COPYRETURNORG        = 0x00000004
LR_COPYDELETEORG        = 0x00000008
LR_LOADFROMFILE         = 0x00000010
LR_LOADTRANSPARENT      = 0x00000020
LR_DEFAULTSIZE          = 0x00000040
LR_VGACOLOR             = 0x00000080
LR_LOADMAP3DCOLORS      = 0x00001000
LR_CREATEDIBSECTION     = 0x00002000
LR_COPYFROMRESOURCE     = 0x00004000
LR_SHARED               = 0x00008000


# PIXELFORMATDESCRIPTOR, iPixelType
PFD_TYPE_RGBA               = 0
PFD_TYPE_COLORINDEX         = 1

# PIXELFORMATDESCRIPTOR, iLayerType
PFD_MAIN_PLANE              = 0
PFD_OVERLAY_PLANE           = 1
PFD_UNDERLAY_PLANE          = (-1)

# PIXELFORMATDESCRIPTOR, dwFlags
PFD_DOUBLEBUFFER            = 0x00000001
PFD_STEREO                  = 0x00000002
PFD_DRAW_TO_WINDOW          = 0x00000004
PFD_DRAW_TO_BITMAP          = 0x00000008
PFD_SUPPORT_GDI             = 0x00000010
PFD_SUPPORT_OPENGL          = 0x00000020
PFD_GENERIC_FORMAT          = 0x00000040
PFD_NEED_PALETTE            = 0x00000080
PFD_NEED_SYSTEM_PALETTE     = 0x00000100
PFD_SWAP_EXCHANGE           = 0x00000200
PFD_SWAP_COPY               = 0x00000400
PFD_SWAP_LAYER_BUFFERS      = 0x00000800
PFD_GENERIC_ACCELERATED     = 0x00001000
PFD_SUPPORT_DIRECTDRAW      = 0x00002000
PFD_DIRECT3D_ACCELERATED    = 0x00004000
PFD_SUPPORT_COMPOSITION     = 0x00008000

PFD_DEPTH_DONTCARE          = 0x20000000
PFD_DOUBLEBUFFER_DONTCARE   = 0x40000000
PFD_STEREO_DONTCARE         = 0x80000000

# PostMessageW, wRemoveMsg
PM_NOREMOVE             = 0x0000
PM_REMOVE               = 0x0001
PM_NOYIELD              = 0x0002

# CreateWindowEx
CW_USEDEFAULT           = 0x80000000

# SystemParametersInfoW, uiAction
SPI_GETWORKAREA         = 0x0030

# Errors
ERROR_INVALID_PARAMETER = 0x57

# Other
EXIT_SUCCESS            = 0
EXIT_FAILURE            = 1

FALSE                   = 0
TRUE                    = 1

WHEEL_DELTA             = 120

COLOR_WINDOW            = 5

INFINITE                = 0xFFFFFFFF

### WinApi Types ###

NULL                    = None

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
LPWORD                  = _wt.LPWORD  
LPDWORD                 = _wt.LPDWORD       

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

SIZE_T                  = ULONG_PTR
SSIZE_T                 = LONG_PTR

DWORD_PTR               = ULONG_PTR
LRESULT                 = LONG_PTR
ATOM                    = _wt.WORD

HANDLE                  = _wt.HANDLE
HBRUSH                  = _wt.HBRUSH
HFONT                   = _wt.HFONT
HICON                   = _wt.HICON
HCURSOR                 = HICON
HINSTANCE               = _wt.HINSTANCE
HMODULE                 = _wt.HMODULE
HMENU                   = _wt.HMENU

HWND                    = _wt.HWND
HDC                     = _wt.HDC

WPARAM                  = _wt.WPARAM
LPARAM                  = _wt.LPARAM

HRESULT                 = _ct.c_long

WNDPROC                 = _ct.WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)

# SetWindowPos, hWndInsertAfter
HWND_TOP                = HWND(0)
HWND_BOTTOM             = HWND(1)
HWND_TOPMOST            = HWND(-1)
HWND_NOTOPMOST          = HWND(-2)

### WinApi Structures ###

POINT                   = _wt.POINT
SIZE                    = _wt.SIZE
RECT                    = _wt.RECT

LPPOINT                 = _wt.LPPOINT
LPSIZE                  = _wt.LPSIZE
LPRECT                  = _wt.LPRECT

MSG                     = _wt.MSG

class WNDCLASSEXW(_ct.Structure):
    _fields_ = [
        ("cbSize",          _ct.c_uint),
        ("style",           _ct.c_uint),
        ("lpfnWndProc",     WNDPROC),
        ("cbClsExtra",      _ct.c_int),
        ("cbWndExtra",      _ct.c_int),
        ("hInstance",       HINSTANCE),
        ("hIcon",           HICON),
        ("hCursor",         HCURSOR),
        ("hbrBackground",   HBRUSH),
        ("lpszMenuName",    LPCWSTR),
        ("lpszClassName",   LPCWSTR),
        ("hIconSm",         HICON)
    ]

class PIXELFORMATDESCRIPTOR(_ct.Structure):
    _fields_ = [
        ("nSize",           WORD),
        ("nVersion",        WORD),
        ("dwFlags",         DWORD),
        ("iPixelType",      BYTE),
        ("cColorBits",      BYTE),
        ("cRedBits",        BYTE),
        ("cRedShift",       BYTE),
        ("cGreenBits",      BYTE),
        ("cGreenShift",     BYTE),
        ("cBlueBits",       BYTE),
        ("cBlueShift",      BYTE),
        ("cAlphaBits",      BYTE),
        ("cAlphaShift",     BYTE),
        ("cAccumBits",      BYTE),
        ("cAccumRedBits",   BYTE),    
        ("cAccumGreenBits", BYTE),    
        ("cAccumBlueBits",  BYTE),    
        ("cAccumAlphaBits", BYTE),    
        ("cDepthBits",      BYTE),
        ("cStencilBits",    BYTE),
        ("cAuxBuffers",     BYTE),
        ("iLayerType",      BYTE),
        ("bReserved",       BYTE),
        ("dwLayerMask",     DWORD),
        ("dwVisibleMask",   DWORD),    
        ("dwDamageMask",    DWORD),
    ]

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

### WinApi Constants which are macro dependent ###

IDC_ARROW               = MAKEINTRESOURCEW(32512)

### WinApi Functions ###

GetLastError            = _ct.WINFUNCTYPE(DWORD)(
    ("GetLastError", _Kernel32), 
    ()
)

GetModuleHandleW        = _ct.WINFUNCTYPE(HMODULE, LPCWSTR)(
    ("GetModuleHandleW", _Kernel32), 
    ((1, "lpModuleName"), )
)

GetSystemMetrics        = _ct.WINFUNCTYPE(_ct.c_int, _ct.c_int)(
    ("GetSystemMetrics", _User32), 
    ((1, "nIndex"), )
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

LoadCursorW             = _ct.WINFUNCTYPE(HCURSOR, HINSTANCE, LPCWSTR)(
    ("LoadCursorW", _User32), 
    ((1, "hInstance"), (1, "lpCursorName"))
)

LoadImageW             = _ct.WINFUNCTYPE(HANDLE, HINSTANCE, LPCWSTR, UINT, _ct.c_int, _ct.c_int, UINT)(
    ("LoadImageW", _User32), 
    ((1, "hInst"), (1, "name"), (1, "_type"), (1, "cx"), (1, "cy"), (1, "fuLoad"))
)

MessageBoxW            = _ct.WINFUNCTYPE(_ct.c_int, HWND, LPCWSTR, LPCWSTR, UINT)(
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
    even when current thread waits to this function finish. 
    Their dispatching resumes after this function finish.
    
    lpText          : LPCWSTR
    lpCaption       : LPCWSTR
    uType           : UINT
    Returns (ctypes.c_int). Same result values as MessageBoxW. 
    """
    class ParameterPack(_ct.Structure):
        _fields_ = [
            ("lpText",      LPCWSTR),
            ("lpCaption",   LPCWSTR),
            ("uType",       UINT),
            ("iResult",     _ct.c_int),
        ]

    def ThreadFunction(param):
        pack = _ct.cast(param, _ct.POINTER(ParameterPack))[0]

        pack.iResult = MessageBoxW(NULL, pack.lpText, pack.lpCaption, pack.uType)
        return 0
    ThreadFunction = LPTHREAD_START_ROUTINE(ThreadFunction)

    pack = ParameterPack(lpText, lpCaption, uType, 0)

    thread_handle = CreateThread(NULL, 0, ThreadFunction, _ct.byref(pack), 0, NULL)
    WaitForSingleObject(thread_handle, INFINITE)

    return pack.iResult

###

RegisterClassExW        = _ct.WINFUNCTYPE(ATOM, _ct.POINTER(WNDCLASSEXW))(
    ("RegisterClassExW", _User32), 
    ((1, "lpwcx"), )
)

UnregisterClassW        = _ct.WINFUNCTYPE(BOOL, LPCWSTR, HINSTANCE)(
    ("UnregisterClassW", _User32), 
    ((1, "lpClassName"), (1, "hInstance"))
)

CreateWindowExW         = _ct.WINFUNCTYPE(HWND, DWORD, LPCWSTR, LPCWSTR, DWORD, _ct.c_int, _ct.c_int, _ct.c_int, _ct.c_int, HWND, HMENU, HINSTANCE, LPVOID)(
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

DestroyWindow           = _ct.WINFUNCTYPE(BOOL, HWND)(
    ("DestroyWindow", _User32), 
    ((1, "hWnd"), )
)

CloseWindow             = _ct.WINFUNCTYPE(BOOL, HWND)(
    ("CloseWindow", _User32), 
    ((1, "hWnd"), )
)

UpdateWindow            = _ct.WINFUNCTYPE(BOOL, HWND)(
    ("UpdateWindow", _User32), 
    ((1, "hWnd"), )
)

DefWindowProcW          = _ct.WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)(
    ("DefWindowProcW", _User32), 
    ((1, "hWnd"), (1, "Msg"), (1, "wParam"), (1, "lParam"))
)

GetMessageW             = _ct.WINFUNCTYPE(BOOL, _ct.POINTER(MSG), HWND, UINT, UINT)(
    ("GetMessageW", _User32), 
    ((1, "lpMsg"), (1, "hWnd"), (1, "wMsgFilterMin"), (1, "wMsgFilterMax"))
)

PeekMessageW            = _ct.WINFUNCTYPE(BOOL, _ct.POINTER(MSG), HWND, UINT, UINT, UINT)(
    ("PeekMessageW", _User32), 
    ((1, "lpMsg"), (1, "hWnd"), (1, "wMsgFilterMin"), (1, "wMsgFilterMax"), (1, "wRemoveMsg"))
)

TranslateMessage        = _ct.WINFUNCTYPE(BOOL, _ct.POINTER(MSG))(
    ("TranslateMessage", _User32), 
    ((1, "lpMsg"), )
)

DispatchMessageW        = _ct.WINFUNCTYPE(LRESULT, _ct.POINTER(MSG))(
    ("DispatchMessageW", _User32), 
    ((1, "lpMsg"), )
)

PostQuitMessage        = _ct.WINFUNCTYPE(None, _ct.c_int)(
    ("PostQuitMessage", _User32), 
    ((1, "nExitCode"), )
)

PostMessageW            = _ct.WINFUNCTYPE(BOOL, HWND, UINT, WPARAM, LPARAM)(
    ("PostMessageW", _User32), 
    ((1, "hWnd"), (1, "Msg"), (1, "wParam"), (1, "lParam"))
)

SendMessageW            = _ct.WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)(
    ("SendMessageW", _User32), 
    ((1, "hWnd"), (1, "Msg"), (1, "wParam"), (1, "lParam"))
)

GetQueueStatus          = _ct.WINFUNCTYPE(DWORD, UINT)(
    ("GetQueueStatus", _User32), 
    ((1, "flags"), )
)

WaitForSingleObject = _ct.WINFUNCTYPE(DWORD, HANDLE, DWORD)(
    ("WaitForSingleObject", _Kernel32), 
    ((1, "hHandle"), (1, "dwMilliseconds"))
)

MsgWaitForMultipleObjectsEx = _ct.WINFUNCTYPE(DWORD, DWORD, _ct.POINTER(HANDLE), DWORD, DWORD, DWORD)(
    ("MsgWaitForMultipleObjectsEx", _User32), 
    ((1, "nCount"), (1, "pHandles"), (1, "dwMilliseconds"), (1, "dwWakeMask"), (1, "dwFlags"))
)

InSendMessage           = _ct.WINFUNCTYPE(BOOL)(
    ("InSendMessage", _User32), 
    ()
)

ReplyMessage            = _ct.WINFUNCTYPE(BOOL, LRESULT)(
    ("ReplyMessage", _User32), 
    ((1, "lResult"), )
)

### WinApi Functions - Mouse ###

GetCursorPos            = _ct.WINFUNCTYPE(BOOL, LPPOINT)(
    ("GetCursorPos", _User32), 
    ((1, "lpPoint"),)
)

SetCapture              = _ct.WINFUNCTYPE(HWND, HWND)(
    ("SetCapture", _User32), 
    ((1, "hWnd"),)
)

GetCapture              = _ct.WINFUNCTYPE(HWND)(
    ("GetCapture", _User32), 
    ()
)

ReleaseCapture          = _ct.WINFUNCTYPE(HWND)(
    ("ReleaseCapture", _User32), 
    ()
)

### Thread ###

CREATE_SUSPENDED                    = 0x00000004
STACK_SIZE_PARAM_IS_A_RESERVATION   = 0x00010000

class SECURITY_ATTRIBUTES(_ct.Structure):
    _fields_ = [
        ("nLength",                 DWORD),
        ("lpSecurityDescriptor",    LPVOID),
        ("bInheritHandle",          BOOL)
    ]

LPSECURITY_ATTRIBUTES   = _ct.POINTER(SECURITY_ATTRIBUTES)
LPTHREAD_START_ROUTINE  = _ct.WINFUNCTYPE(DWORD, LPVOID)


CreateThread            = _ct.WINFUNCTYPE(HANDLE, LPSECURITY_ATTRIBUTES, SIZE_T, LPTHREAD_START_ROUTINE, LPVOID, DWORD, LPDWORD)(
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

### Device Context / Rendering Context ###

GetDC                   = _ct.WINFUNCTYPE(HDC, HWND)(
    ("GetDC", _User32), 
    ((1, "hWnd"), )
)

ReleaseDC               = _ct.WINFUNCTYPE(_ct.c_int, HWND, HDC)(
    ("ReleaseDC", _User32), 
    ((1, "hWnd"), (1, "hDC"), )
)

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

ChoosePixelFormat       = _ct.WINFUNCTYPE(_ct.c_int, HDC, _ct.POINTER(PIXELFORMATDESCRIPTOR))(
    ("ChoosePixelFormat", _Gdi32), 
    ((1, "hdc"), (1, "ppfd"), )
)

SetPixelFormat          = _ct.WINFUNCTYPE(BOOL, HDC, _ct.c_int, _ct.POINTER(PIXELFORMATDESCRIPTOR))(
    ("SetPixelFormat", _Gdi32), 
    ((1, "hdc"), (1, "_format"), (1, "ppfd"), )
)

DescribePixelFormat     = _ct.WINFUNCTYPE(_ct.c_int, HDC, _ct.c_int, UINT, _ct.POINTER(PIXELFORMATDESCRIPTOR))(
    ("DescribePixelFormat", _Gdi32), 
    ((1, "hdc"), (1, "iPixelFormat"), (1, "nBytes"), (1, "ppfd"), )
)


