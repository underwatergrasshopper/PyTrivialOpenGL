import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *
from PyTrivialOpenGL import C_GL
import ctypes
import math


__all__ = [
    "run"
]

def is_close(l_a, l_b, delta):
    if (len(l_a) != len(l_b)):
        return False

    for ix in range(len(l_a)):
        if not math.isclose(l_a[ix], l_b[ix], rel_tol = delta):
            return False

    return True

def list_to_bytes(py_type, list_, c_type):
    return bytes((c_type * len(list_))(*(py_type(item) for item in list_)))

class _Data:
    def __init__(self):
        self.options = set()

_data = _Data()

def do_on_create():
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glClearColor(0, 0, 0.5, 1)
    glLoadIdentity()

    points = [
        -0.3, -0.3, 0.0,
        -0.4, 0.3, 0.0,
        0.5, 0.5, 0.0,
        0.2, 0.1, 0.0,
    ]
    glMap1f(GL_MAP1_VERTEX_3, 0, 1, 3, points)
    glEnable(GL_MAP1_VERTEX_3)

    print("Escape - Exit")
    

def do_on_destroy():
    glPopAttrib()

    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    NUM_OF_STEPS = 100

    glBegin(GL_LINE_STRIP)

    for index in range(NUM_OF_STEPS):
        glEvalCoord1fv([index / NUM_OF_STEPS])

    glEnd()


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
        window_name         = "Bezier Curve (%s)" % (" ".join(options)) if len(options) > 0 else "Bezier Curve",
        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )