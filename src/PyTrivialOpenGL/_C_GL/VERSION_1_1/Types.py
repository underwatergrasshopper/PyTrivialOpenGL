"""
This is an internal module! Shouldn't by imported outside of PyTrivialOpenGL package.

Contains all types of OpenGL 1.1.
"""
import ctypes as _ctypes

GLenum      = _ctypes.c_uint
GLboolean   = _ctypes.c_ubyte
GLbitfield  = _ctypes.c_uint

GLbyte      = _ctypes.c_byte
GLshort     = _ctypes.c_short
GLint       = _ctypes.c_int
GLsizei     = _ctypes.c_int

GLubyte     = _ctypes.c_ubyte
GLushort    = _ctypes.c_ushort
GLuint      = _ctypes.c_uint

GLfloat     = _ctypes.c_float
GLclampf    = _ctypes.c_float
GLdouble    = _ctypes.c_double
GLclampd    = _ctypes.c_double

GLvoid      = None              # ctypes.POINTER(None) is ctypes.c_void_p