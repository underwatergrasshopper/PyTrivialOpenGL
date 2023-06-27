"""
This is an internal module! Shouldn't by imported outside of PyTrivialOpenGL package.

Contains constants, types and functions of WinApi.
"""
import ctypes           as _ctypes
import ctypes.wintypes  as _wintypes

### Libraries ###

_Kernel32   = _ctypes.windll.Kernel32
_User32     = _ctypes.windll.User32
_Dwmapi     = _ctypes.windll.Dwmapi
_Gdi32      = _ctypes.windll.Gdi32

_IS_64_BIT  = _ctypes.sizeof(_ctypes.c_void_p) == 8

### Constants ###

# Virtual Key Codes

VK_LBUTTON              = 0x01
VK_RBUTTON              = 0x02
VK_CANCEL               = 0x03
VK_MBUTTON              = 0x04
VK_XBUTTON1             = 0x05
VK_XBUTTON2             = 0x06
        
VK_BACK                 = 0x08
VK_TAB                  = 0x09
VK_CLEAR                = 0x0C
VK_RETURN               = 0x0D
        
VK_SHIFT                = 0x10
VK_CONTROL              = 0x11
VK_MENU                 = 0x12
VK_PAUSE                = 0x13
VK_CAPITAL              = 0x14
        
VK_KANA                 = 0x15
VK_HANGEUL              = 0x15  # compatibility
VK_HANGUL               = 0x15  # compatibility
VK_IME_ON               = 0x16
VK_JUNJA                = 0x17
VK_FINAL                = 0x18
VK_HANJA                = 0x19
VK_KANJI                = 0x19
VK_IME_OFF              = 0x1A
        
VK_ESCAPE               = 0x1B
        
VK_CONVERT              = 0x1C
VK_NONCONVERT           = 0x1D
VK_ACCEPT               = 0x1E
VK_MODECHANGE           = 0x1F
        
VK_SPACE                = 0x20
VK_PRIOR                = 0x21
VK_NEXT                 = 0x22
VK_END                  = 0x23
VK_HOME                 = 0x24
VK_LEFT                 = 0x25
VK_UP                   = 0x26
VK_RIGHT                = 0x27
VK_DOWN                 = 0x28
VK_SELECT               = 0x29
VK_PRINT                = 0x2A
VK_EXECUTE              = 0x2B
VK_SNAPSHOT             = 0x2C
VK_INSERT               = 0x2D
VK_DELETE               = 0x2E
VK_HELP                 = 0x2F
        
VK_LWIN                 = 0x5B
VK_RWIN                 = 0x5C
VK_APPS                 = 0x5D
        
VK_SLEEP                = 0x5F
        
VK_NUMPAD0              = 0x60
VK_NUMPAD1              = 0x61
VK_NUMPAD2              = 0x62
VK_NUMPAD3              = 0x63
VK_NUMPAD4              = 0x64
VK_NUMPAD5              = 0x65
VK_NUMPAD6              = 0x66
VK_NUMPAD7              = 0x67
VK_NUMPAD8              = 0x68
VK_NUMPAD9              = 0x69
VK_MULTIPLY             = 0x6A
VK_ADD                  = 0x6B
VK_SEPARATOR            = 0x6C
VK_SUBTRACT             = 0x6D
VK_DECIMAL              = 0x6E
VK_DIVIDE               = 0x6F
VK_F1                   = 0x70
VK_F2                   = 0x71
VK_F3                   = 0x72
VK_F4                   = 0x73
VK_F5                   = 0x74
VK_F6                   = 0x75
VK_F7                   = 0x76
VK_F8                   = 0x77
VK_F9                   = 0x78
VK_F10                  = 0x79
VK_F11                  = 0x7A
VK_F12                  = 0x7B
VK_F13                  = 0x7C
VK_F14                  = 0x7D
VK_F15                  = 0x7E
VK_F16                  = 0x7F
VK_F17                  = 0x80
VK_F18                  = 0x81
VK_F19                  = 0x82
VK_F20                  = 0x83
VK_F21                  = 0x84
VK_F22                  = 0x85
VK_F23                  = 0x86
VK_F24                  = 0x87

VK_NAVIGATION_VIEW      = 0x88 # reserved
VK_NAVIGATION_MENU      = 0x89 # reserved
VK_NAVIGATION_UP        = 0x8A # reserved
VK_NAVIGATION_DOWN      = 0x8B # reserved
VK_NAVIGATION_LEFT      = 0x8C # reserved
VK_NAVIGATION_RIGHT     = 0x8D # reserved
VK_NAVIGATION_ACCEPT    = 0x8E # reserved
VK_NAVIGATION_CANCEL    = 0x8F # reserved

VK_NUMLOCK              = 0x90
VK_SCROLL               = 0x91
        
VK_OEM_NEC_EQUAL        = 0x92
        
VK_OEM_FJ_JISHO         = 0x92
VK_OEM_FJ_MASSHOU       = 0x93
VK_OEM_FJ_TOUROKU       = 0x94
VK_OEM_FJ_LOYA          = 0x95
VK_OEM_FJ_ROYA          = 0x96
        
VK_LSHIFT               = 0xA0
VK_RSHIFT               = 0xA1
VK_LCONTROL             = 0xA2
VK_RCONTROL             = 0xA3
VK_LMENU                = 0xA4
VK_RMENU                = 0xA5

VK_BROWSER_BACK         = 0xA6
VK_BROWSER_FORWARD      = 0xA7
VK_BROWSER_REFRESH      = 0xA8
VK_BROWSER_STOP         = 0xA9
VK_BROWSER_SEARCH       = 0xAA
VK_BROWSER_FAVORITES    = 0xAB
VK_BROWSER_HOME         = 0xAC
    
VK_VOLUME_MUTE          = 0xAD
VK_VOLUME_DOWN          = 0xAE
VK_VOLUME_UP            = 0xAF
VK_MEDIA_NEXT_TRACK     = 0xB0
VK_MEDIA_PREV_TRACK     = 0xB1
VK_MEDIA_STOP           = 0xB2
VK_MEDIA_PLAY_PAUSE     = 0xB3
VK_LAUNCH_MAIL          = 0xB4
VK_LAUNCH_MEDIA_SELECT  = 0xB5
VK_LAUNCH_APP1          = 0xB6
VK_LAUNCH_APP2          = 0xB7

VK_OEM_1                = 0xBA   # ';' 
VK_OEM_PLUS             = 0xBB   # '+' 
VK_OEM_COMMA            = 0xBC   # ',' 
VK_OEM_MINUS            = 0xBD   # '-' 
VK_OEM_PERIOD           = 0xBE   # '.' 
VK_OEM_2                = 0xBF   # '/' 
VK_OEM_3                = 0xC0   # '`' 

VK_GAMEPAD_A                        = 0xC3 # reserved
VK_GAMEPAD_B                        = 0xC4 # reserved
VK_GAMEPAD_X                        = 0xC5 # reserved
VK_GAMEPAD_Y                        = 0xC6 # reserved
VK_GAMEPAD_RIGHT_SHOULDER           = 0xC7 # reserved
VK_GAMEPAD_LEFT_SHOULDER            = 0xC8 # reserved
VK_GAMEPAD_LEFT_TRIGGER             = 0xC9 # reserved
VK_GAMEPAD_RIGHT_TRIGGER            = 0xCA # reserved
VK_GAMEPAD_DPAD_UP                  = 0xCB # reserved
VK_GAMEPAD_DPAD_DOWN                = 0xCC # reserved
VK_GAMEPAD_DPAD_LEFT                = 0xCD # reserved
VK_GAMEPAD_DPAD_RIGHT               = 0xCE # reserved
VK_GAMEPAD_MENU                     = 0xCF # reserved
VK_GAMEPAD_VIEW                     = 0xD0 # reserved
VK_GAMEPAD_LEFT_THUMBSTICK_BUTTON   = 0xD1 # reserved
VK_GAMEPAD_RIGHT_THUMBSTICK_BUTTON  = 0xD2 # reserved
VK_GAMEPAD_LEFT_THUMBSTICK_UP       = 0xD3 # reserved
VK_GAMEPAD_LEFT_THUMBSTICK_DOWN     = 0xD4 # reserved
VK_GAMEPAD_LEFT_THUMBSTICK_RIGHT    = 0xD5 # reserved
VK_GAMEPAD_LEFT_THUMBSTICK_LEFT     = 0xD6 # reserved
VK_GAMEPAD_RIGHT_THUMBSTICK_UP      = 0xD7 # reserved
VK_GAMEPAD_RIGHT_THUMBSTICK_DOWN    = 0xD8 # reserved
VK_GAMEPAD_RIGHT_THUMBSTICK_RIGHT   = 0xD9 # reserved
VK_GAMEPAD_RIGHT_THUMBSTICK_LEFT    = 0xDA # reserved

VK_OEM_4                = 0xDB  #  '[' 
VK_OEM_5                = 0xDC  #  '\' 
VK_OEM_6                = 0xDD  #  ']' 
VK_OEM_7                = 0xDE  #  ''' 
VK_OEM_8                = 0xDF
        
VK_OEM_AX               = 0xE1
VK_OEM_102              = 0xE2
VK_ICO_HELP             = 0xE3
VK_ICO_00               = 0xE4
        
        
VK_PROCESSKEY           = 0xE5
VK_ICO_CLEAR            = 0xE6
VK_PACKET               = 0xE7
        
VK_OEM_RESET            = 0xE9
VK_OEM_JUMP             = 0xEA
VK_OEM_PA1              = 0xEB
VK_OEM_PA2              = 0xEC
VK_OEM_PA3              = 0xED
VK_OEM_WSCTRL           = 0xEE
VK_OEM_CUSEL            = 0xEF
VK_OEM_ATTN             = 0xF0
VK_OEM_FINISH           = 0xF1
VK_OEM_COPY             = 0xF2
VK_OEM_AUTO             = 0xF3
VK_OEM_ENLW             = 0xF4
VK_OEM_BACKTAB          = 0xF5
        
VK_ATTN                 = 0xF6
VK_CRSEL                = 0xF7
VK_EXSEL                = 0xF8
VK_EREOF                = 0xF9
VK_PLAY                 = 0xFA
VK_ZOOM                 = 0xFB
VK_NONAME               = 0xFC
VK_PA1                  = 0xFD
VK_OEM_CLEAR            = 0xFE


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

WS_CHILDWINDOW          = WS_CHILD

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

XBUTTON1                = 0x0001
XBUTTON2                = 0x0002

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

# MapVirtualKeyA, uMapType
MAPVK_VK_TO_VSC         = 0
MAPVK_VSC_TO_VK         = 1
MAPVK_VK_TO_CHAR        = 2
MAPVK_VSC_TO_VK_EX      = 3
MAPVK_VK_TO_VSC_EX      = 4

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

### Types ###

NULL                    = None

BYTE                    = _wintypes.BYTE
WORD                    = _wintypes.WORD
DWORD                   = _wintypes.DWORD
CHAR                    = _wintypes.CHAR
WCHAR                   = _wintypes.WCHAR
UINT                    = _wintypes.UINT
INT                     = _wintypes.INT
DOUBLE                  = _wintypes.DOUBLE
FLOAT                   = _wintypes.FLOAT
BOOLEAN                 = _wintypes.BOOLEAN
BOOL                    = _wintypes.BOOL

ULONG                   = _wintypes.ULONG
LONG                    = _wintypes.LONG
USHORT                  = _wintypes.USHORT
SHORT                   = _wintypes.SHORT
LARGE_INTEGER           = _wintypes.LARGE_INTEGER
ULARGE_INTEGER          = _wintypes.ULARGE_INTEGER

LPWSTR                  = _wintypes.LPWSTR
LPCWSTR                 = _wintypes.LPCWSTR
LPSTR                   = _wintypes.LPSTR
LPCSTR                  = _wintypes.LPCSTR
PVOID                   = _ctypes.c_void_p
LPVOID                  = _wintypes.LPVOID
LPCVOID                 = _wintypes.LPCVOID
LPWORD                  = _wintypes.LPWORD  
LPDWORD                 = _wintypes.LPDWORD       

if _IS_64_BIT:
    ULONG_PTR               = _ctypes.c_size_t
    LONG_PTR                = _ctypes.c_ssize_t 
    UINT_PTR                = _ctypes.c_size_t
    INT_PTR                 = _ctypes.c_ssize_t 
else:
    ULONG_PTR               = _ctypes.c_ulong
    LONG_PTR                = _ctypes.c_long 
    UINT_PTR                = _ctypes.c_uint
    INT_PTR                 = _ctypes.c_int 

SIZE_T                  = ULONG_PTR
SSIZE_T                 = LONG_PTR

DWORD_PTR               = ULONG_PTR
LRESULT                 = LONG_PTR
ATOM                    = _wintypes.WORD

HANDLE                  = _wintypes.HANDLE
HBRUSH                  = _wintypes.HBRUSH
HFONT                   = _wintypes.HFONT
HICON                   = _wintypes.HICON
HCURSOR                 = HICON
HINSTANCE               = _wintypes.HINSTANCE
HMODULE                 = _wintypes.HMODULE
HMENU                   = _wintypes.HMENU

HWND                    = _wintypes.HWND
HDC                     = _wintypes.HDC

WPARAM                  = _wintypes.WPARAM
LPARAM                  = _wintypes.LPARAM

HRESULT                 = _ctypes.c_long

WNDPROC                 = _ctypes.WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)
TIMERPROC               = _ctypes.WINFUNCTYPE(None, HWND, UINT, UINT_PTR, DWORD)

# SetWindowPos, hWndInsertAfter
HWND_TOP                = HWND(0)
HWND_BOTTOM             = HWND(1)
HWND_TOPMOST            = HWND(-1)
HWND_NOTOPMOST          = HWND(-2)

### Structures ###

POINT                   = _wintypes.POINT
SIZE                    = _wintypes.SIZE
RECT                    = _wintypes.RECT

LPPOINT                 = _wintypes.LPPOINT
LPSIZE                  = _wintypes.LPSIZE
LPRECT                  = _wintypes.LPRECT

MSG                     = _wintypes.MSG

class WNDCLASSEXW(_ctypes.Structure):
    _fields_ = [
        ("cbSize",          _ctypes.c_uint),
        ("style",           _ctypes.c_uint),
        ("lpfnWndProc",     WNDPROC),
        ("cbClsExtra",      _ctypes.c_int),
        ("cbWndExtra",      _ctypes.c_int),
        ("hInstance",       HINSTANCE),
        ("hIcon",           HICON),
        ("hCursor",         HCURSOR),
        ("hbrBackground",   HBRUSH),
        ("lpszMenuName",    LPCWSTR),
        ("lpszClassName",   LPCWSTR),
        ("hIconSm",         HICON)
    ]

class PIXELFORMATDESCRIPTOR(_ctypes.Structure):
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
    even when current thread waits to this function finish. 
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


