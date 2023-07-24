import math

import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

__all__ = [
    "run"
]

def is_close(l_a, l_b, delta):
    if (len(l_a) != len(l_b)):
        return False

    for ix in range(len(l_a)):
        if not math.isclose(l_a[ix], l_b[ix], rel_tol = delta):
            return False

    return True

def draw_triangle():
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

def draw_prism():
    vertices = [
        # A
        -1, 1, 1,   # 0
        -1, -1, 1,  # 1
        1, -1, 1,   # 2
        1, 1, 1,    # 3
        # B         
        -1, 1, -1,   # 4
        -1, -1, -1, # 5
        -1, -1, 1,  # 6
        -1, 1, 1,   # 7
        # C         
        1, 1, 1,    # 8
        1, -1, 1,   # 9
        1, -1, -1,  # 10
        1, 1, -1,   # 11
        # D         
        -1, -1, 1,  # 12
        -1, -1, -1, # 13
        1, -1, -1,  # 14
        1, -1, 1,   # 15
        # E         
        -1, 1, -1,  # 16 
        -1, 1, 1,   # 17
        1, 1, 1,    # 18
        1, 1, -1,   # 19
        # F         
        -1, -1, -1, # 20
        -1, 1, -1,  # 21
        1, 1, -1,   # 22
        1, -1, -1,  # 23
    ]

    normals = [
        # A
        0, 0, 1,
        0, 0, 1,
        0, 0, 1,
        0, 0, 1,
        # B
        -1, 0, 0,
        -1, 0, 0,
        -1, 0, 0,
        -1, 0, 0,
        # C
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        # D
        0, 1, 0,
        0, 1, 0,
        0, 1, 0,
        0, 1, 0,
        # E
        0, -1, 0,
        0, -1, 0,
        0, -1, 0,
        0, -1, 0,
        # F
        0, 0, -1,
        0, 0, -1,
        0, 0, -1,
        0, 0, -1,
    ]

    colors = [
        # A
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        # B
        0, 1, 0,
        0, 1, 0,
        0, 1, 0,
        0, 1, 0,
        # C
        0, 0, 1,
        0, 0, 1,
        0, 0, 1,
        0, 0, 1,
        # D
        1, 1, 0,
        1, 1, 0,
        1, 1, 0,
        1, 1, 0,
        # E
        1, 0, 1,
        1, 0, 1,
        1, 0, 1,
        1, 0, 1,
        # F
        0, 1, 1,
        0, 1, 1,
        0, 1, 1,
        0, 1, 1,
    ]

    indices = [
        0, 1, 2,
        0, 2, 3,

        4, 5, 6,
        4, 6, 7,

        8, 9, 10,
        8, 10, 11,

        12, 13, 14,
        12, 14, 15,

        16, 17, 18,
        16, 18, 19,

        20, 21, 22,
        20, 22, 23,
    ]

    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glNormalPointer(GL_FLOAT, 0, normals)
    glColorPointer(3, GL_FLOAT, 0, colors)

    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, indices)

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
        self.pos = Vec3(0, -2.1, -2.9)
        self.angle = -30

_data = Data()

def do_on_create():
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    print(glIsEnabled(GL_CULL_FACE))
    print(glIsEnabled(GL_DEPTH_TEST))

    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)

    print(glIsEnabled(GL_CULL_FACE))
    print(glIsEnabled(GL_DEPTH_TEST))

    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1, 1, -1, 1, 0.5, 10)

    glClearColor(0.2, 0.2, 0.5, 1)

    glShadeModel(GL_SMOOTH)

    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 100)

    print(glGetMaterialfv(GL_FRONT, GL_SPECULAR))
    print(glGetMaterialfv(GL_FRONT, GL_SHININESS))

    glLightfv(GL_LIGHT0, GL_POSITION, [2, 2, 2, 0 ])
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0, 0, 0])

    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.0, 0.0, 0.0, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])

    print(glGetLightfv(GL_LIGHT0, GL_POSITION))
    print(glGetLightfv(GL_LIGHT0, GL_SPOT_DIRECTION))
    print(glGetLightfv(GL_LIGHT0, GL_AMBIENT))
    print(glGetLightfv(GL_LIGHT0, GL_DIFFUSE))
    print(glGetLightfv(GL_LIGHT0, GL_SPECULAR))

    glEnable(GL_FOG)
    glFogfv(GL_FOG_COLOR, [0.2, 0.2, 0.5, 1])
    assert is_close(glGetFloatv(GL_FOG_COLOR), [0.2, 0.2, 0.5, 1], 0.01)

    glFogiv(GL_FOG_DENSITY, [2])
    assert glGetIntegerv(GL_FOG_DENSITY) == [2]

    glFogfv(GL_FOG_DENSITY, [0.5])
    assert is_close(glGetFloatv(GL_FOG_DENSITY), [0.5], 0.01)


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

    draw_prism()

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
        window_name         = "Light and Fog",
        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )