import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

__all__ = [
    "run"
]

class Data:
    def __init__(self):
        self.font           = togl.Font()
        self.text_drawer    = togl.TextDrawer()
        self.text_adjuster  = togl.TextAdjuster()

        self.width          = 0
        self.height         = 0

        self.text           = ""

_data = Data()

_FONT_SIZE  = 16
_PADDING    = 10

def draw_rectangle(x, y, width, height):
    glBegin(GL_TRIANGLE_FAN)

    glVertex2i(x,           y)
    glVertex2i(x + width,   y)
    glVertex2i(x + width,   y + height)
    glVertex2i(x,           y + height)

    glEnd()

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

    _data.font.load("Arial", _FONT_SIZE, togl.FontSizeUnitId.PIXELS, togl.FontStyleId.NORMAL, togl.UnicodeCharSetId.ENGLISH)
    if not _data.font.is_ok():
        print(_data.font.get_err_msg())

    _data.text_adjuster.set_number_of_spaces_in_tab(4)

    _data.text = togl.FineText(
        (100, 200, 100, 255),
        "By changing width of window, text will be aligned to new width.\n",
        (200, 200, 200, 255),
        (
            "Some sentence text. Some sentence text. Some sentence text. "
            "Some sentence text. Some sentence text. Some sentence text.\n"
            "Some sentence text. \ttab\n"
            "Some sentence text. i\ttab\n"
            "Some sentence text. ii\ttab\n"
            "Some sentence text. iii\ttab\n"
            "Some sentence text. iiii\ttab\n"
            "Some sentence text. iiiii\ttab\n"
            "Some sentence text. iiiiii\ttab\n"
            "Some sentence text. iiiiiii\ttab\n"
            "Some sentence text. some-simple-very-long-word-to-cut-into-many-pieces\n"
            "Some other interesting text.\n"
        ),
        (200, 100, 100, 255),
        "Escape - Exit.",
    )

    print("Escape - Exit", flush = True)

def do_on_destroy():
    _data.font.unload()

    glPopAttrib()

    print("Bye. Bye.", flush = True)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    x       = _PADDING
    y       = _PADDING
    width   = _data.width - _PADDING * 2
    height  = _data.height - _PADDING * 2

    # Draws border.
    glColor3f(1, 0, 0);
    draw_rectangle(x - 1, y - 1, width + 2, height + 2);

    # Draws text area.
    glColor3f(0.2, 0.2, 0.2)
    draw_rectangle(x, y, width, height)

    # Changes max text line width in pixels after which, words are wrapped.
    _data.text_adjuster.set_line_wrap_width(width)

    # Formats text using information provided by TOGL_SetNumberOfSpacesInTab and TOGL_SetLineWrapWidth.
    text = _data.text_adjuster.adjust_text(_data.font, _data.text)

    _data.text_drawer.set_pos(_PADDING, _data.height - _FONT_SIZE - _PADDING)
    _data.text_drawer.set_color(0, 0, 0, 255)
    _data.text_drawer.render_text(_data.font, text)

def do_on_key(key_id, is_down, extra):
    if key_id == togl.KeyId.ESCAPE:
        if not is_down:
            togl.to_window().request_close()

def do_on_resize(width, height):
    resize(width, height)

def run():
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Formated Text",

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