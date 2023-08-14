import math

import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *
from PyTrivialOpenGL import C_GL
from ...utility.ExampleSupport import is_close

__all__ = [
    "run"
]

class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "% .2f % .2f  % .2f " % (float(self.x), float(self.y), float(self.z))

    def __repr__(self):
        return str(self)

class Data:
    def __init__(self):
        self.NUM_OF_PARTS   = 30

        self.pos            = Vec3(0, -3.3, -7.9)
        self.angle          = 320

_data = Data()

def do_on_create(data):
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glViewport(0, 0, data.width, data.height)

    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_AUTO_NORMAL)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1, 1, -1, 1, 0.5, 100)

    glClearColor(0.2, 0.2, 0.5, 1)

    glShadeModel(GL_SMOOTH)

    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 100)

    glLightfv(GL_LIGHT0, GL_POSITION, [0, -10, 10, 0 ])
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0, 0, 0])

    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.0, 0.0, 0.0, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])

    points = [
        -10, 4, 10,
        -10, -4, -10,

        10, -4, 10,
        10, 4, -10,
    ]

    glMap2f(GL_MAP2_VERTEX_3, 
        0, 1, 
        0, 1, 
        2,
        points
    )

    glMapGrid2f(_data.NUM_OF_PARTS, 0.0, 1.0, _data.NUM_OF_PARTS, 0.0, 1.0)

    glEnable(GL_MAP2_VERTEX_3)

    assert is_close(glGetMapfv(GL_MAP2_VERTEX_3, GL_COEFF), points, 0.01)
    assert glGetMapiv(GL_MAP2_VERTEX_3, GL_ORDER) == [2, 2]
    assert is_close(glGetMapfv(GL_MAP2_VERTEX_3, GL_DOMAIN), [0.0, 1.0, 0.0, 1.0], 0.01)
    
    print("Left/Right Arrow - Rotate Surface")
    print("Escape - Exit")

def do_on_destroy():
    glPopAttrib()

    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslatef(_data.pos.x, _data.pos.y, _data.pos.z)
    glRotated(_data.angle, 0, 1, 0)

    glColor3f(1, 0, 0)
    glEvalMesh2(GL_FILL, 0, _data.NUM_OF_PARTS, 0, _data.NUM_OF_PARTS)

def do_on_key(key_id, is_down, extra):
    if key_id == togl.KeyId.ESCAPE:
        if not is_down:
            togl.to_window().request_close()

    elif key_id == togl.KeyId.ARROW_LEFT:
        if is_down:
            _data.angle -= 10
            _data.angle %= 360
            print(_data.angle)
    elif key_id == togl.KeyId.ARROW_RIGHT:
        if is_down:
            _data.angle += 10
            _data.angle %= 360
            print(_data.angle)
    elif key_id == togl.KeyId.ARROW_DOWN:
        if is_down:
            _data.pos.y -= 0.1
            print(_data.pos)
    elif key_id == togl.KeyId.ARROW_UP:
        if is_down:
            _data.pos.y += 0.1
            print(_data.pos)
    elif key_id == 'A':
        if is_down:
            _data.pos.x -= 0.1
            print(_data.pos)
    elif key_id == 'D':
        if is_down:
            _data.pos.x += 0.1
            print(_data.pos)
    elif key_id == 'W':
        if is_down:
            _data.pos.z += 0.1
            print(_data.pos)
    elif key_id == 'S':
        if is_down:
            _data.pos.z -= 0.1
            print(_data.pos)

def do_on_resize(width, height):
    glViewport(0, 0, width, height)

def run(name, options):
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Bezier Surface",
        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )