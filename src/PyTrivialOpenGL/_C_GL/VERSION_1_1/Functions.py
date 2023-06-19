"""
This is an internal module! Shouldn't by imported outside of PyTrivialOpenGL package.

Contains all functions of OpenGL 1.1.
"""
import ctypes as _ctypes
from .Types import *    # internal module, can be loaded as a whole

### Internal ###

_POINTER = _ctypes.POINTER

### Libraries ###

_OpenGL32 = _ctypes.windll.OpenGL32

### Functions ###

glGetError              = _ctypes.WINFUNCTYPE(GLenum)(
    ("glGetError", _OpenGL32), 
    ()
)

glGetString             = _ctypes.WINFUNCTYPE(_POINTER(GLubyte), GLenum)(
    ("glGetString", _OpenGL32), 
    ((1, "name"), )
)

glGetIntegerv           = _ctypes.WINFUNCTYPE(GLvoid, GLenum, _POINTER(GLint))(
    ("glGetIntegerv", _OpenGL32), 
    ((1, "pname"), (1, "data"))
)

glClearColor            = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat, GLfloat, GLfloat)(
    ("glClearColor", _OpenGL32), 
    ((1, "red"), (1, "green"), (1, "blue"), (1, "alpha"))
)

glClear                 = _ctypes.WINFUNCTYPE(GLvoid, GLbitfield)(
    ("glClear", _OpenGL32), 
    ((1, "mask"), )
)

glBegin                 = _ctypes.WINFUNCTYPE(GLvoid, GLenum)(
    ("glBegin", _OpenGL32), 
    ((1, "mode"), )
)

glEnd                   = _ctypes.WINFUNCTYPE(GLvoid)(
    ("glEnd", _OpenGL32), 
    ()
)

glColor3f               = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat, GLfloat)(
    ("glColor3f", _OpenGL32), 
    ((1, "red"), (1, "green"), (1, "blue"))
)

glVertex2f              = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat)(
    ("glVertex2f", _OpenGL32), 
    ((1, "x"), (1, "y"))
)

glViewport              = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint, GLsizei, GLsizei)(
    ("glViewport", _OpenGL32), 
    ((1, "x"), (1, "y"), (1, "width"), (1, "height"))
)

glPushMatrix            = _ctypes.WINFUNCTYPE(GLvoid)(
    ("glPushMatrix", _OpenGL32), 
    ()
)

glPopMatrix             = _ctypes.WINFUNCTYPE(GLvoid)(
    ("glPopMatrix", _OpenGL32), 
    ()
)

glViewport              = _ctypes.WINFUNCTYPE(GLvoid, GLint, GLint, GLsizei, GLsizei)(
    ("glViewport", _OpenGL32), 
    ((1, "x"), (1, "y"), (1, "width"), (1, "height"))
)

glRotatef               = _ctypes.WINFUNCTYPE(GLvoid, GLfloat, GLfloat, GLfloat, GLfloat)(
    ("glRotatef", _OpenGL32), 
    ((1, "angle"), (1, "x"), (1, "y"), (1, "z"))
)