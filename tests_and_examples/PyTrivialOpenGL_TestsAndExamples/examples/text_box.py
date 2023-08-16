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

        self.is_show_prompt = False
        self.prompt         = "|"
        self.text           = "Type text."

_data = Data()

_FONT_SIZE  = 32
_PADDING    = 40


def pad(area, padding):
    """
    area    : Area
    padding : int
    Returns : Area
    """
    return togl.Area(
        area.x + padding, 
        area.y + padding, 
        area.width - padding * 2, 
        area.height - padding * 2
    )

def get_prompt():
    """
    Returns : str
    """
    if _data.is_show_prompt:
        # If prompt would is outside of text box, then move to new line.
        text = _data.text_adjuster.adjust_text(_data.font, _data.text)

        def get_height(text):
            return _data.text_drawer.get_text_size(_data.font, text).height

        if get_height(text) < get_height(text + _data.prompt):
            return "\n" + _data.prompt
        
        return _data.prompt

    return ""

def get_adjusted_text_with_prompt():
    """
    Returns : FineText
    """
    text = _data.text + _data.prompt

    # Adjust text to specific max line length and replaces tabs with spaces counting from beginning of the line.
    fine_text = _data.text_adjuster.adjust_text(_data.font, togl.FineText(text))

    if not _data.is_show_prompt:
        # Removes prompt but do not change text align. 
        # This prevents text jumping from one line to another when prompt appears.
        element = fine_text.to_elements()[-1]

        if isinstance(element, togl.Text):
            element.set_content(element.get_content()[0:-1])

    return fine_text


def draw_rectangle(x = None, y = None, width = None, height = None, area = None):
    """
    x       : int | None
    y       : int | None
    width   : int | None
    height  : int | None
    area    : int | None
    """
    if area is not None:
        x       = area.x
        y       = area.y
        width   = area.width
        height  = area.height

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

    print("Escape - Exit", flush = True)

def do_on_destroy():
    _data.font.unload()

    glPopAttrib()

    print("Bye. Bye.", flush = True)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    text_area = pad(togl.Area(0, 0, _data.width, _data.height), _PADDING)

    # Draws border.
    glColor3f(0.8, 0.8, 0.8)
    draw_rectangle(area = pad(text_area, -6)) # offset from text to border of text box

    # Draws text area.
    glColor3f(0.2, 0.2, 0.2)
    draw_rectangle(area = pad(text_area, -5)) # offset from text to text box edge

    # Changes max text line width in pixels after which, words are wrapped.
    _data.text_adjuster.set_line_wrap_width(text_area.width)

    _data.text_drawer.set_pos(_PADDING, _data.height - _FONT_SIZE - _PADDING)
    _data.text_drawer.set_color(200, 200, 200, 255)
    _data.text_drawer.render_text(_data.font, get_adjusted_text_with_prompt())

def do_on_key(key_id, is_down, extra):
    if key_id == togl.KeyId.ESCAPE:
        if not is_down:
            togl.to_window().request_close()

def do_on_text(text, is_correct):
    if is_correct:
        if text == '\b':
            if len(_data.text) > 0:
                _data.text = _data.text[0:-1]
        elif text == '\r':
            _data.text += '\n';
        elif text.isprintable() or text == '\t':
            _data.text += text
    

def do_on_resize(width, height):
    resize(width, height)

def do_on_time(time_interval):
    _data.is_show_prompt = not _data.is_show_prompt

def run():
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Text Box",

        # Sets width and height of windows draw area.
        area                = (800, 400),

        # Interprets size from 'area' parameter as size of draw area of window.
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        timer_time_interval = 500,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        do_on_time          = do_on_time,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,

        do_on_text          = do_on_text,
    )

if __name__ == "__main__":
    run()