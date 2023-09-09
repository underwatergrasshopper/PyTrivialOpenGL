import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

from PyTrivialOpenGL import C_GL
from PyTrivialOpenGL._Private import C_WGL

from PyTrivialOpenGL.Font import _FrameBuffer, _FontDataGenerator, _FontInfo
from ...utility.ExampleSupport import FPS_Counter, draw_rectangle

import ctypes
import cProfile
import os

__all__ = [
    "run"
]

class _Data:
    def __init__(self):
        self.options        = set()
        self.output_path    = ""

        self.width          = 800
        self.height         = 400

        self.fps_counter    = FPS_Counter()

        self.font           = togl.Font()
        self.text_drawer    = togl.TextDrawer()
        self.text_adjuster  = togl.TextAdjuster()

        self.fine_text      = togl.FineText()

_data = _Data()

def resize(width, height):
    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, 1, -1)

    _data.width = width
    _data.height = height

    fine_text = togl.FineText(
        (0, 255, 0, 255),
        "Xj\n",
        (255, 0, 0, 255),
        "Xj\n",
        (0, 0, 0, 255),
        (
            "Some text. \u3400\u5016\u9D9B\u0001\U00024B62. Many words in line. Many words in line. Many words in line. Many words in line. Many words in line. Many words in line.\n"
            "Many words in line with \ttab.\n"
            "Many words in line with i\ttab.\n"
            "Many words in line with ii\ttab.\n"
            "Many words in line with iii\ttab.\n"
            "Many words in line with iiii\ttab.\n"
            "New line. "
            "\tTab.Long                                 line. "
            "Very-long-text-to-split-apart. "
        )
    )

    _data.text_adjuster.set_line_wrap_width(_data.width - 10)
    _data.fine_text = _data.text_adjuster.adjust_text(_data.font, fine_text)


def do_on_create(data):
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    resize(data.width, data.height)

    glClearColor(0, 0, 0.5, 1)

    unicode_char_set_id = togl.UnicodeCharSetId.RANGE_0000_FFFF if "plane_0" in _data.options else togl.UnicodeCharSetId.ENGLISH

    font_name = "Arial" if "arial" in _data.options else "Courier New"
    _data.font.load(font_name, 16, togl.FontSizeUnitId.PIXELS, togl.FontStyleId.NORMAL, unicode_char_set_id)

    if "left_top" in _data.options:
        _data.font.set_origin_id(togl.OriginId.LEFT_TOP)

    if not _data.font.is_ok():
        print(_data.font.get_err_msg)
    else:
        if "export" in _data.options:
            print("Exporting textures...")
            _data.font.export_as_bmp(_data.output_path)
            print("Textures has been exported.")

    _data.text_drawer.set_color(255, 255, 255, 255)

    _data.fps_counter.reset()

    print("Escape - Exit")

def do_on_destroy():
    _data.font.unload()

    glPopAttrib()

    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    
    text_size = _data.text_drawer.get_text_size(_data.font, _data.fine_text)
    
    C_GL.glColor3f(1, 1, 1)

    draw_rectangle(0, _data.height - text_size.height, _data.width - 10, text_size.height)
    
    _data.text_drawer.set_pos(0 , _data.height - _data.font.get_height())
            
    _data.text_drawer.set_color(255, 0, 0, 255)
    _data.text_drawer.render_text(_data.font, _data.fine_text)
    
    if "show_fps" in _data.options:
        _data.fps_counter.update()


def do_on_key(key_id, is_down, extra):
    if not is_down:
        if key_id == togl.KeyId.ESCAPE:
            togl.to_window().request_close()

def do_on_resize(width, height):
    resize(width, height)


def run(name, options, output_path):
    _data.options = options
    if output_path:
        _data.output_path = output_path + "/mt_draw_text"
    else:
        _data.output_path = "mt_draw_text"

    if "debug" in options:
        togl.set_log_level(togl.LogLevel.DEBUG)
    else:
        togl.set_log_level(togl.LogLevel.INFO)

    if "stats" in options:
        pr = cProfile.Profile()
        pr.enable()

    result = togl.to_window().create_and_run(
        window_name         = "Draw Text",
        area                = (_data.width, _data.height),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )

    if "stats" in options:
        pr.disable()
        pr.print_stats('tottime') # cumulative, tottime

    return result