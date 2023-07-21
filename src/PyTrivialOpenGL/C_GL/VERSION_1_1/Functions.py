"""
Contains all functions of OpenGL 1.1.
"""
import ctypes as _ctypes
from .Types import *

### Internal ###

_POINTER = _ctypes.POINTER

### Libraries ###

_OpenGL32 = _ctypes.windll.OpenGL32

### Functions ###

### Command Execution ###

glGetError              = _ctypes.WINFUNCTYPE(GLenum)(
    ("glGetError", _OpenGL32),
    ()
)


### Vertex Specification ###

# Begin and End

glBegin                 = _ctypes.WINFUNCTYPE(GLvoid, GLenum)(
    ("glBegin", _OpenGL32),
    ((1, "mode"),)
)

glEnd                   = _ctypes.WINFUNCTYPE(GLvoid)(
    ("glEnd", _OpenGL32),
    ()
)

# Polygon Edges

glEdgeFlag              = _ctypes.WINFUNCTYPE(GLvoid, GLboolean)(
    ("glEdgeFlag", _OpenGL32),
    ((1, "flag"),)
)

glEdgeFlagv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLboolean))(
    ("glEdgeFlagv", _OpenGL32),
    ((1, "flag"),)
)

# Vertex Specification

glVertex2d              = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble)(
    ("glVertex2d", _OpenGL32),
    ((1, "x"), (1, "y"))
)

glVertex2dv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glVertex2dv", _OpenGL32),
    ((1, "v"),)
)

glVertex2f              = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat)(
    ("glVertex2f", _OpenGL32),
    ((1, "x"), (1, "y"))
)

glVertex2fv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glVertex2fv", _OpenGL32),
    ((1, "v"),)
)

glVertex2i              = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint)(
    ("glVertex2i", _OpenGL32),
    ((1, "x"), (1, "y"))
)

glVertex2iv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLint))(
    ("glVertex2iv", _OpenGL32),
    ((1, "v"),)
)

glVertex2s              = _ctypes.WINFUNCTYPE(GLvoid, GLshort, GLshort)(
    ("glVertex2s", _OpenGL32),
    ((1, "x"), (1, "y"))
)

glVertex2sv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLshort))(
    ("glVertex2sv", _OpenGL32),
    ((1, "v"),)
)

glVertex3d              = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble, GLdouble)(
    ("glVertex3d", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"))
)

glVertex3dv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glVertex3dv", _OpenGL32),
    ((1, "v"),)
)

glVertex3f              = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat, GLfloat)(
    ("glVertex3f", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"))
)

glVertex3fv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glVertex3fv", _OpenGL32),
    ((1, "v"),)
)

glVertex3i              = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint, GLint)(
    ("glVertex3i", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"))
)

glVertex3iv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLint))(
    ("glVertex3iv", _OpenGL32),
    ((1, "v"),)
)

glVertex3s              = _ctypes.WINFUNCTYPE(GLvoid, GLshort, GLshort, GLshort)(
    ("glVertex3s", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"))
)

glVertex3sv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLshort))(
    ("glVertex3sv", _OpenGL32),
    ((1, "v"),)
)

glVertex4d              = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble, GLdouble, GLdouble)(
    ("glVertex4d", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"), (1, "w"))
)

glVertex4dv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glVertex4dv", _OpenGL32),
    ((1, "v"),)
)

glVertex4f              = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat, GLfloat, GLfloat)(
    ("glVertex4f", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"), (1, "w"))
)

glVertex4fv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glVertex4fv", _OpenGL32),
    ((1, "v"),)
)

glVertex4i              = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint, GLint, GLint)(
    ("glVertex4i", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"), (1, "w"))
)

glVertex4iv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLint))(
    ("glVertex4iv", _OpenGL32),
    ((1, "v"),)
)

glVertex4s              = _ctypes.WINFUNCTYPE(GLvoid, GLshort, GLshort, GLshort, GLshort)(
    ("glVertex4s", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"), (1, "w"))
)

glVertex4sv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLshort))(
    ("glVertex4sv", _OpenGL32),
    ((1, "v"),)
)


glTexCoord1d            = _ctypes.WINFUNCTYPE(GLvoid, GLdouble)(
    ("glTexCoord1d", _OpenGL32),
    ((1, "s"),)
)

glTexCoord1dv           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glTexCoord1dv", _OpenGL32),
    ((1, "v"),)
)

glTexCoord1f            = _ctypes.WINFUNCTYPE(GLvoid, GLfloat)(
    ("glTexCoord1f", _OpenGL32),
    ((1, "s"),)
)

glTexCoord1fv           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glTexCoord1fv", _OpenGL32),
    ((1, "v"),)
)

glTexCoord1i            = _ctypes.WINFUNCTYPE(GLvoid, GLint)(
    ("glTexCoord1i", _OpenGL32),
    ((1, "s"),)
)

glTexCoord1iv           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLint))(
    ("glTexCoord1iv", _OpenGL32),
    ((1, "v"),)
)

glTexCoord1s            = _ctypes.WINFUNCTYPE(GLvoid, GLshort)(
    ("glTexCoord1s", _OpenGL32),
    ((1, "s"),)
)

glTexCoord1sv           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLshort))(
    ("glTexCoord1sv", _OpenGL32),
    ((1, "v"),)
)

glTexCoord2d            = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble)(
    ("glTexCoord2d", _OpenGL32),
    ((1, "s"), (1, "t"))
)

glTexCoord2dv           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glTexCoord2dv", _OpenGL32),
    ((1, "v"),)
)

glTexCoord2f            = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat)(
    ("glTexCoord2f", _OpenGL32),
    ((1, "s"), (1, "t"))
)

glTexCoord2fv           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glTexCoord2fv", _OpenGL32),
    ((1, "v"),)
)

glTexCoord2i            = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint)(
    ("glTexCoord2i", _OpenGL32),
    ((1, "s"), (1, "t"))
)

glTexCoord2iv           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLint))(
    ("glTexCoord2iv", _OpenGL32),
    ((1, "v"),)
)

glTexCoord2s            = _ctypes.WINFUNCTYPE(GLvoid, GLshort, GLshort)(
    ("glTexCoord2s", _OpenGL32),
    ((1, "s"), (1, "t"))
)

glTexCoord2sv           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLshort))(
    ("glTexCoord2sv", _OpenGL32),
    ((1, "v"),)
)

glTexCoord3d            = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble, GLdouble)(
    ("glTexCoord3d", _OpenGL32),
    ((1, "s"), (1, "t"), (1, "r"))
)

glTexCoord3dv           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glTexCoord3dv", _OpenGL32),
    ((1, "v"),)
)

glTexCoord3f            = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat, GLfloat)(
    ("glTexCoord3f", _OpenGL32),
    ((1, "s"), (1, "t"), (1, "r"))
)

glTexCoord3fv           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glTexCoord3fv", _OpenGL32),
    ((1, "v"),)
)

glTexCoord3i            = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint, GLint)(
    ("glTexCoord3i", _OpenGL32),
    ((1, "s"), (1, "t"), (1, "r"))
)

glTexCoord3iv           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLint))(
    ("glTexCoord3iv", _OpenGL32),
    ((1, "v"),)
)

glTexCoord3s            = _ctypes.WINFUNCTYPE(GLvoid, GLshort, GLshort, GLshort)(
    ("glTexCoord3s", _OpenGL32),
    ((1, "s"), (1, "t"), (1, "r"))
)

glTexCoord3sv           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLshort))(
    ("glTexCoord3sv", _OpenGL32),
    ((1, "v"),)
)

glTexCoord4d            = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble, GLdouble, GLdouble)(
    ("glTexCoord4d", _OpenGL32),
    ((1, "s"), (1, "t"), (1, "r"), (1, "q"))
)

glTexCoord4dv           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glTexCoord4dv", _OpenGL32),
    ((1, "v"),)
)

glTexCoord4f            = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat, GLfloat, GLfloat)(
    ("glTexCoord4f", _OpenGL32),
    ((1, "s"), (1, "t"), (1, "r"), (1, "q"))
)

glTexCoord4fv           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glTexCoord4fv", _OpenGL32),
    ((1, "v"),)
)

glTexCoord4i            = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint, GLint, GLint)(
    ("glTexCoord4i", _OpenGL32),
    ((1, "s"), (1, "t"), (1, "r"), (1, "q"))
)

glTexCoord4iv           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLint))(
    ("glTexCoord4iv", _OpenGL32),
    ((1, "v"),)
)

glTexCoord4s            = _ctypes.WINFUNCTYPE(GLvoid, GLshort, GLshort, GLshort, GLshort)(
    ("glTexCoord4s", _OpenGL32),
    ((1, "s"), (1, "t"), (1, "r"), (1, "q"))
)

glTexCoord4sv           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLshort))(
    ("glTexCoord4sv", _OpenGL32),
    ((1, "v"),)
)


glNormal3b              = _ctypes.WINFUNCTYPE(GLvoid, GLbyte, GLbyte, GLbyte)(
    ("glNormal3b", _OpenGL32),
    ((1, "nx"), (1, "ny"), (1, "nz"))
)

glNormal3bv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLbyte))(
    ("glNormal3bv", _OpenGL32),
    ((1, "v"),)
)

glNormal3d              = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble, GLdouble)(
    ("glNormal3d", _OpenGL32),
    ((1, "nx"), (1, "ny"), (1, "nz"))
)

glNormal3dv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glNormal3dv", _OpenGL32),
    ((1, "v"),)
)

glNormal3f              = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat, GLfloat)(
    ("glNormal3f", _OpenGL32),
    ((1, "nx"), (1, "ny"), (1, "nz"))
)

glNormal3fv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glNormal3fv", _OpenGL32),
    ((1, "v"),)
)

glNormal3i              = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint, GLint)(
    ("glNormal3i", _OpenGL32),
    ((1, "nx"), (1, "ny"), (1, "nz"))
)

glNormal3iv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLint))(
    ("glNormal3iv", _OpenGL32),
    ((1, "v"),)
)

glNormal3s              = _ctypes.WINFUNCTYPE(GLvoid, GLshort, GLshort, GLshort)(
    ("glNormal3s", _OpenGL32),
    ((1, "nx"), (1, "ny"), (1, "nz"))
)

glNormal3sv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLshort))(
    ("glNormal3sv", _OpenGL32),
    ((1, "v"),)
)


glColor3b               = _ctypes.WINFUNCTYPE(GLvoid, GLbyte, GLbyte, GLbyte)(
    ("glColor3b", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"))
)

glColor3bv              = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLbyte))(
    ("glColor3bv", _OpenGL32),
    ((1, "v"),)
)

glColor3d               = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble, GLdouble)(
    ("glColor3d", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"))
)

glColor3dv              = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glColor3dv", _OpenGL32),
    ((1, "v"),)
)

glColor3f               = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat, GLfloat)(
    ("glColor3f", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"))
)

glColor3fv              = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glColor3fv", _OpenGL32),
    ((1, "v"),)
)

glColor3i               = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint, GLint)(
    ("glColor3i", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"))
)

glColor3iv              = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLint))(
    ("glColor3iv", _OpenGL32),
    ((1, "v"),)
)

glColor3s               = _ctypes.WINFUNCTYPE(GLvoid, GLshort, GLshort, GLshort)(
    ("glColor3s", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"))
)

glColor3sv              = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLshort))(
    ("glColor3sv", _OpenGL32),
    ((1, "v"),)
)

glColor3ub              = _ctypes.WINFUNCTYPE(GLvoid, GLubyte, GLubyte, GLubyte)(
    ("glColor3ub", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"))
)

glColor3ubv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLubyte))(
    ("glColor3ubv", _OpenGL32),
    ((1, "v"),)
)

glColor3ui              = _ctypes.WINFUNCTYPE(GLvoid, GLuint, GLuint, GLuint)(
    ("glColor3ui", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"))
)

glColor3uiv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLuint))(
    ("glColor3uiv", _OpenGL32),
    ((1, "v"),)
)

glColor3us              = _ctypes.WINFUNCTYPE(GLvoid, GLushort, GLushort, GLushort)(
    ("glColor3us", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"))
)

glColor3usv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLushort))(
    ("glColor3usv", _OpenGL32),
    ((1, "v"),)
)

glColor4b               = _ctypes.WINFUNCTYPE(GLvoid, GLbyte, GLbyte, GLbyte, GLbyte)(
    ("glColor4b", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"), (1, "alpha"))
)

glColor4bv              = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLbyte))(
    ("glColor4bv", _OpenGL32),
    ((1, "v"),)
)

glColor4d               = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble, GLdouble, GLdouble)(
    ("glColor4d", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"), (1, "alpha"))
)

glColor4dv              = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glColor4dv", _OpenGL32),
    ((1, "v"),)
)

glColor4f               = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat, GLfloat, GLfloat)(
    ("glColor4f", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"), (1, "alpha"))
)

glColor4fv              = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glColor4fv", _OpenGL32),
    ((1, "v"),)
)

glColor4i               = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint, GLint, GLint)(
    ("glColor4i", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"), (1, "alpha"))
)

glColor4iv              = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLint))(
    ("glColor4iv", _OpenGL32),
    ((1, "v"),)
)

glColor4s               = _ctypes.WINFUNCTYPE(GLvoid, GLshort, GLshort, GLshort, GLshort)(
    ("glColor4s", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"), (1, "alpha"))
)

glColor4sv              = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLshort))(
    ("glColor4sv", _OpenGL32),
    ((1, "v"),)
)

glColor4ub              = _ctypes.WINFUNCTYPE(GLvoid, GLubyte, GLubyte, GLubyte, GLubyte)(
    ("glColor4ub", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"), (1, "alpha"))
)

glColor4ubv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLubyte))(
    ("glColor4ubv", _OpenGL32),
    ((1, "v"),)
)

glColor4ui              = _ctypes.WINFUNCTYPE(GLvoid, GLuint, GLuint, GLuint, GLuint)(
    ("glColor4ui", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"), (1, "alpha"))
)

glColor4uiv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLuint))(
    ("glColor4uiv", _OpenGL32),
    ((1, "v"),)
)

glColor4us              = _ctypes.WINFUNCTYPE(GLvoid, GLushort, GLushort, GLushort, GLushort)(
    ("glColor4us", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"), (1, "alpha"))
)

glColor4usv             = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLushort))(
    ("glColor4usv", _OpenGL32),
    ((1, "v"),)
)


glIndexd                = _ctypes.WINFUNCTYPE(GLvoid, GLdouble)(
    ("glIndexd", _OpenGL32),
    ((1, "c"),)
)

glIndexdv               = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glIndexdv", _OpenGL32),
    ((1, "c"),)
)

glIndexf                = _ctypes.WINFUNCTYPE(GLvoid, GLfloat)(
    ("glIndexf", _OpenGL32),
    ((1, "c"),)
)

glIndexfv               = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glIndexfv", _OpenGL32),
    ((1, "c"),)
)

glIndexi                = _ctypes.WINFUNCTYPE(GLvoid, GLint)(
    ("glIndexi", _OpenGL32),
    ((1, "c"),)
)

glIndexiv               = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLint))(
    ("glIndexiv", _OpenGL32),
    ((1, "c"),)
)

glIndexs                = _ctypes.WINFUNCTYPE(GLvoid, GLshort)(
    ("glIndexs", _OpenGL32),
    ((1, "c"),)
)

glIndexsv               = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLshort))(
    ("glIndexsv", _OpenGL32),
    ((1, "c"),)
)

glIndexub               = _ctypes.WINFUNCTYPE(GLvoid, GLubyte)(
    ("glIndexub", _OpenGL32),
    ((1, "c"),)
)

glIndexubv              = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLubyte))(
    ("glIndexubv", _OpenGL32),
    ((1, "c"),)
)

### Vertex Arrays ###

glVertexPointer         = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLenum, GLsizei, _ctypes.POINTER(GLvoid))(
    ("glVertexPointer", _OpenGL32),
    ((1, "size"), (1, "type_"), (1, "stride"), (1, "pointer"))
)

glNormalPointer         = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLsizei, _ctypes.POINTER(GLvoid))(
    ("glNormalPointer", _OpenGL32),
    ((1, "type_"), (1, "stride"), (1, "pointer"))
)

glColorPointer          = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLenum, GLsizei, _ctypes.POINTER(GLvoid))(
    ("glColorPointer", _OpenGL32),
    ((1, "size"), (1, "type_"), (1, "stride"), (1, "pointer"))
)

glIndexPointer          = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLsizei, _ctypes.POINTER(GLvoid))(
    ("glIndexPointer", _OpenGL32),
    ((1, "type_"), (1, "stride"), (1, "pointer"))
)

glEdgeFlagPointer       = _ctypes.WINFUNCTYPE(GLvoid, GLsizei, _ctypes.POINTER(GLvoid))(
    ("glEdgeFlagPointer", _OpenGL32),
    ((1, "stride"), (1, "pointer"))
)

glTexCoordPointer       = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLenum, GLsizei, _ctypes.POINTER(GLvoid))(
    ("glTexCoordPointer", _OpenGL32),
    ((1, "size"), (1, "type_"), (1, "stride"), (1, "pointer"))
)

glEnableClientState     = _ctypes.WINFUNCTYPE(GLvoid, GLenum)(
    ("glEnableClientState", _OpenGL32),
    ((1, "array"),)
)

glDisableClientState    = _ctypes.WINFUNCTYPE(GLvoid, GLenum)(
    ("glDisableClientState", _OpenGL32),
    ((1, "array"),)
)

glArrayElement          = _ctypes.WINFUNCTYPE(GLvoid, GLint)(
    ("glArrayElement", _OpenGL32),
    ((1, "i"),)
)

# Drawing Commands

glDrawArrays            = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint, GLsizei)(
    ("glDrawArrays", _OpenGL32),
    ((1, "mode"), (1, "first"), (1, "count"))
)

glDrawElements          = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLsizei, GLenum, _ctypes.POINTER(GLvoid))(
    ("glDrawElements", _OpenGL32),
    ((1, "mode"), (1, "count"), (1, "type_"), (1, "indices"))
)

glInterleavedArrays     = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLsizei, _ctypes.POINTER(GLvoid))(
    ("glInterleavedArrays", _OpenGL32),
    ((1, "format_"), (1, "stride"), (1, "pointer"))
)

### Rectangles, Matrices, Texture Coordinates ###

# Rectangles

glRectd                 = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble, GLdouble, GLdouble)(
    ("glRectd", _OpenGL32),
    ((1, "x1"), (1, "y1"), (1, "x2"), (1, "y2"))
)

glRectdv                = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble), _ctypes.POINTER(GLdouble))(
    ("glRectdv", _OpenGL32),
    ((1, "v1"), (1, "v2"))
)

glRectf                 = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat, GLfloat, GLfloat)(
    ("glRectf", _OpenGL32),
    ((1, "x1"), (1, "y1"), (1, "x2"), (1, "y2"))
)

glRectfv                = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat), _ctypes.POINTER(GLfloat))(
    ("glRectfv", _OpenGL32),
    ((1, "v1"), (1, "v2"))
)

glRecti                 = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint, GLint, GLint)(
    ("glRecti", _OpenGL32),
    ((1, "x1"), (1, "y1"), (1, "x2"), (1, "y2"))
)

glRectiv                = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLint), _ctypes.POINTER(GLint))(
    ("glRectiv", _OpenGL32),
    ((1, "v1"), (1, "v2"))
)

glRects                 = _ctypes.WINFUNCTYPE(GLvoid, GLshort, GLshort, GLshort, GLshort)(
    ("glRects", _OpenGL32),
    ((1, "x1"), (1, "y1"), (1, "x2"), (1, "y2"))
)

glRectsv                = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLshort), _ctypes.POINTER(GLshort))(
    ("glRectsv", _OpenGL32),
    ((1, "v1"), (1, "v2"))
)

# Matrices

glMatrixMode            = _ctypes.WINFUNCTYPE(GLvoid, GLenum)(
    ("glMatrixMode", _OpenGL32),
    ((1, "mode"),)
)

glLoadMatrixd           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glLoadMatrixd", _OpenGL32),
    ((1, "m"),)
)

glLoadMatrixf           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glLoadMatrixf", _OpenGL32),
    ((1, "m"),)
)

glMultMatrixd           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glMultMatrixd", _OpenGL32),
    ((1, "m"),)
)

glMultMatrixf           = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glMultMatrixf", _OpenGL32),
    ((1, "m"),)
)

glLoadIdentity          = _ctypes.WINFUNCTYPE(GLvoid)(
    ("glLoadIdentity", _OpenGL32),
    ()
)

glRotated               = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble, GLdouble, GLdouble)(
    ("glRotated", _OpenGL32),
    ((1, "angle"), (1, "x"), (1, "y"), (1, "z"))
)

glRotatef               = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat, GLfloat, GLfloat)(
    ("glRotatef", _OpenGL32),
    ((1, "angle"), (1, "x"), (1, "y"), (1, "z"))
)

glTranslated            = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble, GLdouble)(
    ("glTranslated", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"))
)

glTranslatef            = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat, GLfloat)(
    ("glTranslatef", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"))
)

glScaled                = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble, GLdouble)(
    ("glScaled", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"))
)

glScalef                = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat, GLfloat)(
    ("glScalef", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"))
)

glFrustum               = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble)(
    ("glFrustum", _OpenGL32),
    ((1, "left"), (1, "right"), (1, "bottom"), (1, "top"), (1, "zNear"), (1, "zFar"))
)

glOrtho                 = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble)(
    ("glOrtho", _OpenGL32),
    ((1, "left"), (1, "right"), (1, "bottom"), (1, "top"), (1, "zNear"), (1, "zFar"))
)

glPushMatrix            = _ctypes.WINFUNCTYPE(GLvoid)(
    ("glPushMatrix", _OpenGL32),
    ()
)

glPopMatrix             = _ctypes.WINFUNCTYPE(GLvoid)(
    ("glPopMatrix", _OpenGL32),
    ()
)

# Generating Texture Coordinates

glTexGend               = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, GLdouble)(
    ("glTexGend", _OpenGL32),
    ((1, "coord"), (1, "pname"), (1, "param"))
)

glTexGendv              = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLdouble))(
    ("glTexGendv", _OpenGL32),
    ((1, "coord"), (1, "pname"), (1, "params"))
)

glTexGenf               = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, GLfloat)(
    ("glTexGenf", _OpenGL32),
    ((1, "coord"), (1, "pname"), (1, "param"))
)

glTexGenfv              = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLfloat))(
    ("glTexGenfv", _OpenGL32),
    ((1, "coord"), (1, "pname"), (1, "params"))
)

glTexGeni               = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, GLint)(
    ("glTexGeni", _OpenGL32),
    ((1, "coord"), (1, "pname"), (1, "param"))
)

glTexGeniv              = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLint))(
    ("glTexGeniv", _OpenGL32),
    ((1, "coord"), (1, "pname"), (1, "params"))
)

### Viewport and Clipping ###

# Controlling the Viewport

glDepthRange            = _ctypes.WINFUNCTYPE(GLvoid, GLclampd, GLclampd)(
    ("glDepthRange", _OpenGL32),
    ((1, "zNear"), (1, "zFar"))
)

glViewport              = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint, GLsizei, GLsizei)(
    ("glViewport", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "width"), (1, "height"))
)

# Clipping

glClipPlane             = _ctypes.WINFUNCTYPE(GLvoid, GLenum, _ctypes.POINTER(GLdouble))(
    ("glClipPlane", _OpenGL32),
    ((1, "plane"), (1, "equation"))
)

glGetClipPlane          = _ctypes.WINFUNCTYPE(GLvoid, GLenum, _ctypes.POINTER(GLdouble))(
    ("glGetClipPlane", _OpenGL32),
    ((1, "plane"), (1, "equation"))
)

### Lighting and Color ###

# Lighting/ Lighting Parameter Specification

glMaterialf             = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, GLfloat)(
    ("glMaterialf", _OpenGL32),
    ((1, "face"), (1, "pname"), (1, "param"))
)

glMaterialfv            = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLfloat))(
    ("glMaterialfv", _OpenGL32),
    ((1, "face"), (1, "pname"), (1, "params"))
)

glMateriali             = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, GLint)(
    ("glMateriali", _OpenGL32),
    ((1, "face"), (1, "pname"), (1, "param"))
)

glMaterialiv            = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLint))(
    ("glMaterialiv", _OpenGL32),
    ((1, "face"), (1, "pname"), (1, "params"))
)


glLightf                = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, GLfloat)(
    ("glLightf", _OpenGL32),
    ((1, "light"), (1, "pname"), (1, "param"))
)

glLightfv               = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLfloat))(
    ("glLightfv", _OpenGL32),
    ((1, "light"), (1, "pname"), (1, "params"))
)

glLighti                = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, GLint)(
    ("glLighti", _OpenGL32),
    ((1, "light"), (1, "pname"), (1, "param"))
)

glLightiv               = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLint))(
    ("glLightiv", _OpenGL32),
    ((1, "light"), (1, "pname"), (1, "params"))
)


glLightModelf           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLfloat)(
    ("glLightModelf", _OpenGL32),
    ((1, "pname"), (1, "param"))
)

glLightModelfv          = _ctypes.WINFUNCTYPE(GLvoid, GLenum, _ctypes.POINTER(GLfloat))(
    ("glLightModelfv", _OpenGL32),
    ((1, "pname"), (1, "params"))
)

glLightModeli           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint)(
    ("glLightModeli", _OpenGL32),
    ((1, "pname"), (1, "param"))
)

glLightModeliv          = _ctypes.WINFUNCTYPE(GLvoid, GLenum, _ctypes.POINTER(GLint))(
    ("glLightModeliv", _OpenGL32),
    ((1, "pname"), (1, "params"))
)

# ColorMaterial 

glColorMaterial         = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum)(
    ("glColorMaterial", _OpenGL32),
    ((1, "face"), (1, "mode"))
)

# Flatshading

glShadeModel            = _ctypes.WINFUNCTYPE(GLvoid, GLenum)(
    ("glShadeModel", _OpenGL32),
    ((1, "mode"),)
)

# Queries

glGetLightfv            = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLfloat))(
    ("glGetLightfv", _OpenGL32),
    ((1, "light"), (1, "pname"), (1, "params"))
)

glGetLightiv            = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLint))(
    ("glGetLightiv", _OpenGL32),
    ((1, "light"), (1, "pname"), (1, "params"))
)

glGetMaterialfv         = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLfloat))(
    ("glGetMaterialfv", _OpenGL32),
    ((1, "face"), (1, "pname"), (1, "params"))
)

glGetMaterialiv         = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLint))(
    ("glGetMaterialiv", _OpenGL32),
    ((1, "face"), (1, "pname"), (1, "params"))
)

### Rendering Control and Queries ###

# Current Raster Position

glRasterPos2d           = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble)(
    ("glRasterPos2d", _OpenGL32),
    ((1, "x"), (1, "y"))
)

glRasterPos2dv          = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glRasterPos2dv", _OpenGL32),
    ((1, "v"),)
)

glRasterPos2f           = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat)(
    ("glRasterPos2f", _OpenGL32),
    ((1, "x"), (1, "y"))
)

glRasterPos2fv          = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glRasterPos2fv", _OpenGL32),
    ((1, "v"),)
)

glRasterPos2i           = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint)(
    ("glRasterPos2i", _OpenGL32),
    ((1, "x"), (1, "y"))
)

glRasterPos2iv          = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLint))(
    ("glRasterPos2iv", _OpenGL32),
    ((1, "v"),)
)

glRasterPos2s           = _ctypes.WINFUNCTYPE(GLvoid, GLshort, GLshort)(
    ("glRasterPos2s", _OpenGL32),
    ((1, "x"), (1, "y"))
)

glRasterPos2sv          = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLshort))(
    ("glRasterPos2sv", _OpenGL32),
    ((1, "v"),)
)

glRasterPos3d           = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble, GLdouble)(
    ("glRasterPos3d", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"))
)

glRasterPos3dv          = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glRasterPos3dv", _OpenGL32),
    ((1, "v"),)
)

glRasterPos3f           = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat, GLfloat)(
    ("glRasterPos3f", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"))
)

glRasterPos3fv          = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glRasterPos3fv", _OpenGL32),
    ((1, "v"),)
)

glRasterPos3i           = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint, GLint)(
    ("glRasterPos3i", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"))
)

glRasterPos3iv          = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLint))(
    ("glRasterPos3iv", _OpenGL32),
    ((1, "v"),)
)

glRasterPos3s           = _ctypes.WINFUNCTYPE(GLvoid, GLshort, GLshort, GLshort)(
    ("glRasterPos3s", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"))
)

glRasterPos3sv          = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLshort))(
    ("glRasterPos3sv", _OpenGL32),
    ((1, "v"),)
)

glRasterPos4d           = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble, GLdouble, GLdouble)(
    ("glRasterPos4d", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"), (1, "w"))
)

glRasterPos4dv          = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glRasterPos4dv", _OpenGL32),
    ((1, "v"),)
)

glRasterPos4f           = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat, GLfloat, GLfloat)(
    ("glRasterPos4f", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"), (1, "w"))
)

glRasterPos4fv          = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glRasterPos4fv", _OpenGL32),
    ((1, "v"),)
)

glRasterPos4i           = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint, GLint, GLint)(
    ("glRasterPos4i", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"), (1, "w"))
)

glRasterPos4iv          = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLint))(
    ("glRasterPos4iv", _OpenGL32),
    ((1, "v"),)
)

glRasterPos4s           = _ctypes.WINFUNCTYPE(GLvoid, GLshort, GLshort, GLshort, GLshort)(
    ("glRasterPos4s", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "z"), (1, "w"))
)

glRasterPos4sv          = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLshort))(
    ("glRasterPos4sv", _OpenGL32),
    ((1, "v"),)
)

### Rasterization ###

# Points

glPointSize             = _ctypes.WINFUNCTYPE(GLvoid, GLfloat)(
    ("glPointSize", _OpenGL32),
    ((1, "size"),)
)

# Line Segments

glLineWidth             = _ctypes.WINFUNCTYPE(GLvoid, GLfloat)(
    ("glLineWidth", _OpenGL32),
    ((1, "width"),)
)

# Other Line Segments Features

glLineStipple           = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLushort)(
    ("glLineStipple", _OpenGL32),
    ((1, "factor"), (1, "pattern"))
)

# Stipple Query

glGetPolygonStipple     = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLubyte))(
    ("glGetPolygonStipple", _OpenGL32),
    ((1, "mask"),)
)

# Polygons

glFrontFace             = _ctypes.WINFUNCTYPE(GLvoid, GLenum)(
    ("glFrontFace", _OpenGL32),
    ((1, "mode"),)
)

glCullFace              = _ctypes.WINFUNCTYPE(GLvoid, GLenum)(
    ("glCullFace", _OpenGL32),
    ((1, "mode"),)
)

# Stippling

glPolygonStipple        = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLubyte))(
    ("glPolygonStipple", _OpenGL32),
    ((1, "mask"),)
)

# Polygon Rasterization & Depth Offset

glPolygonMode           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum)(
    ("glPolygonMode", _OpenGL32),
    ((1, "face"), (1, "mode"))
)

glPolygonOffset         = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat)(
    ("glPolygonOffset", _OpenGL32),
    ((1, "factor"), (1, "units"))
)

# Pixel Rectangles

glPixelStoref           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLfloat)(
    ("glPixelStoref", _OpenGL32),
    ((1, "pname"), (1, "param"))
)

glPixelStorei           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint)(
    ("glPixelStorei", _OpenGL32),
    ((1, "pname"), (1, "param"))
)

# Pixel Transfer Modes

glPixelTransferf        = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLfloat)(
    ("glPixelTransferf", _OpenGL32),
    ((1, "pname"), (1, "param"))
)

glPixelTransferi        = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint)(
    ("glPixelTransferi", _OpenGL32),
    ((1, "pname"), (1, "param"))
)


glPixelMapfv            = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLsizei, _ctypes.POINTER(GLfloat))(
    ("glPixelMapfv", _OpenGL32),
    ((1, "map_"), (1, "mapsize"), (1, "values"))
)

glPixelMapuiv           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLsizei, _ctypes.POINTER(GLuint))(
    ("glPixelMapuiv", _OpenGL32),
    ((1, "map_"), (1, "mapsize"), (1, "values"))
)

glPixelMapusv           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLsizei, _ctypes.POINTER(GLushort))(
    ("glPixelMapusv", _OpenGL32),
    ((1, "map_"), (1, "mapsize"), (1, "values"))
)

# Enumerated Queries

glGetPixelMapfv         = _ctypes.WINFUNCTYPE(GLvoid, GLenum, _ctypes.POINTER(GLfloat))(
    ("glGetPixelMapfv", _OpenGL32),
    ((1, "map_"), (1, "values"))
)

glGetPixelMapuiv        = _ctypes.WINFUNCTYPE(GLvoid, GLenum, _ctypes.POINTER(GLuint))(
    ("glGetPixelMapuiv", _OpenGL32),
    ((1, "map_"), (1, "values"))
)

glGetPixelMapusv        = _ctypes.WINFUNCTYPE(GLvoid, GLenum, _ctypes.POINTER(GLushort))(
    ("glGetPixelMapusv", _OpenGL32),
    ((1, "map_"), (1, "values"))
)

# Rasterization of Pixel Rectangles

glDrawPixels            = _ctypes.WINFUNCTYPE(GLvoid, GLsizei, GLsizei, GLenum, GLenum, _ctypes.POINTER(GLvoid))(
    ("glDrawPixels", _OpenGL32),
    ((1, "width"), (1, "height"), (1, "format_"), (1, "type_"), (1, "pixels"))
)

glPixelZoom             = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat)(
    ("glPixelZoom", _OpenGL32),
    ((1, "xfactor"), (1, "yfactor"))
)

# Bitmaps

glBitmap                = _ctypes.WINFUNCTYPE(GLvoid, GLsizei, GLsizei, GLfloat, GLfloat, GLfloat, GLfloat, _ctypes.POINTER(GLubyte))(
    ("glBitmap", _OpenGL32),
    ((1, "width"), (1, "height"), (1, "xorig"), (1, "yorig"), (1, "xmove"), (1, "ymove"), (1, "bitmap"))
)

### Texturing ###

# Texture Image Specification

glTexImage1D            = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint, GLint, GLsizei, GLint, GLenum, GLenum, _ctypes.POINTER(GLvoid))(
    ("glTexImage1D", _OpenGL32),
    ((1, "target"), (1, "level"), (1, "internalformat"), (1, "width"), (1, "border"), (1, "format_"), (1, "type_"), (1, "pixels"))
)

glTexImage2D            = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint, GLint, GLsizei, GLsizei, GLint, GLenum, GLenum, _ctypes.POINTER(GLvoid))(
    ("glTexImage2D", _OpenGL32),
    ((1, "target"), (1, "level"), (1, "internalformat"), (1, "width"), (1, "height"), (1, "border"), (1, "format_"), (1, "type_"), (1, "pixels"))
)

# Alt. Texture Image Specification Commands 

glCopyTexImage1D        = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLint)(
    ("glCopyTexImage1D", _OpenGL32),
    ((1, "target"), (1, "level"), (1, "internalFormat"), (1, "x"), (1, "y"), (1, "width"), (1, "border"))
)

glCopyTexImage2D        = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLsizei, GLint)(
    ("glCopyTexImage2D", _OpenGL32),
    ((1, "target"), (1, "level"), (1, "internalFormat"), (1, "x"), (1, "y"), (1, "width"), (1, "height"), (1, "border"))
)

glTexSubImage1D         = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint, GLint, GLsizei, GLenum, GLenum, _ctypes.POINTER(GLvoid))(
    ("glTexSubImage1D", _OpenGL32),
    ((1, "target"), (1, "level"), (1, "xoffset"), (1, "width"), (1, "format_"), (1, "type_"), (1, "pixels"))
)

glTexSubImage2D         = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, _ctypes.POINTER(GLvoid))(
    ("glTexSubImage2D", _OpenGL32),
    ((1, "target"), (1, "level"), (1, "xoffset"), (1, "yoffset"), (1, "width"), (1, "height"), (1, "format_"), (1, "type_"), (1, "pixels"))
)

glCopyTexSubImage1D     = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint, GLint, GLint, GLint, GLsizei)(
    ("glCopyTexSubImage1D", _OpenGL32),
    ((1, "target"), (1, "level"), (1, "xoffset"), (1, "x"), (1, "y"), (1, "width"))
)

glCopyTexSubImage2D     = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei)(
    ("glCopyTexSubImage2D", _OpenGL32),
    ((1, "target"), (1, "level"), (1, "xoffset"), (1, "yoffset"), (1, "x"), (1, "y"), (1, "width"), (1, "height"))
)

# Texture Parameters

glTexParameterf         = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, GLfloat)(
    ("glTexParameterf", _OpenGL32),
    ((1, "target"), (1, "pname"), (1, "param"))
)

glTexParameterfv        = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLfloat))(
    ("glTexParameterfv", _OpenGL32),
    ((1, "target"), (1, "pname"), (1, "params"))
)

glTexParameteri         = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, GLint)(
    ("glTexParameteri", _OpenGL32),
    ((1, "target"), (1, "pname"), (1, "param"))
)

glTexParameteriv        = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLint))(
    ("glTexParameteriv", _OpenGL32),
    ((1, "target"), (1, "pname"), (1, "params"))
)

# Texture Objects

glBindTexture           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLuint)(
    ("glBindTexture", _OpenGL32),
    ((1, "target"), (1, "texture"))
)

glDeleteTextures        = _ctypes.WINFUNCTYPE(GLvoid, GLsizei, _ctypes.POINTER(GLuint))(
    ("glDeleteTextures", _OpenGL32),
    ((1, "n"), (1, "textures"))
)

glGenTextures           = _ctypes.WINFUNCTYPE(GLvoid, GLsizei, _ctypes.POINTER(GLuint))(
    ("glGenTextures", _OpenGL32),
    ((1, "n"), (1, "textures"))
)

glAreTexturesResident   = _ctypes.WINFUNCTYPE(GLboolean, GLsizei, _ctypes.POINTER(GLuint), _ctypes.POINTER(GLboolean))(
    ("glAreTexturesResident", _OpenGL32),
    ((1, "n"), (1, "textures"), (1, "residences"))
)

glPrioritizeTextures    = _ctypes.WINFUNCTYPE(GLvoid, GLsizei, _ctypes.POINTER(GLuint), _ctypes.POINTER(GLclampf))(
    ("glPrioritizeTextures", _OpenGL32),
    ((1, "n"), (1, "textures"), (1, "priorities"))
)

# Texture Environments & Texture Functions 

glTexEnvf               = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, GLfloat)(
    ("glTexEnvf", _OpenGL32),
    ((1, "target"), (1, "pname"), (1, "param"))
)

glTexEnvfv              = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLfloat))(
    ("glTexEnvfv", _OpenGL32),
    ((1, "target"), (1, "pname"), (1, "params"))
)

glTexEnvi               = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, GLint)(
    ("glTexEnvi", _OpenGL32),
    ((1, "target"), (1, "pname"), (1, "param"))
)

glTexEnviv              = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLint))(
    ("glTexEnviv", _OpenGL32),
    ((1, "target"), (1, "pname"), (1, "params"))
)

# Enumerated Queries

glGetTexEnvfv           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLfloat))(
    ("glGetTexEnvfv", _OpenGL32),
    ((1, "target"), (1, "pname"), (1, "params"))
)

glGetTexEnviv           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLint))(
    ("glGetTexEnviv", _OpenGL32),
    ((1, "target"), (1, "pname"), (1, "params"))
)

glGetTexGendv           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLdouble))(
    ("glGetTexGendv", _OpenGL32),
    ((1, "coord"), (1, "pname"), (1, "params"))
)

glGetTexGenfv           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLfloat))(
    ("glGetTexGenfv", _OpenGL32),
    ((1, "coord"), (1, "pname"), (1, "params"))
)

glGetTexGeniv           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLint))(
    ("glGetTexGeniv", _OpenGL32),
    ((1, "coord"), (1, "pname"), (1, "params"))
)


glGetTexParameterfv     = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLfloat))(
    ("glGetTexParameterfv", _OpenGL32),
    ((1, "target"), (1, "pname"), (1, "params"))
)

glGetTexParameteriv     = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLint))(
    ("glGetTexParameteriv", _OpenGL32),
    ((1, "target"), (1, "pname"), (1, "params"))
)

glGetTexLevelParameterfv= _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint, GLenum, _ctypes.POINTER(GLfloat))(
    ("glGetTexLevelParameterfv", _OpenGL32),
    ((1, "target"), (1, "level"), (1, "pname"), (1, "params"))
)

glGetTexLevelParameteriv= _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint, GLenum, _ctypes.POINTER(GLint))(
    ("glGetTexLevelParameteriv", _OpenGL32),
    ((1, "target"), (1, "level"), (1, "pname"), (1, "params"))
)

# Texture Queries

glGetTexImage           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint, GLenum, GLenum, _ctypes.POINTER(GLvoid))(
    ("glGetTexImage", _OpenGL32),
    ((1, "target"), (1, "level"), (1, "format_"), (1, "type_"), (1, "pixels"))
)

glIsTexture             = _ctypes.WINFUNCTYPE(GLboolean, GLuint)(
    ("glIsTexture", _OpenGL32),
    ((1, "texture"),)
)

### Color Sum, Fog, and Hints  ###

# Fog

glFogf                  = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLfloat)(
    ("glFogf", _OpenGL32),
    ((1, "pname"), (1, "param"))
)

glFogfv                 = _ctypes.WINFUNCTYPE(GLvoid, GLenum, _ctypes.POINTER(GLfloat))(
    ("glFogfv", _OpenGL32),
    ((1, "pname"), (1, "params"))
)

glFogi                  = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint)(
    ("glFogi", _OpenGL32),
    ((1, "pname"), (1, "param"))
)

glFogiv                 = _ctypes.WINFUNCTYPE(GLvoid, GLenum, _ctypes.POINTER(GLint))(
    ("glFogiv", _OpenGL32),
    ((1, "pname"), (1, "params"))
)

# Hints

glHint                  = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum)(
    ("glHint", _OpenGL32),
    ((1, "target"), (1, "mode"))
)

### Drawing, Reading, and Copying Pixels ###

# Reading Pixels

glReadPixels            = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, _ctypes.POINTER(GLvoid))(
    ("glReadPixels", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "width"), (1, "height"), (1, "format_"), (1, "type_"), (1, "pixels"))
)

glReadBuffer            = _ctypes.WINFUNCTYPE(GLvoid, GLenum)(
    ("glReadBuffer", _OpenGL32),
    ((1, "mode"),)
)

# Copying Pixels

glCopyPixels            = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint, GLsizei, GLsizei, GLenum)(
    ("glCopyPixels", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "width"), (1, "height"), (1, "type_"))
)

### Per-Fragment Operations ###

# Scissor Test

glScissor               = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint, GLsizei, GLsizei)(
    ("glScissor", _OpenGL32),
    ((1, "x"), (1, "y"), (1, "width"), (1, "height"))
)

# Alpha Test

glAlphaFunc             = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLclampf)(
    ("glAlphaFunc", _OpenGL32),
    ((1, "func"), (1, "ref"))
)

# Stencil Test

glStencilFunc           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint, GLuint)(
    ("glStencilFunc", _OpenGL32),
    ((1, "func"), (1, "ref"), (1, "mask"))
)

glStencilOp             = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, GLenum)(
    ("glStencilOp", _OpenGL32),
    ((1, "fail"), (1, "zfail"), (1, "zpass"))
)

# Depth Buffer Test

glDepthFunc             = _ctypes.WINFUNCTYPE(GLvoid, GLenum)(
    ("glDepthFunc", _OpenGL32),
    ((1, "func"),)
)


# Blending

glBlendFunc             = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum)(
    ("glBlendFunc", _OpenGL32),
    ((1, "sfactor"), (1, "dfactor"))
)

# Logical Operation 

glLogicOp               = _ctypes.WINFUNCTYPE(GLvoid, GLenum)(
    ("glLogicOp", _OpenGL32),
    ((1, "opcode"),)
)

### Whole Framebuffer Operations ###

# Selecting a Buffer for Writing

glDrawBuffer            = _ctypes.WINFUNCTYPE(GLvoid, GLenum)(
    ("glDrawBuffer", _OpenGL32),
    ((1, "mode"),)
)

# Fine Control of Buffer Updates

glIndexMask             = _ctypes.WINFUNCTYPE(GLvoid, GLuint)(
    ("glIndexMask", _OpenGL32),
    ((1, "mask"),)
)

glColorMask             = _ctypes.WINFUNCTYPE(GLvoid, GLboolean, GLboolean, GLboolean, GLboolean)(
    ("glColorMask", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"), (1, "alpha"))
)

glDepthMask             = _ctypes.WINFUNCTYPE(GLvoid, GLboolean)(
    ("glDepthMask", _OpenGL32),
    ((1, "flag"),)
)

glStencilMask           = _ctypes.WINFUNCTYPE(GLvoid, GLuint)(
    ("glStencilMask", _OpenGL32),
    ((1, "mask"),)
)

# Clearing the Buffers

glClear                 = _ctypes.WINFUNCTYPE(GLvoid, GLbitfield)(
    ("glClear", _OpenGL32),
    ((1, "mask"),)
)

glClearColor            = _ctypes.WINFUNCTYPE(GLvoid, GLclampf, GLclampf, GLclampf, GLclampf)(
    ("glClearColor", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"), (1, "alpha"))
)

glClearIndex            = _ctypes.WINFUNCTYPE(GLvoid, GLfloat)(
    ("glClearIndex", _OpenGL32),
    ((1, "c"),)
)

glClearDepth            = _ctypes.WINFUNCTYPE(GLvoid, GLclampd)(
    ("glClearDepth", _OpenGL32),
    ((1, "depth"),)
)

glClearStencil          = _ctypes.WINFUNCTYPE(GLvoid, GLint)(
    ("glClearStencil", _OpenGL32),
    ((1, "s"),)
)

glClearAccum            = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat, GLfloat, GLfloat)(
    ("glClearAccum", _OpenGL32),
    ((1, "red"), (1, "green"), (1, "blue"), (1, "alpha"))
)

# Accumulation Buffer

glAccum                 = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLfloat)(
    ("glAccum", _OpenGL32),
    ((1, "op"), (1, "value"))
)

### Special Functions ###

# Evaluators

glMap1d                 = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLdouble, GLdouble, GLint, GLint, _ctypes.POINTER(GLdouble))(
    ("glMap1d", _OpenGL32),
    ((1, "target"), (1, "u1"), (1, "u2"), (1, "stride"), (1, "order"), (1, "points"))
)

glMap1f                 = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLfloat, GLfloat, GLint, GLint, _ctypes.POINTER(GLfloat))(
    ("glMap1f", _OpenGL32),
    ((1, "target"), (1, "u1"), (1, "u2"), (1, "stride"), (1, "order"), (1, "points"))
)

glMap2d                 = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLdouble, GLdouble, GLint, GLint, GLdouble, GLdouble, GLint, GLint, _ctypes.POINTER(GLdouble))(
    ("glMap2d", _OpenGL32),
    ((1, "target"), (1, "u1"), (1, "u2"), (1, "ustride"), (1, "uorder"), (1, "v1"), (1, "v2"), (1, "vstride"), (1, "vorder"), (1, "points"))
)

glMap2f                 = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLfloat, GLfloat, GLint, GLint, GLfloat, GLfloat, GLint, GLint, _ctypes.POINTER(GLfloat))(
    ("glMap2f", _OpenGL32),
    ((1, "target"), (1, "u1"), (1, "u2"), (1, "ustride"), (1, "uorder"), (1, "v1"), (1, "v2"), (1, "vstride"), (1, "vorder"), (1, "points"))
)


glEvalCoord1d           = _ctypes.WINFUNCTYPE(GLvoid, GLdouble)(
    ("glEvalCoord1d", _OpenGL32),
    ((1, "u"),)
)

glEvalCoord1dv          = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glEvalCoord1dv", _OpenGL32),
    ((1, "u"),)
)

glEvalCoord1f           = _ctypes.WINFUNCTYPE(GLvoid, GLfloat)(
    ("glEvalCoord1f", _OpenGL32),
    ((1, "u"),)
)

glEvalCoord1fv          = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glEvalCoord1fv", _OpenGL32),
    ((1, "u"),)
)

glEvalCoord2d           = _ctypes.WINFUNCTYPE(GLvoid, GLdouble, GLdouble)(
    ("glEvalCoord2d", _OpenGL32),
    ((1, "u"), (1, "v"))
)

glEvalCoord2dv          = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLdouble))(
    ("glEvalCoord2dv", _OpenGL32),
    ((1, "u"),)
)

glEvalCoord2f           = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat)(
    ("glEvalCoord2f", _OpenGL32),
    ((1, "u"), (1, "v"))
)

glEvalCoord2fv          = _ctypes.WINFUNCTYPE(GLvoid, _ctypes.POINTER(GLfloat))(
    ("glEvalCoord2fv", _OpenGL32),
    ((1, "u"),)
)


glMapGrid1d             = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLdouble, GLdouble)(
    ("glMapGrid1d", _OpenGL32),
    ((1, "un"), (1, "u1"), (1, "u2"))
)

glMapGrid1f             = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLfloat, GLfloat)(
    ("glMapGrid1f", _OpenGL32),
    ((1, "un"), (1, "u1"), (1, "u2"))
)

glMapGrid2d             = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLdouble, GLdouble, GLint, GLdouble, GLdouble)(
    ("glMapGrid2d", _OpenGL32),
    ((1, "un"), (1, "u1"), (1, "u2"), (1, "vn"), (1, "v1"), (1, "v2"))
)

glMapGrid2f             = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLfloat, GLfloat, GLint, GLfloat, GLfloat)(
    ("glMapGrid2f", _OpenGL32),
    ((1, "un"), (1, "u1"), (1, "u2"), (1, "vn"), (1, "v1"), (1, "v2"))
)


glEvalMesh1             = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint, GLint)(
    ("glEvalMesh1", _OpenGL32),
    ((1, "mode"), (1, "i1"), (1, "i2"))
)

glEvalMesh2             = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLint, GLint, GLint, GLint)(
    ("glEvalMesh2", _OpenGL32),
    ((1, "mode"), (1, "i1"), (1, "i2"), (1, "j1"), (1, "j2"))
)


glEvalPoint1            = _ctypes.WINFUNCTYPE(GLvoid, GLint)(
    ("glEvalPoint1", _OpenGL32),
    ((1, "i"),)
)

glEvalPoint2            = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint)(
    ("glEvalPoint2", _OpenGL32),
    ((1, "i"), (1, "j"))
)

# Enumerated Query

glGetMapdv              = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLdouble))(
    ("glGetMapdv", _OpenGL32),
    ((1, "target"), (1, "query"), (1, "v"))
)

glGetMapfv              = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLfloat))(
    ("glGetMapfv", _OpenGL32),
    ((1, "target"), (1, "query"), (1, "v"))
)

glGetMapiv              = _ctypes.WINFUNCTYPE(GLvoid, GLenum, GLenum, _ctypes.POINTER(GLint))(
    ("glGetMapiv", _OpenGL32),
    ((1, "target"), (1, "query"), (1, "v"))
)

# Selection

glInitNames             = _ctypes.WINFUNCTYPE(GLvoid)(
    ("glInitNames", _OpenGL32),
    ()
)

glPopName               = _ctypes.WINFUNCTYPE(GLvoid)(
    ("glPopName", _OpenGL32),
    ()
)

glPushName              = _ctypes.WINFUNCTYPE(GLvoid, GLuint)(
    ("glPushName", _OpenGL32),
    ((1, "name"),)
)

glLoadName              = _ctypes.WINFUNCTYPE(GLvoid, GLuint)(
    ("glLoadName", _OpenGL32),
    ((1, "name"),)
)

glRenderMode            = _ctypes.WINFUNCTYPE(GLint, GLenum)(
    ("glRenderMode", _OpenGL32),
    ((1, "mode"),)
)

glSelectBuffer          = _ctypes.WINFUNCTYPE(GLvoid, GLsizei, _ctypes.POINTER(GLuint))(
    ("glSelectBuffer", _OpenGL32),
    ((1, "size"), (1, "buffer"))
)

# Feedback

glFeedbackBuffer        = _ctypes.WINFUNCTYPE(GLvoid, GLsizei, GLenum, _ctypes.POINTER(GLfloat))(
    ("glFeedbackBuffer", _OpenGL32),
    ((1, "size"), (1, "type_"), (1, "buffer"))
)

glPassThrough           = _ctypes.WINFUNCTYPE(GLvoid, GLfloat)(
    ("glPassThrough", _OpenGL32),
    ((1, "token"),)
)

# Display Lists

glNewList               = _ctypes.WINFUNCTYPE(GLvoid, GLuint, GLenum)(
    ("glNewList", _OpenGL32),
    ((1, "list_"), (1, "mode"))
)

glEndList               = _ctypes.WINFUNCTYPE(GLvoid)(
    ("glEndList", _OpenGL32),
    ()
)

glCallList              = _ctypes.WINFUNCTYPE(GLvoid, GLuint)(
    ("glCallList", _OpenGL32),
    ((1, "list_"),)
)

glCallLists             = _ctypes.WINFUNCTYPE(GLvoid, GLsizei, GLenum, _ctypes.POINTER(GLvoid))(
    ("glCallLists", _OpenGL32),
    ((1, "n"), (1, "type_"), (1, "lists"))
)

glListBase              = _ctypes.WINFUNCTYPE(GLvoid, GLuint)(
    ("glListBase", _OpenGL32),
    ((1, "base"),)
)

glGenLists              = _ctypes.WINFUNCTYPE(GLuint, GLsizei)(
    ("glGenLists", _OpenGL32),
    ((1, "range_"),)
)

glIsList                = _ctypes.WINFUNCTYPE(GLboolean, GLuint)(
    ("glIsList", _OpenGL32),
    ((1, "list_"),)
)

glDeleteLists           = _ctypes.WINFUNCTYPE(GLvoid, GLuint, GLsizei)(
    ("glDeleteLists", _OpenGL32),
    ((1, "list_"), (1, "range_"))
)

### Synchronization ###

# Flush and Finish 

glFlush                 = _ctypes.WINFUNCTYPE(GLvoid)(
    ("glFlush", _OpenGL32),
    ()
)

glFinish                = _ctypes.WINFUNCTYPE(GLvoid)(
    ("glFinish", _OpenGL32),
    ()
)


### State and State Requests  ###

glDisable               = _ctypes.WINFUNCTYPE(GLvoid, GLenum)(
    ("glDisable", _OpenGL32),
    ((1, "cap"),)
)

glEnable                = _ctypes.WINFUNCTYPE(GLvoid, GLenum)(
    ("glEnable", _OpenGL32),
    ((1, "cap"),)
)


# Simple Queries

glGetBooleanv           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, _ctypes.POINTER(GLboolean))(
    ("glGetBooleanv", _OpenGL32),
    ((1, "pname"), (1, "params"))
)

glGetIntegerv           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, _ctypes.POINTER(GLint))(
    ("glGetIntegerv", _OpenGL32),
    ((1, "pname"), (1, "params"))
)

glGetFloatv             = _ctypes.WINFUNCTYPE(GLvoid, GLenum, _ctypes.POINTER(GLfloat))(
    ("glGetFloatv", _OpenGL32),
    ((1, "pname"), (1, "params"))
)

glGetDoublev            = _ctypes.WINFUNCTYPE(GLvoid, GLenum, _ctypes.POINTER(GLdouble))(
    ("glGetDoublev", _OpenGL32),
    ((1, "pname"), (1, "params"))
)

glIsEnabled             = _ctypes.WINFUNCTYPE(GLboolean, GLenum)(
    ("glIsEnabled", _OpenGL32),
    ((1, "cap"),)
)

# Pointer and String Queries 

glGetPointerv           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, _ctypes.POINTER(_ctypes.POINTER(GLvoid)))(
    ("glGetPointerv", _OpenGL32),
    ((1, "pname"), (1, "params"))
)

glGetString             = _ctypes.WINFUNCTYPE(_ctypes.POINTER(GLubyte), GLenum)(
    ("glGetString", _OpenGL32),
    ((1, "name"),)
)

# Saving and Restoring State

glPushAttrib            = _ctypes.WINFUNCTYPE(GLvoid, GLbitfield)(
    ("glPushAttrib", _OpenGL32),
    ((1, "mask"),)
)

glPushClientAttrib      = _ctypes.WINFUNCTYPE(GLvoid, GLbitfield)(
    ("glPushClientAttrib", _OpenGL32),
    ((1, "mask"),)
)

glPopAttrib             = _ctypes.WINFUNCTYPE(GLvoid)(
    ("glPopAttrib", _OpenGL32),
    ()
)

glPopClientAttrib       = _ctypes.WINFUNCTYPE(GLvoid)(
    ("glPopClientAttrib", _OpenGL32),
    ()
)

