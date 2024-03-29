"""
Contains selected constants of WinApi.

Note: Some type and macro dependent constants can be in C_WinApi.Function module.
"""

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
WM_NULL                             = 0x0000
WM_CREATE                           = 0x0001
WM_DESTROY                          = 0x0002
WM_MOVE                             = 0x0003
WM_SIZE                             = 0x0005
WM_ACTIVATE                         = 0x0006
WM_SETFOCUS                         = 0x0007
WM_KILLFOCUS                        = 0x0008
WM_ENABLE                           = 0x000A
WM_SETREDRAW                        = 0x000B
WM_SETTEXT                          = 0x000C
WM_GETTEXT                          = 0x000D
WM_GETTEXTLENGTH                    = 0x000E
WM_PAINT                            = 0x000F
WM_CLOSE                            = 0x0010
WM_QUERYENDSESSION                  = 0x0011
WM_QUIT                             = 0x0012
WM_QUERYOPEN                        = 0x0013
WM_ERASEBKGND                       = 0x0014
WM_SYSCOLORCHANGE                   = 0x0015
WM_ENDSESSION                       = 0x0016
WM_SHOWWINDOW                       = 0x0018
WM_WININICHANGE                     = 0x001A
WM_SETTINGCHANGE                    = WM_WININICHANGE
WM_DEVMODECHANGE                    = 0x001B
WM_ACTIVATEAPP                      = 0x001C
WM_FONTCHANGE                       = 0x001D
WM_TIMECHANGE                       = 0x001E
WM_CANCELMODE                       = 0x001F
WM_SETCURSOR                        = 0x0020
WM_MOUSEACTIVATE                    = 0x0021
WM_CHILDACTIVATE                    = 0x0022
WM_QUEUESYNC                        = 0x0023
WM_GETMINMAXINFO                    = 0x0024
WM_PAINTICON                        = 0x0026
WM_ICONERASEBKGND                   = 0x0027
WM_NEXTDLGCTL                       = 0x0028
WM_SPOOLERSTATUS                    = 0x002A
WM_DRAWITEM                         = 0x002B
WM_MEASUREITEM                      = 0x002C
WM_DELETEITEM                       = 0x002D
WM_VKEYTOITEM                       = 0x002E
WM_CHARTOITEM                       = 0x002F
WM_SETFONT                          = 0x0030
WM_GETFONT                          = 0x0031
WM_SETHOTKEY                        = 0x0032
WM_GETHOTKEY                        = 0x0033
WM_QUERYDRAGICON                    = 0x0037
WM_COMPAREITEM                      = 0x0039
WM_GETOBJECT                        = 0x003D
WM_COMPACTING                       = 0x0041
WM_COMMNOTIFY                       = 0x0044  
WM_WINDOWPOSCHANGING                = 0x0046
WM_WINDOWPOSCHANGED                 = 0x0047
WM_POWER                            = 0x0048
WM_COPYDATA                         = 0x004A
WM_CANCELJOURNAL                    = 0x004B
WM_NOTIFY                           = 0x004E
WM_INPUTLANGCHANGEREQUEST           = 0x0050
WM_INPUTLANGCHANGE                  = 0x0051
WM_TCARD                            = 0x0052
WM_HELP                             = 0x0053
WM_USERCHANGED                      = 0x0054
WM_NOTIFYFORMAT                     = 0x0055
WM_CONTEXTMENU                      = 0x007B
WM_STYLECHANGING                    = 0x007C
WM_STYLECHANGED                     = 0x007D
WM_DISPLAYCHANGE                    = 0x007E
WM_GETICON                          = 0x007F
WM_SETICON                          = 0x0080
WM_NCCREATE                         = 0x0081
WM_NCDESTROY                        = 0x0082
WM_NCCALCSIZE                       = 0x0083
WM_NCHITTEST                        = 0x0084
WM_NCPAINT                          = 0x0085
WM_NCACTIVATE                       = 0x0086
WM_GETDLGCODE                       = 0x0087
WM_SYNCPAINT                        = 0x0088
WM_NCMOUSEMOVE                      = 0x00A0
WM_NCLBUTTONDOWN                    = 0x00A1
WM_NCLBUTTONUP                      = 0x00A2
WM_NCLBUTTONDBLCLK                  = 0x00A3
WM_NCRBUTTONDOWN                    = 0x00A4
WM_NCRBUTTONUP                      = 0x00A5
WM_NCRBUTTONDBLCLK                  = 0x00A6
WM_NCMBUTTONDOWN                    = 0x00A7
WM_NCMBUTTONUP                      = 0x00A8
WM_NCMBUTTONDBLCLK                  = 0x00A9
WM_NCXBUTTONDOWN                    = 0x00AB
WM_NCXBUTTONUP                      = 0x00AC
WM_NCXBUTTONDBLCLK                  = 0x00AD
WM_INPUT_DEVICE_CHANGE              = 0x00FE
WM_INPUT                            = 0x00FF
WM_KEYDOWN                          = 0x0100
WM_KEYUP                            = 0x0101
WM_CHAR                             = 0x0102
WM_DEADCHAR                         = 0x0103
WM_SYSKEYDOWN                       = 0x0104
WM_SYSKEYUP                         = 0x0105
WM_SYSCHAR                          = 0x0106
WM_SYSDEADCHAR                      = 0x0107
WM_UNICHAR                          = 0x0109
WM_IME_STARTCOMPOSITION             = 0x010D
WM_IME_ENDCOMPOSITION               = 0x010E
WM_IME_COMPOSITION                  = 0x010F
WM_INITDIALOG                       = 0x0110
WM_COMMAND                          = 0x0111
WM_SYSCOMMAND                       = 0x0112
WM_TIMER                            = 0x0113
WM_HSCROLL                          = 0x0114
WM_VSCROLL                          = 0x0115
WM_INITMENU                         = 0x0116
WM_INITMENUPOPUP                    = 0x0117
WM_GESTURE                          = 0x0119
WM_GESTURENOTIFY                    = 0x011A
WM_MENUSELECT                       = 0x011F
WM_MENUCHAR                         = 0x0120
WM_ENTERIDLE                        = 0x0121
WM_MENURBUTTONUP                    = 0x0122
WM_MENUDRAG                         = 0x0123
WM_MENUGETOBJECT                    = 0x0124
WM_UNINITMENUPOPUP                  = 0x0125
WM_MENUCOMMAND                      = 0x0126
WM_CHANGEUISTATE                    = 0x0127
WM_UPDATEUISTATE                    = 0x0128
WM_QUERYUISTATE                     = 0x0129
WM_CTLCOLORMSGBOX                   = 0x0132
WM_CTLCOLOREDIT                     = 0x0133
WM_CTLCOLORLISTBOX                  = 0x0134
WM_CTLCOLORBTN                      = 0x0135
WM_CTLCOLORDLG                      = 0x0136
WM_CTLCOLORSCROLLBAR                = 0x0137
WM_CTLCOLORSTATIC                   = 0x0138
MN_GETHMENU                         = 0x01E1
WM_MOUSEMOVE                        = 0x0200
WM_LBUTTONDOWN                      = 0x0201
WM_LBUTTONUP                        = 0x0202
WM_LBUTTONDBLCLK                    = 0x0203
WM_RBUTTONDOWN                      = 0x0204
WM_RBUTTONUP                        = 0x0205
WM_RBUTTONDBLCLK                    = 0x0206
WM_MBUTTONDOWN                      = 0x0207
WM_MBUTTONUP                        = 0x0208
WM_MBUTTONDBLCLK                    = 0x0209
WM_MOUSEWHEEL                       = 0x020A
WM_XBUTTONDOWN                      = 0x020B
WM_XBUTTONUP                        = 0x020C
WM_XBUTTONDBLCLK                    = 0x020D
WM_MOUSEHWHEEL                      = 0x020E
WM_PARENTNOTIFY                     = 0x0210
WM_ENTERMENULOOP                    = 0x0211
WM_EXITMENULOOP                     = 0x0212
WM_NEXTMENU                         = 0x0213
WM_SIZING                           = 0x0214
WM_CAPTURECHANGED                   = 0x0215
WM_MOVING                           = 0x0216
WM_POWERBROADCAST                   = 0x0218
WM_DEVICECHANGE                     = 0x0219
WM_MDICREATE                        = 0x0220
WM_MDIDESTROY                       = 0x0221
WM_MDIACTIVATE                      = 0x0222
WM_MDIRESTORE                       = 0x0223
WM_MDINEXT                          = 0x0224
WM_MDIMAXIMIZE                      = 0x0225
WM_MDITILE                          = 0x0226
WM_MDICASCADE                       = 0x0227
WM_MDIICONARRANGE                   = 0x0228
WM_MDIGETACTIVE                     = 0x0229
WM_MDISETMENU                       = 0x0230
WM_ENTERSIZEMOVE                    = 0x0231
WM_EXITSIZEMOVE                     = 0x0232
WM_DROPFILES                        = 0x0233
WM_MDIREFRESHMENU                   = 0x0234
WM_POINTERDEVICECHANGE              = 0x0238
WM_POINTERDEVICEINRANGE             = 0x0239
WM_POINTERDEVICEOUTOFRANGE          = 0x023A
WM_TOUCH                            = 0x0240
WM_NCPOINTERUPDATE                  = 0x0241
WM_NCPOINTERDOWN                    = 0x0242
WM_NCPOINTERUP                      = 0x0243
WM_POINTERUPDATE                    = 0x0245
WM_POINTERDOWN                      = 0x0246
WM_POINTERUP                        = 0x0247
WM_POINTERENTER                     = 0x0249
WM_POINTERLEAVE                     = 0x024A
WM_POINTERACTIVATE                  = 0x024B
WM_POINTERCAPTURECHANGED            = 0x024C
WM_TOUCHHITTESTING                  = 0x024D
WM_POINTERWHEEL                     = 0x024E
WM_POINTERHWHEEL                    = 0x024F
DM_POINTERHITTEST                   = 0x0250
WM_POINTERROUTEDTO                  = 0x0251
WM_POINTERROUTEDAWAY                = 0x0252
WM_POINTERROUTEDRELEASED            = 0x0253
WM_IME_SETCONTEXT                   = 0x0281
WM_IME_NOTIFY                       = 0x0282
WM_IME_CONTROL                      = 0x0283
WM_IME_COMPOSITIONFULL              = 0x0284
WM_IME_SELECT                       = 0x0285
WM_IME_CHAR                         = 0x0286
WM_IME_REQUEST                      = 0x0288
WM_IME_KEYDOWN                      = 0x0290
WM_IME_KEYUP                        = 0x0291
WM_MOUSEHOVER                       = 0x02A1
WM_MOUSELEAVE                       = 0x02A3
WM_NCMOUSEHOVER                     = 0x02A0
WM_NCMOUSELEAVE                     = 0x02A2
WM_WTSSESSION_CHANGE                = 0x02B1
WM_TABLET_FIRST                     = 0x02C0
WM_TABLET_LAST                      = 0x02DF
WM_DPICHANGED                       = 0x02E0
WM_DPICHANGED_BEFOREPARENT          = 0x02E2
WM_DPICHANGED_AFTERPARENT           = 0x02E3
WM_GETDPISCALEDSIZE                 = 0x02E4
WM_CUT                              = 0x0300
WM_COPY                             = 0x0301
WM_PASTE                            = 0x0302
WM_CLEAR                            = 0x0303
WM_UNDO                             = 0x0304
WM_RENDERFORMAT                     = 0x0305
WM_RENDERALLFORMATS                 = 0x0306
WM_DESTROYCLIPBOARD                 = 0x0307
WM_DRAWCLIPBOARD                    = 0x0308
WM_PAINTCLIPBOARD                   = 0x0309
WM_VSCROLLCLIPBOARD                 = 0x030A
WM_SIZECLIPBOARD                    = 0x030B
WM_ASKCBFORMATNAME                  = 0x030C
WM_CHANGECBCHAIN                    = 0x030D
WM_HSCROLLCLIPBOARD                 = 0x030E
WM_QUERYNEWPALETTE                  = 0x030F
WM_PALETTEISCHANGING                = 0x0310
WM_PALETTECHANGED                   = 0x0311
WM_HOTKEY                           = 0x0312
WM_PRINT                            = 0x0317
WM_PRINTCLIENT                      = 0x0318
WM_APPCOMMAND                       = 0x0319
WM_THEMECHANGED                     = 0x031A
WM_CLIPBOARDUPDATE                  = 0x031D
WM_DWMCOMPOSITIONCHANGED            = 0x031E
WM_DWMNCRENDERINGCHANGED            = 0x031F
WM_DWMCOLORIZATIONCOLORCHANGED      = 0x0320
WM_DWMWINDOWMAXIMIZEDCHANGE         = 0x0321
WM_DWMSENDICONICTHUMBNAIL           = 0x0323
WM_DWMSENDICONICLIVEPREVIEWBITMAP   = 0x0326
WM_GETTITLEBARINFOEX                = 0x033F
WM_HANDHELDFIRST                    = 0x0358
WM_HANDHELDLAST                     = 0x035F
WM_AFXFIRST                         = 0x0360
WM_AFXLAST                          = 0x037F
WM_PENWINFIRST                      = 0x0380
WM_PENWINLAST                       = 0x038F

# Key State Masks for Mouse Messages
MK_LBUTTON                          = 0x0001
MK_RBUTTON                          = 0x0002
MK_SHIFT                            = 0x0004
MK_CONTROL                          = 0x0008
MK_MBUTTON                          = 0x0010
MK_XBUTTON1                         = 0x0020
MK_XBUTTON2                         = 0x0040

# WM_XBUTTON{DOWN|UP}, wParam high word
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

# MapVirtualKeyA, uMapType
DWMWA_EXTENDED_FRAME_BOUNDS = 9

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

# WM_SIZING, wParam
WMSZ_LEFT               = 1
WMSZ_RIGHT              = 2
WMSZ_TOP                = 3
WMSZ_TOPLEFT            = 4
WMSZ_TOPRIGHT           = 5
WMSZ_BOTTOM             = 6
WMSZ_BOTTOMLEFT         = 7
WMSZ_BOTTOMRIGHT        = 8

# WM_SIZE, wParam
SIZE_RESTORED           = 0
SIZE_MINIMIZED          = 1
SIZE_MAXIMIZED          = 2
SIZE_MAXSHOW            = 3
SIZE_MAXHIDE            = 4

# WM_SHOWWINDOW, lParam
SW_PARENTCLOSING        = 1
SW_OTHERZOOM            = 2
SW_PARENTOPENING        = 3
SW_OTHERUNZOOM          = 4

# WM_ACTIVATE, LOWORD(w_param)
WA_INACTIVE             = 0
WA_ACTIVE               = 1
WA_CLICKACTIVE          = 2

# WM_SYSCOMMAND, wParam
SC_SIZE                 = 0xF000
SC_MOVE                 = 0xF010
SC_MINIMIZE             = 0xF020
SC_MAXIMIZE             = 0xF030
SC_NEXTWINDOW           = 0xF040
SC_PREVWINDOW           = 0xF050
SC_CLOSE                = 0xF060
SC_VSCROLL              = 0xF070
SC_HSCROLL              = 0xF080
SC_MOUSEMENU            = 0xF090
SC_KEYMENU              = 0xF100
SC_ARRANGE              = 0xF110
SC_RESTORE              = 0xF120
SC_TASKLIST             = 0xF130
SC_SCREENSAVE           = 0xF140
SC_HOTKEY               = 0xF150
SC_DEFAULT              = 0xF160
SC_MONITORPOWER         = 0xF170
SC_CONTEXTHELP          = 0xF180
SC_SEPARATOR            = 0xF00F

TA_NOUPDATECP                = 0
TA_UPDATECP                  = 1

# SetTextAlign
TA_LEFT                      = 0
TA_RIGHT                     = 2
TA_CENTER                    = 6

TA_TOP                       = 0
TA_BOTTOM                    = 8
TA_BASELINE                  = 24

TA_RTLREADING                = 256
TA_MASK                      = (TA_BASELINE + TA_CENTER + TA_UPDATECP + TA_RTLREADING)

GDI_ERROR                   = 0xFFFFFFFF

# SetMapMode
MM_TEXT                     = 1
MM_LOMETRIC                 = 2
MM_HIMETRIC                 = 3
MM_LOENGLISH                = 4
MM_HIENGLISH                = 5
MM_TWIPS                    = 6
MM_ISOTROPIC                = 7
MM_ANISOTROPIC              = 8

MM_MIN                      = MM_TEXT
MM_MAX                      = MM_ANISOTROPIC
MM_MAX_FIXEDSCALE           = MM_TWIPS

# CreateFontW
FW_DONTCARE                 = 0
FW_THIN                     = 100
FW_EXTRALIGHT               = 200
FW_LIGHT                    = 300
FW_NORMAL                   = 400
FW_MEDIUM                   = 500
FW_SEMIBOLD                 = 600
FW_BOLD                     = 700
FW_EXTRABOLD                = 800
FW_HEAVY                    = 900
                        
FW_ULTRALIGHT               = FW_EXTRALIGHT
FW_REGULAR                  = FW_NORMAL
FW_DEMIBOLD                 = FW_SEMIBOLD
FW_ULTRABOLD                = FW_EXTRABOLD
FW_BLACK                    = FW_HEAVY

ANSI_CHARSET                = 0
DEFAULT_CHARSET             = 1
SYMBOL_CHARSET              = 2
SHIFTJIS_CHARSET            = 128
HANGEUL_CHARSET             = 129
HANGUL_CHARSET              = 129
GB2312_CHARSET              = 134
CHINESEBIG5_CHARSET         = 136
OEM_CHARSET                 = 255
                            
JOHAB_CHARSET               = 130
HEBREW_CHARSET              = 177
ARABIC_CHARSET              = 178
GREEK_CHARSET               = 161
TURKISH_CHARSET             = 162
VIETNAMESE_CHARSET          = 163
THAI_CHARSET                = 222
EASTEUROPE_CHARSET          = 238
RUSSIAN_CHARSET             = 204
                            
MAC_CHARSET                 = 77
BALTIC_CHARSET              = 186

OUT_DEFAULT_PRECIS          = 0
OUT_STRING_PRECIS           = 1
OUT_CHARACTER_PRECIS        = 2
OUT_STROKE_PRECIS           = 3
OUT_TT_PRECIS               = 4
OUT_DEVICE_PRECIS           = 5
OUT_RASTER_PRECIS           = 6
OUT_TT_ONLY_PRECIS          = 7
OUT_OUTLINE_PRECIS          = 8
OUT_SCREEN_OUTLINE_PRECIS   = 9
OUT_PS_ONLY_PRECIS          = 10

CLIP_DEFAULT_PRECIS         = 0
CLIP_CHARACTER_PRECIS       = 1
CLIP_STROKE_PRECIS          = 2
CLIP_MASK                   = 0x0F
CLIP_LH_ANGLES              = (1 << 4)
CLIP_TT_ALWAYS              = (2 << 4)
CLIP_DFA_DISABLE            = (4 << 4)
CLIP_EMBEDDED               = (8 << 4)

DEFAULT_QUALITY             = 0
DRAFT_QUALITY               = 1
PROOF_QUALITY               = 2
NONANTIALIASED_QUALITY      = 3
ANTIALIASED_QUALITY         = 4

FF_DONTCARE                 = (0 << 4)
FF_ROMAN                    = (1 << 4)
FF_SWISS                    = (2 << 4)
FF_MODERN                   = (3 << 4)
FF_SCRIPT                   = (4 << 4)
FF_DECORATIVE               = (5 << 4)

DEFAULT_PITCH               = 0
FIXED_PITCH                 = 1
VARIABLE_PITCH              = 2
MONO_FONT                   = 8

# BMP
BI_BITFIELDS            = 3
LCS_GM_GRAPHICS         = 0x00000002
LCS_sRGB                = int.from_bytes(b'sRGB', byteorder = "big")