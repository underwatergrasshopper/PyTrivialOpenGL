import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *
from PyTrivialOpenGL import C_GL

from PyTrivialOpenGL.Utility import get_gl_error_str
from ...utility.ExampleSupport import is_close

__all__ = [
    "run"
]

_WIDTH = 800
_HEIGHT = 400

def do_on_create(data):
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glViewport(0, 0, data.width, data.height)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glOrtho(0, data.width, 0, data.height, 1, -1)

    glClearColor(0, 0, 0.5, 1)

    glPixelTransferi(GL_MAP_COLOR, GL_TRUE)

    c_values = (C_GL.GLfloat * 256)(*([0] * 256))
    C_GL.glPixelMapfv(GL_PIXEL_MAP_R_TO_R, 256, c_values)
    C_GL.glPixelMapfv(GL_PIXEL_MAP_G_TO_G, 256, c_values)
    C_GL.glPixelMapfv(GL_PIXEL_MAP_B_TO_B, 256, c_values)
    print(glGetIntegerv(GL_PIXEL_MAP_R_TO_R_SIZE))
    print(glGetIntegerv(GL_MAX_PIXEL_MAP_TABLE))
    
    glPixelMapfv(GL_PIXEL_MAP_G_TO_G, b"\x00\x00\x00\x00" * 256)

    values = [0.5] * 256
    glPixelMapfv(GL_PIXEL_MAP_R_TO_R, values)
    print(len(glGetPixelMapfv(GL_PIXEL_MAP_R_TO_R)), glGetPixelMapfv(GL_PIXEL_MAP_R_TO_R))
    assert is_close(glGetPixelMapfv(GL_PIXEL_MAP_R_TO_R), values, 0.01)


    values = b"\x04\x03\x02\x01" * 256
    glPixelMapfv(GL_PIXEL_MAP_R_TO_R, values)
    print(len(glGetPixelMapfv(GL_PIXEL_MAP_R_TO_R, is_return_bytes = True)), glGetPixelMapfv(GL_PIXEL_MAP_R_TO_R, is_return_bytes = True))
    assert glGetPixelMapfv(GL_PIXEL_MAP_R_TO_R, is_return_bytes = True) == values

    values = [127] * 256
    glPixelMapusv(GL_PIXEL_MAP_R_TO_R, values)
    print(len(glGetPixelMapusv(GL_PIXEL_MAP_R_TO_R)), glGetPixelMapusv(GL_PIXEL_MAP_R_TO_R))
    assert glGetPixelMapusv(GL_PIXEL_MAP_R_TO_R) == values


    values = b"\x02\x01" * 256
    glPixelMapusv(GL_PIXEL_MAP_R_TO_R, values)
    print(len(glGetPixelMapusv(GL_PIXEL_MAP_R_TO_R, is_return_bytes = True)), glGetPixelMapusv(GL_PIXEL_MAP_R_TO_R, is_return_bytes = True))
    assert glGetPixelMapusv(GL_PIXEL_MAP_R_TO_R, is_return_bytes = True) == values

    values = [127] * 256
    glPixelMapuiv(GL_PIXEL_MAP_R_TO_R, values)
    print(len(glGetPixelMapuiv(GL_PIXEL_MAP_R_TO_R)), glGetPixelMapuiv(GL_PIXEL_MAP_R_TO_R))
    assert glGetPixelMapuiv(GL_PIXEL_MAP_R_TO_R) == values


    values = b"\x04\x03\x02\x01" * 256
    glPixelMapuiv(GL_PIXEL_MAP_R_TO_R, values)
    print(len(glGetPixelMapuiv(GL_PIXEL_MAP_R_TO_R, is_return_bytes = True)), glGetPixelMapuiv(GL_PIXEL_MAP_R_TO_R, is_return_bytes = True))
    assert glGetPixelMapuiv(GL_PIXEL_MAP_R_TO_R, is_return_bytes = True) == values

    

    print("Escape - Exit")

def do_on_destroy():
    glPopAttrib()

    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

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
    for _ in range(15 * 12):
        data += b"\xFF\x00\x00"
    for _ in range(15 * 4):
        data += b"\x00\xFF\x00"

    glRasterPos2i(16, 0)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1) # when GL_RGB
    glDrawPixels(15, 16, GL_RGB, GL_UNSIGNED_BYTE, data)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4) 

    glPixelStorei(GL_PACK_ALIGNMENT, 1) # when GL_RGB
    data_out = glReadPixels(16, 0, 15, 16, GL_RGB, GL_UNSIGNED_BYTE)
    glPixelStorei(GL_PACK_ALIGNMENT, 4) 

    # debug
    #print(data)
    #print(data_out)
    #exit(1)

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
        "FFFF"
        "FFFF"
        "FFFF"
        "FFFF"
        "FFFF"
        "FFFF"
        "FFFF"
        "FFFF"
        "FFFF"
        "FFFF"
        "FFFF"
        "FFFF"
        "FFFF"
        "FFFF"
        "FFFF"
        "FFFF"
    )
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glColor3f(0.5, 0, 1)
    glRasterPos2i(128, 128)
    glBitmap(16, 16, 0, 0, 0, 0, data)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)

    data = bytes.fromhex(
        "FF00"
        "FF00"
        "FF00"
        "FF00"
        "FF00"
        "FF00"
        "FF00"
        "FF00"
        "FFF0"
        "FFF0"
        "FF00"
        "FF00"
        "FF00"
        "FF00"
        "FFFF"
        "FFFF"
    )
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    glColor3f(0, 1, 0)
    glRasterPos2i(128, 128)
    glBitmap(16, 16, 0, 0, 0, 0, data)

    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)

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