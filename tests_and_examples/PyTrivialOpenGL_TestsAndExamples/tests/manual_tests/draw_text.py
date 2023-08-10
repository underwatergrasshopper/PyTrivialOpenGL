import PyTrivialOpenGL as togl
from PyTrivialOpenGL import TextAdjuster
from PyTrivialOpenGL.GL import *

from PyTrivialOpenGL import C_GL
from PyTrivialOpenGL._Private import C_WGL

from PyTrivialOpenGL.Font import _FrameBuffer, _FontDataGenerator, _FontInfo
from ...utility.ExampleSupport import FPS_Counter

import ctypes

__all__ = [
    "run"
]
class _Data:
    def __init__(self):
        self.options        = set()

        self.width          = 800
        self.height         = 400

        self.fps_counter    = FPS_Counter()

        self.font           = togl.Font()
        self.text_drawer    = togl.TextDrawer()

_data = _Data()

def set_orthogonal_projection(width, height):
    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()
    glOrtho(0, width, 0, height, 1, -1)

def do_on_create():
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    set_orthogonal_projection(_data.width, _data.height)

    glClearColor(0, 0, 0.5, 1)

    unicode_char_set_id = togl.UnicodeCharSetId.RANGE_0000_FFFF if "plane_0" in _data.options else togl.UnicodeCharSetId.ENGLISH

    _data.font.load("Courier New", 32, togl.FontSizeUnitId.PIXELS, togl.FontStyleId.NORMAL, unicode_char_set_id)

    if "left_top" in _data.options:
        _data.font.set_origin_id(togl.OriginId.LEFT_TOP)

    if not _data.font.is_ok():
        print(_data.font.get_err_msg)
    else:
        if "export" in _data.options:
            print("Exporting textures...")
            _data.font.export_as_bmp("out/font")
            print("Textures has been exported.")

    _data.text_drawer.set_color(1, 1, 1, 1)

    _data.fps_counter.reset()

    print("Escape - Exit")

def do_on_destroy():
    _data.font.unload()

    glPopAttrib()

    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)

    _data.text_drawer.set_pos(100, 100)
    _data.text_drawer.render_text(_data.font, "Some text.\nNew line text.")
    
    _data.text_drawer.set_pos(100, 300)
    line_width = _data.width - 100
    text_adjuster = TextAdjuster()
    text_adjuster.set_line_wrap_width(line_width)
    fine_text = text_adjuster.adjust_text(_data.font, togl.FineText("Some text.", (255, 0, 0, 255), "\nNew line red text."))
    _data.text_drawer.render_text(_data.font, fine_text)
    
    if "show_fps" in _data.options:
        _data.fps_counter.update()


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
    _data.options = options

    if "debug" in options:
        togl.set_log_level(togl.LogLevel.DEBUG)
    else:
        togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Draw Text",
        area                = (_data.width, _data.height),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )