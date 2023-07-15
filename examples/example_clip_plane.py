import math

import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

__all__ = [
    "run"
]

def isclose(l_a, l_b, delta):
    if len(l_a) != len(l_b):
        return False
    for ix in range(len(l_a)):
        if not math.isclose(l_a[ix], l_b[ix], rel_tol = delta):
            return False
    return True


def do_on_create():
    print("X - Exit")

    glPushAttrib(GL_ENABLE_BIT)

    glEnable(GL_CLIP_PLANE0)
    glEnable(GL_CLIP_PLANE1)
    glEnable(GL_CLIP_PLANE2)
    glEnable(GL_CLIP_PLANE3)

    glClipPlane(GL_CLIP_PLANE0, [1, 0, 0, 0.7])
    glClipPlane(GL_CLIP_PLANE1, [-1, 0, 0, 0.7])
    glClipPlane(GL_CLIP_PLANE2, [0, 1, 0, 0.7])
    glClipPlane(GL_CLIP_PLANE3, [0, -1, 0, 0.7])

    print(glGetClipPlane(GL_CLIP_PLANE0))
    print(glGetClipPlane(GL_CLIP_PLANE1))
    print(glGetClipPlane(GL_CLIP_PLANE2))
    print(glGetClipPlane(GL_CLIP_PLANE3))

    assert isclose(glGetClipPlane(GL_CLIP_PLANE0), [1, 0, 0, 0.7], 0.001)
    assert isclose(glGetClipPlane(GL_CLIP_PLANE1), [-1, 0, 0, 0.7], 0.001)
    assert isclose(glGetClipPlane(GL_CLIP_PLANE2), [0, 1, 0, 0.7], 0.001)
    assert isclose(glGetClipPlane(GL_CLIP_PLANE3), [0, -1, 0, 0.7], 0.001)

    glClearColor(0, 0, 0.5, 1)

def do_on_destroy():
    glPopAttrib()

    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_TRIANGLES)

    glColor3f(1, 0, 0)
    angle = 0
    glVertex2f(math.sin(angle), math.cos(angle))

    glColor3f(0, 1, 0)
    angle += math.pi * 2 / 3
    glVertex2f(math.sin(angle), math.cos(angle))
    
    glColor3f(0, 0, 1)
    angle += math.pi * 2 / 3
    glVertex2f(math.sin(angle), math.cos(angle))

    glEnd()

def do_on_key(key_id, is_down, extra):
    if not is_down:
        if key_id == 'X':
            togl.to_window().request_close()

def do_on_resize(width, height):
    glViewport(0, 0, width, height)

def run(name, options):
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Clip Plane",
        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )