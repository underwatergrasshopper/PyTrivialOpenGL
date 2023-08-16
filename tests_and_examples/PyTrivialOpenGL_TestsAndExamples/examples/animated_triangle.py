import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

import math

__all__ = [
    "run"
]

def draw_rgb_triangle():
    glPushMatrix()

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

class AnimatedTriangle:
    def __init__(self, x, y, scale, rotation_speed):
        """
        x               : int
        y               : int
        scale           : float
        rotation_speed  : float
            In degrees per second.
        """
        self.set_pos(x, y)
        self.set_scale(scale)
        self.set_rotation_speed(rotation_speed)

        self._angle = 0.0
      
    def set_pos(self, x, y):
        """
        x               : int
        y               : int
        """
        self._x     = x
        self._y     = y

    def set_scale(self, scale):
        """
        scale          : float
        """
        self._scale  = scale

    def set_rotation_speed(self, rotation_speed):
        """
        rotation_speed  : float
            In degrees per second.
        """
        self._rotation_speed = rotation_speed

    def draw(self):
        glPushMatrix()

        glTranslatef(self._x, self._y, 0)
        glRotatef(self._angle, 0, 0, 1)
        glScalef(self._scale, self._scale, 1)

        draw_rgb_triangle()

        glPopMatrix()

    def update(self, delta_time):
        """
        delta_time : float
            In seconds.
        """
        self._angle += self._rotation_speed * delta_time
        self._angle %= 360

_animated_triangle = AnimatedTriangle(0, 0, 100.0, 20.0)

def resize(width, height):
    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, 1, -1)

    _animated_triangle.set_pos(width // 2, height // 2)

    scale = width if width < height else height
    scale *= 0.5

    _animated_triangle.set_scale(scale)

def do_on_create(data):
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    resize(data.width, data.height)

    glClearColor(0, 0, 0.5, 1)

    print("Escape - Exit", flush = True)

def do_on_destroy():
    glPopAttrib()

    print("Bye. Bye.", flush = True)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    _animated_triangle.draw()

def do_on_time(time_interval):
    _animated_triangle.update(time_interval / 1000)

def do_on_key(key_id, is_down, extra):
    if key_id == togl.KeyId.ESCAPE:
        if not is_down:
            togl.to_window().request_close()

def do_on_resize(width, height):
    resize(width, height)

def run():
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Animated Triangle",

        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,
        timer_time_interval = 20,
        

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,
        do_on_time          = do_on_time,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )

if __name__ == "__main__":
    run()