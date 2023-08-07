import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

from PyTrivialOpenGL import C_GL
from PyTrivialOpenGL._Private import C_WGL

from PyTrivialOpenGL.Font import _FrameBuffer, _FontDataGenerator, _FontInfo
import ctypes

__all__ = [
    "run"
]
class _Data:
    def __init__(self):
        self.width  = 800
        self.height = 400

        self.frame_buffer = _FrameBuffer()

_data = _Data()

def set_orthogonal_projection(width, height):
    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()
    glOrtho(0, width, 0, height, 1, -1)

def do_on_create():
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    set_orthogonal_projection(_data.width, _data.height)

    glClearColor(0, 0, 0.5, 1)

    # address = C_WGL.wglGetProcAddress(b"glGenFramebuffersEXT")
    # print(address)
    # 
    # glGenFramebuffersEXT = ctypes.WINFUNCTYPE(None, C_GL.GLsizei, ctypes.POINTER(C_GL.GLuint))(address)
    # if glGenFramebuffersEXT:
    #     print("ok")
    # print(glGenFramebuffersEXT)
    # 
    # c_fbo = C_GL.GLuint(0)
    # 
    # glGenFramebuffersEXT(1, ctypes.byref(c_fbo))
    # print(c_fbo.value)
    # 
    # glGenFramebuffersEXT(1, ctypes.byref(c_fbo))
    # print(c_fbo.value)
    # 
    # _GL_FRAMEBUFFER_EXT             = 0x8D40
    # _GL_FRAMEBUFFER_BINDING         = 0x8CA6
    # _GL_COLOR_ATTACHMENT0_EXT       = 0x8CE0
    # _GL_FRAMEBUFFER_COMPLETE_EXT    = 0x8CD5
    # 
    # c_prev_fbo = C_GL.GLint(0)
    # C_GL.glGetIntegerv(_GL_FRAMEBUFFER_BINDING, ctypes.byref(c_prev_fbo))
    # print(c_prev_fbo.value)

    # _data.frame_buffer.create(_data.width, _data.height)
    # print(_data.frame_buffer.get_err_msg())
    # print(_data.frame_buffer.gen_and_bind_tex())
    # print(_data.frame_buffer.get_err_msg())
    # _data.frame_buffer.destroy()
    # print(_data.frame_buffer.get_err_msg())

    generator = _FontDataGenerator()
    font_data = generator.generate(_FontInfo("Courier New", 16, togl.FontSizeUnitId.PIXELS, togl.FontStyleId.NORMAL, togl.UnicodeCharSetId.ENGLISH))
    if not generator.is_ok():
        print(generator.get_err_msg())

    togl.save_texture_as_bmp("out/font.bmp", font_data.tex_objs[0])



    print("Escape - Exit")

def do_on_destroy():
    glPopAttrib()

    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)

    glColor3f(1, 0, 0)
    glRectdv([10, 10], [400, 200])


def do_on_key(key_id, is_down, extra):
    if not is_down:
        if key_id == togl.KeyId.ESCAPE:
            togl.to_window().request_close()

def do_on_resize(width, height):
    glViewport(0, 0, width, height)

    _data.width = width
    _data.height = height

    set_orthogonal_projection(_data.width, _data.height)

def run(name, options):
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Draw Font",
        area                = (_data.width, _data.height),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )