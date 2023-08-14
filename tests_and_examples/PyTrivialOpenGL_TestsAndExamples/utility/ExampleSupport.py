import ctypes
import math
import copy
import os
from timeit import default_timer as _timer

import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

__all__ = [
    "EXIT_SUCCESS",
    "EXIT_FAILURE",
    "check_gl_error",
    "get_path_to_assets",
    "print_rect",
    "rect_to_area",
    "display_info",
    "draw_rgb_triangle",
    "draw_rectangle",
    "is_close",
]

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

def check_gl_error():
    error_code = glGetError()
    if error_code != 0:
        print("gl error code: %s." % togl.get_gl_error_str(error_code))
        exit(EXIT_FAILURE)

def get_path_to_assets():
    return os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../assets")

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
    if window.is_windowed_full_screened():  flags[4] = "+"
    print("".join(flags))

    print("---")

class FPS_Counter:
    def __init__(self, interval = 1):
        """
        interval : float
            In seconds.
        """
        self._now       = 0
        self._accum     = 0
        self._count     = 0
        self._interval  = interval
        self._fps       = 0

    def reset(self):
        self._now   = _timer()
        self._accum = 0
        self._fps   = 0.0

    def get_fps(self):
        """
        Returns : float
        """
        return self._fps

    def update(self, is_display = True):
        self._count += 1

        new_now = _timer()

        self._accum += new_now - self._now
        self._now = new_now

        if self._accum >= self._interval:
            fps = self._count / self._accum
            self._accum = 0
            self._count = 0

            self._fps = fps

            if is_display:
                print("FPS: %.0f" % (fps), flush = True)
     
def draw_rgb_triangle(x, y, scale, angle):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glRotatef(angle, 0, 0, 1)
    glScalef(scale, scale, 0)

    glBegin(GL_TRIANGLES)

    glColor3f(1, 0, 0)

    #glColor3bv([127, 0, 0])
    #glColor3ubv([255, 0, 0])
    #glColor3ubv(b"\xFF\x00\x00")
    #glColor4ubv([255, 0, 0, 63])
    #glColor4ubv(b"\xFF\x00\x00\x3F")

    #glIndexiv([1])
    #glIndexfv([1.5]) # blends
    #glIndexubv(b"\x05")

    angle = 0
    glVertex2f(math.sin(angle), math.cos(angle))

    #glEdgeFlagv([GL_TRUE])
    #glVertex2fv([math.sin(angle), math.cos(angle)])
    #glVertex2dv([math.sin(angle), math.cos(angle)])
    #glVertex2sv([math.sin(angle), math.cos(angle)])
    #glVertex2iv([math.sin(angle), math.cos(angle)])

    #glVertex3fv([math.sin(angle), math.cos(angle), 0])
    #glVertex3dv([math.sin(angle), math.cos(angle), 0])
    #glVertex3sv([math.sin(angle), math.cos(angle), 0])
    #glVertex3iv([math.sin(angle), math.cos(angle), 0])

    #glVertex4fv([math.sin(angle), math.cos(angle), 0, 1])
    #glVertex4dv([math.sin(angle), math.cos(angle), 0, 1])
    #glVertex4sv([math.sin(angle), math.cos(angle), 0, 1])
    #glVertex4iv([math.sin(angle), math.cos(angle), 0, 1])

    glColor3f(0, 1, 0)
    angle += math.pi * 2 / 3
    glVertex2f(math.sin(angle), math.cos(angle))
    #glVertex2dv([math.sin(angle), math.cos(angle)])
            
    glColor3f(0, 0, 1)
    angle += math.pi * 2 / 3
    glVertex2f(math.sin(angle), math.cos(angle))
    #glVertex2dv([math.sin(angle), math.cos(angle)])

    glEnd()

    glPopMatrix()

def draw_rectangle(x, y, width, height):
    glBegin(GL_TRIANGLE_FAN)

    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)

    glEnd()

def is_close(a, b, delta = 0.001):
    if isinstance(a, (list, tuple)):
        if not isinstance(b, (list, tuple)):
            return False

        if len(a) != len(b):
            return False

        l = len(a)
        for i in range(l):
            if not is_close(a[i], b[i], delta):
                return False
        return True
    else:
        return math.isclose(a, b, abs_tol = delta)