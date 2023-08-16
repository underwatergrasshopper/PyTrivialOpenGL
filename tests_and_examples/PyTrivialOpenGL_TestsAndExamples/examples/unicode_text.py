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

        self.text           = ""

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

    # Loading temporal font for displaying load message.
    _data.font.load("Courier New", _FONT_SIZE, togl.FontSizeUnitId.PIXELS, togl.FontStyleId.NORMAL, togl.UnicodeCharSetId.ENGLISH)
    if not _data.font.is_ok():
        print(_data.font.get_err_msg())

    _data.text = "Loading Font - Unicode Plane 0 ..."
    togl.to_window().draw_now()

    # Loading actual font.
    _data.font.load("Courier New", _FONT_SIZE, togl.FontSizeUnitId.PIXELS, togl.FontStyleId.NORMAL, togl.UnicodeCharSetId.RANGE_0000_FFFF)
    if not _data.font.is_ok():
        print(_data.font.get_err_msg())

    _data.text = "Unicode Text (Plane 0): \u0444\u3400\u5016\u9D9B.\nEscape - Exit."

    print("Escape - Exit", flush = True)

def do_on_destroy():
    _data.font.unload()

    glPopAttrib()

    print("Bye. Bye.", flush = True)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    _data.text_drawer.set_color(255, 255, 255, 255)
    _data.text_drawer.set_pos(10, _data.height - _FONT_SIZE)
    _data.text_drawer.render_text(_data.font, _data.text)

def do_on_key(key_id, is_down, extra):
    if key_id == togl.KeyId.ESCAPE:
        if not is_down:
            togl.to_window().request_close()

def do_on_resize(width, height):
    resize(width, height)

def run():
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Unicode Text",

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