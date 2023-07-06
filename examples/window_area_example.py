import PyTrivialOpenGL as togl
from PyTrivialOpenGL._C_GL import *

import math

__all__ = [
    "run"
]

area = togl.Area(0, 0, 800, 400)

def draw_rectangle(x, y, width, height):
    glBegin(GL_TRIANGLE_FAN)

    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)

    glEnd()

def draw_triangle(x, y, scale):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glScalef(scale, scale, 0)

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

def set_ortogonal_projection(width, height):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, 1, -1)

def do_on_create():
    print("X - Exit")

    set_ortogonal_projection(area.width, area.height)

    glClearColor(0, 0, 0.5, 1)

def do_on_destroy():
    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor3f(1, 0, 0)
    draw_rectangle(0, 0, area.width, area.height)

    glColor3f(0, 0, 0.5)
    draw_rectangle(1, 1, area.width - 2, area.height - 2)

    scale = area.height if area.height < area.width else area.width
    scale /= 3
    draw_triangle(area.width / 2, area.height / 2, scale)

def do_on_key(key_id, is_down, extra):
    if not is_down:
        if key_id == 'X':
            togl.to_window().request_close()

def do_on_resize(width, height):
    glViewport(0, 0, width, height)

    area.width = width
    area.height = height
    set_ortogonal_projection(width, height)

def run(name, options):
    togl.set_log_level(togl.LogLevel.DEBUG)

    return togl.to_window().create_and_run(
        window_name         = "Window Area",
        area                = area,
        style               = togl.WindowStyleBit.CENTERED | togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )