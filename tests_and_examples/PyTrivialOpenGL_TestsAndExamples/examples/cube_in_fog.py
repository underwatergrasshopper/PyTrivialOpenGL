import math

import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *
from PyTrivialOpenGL import C_GL

__all__ = [
    "run"
]

class Cube:
    def __init__(self):
        self._c_indices = None

    def create(self):
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

        self._c_indices = (C_GL.GLuint * len(indices))(*indices)

    def draw(self):
        if self._c_indices is not None:
            C_GL.glDrawElements(GL_TRIANGLES, len(self._c_indices), GL_UNSIGNED_INT, self._c_indices)

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
        self.pos            = Vec3(0, -2.1, -2.9)
        self.angle          = -30

        self.width          = 0
        self.height         = 0

        self.cube           = Cube()

        self.font           = togl.Font()
        self.text_drawer    = togl.TextDrawer()

        self.light_angle    = 0.0

        self.legend = (
            "Light Angle: % 3.0f, Cube Angle: % 3.0f, Position: %s\n"
            "WSAD            - Move\n"
            "Arrow Up        - Move Up\n"
            "Arrow Down      - Move Down\n"
            "Arrow Left      - Rotate Left\n"
            "Arrow Right     - Rotate Right\n"
            "Escape          - Exit\n"
        )


_data = Data()

def resize(width, height):
    glViewport(0, 0, width, height)
    _data.width     = width
    _data.height    = height

def do_on_create(data):
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    resize(data.width, data.height)

    glClearColor(0.2, 0.2, 0.5, 1)
    
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 100)
    
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0, 0, 0])
    
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.0, 0.0, 0.0, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    
    glFogfv(GL_FOG_COLOR, [0.2, 0.2, 0.5, 1])
    glFogf(GL_FOG_DENSITY, 0.5)

    _data.cube.create()

    _data.font.load("Courier New", 16, togl.FontSizeUnitId.PIXELS, togl.FontStyleId.NORMAL, togl.UnicodeCharSetId.ENGLISH)
    if not _data.font.is_ok():
        print("Error: %s" % _data.font.get_err_msg())

    _data.text_drawer.set_origin(togl.OriginId.LEFT_TOP)

    print("Escape - Exit")

def do_on_destroy():
    _data.font.unload()

    glPopAttrib()

    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    ### 2D ### 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, _data.width, _data.height, 0, 1, -1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    _data.text_drawer.set_pos(0, 0)
    _data.text_drawer.set_color(255, 255, 255, 255)
    _data.text_drawer.render_text(_data.font, _data.legend % (_data.light_angle / math.pi * 180, _data.angle, _data.pos))
    
    ### 3D ###
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glShadeModel(GL_SMOOTH)

    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    
    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)

    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_FOG)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1, 1, -1, 1, 0.5, 10)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glTranslatef(_data.pos.x, _data.pos.y, _data.pos.z)
    glRotated(_data.angle, 0, 1, 0)
    
    _data.cube.draw()

    glPopAttrib()

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
    resize(width, height)

def do_on_time(time_interval):
    delta_time = time_interval / 1000
    rotation_speed = 120 # degrees per second

    _data.light_angle += math.pi / 180 * rotation_speed * delta_time
    _data.light_angle %= (math.pi * 2)

    x = 0
    y = math.sin(_data.light_angle)
    z = math.cos(_data.light_angle)

    glLightfv(GL_LIGHT0, GL_POSITION, [x, y, z, 0])

def run():
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Cube in Fog",

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