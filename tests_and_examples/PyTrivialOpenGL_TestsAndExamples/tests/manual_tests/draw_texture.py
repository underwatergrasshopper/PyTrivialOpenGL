import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *
from PyTrivialOpenGL import C_GL
import ctypes

from ...utility.ExampleSupport import check_gl_error

__all__ = [
    "run"
]

class _Data:
    def __init__(self):
        self.tex_obj = None

_data = _Data()

def do_on_create():
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glClearColor(0, 0, 0.5, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
        
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

    glEnable(GL_TEXTURE_2D)

    _data.tex_obj = glGenTextures(1)[0]
    check_gl_error()
    print("tex_obj:", _data.tex_obj)
    
    glBindTexture(GL_TEXTURE_2D, _data.tex_obj)
    check_gl_error()
    assert glIsTexture(_data.tex_obj)

    pixels = bytes.fromhex(
        "FF0000FF 00FF00FF 0000FFFF"
        "FFFFFFFF 000000FF FFFFFF7F"
    )
    print("pixel data:", pixels)

    glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
    check_gl_error()

    # equivalent 1
    #c_pixels = (C_GL.GLubyte * len(pixels)).from_buffer_copy(pixels)
    #c_pixels = ctypes.cast(c_pixels, ctypes.c_void_p)
    #C_GL.glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 3, 2, 0, GL_RGBA, GL_UNSIGNED_BYTE, c_pixels)

    # equivalent 2
    #C_GL.glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 3, 2, 0, GL_RGBA, GL_UNSIGNED_BYTE, pixels)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 3, 2, 0, GL_RGBA, GL_UNSIGNED_BYTE, pixels)
    check_gl_error()

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    check_gl_error()

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    check_gl_error()

    print("Escape - Exit")

def do_on_destroy():
    glBindTexture(GL_TEXTURE_2D, 0)
    check_gl_error()
    assert glIsTexture(_data.tex_obj)
    
    glDeleteTextures([_data.tex_obj])
    check_gl_error()
    assert not glIsTexture(_data.tex_obj)

    glPopAttrib()

    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glBegin(GL_TRIANGLE_FAN)
    
    glTexCoord2f(0, 0)
    glVertex2f(-0.5, -0.5)
    
    glTexCoord2f(1, 0)
    glVertex2f(0.5, -0.5)
    
    glTexCoord2f(1, 1)
    glVertex2f(0.5, 0.5)
    
    glTexCoord2f(0, 1)
    glVertex2f(-0.5, 0.5)
    
    glEnd()

def do_on_key(key_id, is_down, extra):
    if not is_down:
        if key_id == togl.KeyId.ESCAPE:
            togl.to_window().request_close()

def do_on_resize(width, height):
    glViewport(0, 0, width, height)

def run(name, options):
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Draw Texture",
        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )