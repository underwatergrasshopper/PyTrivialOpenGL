import ctypes
import math
import copy

import PyTrivialOpenGL as togl
from PyTrivialOpenGL._C_GL import *
import PyTrivialOpenGL._C_WinApi as _C_WinApi

__all__ = [
    "EXIT_SUCCESS",
    "EXIT_FAILURE",
    "print_rect",
    "rect_to_area",
    "display_info",
    "draw_rgb_triangle",
    "draw_rectangle",
]

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

def print_rect(r):
    print("%d %d %d %d" % (r.left, r.top, r.right, r.bottom))

def rect_to_area(r):
    return togl.Area(r.left, r.top, r.right - r.left, r.bottom - r.top)

def display_info():
    print("--- Info ---")

    padding = 30
    screen_size = togl.get_screen_size()
    print("%-*s: %s" % (padding, "Screen Size", screen_size))

    work_area = togl.get_work_area()
    print("%-*s: %s" % (padding, "Work Area", work_area))

    window = togl.to_window()

    window_area = window.get_area()
    print("%-*s: %s" % (padding, "Window Area", window_area))

    draw_area = window.get_draw_area()
    print("%-*s: %s" % (padding, "Window Draw Area", draw_area))

    center_check_size = togl.Size(
        (window_area.x - work_area.x) * 2 + window_area.width,
        (window_area.y - work_area.y) * 2 + window_area.height
    )
    print("%-*s: %s (= %s)" % (padding, "Window Center Check", center_check_size, work_area.get_size()))

    cursor_pos = window.get_cursor_pos_in_draw_area()
    print("%-*s: %s" % (padding, "Cursor Pos. in Draw Area", cursor_pos))
    
    print("%-*s: %s" % (padding, "is_running", window.is_running()))
    print("%-*s: %s" % (padding, "is_visible", window.is_visible()))
    print("%-*s: %s" % (padding, "is_foreground", window.is_foreground()))
    print("%-*s: %s" % (padding, "is_enabled AUTO_SLEEP_MODE", window.is_enabled(togl.WindowOptionId.AUTO_SLEEP_MODE)))

    print("%-*s: %s" % (padding, "OpenGL Version", window.get_opengl_version()))
    print("%-*s: %s" % (padding, "Previous State", window.get_previous_state_id()))
    print("%-*s: %s" % (padding, "Style", togl.window_style_bitfield_to_str(window.get_style())))
    print("HmNMf")

    flags = list("     ")
    ps_id = window.get_previous_state_id()
    if ps_id == togl.WindowStateId.MINIMIZED:               flags[1] = "-"
    if ps_id == togl.WindowStateId.NORMAL:                  flags[2] = "-"
    if ps_id == togl.WindowStateId.MAXIMIZED:               flags[3] = "-"
    if ps_id == togl.WindowStateId.WINDOWED_FULL_SCREENED:  flags[4] = "-"

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