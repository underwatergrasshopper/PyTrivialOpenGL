import math

import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

__all__ = [
    "run"
]

def do_on_create():
    print("X - Exit")

    glClearColor(0, 0, 0.5, 1)

def do_on_destroy():
    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()

    glLoadIdentity()

    # rotate 30 degrees clockwise
    angle = math.pi / 6 
    glLoadMatrixf([
        math.cos(angle), -math.sin(angle), 0, 0,
        math.sin(angle), math.cos(angle), 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1,
    ])

    # shrink to half size
    scale = 0.5 
    glMultMatrixf([
        scale, 0, 0, 0,
        0, scale, 0, 0,
        0, 0, 1, 0,
        0, 0, 0, 1,
    ])

    # draw triangle
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

    glPopMatrix()

def do_on_key(key_id, is_down, extra):
    if not is_down:
        if key_id == 'X':
            togl.to_window().request_close()

def do_on_resize(width, height):
    glViewport(0, 0, width, height)

def run(name, options):
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Matrix",
        area                = (400, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )