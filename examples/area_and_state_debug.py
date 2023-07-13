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

_MOVE_STEP  = 30    # in pixels

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
        self.angle              = 0
        self.is_draw_area       = False
        self.options            = set() 
        self.action_chain       = ActionChain()
        self.animated_triangle  = AnimatedTriangle()
        self.fps_counter        = FPS_Counter()

_data   = Data()
_window = togl.to_window()

_legend = """--- Legend ---
Arrows      - Move by 30px
T           - Delay 3s -> Foreground                        [wait for 'done']
H           - Hide 1s -> Show                               [wait for 'done']
M           - Minimize 1s -> Center (width=600, height=300) [wait for 'done']
Shift + M   - Maximize
F           - Windowed Full Screen

C           - Center
Shift + C   - Center (width=600, height=300)
L. Ctrl + C - Center Draw Area (width=600, height=300)
R. Ctrl + C - Center Window Area (width=600, height=300)
 
P           - Move to (x=10, y=50)
L. Ctrl + P - Move to (x=10)
R. Ctrl + P - Move to (y=50)
O           - Move to (x=0, y=0)
Shift + O   - Move to (pos=Point(0,0))
    
S           - Resize (width=300, height=200)
L. Ctrl + S - Resize (width=300)
R. Ctrl + S - Resize (height=200)
Shift + S   - Resize (width=600, height=300)
    
A           - Reshape(x=10, y=50, width=600, height=300)
Shift + A   - Reshape(area=Area(10, 50, 600, 300)
L. Ctrl + A - Reshape(x=10, width=600)
R. Ctrl + A - Reshape(y=50, height=300)
    
D           - Toggle: by Window Area <-> by Draw Area
R           - Request Draw
        
0           - Move by (none) 1s -> Move to (none) 1s -> Resize (none) 1s -> 
              Reshape (none)  1s -> Center (none)           [wait for 'done']
1           - Minimize -> Move by (30, 0) -> Resize (600, 300) [wait for 'done']

I           - Info
L           - Legend
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
    print("do_on_create")
    print("L - Legend")

    set_orthogonal_projection(_WIDTH, _HEIGHT)

    glClearColor(0, 0, 0, 1)

    _data.fps_counter.reset()

    # Cause exception.
    #togl.to_window().center()

def do_on_close():
    print("do_on_close")
    return togl.run_question_box("Close", "Are you sure?")

def do_on_destroy():
    print("do_on_destroy")
    print("Bye. Bye.")

def draw():
    glPushAttrib(GL_COLOR_BUFFER_BIT)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    _data.animated_triangle.draw()

    if "show_fps" in _data.options: _data.fps_counter.update()

    glPopAttrib()

def do_on_key(key_id, is_down, extra):
    if False:
        pass

    elif key_id == togl.KeyId.ARROW_LEFT and is_down:
        _window.move_by(-_MOVE_STEP, 0)
    elif key_id == togl.KeyId.ARROW_RIGHT and is_down:
        _window.move_by(_MOVE_STEP, 0)
    elif key_id == togl.KeyId.ARROW_UP and is_down:
        _window.move_by(0, -_MOVE_STEP)
    elif key_id == togl.KeyId.ARROW_DOWN and is_down:
        _window.move_by(0, _MOVE_STEP)

    elif key_id == 'T' and not is_down:
        def do():
            display_info()
            _window.go_foreground()
            print("done")
        _data.action_chain.add(3, do)

    elif key_id == 'H' and not is_down:
        def do():
            _window.hide()
            display_info()
        _data.action_chain.add(0, do)

        def do():
            _window.show()
            print("done")
        _data.action_chain.add(1, do)

    elif key_id == 'M' and not is_down:
        if extra.is_shift_down:
            _window.maximize()
        else:
            def do():
                _window.minimize()
                display_info()
            _data.action_chain.add(0, do)

            def do():
                _window.center(_WIDTH, _HEIGHT, is_draw_area_size = _data.is_draw_area)
                print("done")
            _data.action_chain.add(1, do)

    elif key_id == 'F' and not is_down:
        _window.go_windowed_full_screen()

    elif key_id == 'C' and not is_down:
        if extra.is_shift_down:
            _window.center(_WIDTH, _HEIGHT, is_draw_area_size = _data.is_draw_area)
        elif extra.is_left_ctrl_down:
            _window.center(_WIDTH, _HEIGHT, is_draw_area_size = True)
        elif extra.is_right_ctrl_down:
            _window.center(_WIDTH, _HEIGHT, is_draw_area_size = False)
        else:
            _window.center()

    elif key_id == 'P' and not is_down:
        if extra.is_left_ctrl_down:
            _window.move_to(x = 10, is_draw_area = _data.is_draw_area)
        elif extra.is_right_ctrl_down:
            _window.move_to(y = 50, is_draw_area = _data.is_draw_area)
        else:
            _window.move_to(10, 50, is_draw_area = _data.is_draw_area)

    elif key_id == 'O' and not is_down:
        if extra.is_shift_down:
            _window.move_to(pos = togl.Point(0, 0), is_draw_area = _data.is_draw_area)
        else:
            _window.move_to(0, 0, is_draw_area = _data.is_draw_area)

    elif key_id == 'S' and not is_down:
        if extra.is_shift_down:
            _window.resize(_WIDTH, _HEIGHT, is_draw_area = _data.is_draw_area)
        elif extra.is_left_ctrl_down:
            _window.resize(width = _WIDTH / 2, is_draw_area = _data.is_draw_area)
        elif extra.is_right_ctrl_down:
            _window.resize(height = _HEIGHT / 2, is_draw_area = _data.is_draw_area)
        else:
            _window.resize(_WIDTH / 2, _HEIGHT / 2, is_draw_area = _data.is_draw_area)

    elif key_id == 'A' and not is_down:
        if extra.is_shift_down:
            _window.reshape(area = togl.Area(10, 50, _WIDTH, _HEIGHT), is_draw_area = _data.is_draw_area)
        elif extra.is_left_ctrl_down:
            _window.reshape(x = 10, width = _WIDTH, is_draw_area = _data.is_draw_area)
        elif extra.is_right_ctrl_down:
            _window.reshape(y = 50, height = _HEIGHT, is_draw_area = _data.is_draw_area)
        else:
            _window.reshape(10, 50, _WIDTH, _HEIGHT, is_draw_area = _data.is_draw_area)
 
    elif key_id == 'D' and not is_down:
        _data.is_draw_area = not _data.is_draw_area
        if _data.is_draw_area:
            print("window area -> draw area")
        else:
            print("draw area -> window area")

   
    elif key_id == 'R' and not is_down:
        _window.request_draw()

    elif key_id == '0' and not is_down:
        def do():
            _window.move_by()
            display_info()
        _data.action_chain.add(0, do)

        def do():
            _window.move_to()
            display_info()
        _data.action_chain.add(1, do)

        def do():
            _window.resize()
            display_info()
        _data.action_chain.add(1, do)

        def do():
            _window.reshape()
            display_info()
        _data.action_chain.add(1, do)

        def do():
            _window.center()
            print("done")
        _data.action_chain.add(1, do)

    elif key_id == '1' and not is_down:
        def do():
            display_info()
            _window.minimize()
        _data.action_chain.add(0, do)

        def do():
            _window.move_by(30, 0)
        _data.action_chain.add(0, do)

        def do():
            _window.resize(_WIDTH, _HEIGHT, is_draw_area = _data.is_draw_area)
            display_info()
            print("done")
        _data.action_chain.add(0, do)

    elif key_id == 'I' and not is_down:
        display_info()

    elif key_id == 'L' and not is_down:
        display_legend()

    elif key_id == togl.KeyId.ESCAPE and not is_down:
        _window.request_close()

def do_on_resize(width, height):
    print("do_on_resize: %d %d" % (width, height))
    if height < 1: 
        height = 1

    glViewport(0, 0, width, height)

    set_orthogonal_projection(width, height)

    _data.animated_triangle.resize(width, height)


def do_on_state_change(state_id):
    print("do_on_state_change: %s" % state_id.name)

def do_on_time(time_interval):
    if "notify_timer" in _data.options: 
        print("time_interval: %dms" % time_interval)

    _data.animated_triangle.update(time_interval / 1000.0)
    _data.action_chain.try_execute()

def do_on_hide():
    print("do_on_hide")

def do_on_show():
    print("do_on_show")

def do_on_foreground(is_gain):
    text = "gain" if is_gain else "lose"
    print("do_on_forground: %s" % text)


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
        window_name             = "Area and State (debug)",
        area                    = (0, 0, _WIDTH, _HEIGHT) if "alt_center" not in options else (_WIDTH, _HEIGHT),
        style                   = style,
        state_id                = state_id,
        is_hidden               = True if "hidden" in options else False,

        opengl_version          = (3, 3) if "opengl_3_3" in options else None,

        timer_time_interval     = 20,
        icon_file_name          = "tests\\assets\\icon.ico" if "no_icon" not in options else "",

        do_on_create            = do_on_create,
        do_on_close             = do_on_close if "ask_on_close" in options else None,
        do_on_destroy           = do_on_destroy,
        draw                    = draw,

        do_on_key               = do_on_key,

        do_on_resize            = do_on_resize,
        do_on_state_change      = do_on_state_change,

        do_on_hide              = do_on_hide,
        do_on_show              = do_on_show,
        do_on_foreground        = do_on_foreground,

        do_on_time              = do_on_time,
    )