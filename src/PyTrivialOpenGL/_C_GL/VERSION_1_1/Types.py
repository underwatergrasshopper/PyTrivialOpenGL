"""
This is an internal module! Shouldn't by imported outside of PyTrivialOpenGL package.

Contains all types of OpenGL 1.1.
"""
import ctypes as _ct

GLenum      = _ct.c_uint
GLboolean   = _ct.c_ubyte
GLbitfield  = _ct.c_uint

GLbyte      = _ct.c_byte
GLshort     = _ct.c_short
GLint       = _ct.c_int
GLsizei     = _ct.c_int

GLubyte     = _ct.c_ubyte
GLushort    = _ct.c_ushort
GLuint      = _ct.c_uint

GLfloat     = _ct.c_float
GLclampf    = _ct.c_float
GLdouble    = _ct.c_double
GLclampd    = _ct.c_double

GLvoid      = None              # ctypes.POINTER(None) is ctypes.c_void_p