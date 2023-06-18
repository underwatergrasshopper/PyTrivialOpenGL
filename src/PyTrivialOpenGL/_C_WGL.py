import ctypes           as _ct
import ctypes.wintypes  as _wt

### Libraries ###

_OpenGL32   = _ct.windll.OpenGL32

### Constants ###

# wglCreateContextAttribsARB, attribList
WGL_CONTEXT_MAJOR_VERSION_ARB               = 0x2091
WGL_CONTEXT_MINOR_VERSION_ARB               = 0x2092
WGL_CONTEXT_LAYER_PLANE_ARB                 = 0x2093
WGL_CONTEXT_FLAGS_ARB                       = 0x2094
WGL_CONTEXT_PROFILE_MASK_ARB                = 0x9126

# wglCreateContextAttribsARB, attribList, WGL_CONTEXT_FLAGS_ARB 
WGL_CONTEXT_DEBUG_BIT_ARB                   = 0x0001
WGL_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB      = 0x0002

# wglCreateContextAttribsARB, attribList, WGL_CONTEXT_PROFILE_MASK_ARB 
WGL_CONTEXT_CORE_PROFILE_BIT_ARB            = 0x00000001
WGL_CONTEXT_COMPATIBILITY_PROFILE_BIT_ARB   = 0x00000002

# wglCreateContextAttribsARB, GetLastError()
ERROR_INVALID_VERSION_ARB                   = 0x2095
ERROR_INVALID_PROFILE_ARB                   = 0x2096

### Types ###

BOOL        = _wt.BOOL
DWORD       = _wt.DWORD

LPCSTR      = _wt.LPCSTR

HDC         = _wt.HANDLE
HGLRC       = _wt.HANDLE

PROC        = _ct.c_void_p

### Functions - Rendering Context ###

wglGetProcAddress           = _ct.WINFUNCTYPE(PROC, LPCSTR)(
    ("wglGetProcAddress", _OpenGL32), 
    ((1, "functionName"), )
)

wglCreateContext            = _ct.WINFUNCTYPE(HGLRC, HDC)(
    ("wglCreateContext", _OpenGL32), 
    ((1, "hDC"), )
)

#wglCreateContextAttribsARB  = _ct.WINFUNCTYPE(HGLRC, HDC, HGLRC, _ct.POINTER(_ct.c_int))(
#    ("wglCreateContextAttribsARB", _OpenGL32), 
#    ((1, "hDC"), (1, "hShareContext"), (1, "attribList"))
#)

wglDeleteContext            = _ct.WINFUNCTYPE(BOOL, HGLRC)(
    ("wglDeleteContext", _OpenGL32), 
    ((1, "hGLRC"), )
)

wglMakeCurrent              = _ct.WINFUNCTYPE(BOOL, HDC, HGLRC)(
    ("wglMakeCurrent", _OpenGL32), 
    ((1, "hDC"), (1, "hGLRC"))
)

### Functions - Font ###

wglUseFontBitmapsW          = _ct.WINFUNCTYPE(BOOL, HDC, DWORD, DWORD, DWORD)(
    ("wglUseFontBitmapsW", _OpenGL32), 
    ((1, "hDC"), (1, "first"), (1, "count"), (1, "listBase"))
)
