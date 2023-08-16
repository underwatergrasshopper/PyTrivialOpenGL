
import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

__all__ = [
    "run"
]

_WIDTH      = 800   # in pixels
_HEIGHT     = 400   # in pixels

_MOVE_STEP  = 30    # in pixels
_FONT_SIZE  = 16    # in pixels

class Data:
    def __init__(self):
        self.reset()

    def reset(self):
        self.width              = _WIDTH
        self.height             = _HEIGHT

        self.legend_offset      = 0

        self.font               = togl.Font()
        self.text_drawer        = togl.TextDrawer()

        self.show_count_down    = 2000 # in ms

_data   = Data()

_legend = (
    "Mouse Wheel - Scroll Legend\n"

    "Arrows      - Move Window\n"
    "F           - Go Windowed Full Screen\n"
    "M           - Minimize\n"
    "Shift + M   - Maximize\n"
    "C           - Center\n"
    "H           - Hide                     [shows back after up to 2 sec]\n"
    "Arrows      - Move Window\n"
    "S           - Normal Size Window\n"
    "Shift + S   - Big Size Window\n"

    "Escape      - Exit\n"
)

def resize(width, height):
    glViewport(0, 0, width, height)

    glPushAttrib(GL_TRANSFORM_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, 1, -1)

    glPopAttrib()

    _data.width     = width
    _data.height    = height

def do_on_create(data):
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    resize(data.width, data.height)

    glClearColor(0.2, 0.2, 0.7, 1)

    _data.font.load("Courier New", _FONT_SIZE, togl.FontSizeUnitId.PIXELS, togl.FontStyleId.NORMAL, togl.UnicodeCharSetId.ENGLISH)
    if _data.font.is_ok():
        print("Font loaded.")
    else:
        print("Can not load font.")
        print("Error: " + _data.font.get_err_msg())

    print("Escape - Exit", flush = True)


def do_on_destroy():
    _data.font.unload()

    glPopAttrib()

    print("Bye. Bye.", flush = True)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    _data.text_drawer.set_color(255, 255, 255, 255)
    _data.text_drawer.set_pos(0, _data.height - _FONT_SIZE + _data.legend_offset)
    _data.text_drawer.render_text(_data.font, _legend)

def do_on_mouse_wheel_roll(step_cout, x, y):
    _data.legend_offset -= step_cout * _FONT_SIZE

def do_on_key(key_id, is_down, extra):
    is_up = not is_down

    if False:
        pass

    elif key_id == togl.KeyId.ARROW_LEFT and is_down:
        togl.to_window().move_by(-_MOVE_STEP, 0)
    elif key_id == togl.KeyId.ARROW_RIGHT and is_down:
        togl.to_window().move_by(_MOVE_STEP, 0)
    elif key_id == togl.KeyId.ARROW_UP and is_down:
        togl.to_window().move_by(0, -_MOVE_STEP)
    elif key_id == togl.KeyId.ARROW_DOWN and is_down:
        togl.to_window().move_by(0, _MOVE_STEP)

    elif key_id == 'F' and is_up:
        togl.to_window().go_windowed_full_screen()

    elif key_id == 'M' and is_up:
        if extra.is_shift_down:
            togl.to_window().maximize()
        else:
            togl.to_window().minimize()

    elif key_id == 'C' and is_up:
        togl.to_window().center(is_draw_area_size = True)

    elif key_id == 'H' and is_up:
        togl.to_window().hide()

    elif key_id == 'S' and is_up:
        if extra.is_shift_down:
            togl.to_window().resize(_WIDTH * 2, _HEIGHT * 2, is_draw_area = True)
        else:
            togl.to_window().resize(_WIDTH, _HEIGHT, is_draw_area = True)

    elif key_id == togl.KeyId.ESCAPE and not is_down:
        togl.to_window().request_close()

def do_on_resize(width, height):
    resize(width, height)

def do_on_time(time_interval):
    if not togl.to_window().is_visible():
        _data.show_count_down -= time_interval
        if _data.show_count_down <= 0:
            togl.to_window().show()
            _data.show_count_down = 2000

def run():
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name             = "Window State",
        area                    = (_WIDTH, _HEIGHT),
        style                   = togl.WindowStyleBit.DRAW_AREA_SIZE,

        timer_time_interval     = 20,

        do_on_create            = do_on_create,
        do_on_destroy           = do_on_destroy,
        draw                    = draw,

        do_on_mouse_wheel_roll  = do_on_mouse_wheel_roll,
        do_on_key               = do_on_key,

        do_on_resize            = do_on_resize,
        do_on_time              = do_on_time,
    )