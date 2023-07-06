from ExampleManager import *
from ActionChain import *

import PyTrivialOpenGL as togl
from PyTrivialOpenGL._C_GL import *

import PyTrivialOpenGL._C_WinApi as _C_WinApi

import ctypes
import math
import copy

################################################################################

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

################################################################################

def print_rect(r):
    print("%d %d %d %d" % (r.left, r.top, r.right, r.bottom))

def rect_to_area(r):
    return togl.Area(r.left, r.top, r.right - r.left, r.bottom - r.top)

def display_info():
    print("--- Info ---")

    window = togl.to_window()

    window_handle = _C_WinApi.GetForegroundWindow()

    window_area = window.get_area()
    print("%-20s: %s" % ("Window Area", window_area))

    draw_area = window.get_draw_area()
    print("%-20s: %s" % ("Window Draw Area", draw_area))

    screen_size = togl.get_screen_size()

    print("%-20s: %s" % ("Screen Size", screen_size))

    work_area = togl.get_work_area()

    print("%-20s: %s" % ("Work Area", work_area))

    print("%-20s: %s" % ("is_visible", window.is_visible()))
    print("%-20s: %s" % ("is_foreground", window.is_foreground()))

    center_check_size = togl.Size(
        (window_area.x - work_area.x) * 2 + window_area.width,
        (window_area.y - work_area.y) * 2 + window_area.height
    )
    print("%-20s: %s (= %s)" % ("Window Center Check", center_check_size, work_area.get_size()))

    print("%-20s: %s" % ("OpenGL Version", window.get_opengl_version()))

    print("HmNMf")
    flags = list("     ")
    if not window.is_visible():             flags[0] = "+"
    if window.is_minimized():               flags[1] = "+"
    if window.is_normal():                  flags[2] = "+"
    if window.is_maximized():               flags[3] = "+"
    if window.is_windowed_full_screen():    flags[4] = "+"
    print("".join(flags))

    print("---")

def draw_rgb_triangle(x, y, scale, angle):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glRotatef(angle, 0, 0, 1)
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

def draw_rectangle(x, y, width, height):
    glBegin(GL_TRIANGLE_FAN)

    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)

    glEnd()