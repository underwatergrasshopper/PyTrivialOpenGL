import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

__all__ = [
    "run"
]

class Data:
    def __init__(self):
        self.font           = togl.Font()
        self.text_drawer    = togl.TextDrawer()

        self.width          = 0
        self.height         = 0

_data = Data()

_FONT_SIZE = 32

def resize(width, height):
    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, 1, -1)

    _data.width     = width
    _data.height    = height

def do_on_create(data):
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    resize(data.width, data.height)

    glClearColor(0, 0, 0.5, 1)

    _data.font.load(
        "Courier New", 
        _FONT_SIZE, 
        togl.FontSizeUnitId.PIXELS, 
        togl.FontStyleId.NORMAL, 
        togl.UnicodeCharSetId.CUSTOM, 
        [
            (0x0020, 0x007F), # Basic Latin
            (0x00A0, 0x00FF), # Latin-1 Supplement
            (0x0100, 0x017F), # Latin Extended-A
            (0x0180, 0x024F), # Latin Extended-B
            (0x0250, 0x02AF), # IPA Extensions
            (0x02B0, 0x02FF), # Spacing Modifier Letters
            (0x0300, 0x036F), # Combining Diacritical Marks
            (0x0370, 0x03FF), # Greek and Coptic
            togl.UnicodeCodePoint.WHITE_SQUARE,
            togl.UnicodeCodePoint.REPLACEMENT_CHARACTER,
        ]
    )
    if not _data.font.is_ok():
        print(_data.font.get_err_msg())

    print("Escape - Exit", flush = True)

def do_on_destroy():
    _data.font.unload()

    glPopAttrib()

    print("Bye. Bye.", flush = True)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    _data.text_drawer.set_color(255, 255, 127, 255) # optional
    _data.text_drawer.set_pos(10, _data.height - _FONT_SIZE)
    _data.text_drawer.render_text(_data.font, "Eastern european glyphs: \u015B\u0144\u0107.\n")
    _data.text_drawer.render_text(_data.font, "Escape - Exit.")

def do_on_key(key_id, is_down, extra):
    if key_id == togl.KeyId.ESCAPE:
        if not is_down:
            togl.to_window().request_close()

def do_on_resize(width, height):
    resize(width, height)

def run():
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Font - custom code point range",

        # Sets width and height of windows draw area.
        area                = (800, 400),

        # Interprets size from 'area' parameter as size of draw area of window.
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )

if __name__ == "__main__":
    run()