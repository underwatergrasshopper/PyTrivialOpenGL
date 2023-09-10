"""
Contains selected types and structures of WinApi.
"""

import sys              as _sys
import ctypes           as _ctypes
import ctypes.wintypes  as _wintypes

###

_IS_64_BIT = _sys.maxsize > 2**32

### Generic Types ###

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
    ULONG_PTR               = _ctypes.c_size_t      # type: ignore
    LONG_PTR                = _ctypes.c_ssize_t     # type: ignore
    UINT_PTR                = _ctypes.c_size_t      # type: ignore
    INT_PTR                 = _ctypes.c_ssize_t     # type: ignore
else:
    ULONG_PTR               = _ctypes.c_ulong       # type: ignore
    LONG_PTR                = _ctypes.c_long        # type: ignore
    UINT_PTR                = _ctypes.c_uint        # type: ignore
    INT_PTR                 = _ctypes.c_int         # type: ignore

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
HGDIOBJ                 = _wintypes.HGDIOBJ

HWND                    = _wintypes.HWND
HDC                     = _wintypes.HDC

WPARAM                  = _wintypes.WPARAM
LPARAM                  = _wintypes.LPARAM

HRESULT                 = _ctypes.c_long

WNDPROC                 = _ctypes.WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)
TIMERPROC               = _ctypes.WINFUNCTYPE(None, HWND, UINT, UINT_PTR, DWORD)

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

class TEXTMETRICW(_ctypes.Structure):
    _fields_ = [
        ("tmHeight",            LONG),
        ("tmAscent",            LONG),
        ("tmDescent",           LONG),
        ("tmInternalLeading",   LONG),
        ("tmExternalLeading",   LONG),
        ("tmAveCharWidth",      LONG),
        ("tmMaxCharWidth",      LONG),
        ("tmWeight",            LONG),
        ("tmOverhang",          LONG),
        ("tmDigitizedAspectX",  LONG),
        ("tmDigitizedAspectY",  LONG),
        ("tmFirstChar",         WCHAR),
        ("tmLastChar",          WCHAR),
        ("tmDefaultChar",       WCHAR),
        ("tmBreakChar",         WCHAR),
        ("tmItalic",            BYTE),
        ("tmUnderlined",        BYTE),
        ("tmStruckOut",         BYTE),
        ("tmPitchAndFamily",    BYTE),
        ("tmCharSet",           BYTE),
    ]

LPTEXTMETRICW = _ctypes.POINTER(TEXTMETRICW) 

class WCRANGE(_ctypes.Structure):
    _fields_ = [
        ("wcLow",   WCHAR),
        ("cGlyphs", USHORT),
    ]

LPWCRANGE = _ctypes.POINTER(WCRANGE)

class GLYPHSET(_ctypes.Structure):
    _fields_ = [
        ("cbThis",              DWORD),
        ("flAccel",             DWORD),
        ("cGlyphsSupported",    DWORD),
        ("cRanges",             DWORD),
        ("ranges",              WCRANGE * 1),
    ]

LPGLYPHSET = _ctypes.POINTER(GLYPHSET)


class BITMAPFILEHEADER(_ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("bfType",      WORD),
        ("bfSize",      DWORD),
        ("bfReserved1", WORD),
        ("bfReserved2", WORD),
        ("bfOffBits",   DWORD),
    ]

LPBITMAPFILEHEADER = _ctypes.POINTER(BITMAPFILEHEADER)

FXPT2DOT30      = _ctypes.c_long

class CIEXYZ(_ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("ciexyzX", FXPT2DOT30),
        ("ciexyzY", FXPT2DOT30),
        ("ciexyzZ", FXPT2DOT30),
    ]

class CIEXYZTRIPLE(_ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("ciexyzRed",   CIEXYZ),
        ("ciexyzGreen", CIEXYZ),
        ("ciexyzBlue",  CIEXYZ),
    ]

class BITMAPV5HEADER(_ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("bV5Size",             DWORD),
        ("bV5Width",            LONG),
        ("bV5Height",           LONG),
        ("bV5Planes",           WORD),
        ("bV5BitCount",         WORD),
        ("bV5Compression",      DWORD),
        ("bV5SizeImage",        DWORD),
        ("bV5XPelsPerMeter",    LONG),
        ("bV5YPelsPerMeter",    LONG),
        ("bV5ClrUsed",          DWORD),
        ("bV5ClrImportant",     DWORD),
        ("bV5RedMask",          DWORD),
        ("bV5GreenMask",        DWORD),
        ("bV5BlueMask",         DWORD),
        ("bV5AlphaMask",        DWORD),
        ("bV5CSType",           DWORD),
        ("bV5Endpoints",        CIEXYZTRIPLE),
        ("bV5GammaRed",         DWORD),
        ("bV5GammaGreen",       DWORD),
        ("bV5GammaBlue",        DWORD),
        ("bV5Intent",           DWORD),
        ("bV5ProfileData",      DWORD),
        ("bV5ProfileSize",      DWORD),
        ("bV5Reserved",         DWORD),
    ]

LPBITMAPV5HEADER = _ctypes.POINTER(BITMAPV5HEADER)