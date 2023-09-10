import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

import math

__all__ = [
    "run"
]

class HitRecord:
    def __init__(self, z_min, z_max, names):
        self.z_min = z_min
        self.z_max = z_max
        self.names = names

def do_on_create(data):
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glViewport(0, 0, data.width, data.height)

    glClearColor(0, 0, 0.5, 1)

    print("Escape - Exit")

def do_on_destroy():
    glPopAttrib()

    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    LENGTH = 32
    glSelectBuffer(LENGTH) # creates and attaches buffer
    glRenderMode(GL_SELECT)

    glInitNames()
    glPushName(0)

    glLoadName(1)
    glColor3f(1, 0, 0)
    glRectd(-0.5, -0.5, 0.5, 0.5)
    
    glLoadName(2)
    glColor3f(0, 1, 0)
    glRectd(-1.2, -1.2, -0.4, -0.4)
    
    # out of view, won't hit
    glLoadName(3)
    glColor3f(1, 1, 0)
    glRectd(-2, -2, -1.2, -1.2)

    glFlush()
    number_of_hits = glRenderMode(GL_RENDER)

    assert number_of_hits == 2
    buffer = glSelectBuffer() # gets buffer
    assert buffer is not None

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
        window_name         = "Selection",
        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,
        opengl_version      = (2, 0),

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )