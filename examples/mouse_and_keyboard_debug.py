import enum

import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

from ExampleSupport    import *
from ExampleManager    import *
from ActionChain       import *
from AnimatedTriangle  import *
from examples.ExampleSupport import FPS_Counter

__all__ = [
    "run"
]

_WIDTH      = 600   # in pixels
_HEIGHT     = 300   # in pixels

class Data:
    """
    angle               : int | float
    is_draw_area        : bool
    area                : Area
    options             : Set[str]
    action_chain        : ActionChain
    animated_triangle   : AnimatedTriangle
    """
    def __init__(self):
        self.reset()

    def reset(self):
        self.options            = set() 
        self.action_chain       = ActionChain()
        self.animated_triangle  = AnimatedTriangle()
        self.fps_counter        = FPS_Counter()

_data   = Data()
_window = togl.to_window()

_legend = """--- Legend ---
C           - Center
I           - Info
L           - Legend
Alt + F4    - Exit (managed by system)
Escape      - Exit
---
"""

def display_legend():
    print(_legend)

def set_orthogonal_projection(width, height):
    glPushAttrib(GL_TRANSFORM_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, 1, -1)

    glPopAttrib()

def do_on_create():
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    display_legend()

    set_orthogonal_projection(_WIDTH, _HEIGHT)

    glClearColor(0, 0, 0.5, 1)

    _data.fps_counter.reset()


def do_on_close():
    return togl.run_question_box("Close", "Are you sure?")

def do_on_destroy():
    glPopAttrib()

    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    _data.animated_triangle.draw()

    _data.action_chain.try_execute()

    if "show_fps" in _data.options: _data.fps_counter.update()

def do_on_mouse_move(x, y):
    print("do_on_mouse_move: %d %d" % (x, y))

def do_on_mouse_wheel_roll(step_cout, x, y):
    print("do_on_mouse_wheel_roll: %d %d %d" % (step_cout, x, y))

def do_on_key(key_id, is_down, extra):
    print("do_on_key: key_id=%s, is_down=%d, %s" % (key_id.name, is_down, extra))

    if False:
        pass

    elif key_id == togl.KeyId.F4 and extra.is_alt_down:
        return False # Allows 'Alt + F4' to get through.

    elif key_id == 'C' and not is_down:
        _window.center(_WIDTH, _HEIGHT, is_draw_area_size = True)

    elif key_id == 'I' and not is_down:
        display_info()

    elif key_id == 'L' and not is_down:
        display_legend()

    elif key_id == togl.KeyId.ESCAPE and not is_down:
        _window.request_close()


def do_on_text(text, is_correct):
    print("do_on_text: text='%s', code_point=%Xh, is_correct=%d" % (text, ord(text), is_correct))

def do_on_resize(width, height):
    print("do_on_resize: %d %d" % (width, height))

    glViewport(0, 0, width, height)

    _data.animated_triangle.resize(width, height)
        
    set_orthogonal_projection(width, height)

def do_on_time(time_interval):
    if "notify_timer" in _data.options: 
        print("time_interval: %dms" % time_interval)

    _data.animated_triangle.update(time_interval / 1000.0)


def run(name, options):
    _data.reset()
    _data.options = options

    if "no_debug" in options:   togl.set_log_level(togl.LogLevel.INFO)
    else:                       togl.set_log_level(togl.LogLevel.DEBUG)
    
    togl.to_special_debug().reset()
    if "notify_remaining_messages" in options:      togl.to_special_debug().is_notify_remaining_messages    = True
    if "notify_draw_call" in options:               togl.to_special_debug().is_notify_draw_call             = True
    if "notify_mouse_move" in options:              togl.to_special_debug().is_notify_mouse_move            = True
    if "notify_key_message" in options:             togl.to_special_debug().is_notify_key_message           = True
    if "notify_character_message" in options:       togl.to_special_debug().is_notify_character_message     = True
    if "notify_timer" in options:                   togl.to_special_debug().is_notify_timer                 = True
    if "full_exit_track_in_callback" in options:    togl.to_special_debug().is_full_exit_track_in_callback  = True

    if "disable_auto_sleep" in options:             togl.to_window().set_option(togl.WindowOptionId.AUTO_SLEEP_MODE, True)

    style = 0
    if "no_resize" in options:          style |= togl.WindowStyleBit.NO_RESIZE
    if "no_maximize" in options:        style |= togl.WindowStyleBit.NO_MAXIMIZE
    if "centered" in options:           style |= togl.WindowStyleBit.CENTERED
    if "draw_area_size" in options:     style |= togl.WindowStyleBit.DRAW_AREA_SIZE
    if "draw_area_only" in options:     style |= togl.WindowStyleBit.DRAW_AREA_ONLY
    if "redraw_on_request" in options:  style |= togl.WindowStyleBit.REDRAW_ON_CHANGE_OR_REQUEST

    if "minimized" in options:                  state_id = togl.WindowStateId.MINIMIZED
    elif "maximized" in options:                state_id = togl.WindowStateId.MAXIMIZED
    elif "windowed_full_screened" in options:   state_id = togl.WindowStateId.WINDOWED_FULL_SCREENED
    else:                                       state_id = togl.WindowStateId.NORMAL

    return togl.to_window().create_and_run(
        window_name         = "Mouse and Keyboard (debug)",
        area                = (0, 0, _WIDTH, _HEIGHT) if "alt_center" not in options else (_WIDTH, _HEIGHT),
        style               = style,
        state_id            = state_id,
        is_hidden           = True if "hidden" in options else False,

        opengl_version      = (3, 3) if "opengl_3_3" in options else None,

        timer_time_interval = 20,
        icon_file_name      = "tests\\assets\\icon.ico" if "no_icon" not in options else "",

        do_on_create            = do_on_create,
        do_on_close             = do_on_close if "ask_on_close" in options else None,
        do_on_destroy           = do_on_destroy,
        draw                    = draw,

        do_on_mouse_move        = do_on_mouse_move,
        do_on_mouse_wheel_roll  = do_on_mouse_wheel_roll,
        do_on_key               = do_on_key,
        do_on_text              = do_on_text,

        do_on_resize            = do_on_resize,
        do_on_time              = do_on_time,
    )