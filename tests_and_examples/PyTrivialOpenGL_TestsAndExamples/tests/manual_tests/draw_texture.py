import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *
from PyTrivialOpenGL import C_GL
import ctypes
import math
from ...utility.ExampleSupport import FPS_Counter, check_gl_error, is_close


__all__ = [
    "run"
]

class _Data:
    def __init__(self):
        self.tex_obj = None
        self.other_tex_objs = []
        self.options = set()
        self.fps_counter = FPS_Counter()

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

            if "sub" in _data.options:
                glTexSubImage1D(GL_TEXTURE_1D, 0, 1, 2, GL_RGBA, GL_FLOAT, [1, 1, 0, 0.5,   1, 0, 1, 0.5])
        else:
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 3, 2, 0, GL_RGBA, GL_FLOAT, pixels)

            print(glGetTexImage(GL_TEXTURE_2D, 0, GL_RGBA, GL_FLOAT, is_return_list = True))
            assert is_close(glGetTexImage(GL_TEXTURE_2D, 0, GL_RGBA, GL_FLOAT, is_return_list = True), pixels, 0.01)

            if "sub" in _data.options:
                # debug
                #glTexSubImage2D(GL_TEXTURE_2D, 0, 1, 0, 1, 2, GL_RGBA, GL_UNSIGNED_BYTE, b"\xFF\xFF\x00\x7F\xFF\x00\xFF\x7F")
                glTexSubImage2D(GL_TEXTURE_2D, 0, 1, 0, 1, 2, GL_RGBA, GL_FLOAT, [1, 1, 0, 0.5,   1, 0, 1, 0.5])

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

            assert glGetTexLevelParameteriv(GL_TEXTURE_1D, 0, GL_TEXTURE_WIDTH)[0] == 6
            assert glGetTexLevelParameteriv(GL_TEXTURE_1D, 0, GL_TEXTURE_HEIGHT)[0] == 1

            assert glGetTexImage(GL_TEXTURE_1D, 0, GL_RGBA, GL_UNSIGNED_BYTE) == pixels

            if "sub" in _data.options:
                glTexSubImage1D(GL_TEXTURE_1D, 0, 1, 2, GL_RGBA, GL_UNSIGNED_BYTE, b"\xFF\xFF\x00\x7F\xFF\x00\xFF\x7F")

        else:
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 3, 2, 0, GL_RGBA, GL_UNSIGNED_BYTE, pixels)

            assert glGetTexLevelParameteriv(GL_TEXTURE_2D, 0, GL_TEXTURE_WIDTH)[0] == 3
            assert glGetTexLevelParameteriv(GL_TEXTURE_2D, 0, GL_TEXTURE_HEIGHT)[0] == 2

            assert glGetTexImage(GL_TEXTURE_2D, 0, GL_RGBA, GL_UNSIGNED_BYTE) == pixels

            if "sub" in _data.options:
                glTexSubImage2D(GL_TEXTURE_2D, 0, 1, 0, 1, 2, GL_RGBA, GL_UNSIGNED_BYTE, b"\xFF\xFF\x00\x7F\xFF\x00\xFF\x7F")


        check_gl_error()

        _data.fps_counter.reset()

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


    print("GL_TEXTURE_ENV_MODE:", glGetTexEnviv(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE))
    assert glGetTexEnviv(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE) == [GL_MODULATE]
    glTexEnviv(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, [GL_ADD])
    assert glGetTexEnviv(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE) == [GL_ADD]
    glTexEnviv(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, [GL_MODULATE])

    print("GL_TEXTURE_ENV_COLOR:", glGetTexEnvfv(GL_TEXTURE_ENV, GL_TEXTURE_ENV_COLOR))
    assert glGetTexEnvfv(GL_TEXTURE_ENV, GL_TEXTURE_ENV_COLOR) == [0.0, 0.0, 0.0, 0.0]
    glTexEnvfv(GL_TEXTURE_ENV, GL_TEXTURE_ENV_COLOR, [0.5, 0.1, 1.0, 0.7])
    assert is_close(glGetTexEnvfv(GL_TEXTURE_ENV, GL_TEXTURE_ENV_COLOR), [0.5, 0.1, 1.0, 0.7], 0.01)
    glTexEnvfv(GL_TEXTURE_ENV, GL_TEXTURE_ENV_COLOR, [0, 0, 0, 0])
    assert glGetTexEnvfv(GL_TEXTURE_ENV, GL_TEXTURE_ENV_COLOR) == [0.0, 0.0, 0.0, 0.0]

    print("GL_TEXTURE_GEN_MODE:", glGetTexGeniv(GL_S, GL_TEXTURE_GEN_MODE))
    assert glGetTexGeniv(GL_S, GL_TEXTURE_GEN_MODE) == [GL_EYE_LINEAR]
    glTexGenfv(GL_S, GL_TEXTURE_GEN_MODE, [GL_OBJECT_LINEAR])
    assert glGetTexGeniv(GL_S, GL_TEXTURE_GEN_MODE) == [GL_OBJECT_LINEAR]
    glTexGenfv(GL_S, GL_TEXTURE_GEN_MODE, [GL_EYE_LINEAR])
    
    print("GL_EYE_PLANE:", glGetTexGenfv(GL_S, GL_EYE_PLANE))
    assert glGetTexGenfv(GL_S, GL_EYE_PLANE) == [1, 0, 0, 0]
    glTexGenfv(GL_S, GL_EYE_PLANE, [1, 1, 0, 0])
    assert glGetTexGenfv(GL_S, GL_EYE_PLANE) == [1, 1, 0, 0]
    glTexGenfv(GL_S, GL_EYE_PLANE, [1, 0, 0, 0])

    # Bug: ctypes.windll.OpenGL32.glTexGeniv generates access violation.
    #c_params = C_GL.GLint(GL_EYE_LINEAR)
    #ctypes.windll.OpenGL32.glTexGeniv(GL_S, GL_TEXTURE_GEN_MODE, ctypes.byref(c_params))


    pixel_data = bytes.fromhex(
        "FF0000FF 00FF00FF 0000FFFF"
        "FFFFFFFF 000000FF FFFFFF7F"
    )

    togl.save_as_bmp("out/pixels.bmp", pixel_data, 3, 2, False)
    togl.save_texture_as_bmp("out/texture.bmp", _data.tex_obj)


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
    
    if "vec" in _data.options:
        glTexCoord2fv([0, 0])
        glVertex2fv([-0.5, -0.5])
    
        glTexCoord2fv([1, 0])
        glVertex2fv([0.5, -0.5])
    
        glTexCoord2fv([1, 1])
        glVertex2fv([0.5, 0.5])
    
        glTexCoord2fv([0, 1])
        glVertex2fv([-0.5, 0.5])
    else:
        glTexCoord2f(0, 0)
        glVertex2f(-0.5, -0.5)
        
        glTexCoord2f(1, 0)
        glVertex2f(0.5, -0.5)
        
        glTexCoord2f(1, 1)
        glVertex2f(0.5, 0.5)
        
        glTexCoord2f(0, 1)
        glVertex2f(-0.5, 0.5)
    
    glEnd()

    if "fps" in _data.options:
        _data.fps_counter.update()

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