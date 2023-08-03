import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *
from PyTrivialOpenGL import C_GL
import ctypes
import math

__all__ = [
    "run"
]

class HitRecord:
    def __init__(self, z_min, z_max, names):
        self.z_min = z_min
        self.z_max = z_max
        self.names = names

def do_on_create():
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glClearColor(0, 0, 0.5, 1)

    print("Escape - Exit")

def do_on_destroy():
    glPopAttrib()

    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    LENGTH = 32
    c_buffer = (C_GL.GLuint * LENGTH)()
    C_GL.glSelectBuffer(LENGTH, c_buffer)
    C_GL.glRenderMode(GL_SELECT)

    C_GL.glInitNames()
    C_GL.glPushName(0)

    C_GL.glLoadName(1)
    glColor3f(1, 0, 0)
    glRectd(-0.5, -0.5, 0.5, 0.5)
    
    C_GL.glLoadName(2)
    glColor3f(0, 1, 0)
    glRectd(-1.2, -1.2, -0.4, -0.4)
    
    # is out of view, won't hit
    C_GL.glLoadName(3)
    glColor3f(1, 1, 0)
    glRectd(-2, -2, -1.2, -1.2)

    C_GL.glFlush()
    number_of_hits = C_GL.glRenderMode(GL_RENDER)

    assert number_of_hits == 2
    buffer = [int(e) for e in c_buffer]

    hit_records = []
    index = 0
    while index < len(buffer):
        num_of_names = buffer[index]
        index += 1

        if num_of_names == 0:
            break

        z_min = buffer[index] / 0x7FFFFFFF
        index += 1

        z_max = buffer[index] / 0x7FFFFFFF
        index += 1

        names = [buffer[name_ix] for name_ix in range(index, index + num_of_names)]
        index += num_of_names

        hit_records.append(HitRecord(z_min, z_max, names))

    assert len(hit_records) == 2

    assert math.isclose(hit_records[0].z_min, 1.0, rel_tol = 0.001)
    assert math.isclose(hit_records[0].z_max, 1.0, rel_tol = 0.001)
    assert hit_records[0].names == [1]

    assert math.isclose(hit_records[1].z_min, 1.0, rel_tol = 0.001)
    assert math.isclose(hit_records[1].z_max, 1.0, rel_tol = 0.001)
    assert hit_records[1].names == [2]



def do_on_key(key_id, is_down, extra):
    if not is_down:
        if key_id == togl.KeyId.ESCAPE:
            togl.to_window().request_close()

def do_on_resize(width, height):
    glViewport(0, 0, width, height)

def run(name, options):
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "C Selection",
        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )