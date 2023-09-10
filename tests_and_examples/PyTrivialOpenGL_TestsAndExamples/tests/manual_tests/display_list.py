import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

__all__ = [
    "run"
]

_WIDTH = 800
_HEIGHT = 400

class _Data:
    def __init__(self):
        self.list_range = 1
        self.list_base  = 0

_data = _Data()

def do_on_create(data):
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glViewport(0, 0, data.width, data.height)

    glOrtho(0, data.width, 0, data.height, 1, -1)

    glClearColor(0, 0, 0.5, 1)

    _data.list_range = 256
    _data.list_base = glGenLists(_data.list_range)

    glNewList(_data.list_base + ord("H"), GL_COMPILE)
    data = bytes.fromhex(
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "FFFF"
        "FFFF"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
    )
    glColor3f(1, 1, 1)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glBitmap(16, 16, 0, 0, 18, 0, data)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
    glEndList()

    glNewList(_data.list_base + ord("E"), GL_COMPILE)
    data = bytes.fromhex(
        "FFFF"
        "F000"
        "F000"
        "F000"
        "F000"
        "F000"
        "F000"
        "FFFF"
        "FFFF"
        "F000"
        "F000"
        "F000"
        "F000"
        "F000"
        "F000"
        "FFFF"
    )
    glColor3f(1, 1, 1)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glBitmap(16, 16, 0, 0, 18, 0, data)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
    glEndList()

    glNewList(_data.list_base + ord("L"), GL_COMPILE)
    data = bytes.fromhex(
        "FFFF"
        "F000"
        "F000"
        "F000"
        "F000"
        "F000"
        "F000"
        "F000"
        "F000"
        "F000"
        "F000"
        "F000"
        "F000"
        "F000"
        "F000"
        "F000"
    )
    glColor3f(1, 1, 1)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glBitmap(16, 16, 0, 0, 18, 0, data)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
    glEndList()


    glNewList(_data.list_base + ord("O"), GL_COMPILE)
    data = bytes.fromhex(
        "0FF0"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "F00F"
        "0FF0"
    )
    glColor3f(1, 1, 1)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glBitmap(16, 16, 0, 0, 18, 0, data)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
    glEndList()

    print("Escape - Exit")

def do_on_destroy():
    glPopAttrib()

    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glListBase(_data.list_base)
    glRasterPos2i(0, 10)
    glCallLists(GL_UNSIGNED_BYTE, [ord('H'), ord('E'), ord('L'), ord('L'), ord('O')])
    glRasterPos2i(0, 40)
    glCallLists(GL_UNSIGNED_BYTE, b"HELLO")
    glRasterPos2i(0, 70)
    glCallLists(GL_UNSIGNED_INT, "HELLO")

def do_on_key(key_id, is_down, extra):
    if not is_down:
        if key_id == togl.KeyId.ESCAPE:
            togl.to_window().request_close()

def do_on_resize(width, height):
    glViewport(0, 0, width, height)

def run(name, options):
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Display List",
        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )