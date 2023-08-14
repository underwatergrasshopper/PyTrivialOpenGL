import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *
from PyTrivialOpenGL import C_GL
import ctypes

from ...utility.ExampleSupport import is_close

__all__ = [
    "run"
]

def list_to_bytes(py_type, list_, c_type):
    return bytes((c_type * len(list_))(*(py_type(item) for item in list_)))

class _Data:
    def __init__(self):
        self.options = set()

_data = _Data()

def do_on_create(data):
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glViewport(0, 0, data.width, data.height)

    glClearColor(0, 0, 0.5, 1)

    print(glGetFloatv(GL_COLOR_CLEAR_VALUE))
    print(glGetIntegerv(GL_MAX_TEXTURE_SIZE))
    print(glGetBooleanv(GL_COLOR_WRITEMASK))

    print(glGetBooleanv(GL_COLOR_WRITEMASK) == [GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE])

    vertices = [
        0,      0.5,
        -0.5,   -0.5,
        0.5,    -0.5,
    ]

    glEnableClientState(GL_VERTEX_ARRAY)

    glVertexPointer(2, GL_FLOAT, 0, vertices)
    print("GL_VERTEX_ARRAY_POINTER:", glGetPointerv(GL_VERTEX_ARRAY_POINTER))
    assert is_close(glGetPointerv(GL_VERTEX_ARRAY_POINTER), vertices, 0.01)

    c_vertices = list_to_bytes(float, vertices, C_GL.GLfloat)

    glVertexPointer(2, GL_FLOAT, 0, c_vertices)
    print("GL_VERTEX_ARRAY_POINTER:", glGetPointerv(GL_VERTEX_ARRAY_POINTER))
    assert glGetPointerv(GL_VERTEX_ARRAY_POINTER) == c_vertices
    
    glDisableClientState(GL_VERTEX_ARRAY)

    print("Escape - Exit")
    

def do_on_destroy():
    glPopAttrib()

    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    if "inter" in _data.options:
        if "stride" in _data.options:
            color_and_vertex_array = [
                1, 0, 0,        # color
                0, 0.5, 0,      # vertex
                0,

                0, 1, 0,
                -0.5, -0.5, 0,
                0,

                1, 1, 1,
                0.5, -0.5, 0,
                0,
            ]

            c_color_and_vertex_array = list_to_bytes(float, color_and_vertex_array, C_GL.GLfloat)
        
            glInterleavedArrays(GL_C3F_V3F, 4 * 7, c_color_and_vertex_array)
            glDrawArrays(GL_TRIANGLES, 0, 3)
        else:
            color_and_vertex_array = [
                1, 0, 0,        # color
                0, 0.5, 0,      # vertex

                0, 1, 0,
                -0.5, -0.5, 0,

                1, 1, 1,
                0.5, -0.5, 0,
            ]
        
            glInterleavedArrays(GL_C3F_V3F, 0, color_and_vertex_array)
            glDrawArrays(GL_TRIANGLES, 0, 3)
    else:
        if "stride" in _data.options:
            vertices = [
                0,      0.5,
                0,
                -0.5,   -0.5,
                0,
                0.5,    -0.5,
                0,
            ]

            colors = [
                1, 0, 0,
                0,
                0, 1, 0,
                0,
                0, 0, 1,
                0,
            ]

            glEnableClientState(GL_VERTEX_ARRAY)
            glEnableClientState(GL_COLOR_ARRAY)

            c_vertices = list_to_bytes(float, vertices, C_GL.GLfloat)
            glVertexPointer(2, GL_FLOAT, 4 * 3, c_vertices)

            c_colors = list_to_bytes(float, colors, C_GL.GLfloat)
            glColorPointer(3, GL_FLOAT, 4 * 4, c_colors)

            glDrawArrays(GL_TRIANGLES, 0, 3)

            glDisableClientState(GL_VERTEX_ARRAY)
            glDisableClientState(GL_COLOR_ARRAY)
        else:
            vertices = [
                0,      0.5,
                -0.5,   -0.5,
                0.5,    -0.5,
            ]

            colors = [
                1, 0, 0,
                0, 1, 0,
                0, 0, 1,
            ]

            glEnableClientState(GL_VERTEX_ARRAY)
            glEnableClientState(GL_COLOR_ARRAY)

            glVertexPointer(2, GL_FLOAT, 0, vertices)
            glColorPointer(3, GL_FLOAT, 0, colors)

            glDrawArrays(GL_TRIANGLES, 0, 3)

            glDisableClientState(GL_VERTEX_ARRAY)
            glDisableClientState(GL_COLOR_ARRAY)

def do_on_key(key_id, is_down, extra):
    if not is_down:
        if key_id == togl.KeyId.ESCAPE:
            togl.to_window().request_close()

def do_on_resize(width, height):
    glViewport(0, 0, width, height)

def run(name, options):
    _data.options = options

    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Draw Array (%s)" % (" ".join(options)) if len(options) > 0 else "Draw Array",
        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )