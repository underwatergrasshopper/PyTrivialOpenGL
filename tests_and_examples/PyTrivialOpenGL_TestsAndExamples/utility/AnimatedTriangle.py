import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

from ..utility.ExampleSupport import *

__all__ = [
    "AnimatedTriangle"
]

class AnimatedTriangle:
    """
    speed   : float
        In degrees per seconds.
    angle   : float
        In degrees.
    size    : Size
    scale   : int | float
    """

    def __init__(self, speed = 10.0):
        """
        speed : float
            In degrees per seconds.
        """
        self.speed  = speed # in degrees per second
        self.angle  = 0.0   # in degrees
        self.size   = togl.Size(0, 1)
        self.scale  = 1

    def update(self, delta_time):
        """
        delta_time : float
            In seconds.
        """
        self.angle += self.speed * delta_time
        self.angle %= 360.0

    def resize(self, width, height):
        """
        width   : int | float
        height  : int | float
        """
        self.size = togl.Size(width, height)

        self.scale = min(width, height)
        self.scale /= 3

    def draw(self):
        glColor3f(1, 0, 0)
        draw_rectangle(0, 0, self.size.width, self.size.height)

        glColor3f(0, 0, 0.5)
        draw_rectangle(1, 1, self.size.width - 2, self.size.height - 2)

        draw_rgb_triangle(self.size.width / 2, self.size.height / 2, self.scale, self.angle)