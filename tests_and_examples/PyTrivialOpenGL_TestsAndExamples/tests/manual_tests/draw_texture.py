import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *
from PyTrivialOpenGL import C_GL
import ctypes
import math

from ...utility.ExampleSupport import check_gl_error

__all__ = [
    "run"
]

class _Data:
    def __init__(self):
        self.tex_obj = None
        self.other_tex_objs = []
        self.options = set()

_data = _Data()

def do_on_create():
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glClearColor(0, 0, 0.5, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
        
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

    if "1d" in _data.options:
        glEnable(GL_TEXTURE_1D)
    else:
        glEnable(GL_TEXTURE_2D)
        
    _data.other_tex_objs = glGenTextures(3)
    _data.tex_obj = glGenTextures(1)[0]
    check_gl_error()
    print("tex_obj:", _data.tex_obj)

    
    if "1d" in _data.options:
        glBindTexture(GL_TEXTURE_1D, _data.tex_obj)
    else:
        glBindTexture(GL_TEXTURE_2D, _data.tex_obj)

    check_gl_error()
    assert glIsTexture(_data.tex_obj)

    if "float" in _data.options:
        pixels = [
            1, 0, 0, 1,   0, 1, 0, 1,   0, 0, 1, 1,
            1, 1, 1, 1,   0, 0, 0, 1,   1, 1, 1, 0.5,
        ]
        print("pixel data:", pixels)

        glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
        check_gl_error()

        if "1d" in _data.options:
            glTexImage1D(GL_TEXTURE_1D, 0, GL_RGBA, 6, 0, GL_RGBA, GL_FLOAT, pixels)
        else:
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 3, 2, 0, GL_RGBA, GL_FLOAT, pixels)
        check_gl_error()
    else:
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

        if "1d" in _data.options:
            glTexImage1D(GL_TEXTURE_1D, 0, GL_RGBA, 6, 0, GL_RGBA, GL_UNSIGNED_BYTE, pixels)
        else:
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 3, 2, 0, GL_RGBA, GL_UNSIGNED_BYTE, pixels)

        check_gl_error()

    if "1d" in _data.options:
        glTexParameteri(GL_TEXTURE_1D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        check_gl_error()

        glTexParameteri(GL_TEXTURE_1D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        check_gl_error()
    else:
        glTexParameteriv(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, [GL_NEAREST])
        check_gl_error()
        assert glGetTexParameteriv(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER) == [GL_NEAREST]

        glTexParameteriv(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, [GL_NEAREST])
        check_gl_error()
        assert glGetTexParameteriv(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER) == [GL_NEAREST]

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)

        glTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR, [1, 0, 0, 1])
        check_gl_error()
        assert glGetTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_BORDER_COLOR) == [1, 0, 0, 1]

        # glAreTexturesResident is deprecated. Information provided by this function might not be correct.
        # From observation, it seams, that if any texture from 'textures' parameter is not resident, 
        # then all items of 'residents' parameter are set to False, event if any texture is resident.

        residences = []
        print("glAreTexturesResident: %s" % glAreTexturesResident([_data.tex_obj], residences))
        print("residences: %s" % residences)

        print("glAreTexturesResident: %s" % glAreTexturesResident([_data.tex_obj]))

        residences = []
        print("glAreTexturesResident: %s" % glAreTexturesResident([_data.other_tex_objs[0]], residences))
        print("residences: %s" % residences)

        residences = []
        print("glAreTexturesResident: %s" % glAreTexturesResident(_data.other_tex_objs, residences))
        print("residences: %s" % residences)

        print("Texture Priority: %s" % glGetTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_PRIORITY))
        glPrioritizeTextures([_data.tex_obj],[0.5])
        assert math.isclose(glGetTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_PRIORITY)[0], 0.5, rel_tol = 0.0001)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_PRIORITY, 0.7)
        assert math.isclose(glGetTexParameterfv(GL_TEXTURE_2D, GL_TEXTURE_PRIORITY)[0], 0.7, rel_tol = 0.0001)

    print("Escape - Exit")

def do_on_destroy():
    if "1d" in _data.options:
        glBindTexture(GL_TEXTURE_1D, 0)
    else:
        print("texture name before unbind:", glGetIntegerv(GL_TEXTURE_BINDING_2D)[0])
        glBindTexture(GL_TEXTURE_2D, 0)
        # According to OpenGl specification of glBindTexture function. 
        # When texture name, which is not generated by glGenTextures, is binded then GL_INVALID_VALUE error is registered. 
        assert glGetError() == GL_INVALID_VALUE
        print("texture name after unbind:", glGetIntegerv(GL_TEXTURE_BINDING_2D)[0])


    check_gl_error()
    assert glIsTexture(_data.tex_obj)
   
    glDeleteTextures([_data.tex_obj])
    check_gl_error()
    assert not glIsTexture(_data.tex_obj)

    glDeleteTextures(_data.other_tex_objs)
    check_gl_error()

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
    _data.options = options

    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Draw Texture (%s)" % (" ".join(options)) if len(options) > 0 else "Draw Texture",
        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )