import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *
from PyTrivialOpenGL.Utility import get_gl_error_str

__all__ = [
    "run"
]

_WIDTH = 800
_HEIGHT = 400

def do_on_create():
    print("X - Exit")

    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glOrtho(0, _WIDTH, 0, _HEIGHT, 1, -1)

    glClearColor(0, 0, 0.5, 1)

def do_on_destroy():
    
    glPopAttrib()

    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    # Byte align: glPixelStorei, GL_UNPACK_ALIGNMENT.

    data = b""
    for _ in range(16 * 12):
        data += b"\xFF\x00\x00\x7F"
    for _ in range(16 * 4):
        data += b"\x00\xFF\x00\x7F"

    glRasterPos2i(0, 0)
    glDrawPixels(16, 16, GL_RGBA, GL_UNSIGNED_BYTE, data)

    data_out = glReadPixels(0, 0, 16, 16, GL_RGBA, GL_UNSIGNED_BYTE)
    assert data_out[0:3] == b"\x7F\x00\x40" # half red and half clear color

    data = b""
    for _ in range(16 * 12):
        data += b"\xFF\x00\x00"
    for _ in range(16 * 4):
        data += b"\x00\xFF\x00"

    glRasterPos2i(16, 0)
    glDrawPixels(16, 16, GL_RGB, GL_UNSIGNED_BYTE, data)

    data_out = glReadPixels(16, 0, 16, 16, GL_RGB, GL_UNSIGNED_BYTE)
    assert data == data_out

    data = [
        1, 0, 1,    1, 0, 1,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    
        1, 0, 1,    1, 0, 1,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    
        1, 0, 1,    1, 0, 1,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    
        1, 0, 1,    1, 0, 1,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    
        1, 0, 1,    1, 0, 1,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    
        1, 0, 1,    1, 0, 1,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    
        1, 0, 1,    1, 0, 1,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    
        1, 0, 1,    1, 0, 1,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    
        1, 0, 1,    1, 0, 1,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    
        1, 0, 1,    1, 0, 1,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    
        1, 0, 1,    1, 0, 1,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    
        1, 0, 1,    1, 0, 1,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,    1, 0, 0,  
        0, 1, 1,    0, 1, 1,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    
        0, 1, 1,    0, 1, 1,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    
        0, 1, 1,    0, 1, 1,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    
        0, 1, 1,    0, 1, 1,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,    0, 1, 0,      
    ]
    glRasterPos2i(32, 0)
    glDrawPixels(16, 16, GL_RGB, GL_FLOAT, data)


    data = bytes.fromhex(
        "FFFFFFFF"
        "FFFFFFFF"
        "FFFFFFFF"
        "FFFFFFFF"
        "FFFFFFFF"
        "FFFFFFFF"
        "FFFFFFFF"
        "FFFFFFFF"
        "FFFFFFFF"
        "FFFFFFFF"
        "FFFFFFFF"
        "FFFFFFFF"
        "FFFFFFFF"
        "FFFFFFFF"
        "FFFFFFFF"
        "FFFFFFFF"
    )
    glColor3f(0.5, 0, 1)
    glRasterPos2i(128, 128)
    glBitmap(32, 16, 0, 0, 0, 0, data)

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
    )
    glColor3f(0, 1, 0)
    glRasterPos2i(128, 128)
    glBitmap(32, 16, 0, 0, 0, 0, data)

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
        window_name         = "Draw Pixels",
        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )