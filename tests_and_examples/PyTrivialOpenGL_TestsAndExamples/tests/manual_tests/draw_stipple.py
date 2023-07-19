import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *
from PyTrivialOpenGL.Utility import get_gl_error_str

__all__ = [
    "run"
]

_WIDTH = 800
_HEIGHT = 400

def do_on_create():
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glOrtho(0, _WIDTH, 0, _HEIGHT, 1, -1)

    glClearColor(0, 0, 0.5, 1)

    print("Escape - Exit")

def do_on_destroy():
    glPopAttrib()

    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    data = bytes.fromhex(
        "FF000000"
        "FF000000"
        "FF000000"
        "FF000000"
        "FF000000"
        "FF000000"
        "FF000000"
        "FF000000"
        "FFFF0000"
        "FFFF0000"
        "FF000000"
        "FF000000"
        "FF000000"
        "FF000000"
        "FFFFF000"
        "FFFFF000"
        "FF000000"
        "FF000000"
        "FF000000"
        "FF000000"
        "FF000000"
        "FF000000"
        "FF000000"
        "FF000000"
        "FF0F0F00"
        "FF0F0F00"
        "FF000000"
        "FF000000"
        "FF000000"
        "FF0FF000"
        "FF0FF000"
        "00000000"
    )
    glEnable(GL_POLYGON_STIPPLE)
    glRectf(128, 128, 256, 256) # stipple will be drawn multiple times, 4x4
    glPolygonStipple(data)
    glDisable(GL_POLYGON_STIPPLE)

    data_out = glGetPolygonStipple()
    assert data == data_out

    # debug 
    #print(data)
    #print(data_out)
    #exit(1)

    error_code = glGetError()
    if error_code != 0:
        print(get_gl_error_str(error_code))
        exit(1)

def do_on_key(key_id, is_down, extra):
    if not is_down:
        if key_id == togl.KeyId.ESCAPE:
            togl.to_window().request_close()

def do_on_resize(width, height):
    glViewport(0, 0, width, height)

def run(name, options):
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Draw Stipple",
        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )