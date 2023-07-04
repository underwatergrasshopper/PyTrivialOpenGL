from ExampleManager import *
from ActionManager import *

import PyTrivialOpenGL as togl
from PyTrivialOpenGL._C_GL import *

import PyTrivialOpenGL._C_WinApi as _C_WinApi
from PyTrivialOpenGL._WindowAreaCorrector import _WindowAreaCorrector
import ctypes

################################################################################

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

example_manager = ExampleManager()
action_manager = ActionManager()

def print_rect(r):
    print("%d %d %d %d" % (r.left, r.top, r.right, r.bottom))

def rect_to_area(r):
    return togl.Area(r.left, r.top, r.right - r.left, r.bottom - r.top)

def display_info():
    print("--- Info ---")

    window_area_corrector = _WindowAreaCorrector()

    window_handle = _C_WinApi.GetForegroundWindow()

    window_rect = _C_WinApi.RECT()
    _C_WinApi.GetWindowRect(window_handle, ctypes.byref(window_rect))
    area = window_area_corrector.remove_invisible_frame_from_area(rect_to_area(window_rect), window_handle)

    print("Window Area:", area)
    print("is_visible:", togl.to_window().is_visible())

    print("---")

################################################################################

def run_window_example(name, options):
    togl.set_log_level(togl.LogLevel.DEBUG)
    # togl.to_special_debug().is_full_exit_track_in_callback = True
    # togl.to_special_debug().is_notify_mouse_move = True
    # togl.to_special_debug().is_notify_character_message = True
    # togl.to_special_debug().is_notify_timer = True

    def do_on_create():
        print("0 - Show -> Hide")
        print("X - Exit")

        glClearColor(0, 0, 0.2, 1)

        action_manager.reset()

    def do_on_destroy():
        print("Bye. Bye.")

    def do_on_mouse_move(x, y):
        print("do_on_mouse_move: %d %d" % (x, y))

    def do_on_mouse_wheel_roll(step_cout, x, y):
        print("do_on_mouse_wheel_roll: %d %d %d" % (step_cout, x, y))

    def do_on_key(key_id, is_down, extra):
        # print("do_on_key: key_id=%s, is_down=%d, %s" % (key_id.name, is_down, extra))
        if is_down:
            if key_id == 'X':
                togl.to_window().request_close()
            elif key_id == 'I':
                display_info()

            elif key_id == togl.KeyId.ARROW_LEFT:
                togl.to_window().move_by(-30, 0)
            elif key_id == togl.KeyId.ARROW_RIGHT:
                togl.to_window().move_by(30, 0)
            elif key_id == togl.KeyId.ARROW_UP:
                togl.to_window().move_by(0, -30)
            elif key_id == togl.KeyId.ARROW_DOWN:
                togl.to_window().move_by(0, 30)

            elif key_id == '0':
                def do():
                    display_info()
                    togl.to_window().hide()
                    display_info()
                action_manager.add(0, do)

                def do():
                    togl.to_window().show()
                    display_info()
                action_manager.add(1, do)



    def do_on_text(text, is_correct):
        # print("do_on_text: text='%s', code_point=%Xh, is_correct=%d" % (text, ord(text), is_correct))
        pass

    def do_on_resize(width, height):
        print("do_on_resize: %d %d" % (width, height))
        glViewport(0, 0, width, height)

    def do_on_state_change(state_id):
        print("do_on_state_change: %s" % state_id.name)

    def do_on_time(time_interval):
        print("time_interval: %dms" % time_interval)

    def do_on_foreground(is_gain):
        text = "gain" if is_gain else "lose"
        print("do_on_forground: %s" % text)

    def draw():
        glClear(GL_COLOR_BUFFER_BIT)

        glBegin(GL_TRIANGLES)
        glColor3f(1, 0, 0)
        glVertex2f(-0.5, -0.5)

        glColor3f(0, 1, 0)
        glVertex2f(0.5, -0.5)

        glColor3f(0, 0, 1)
        glVertex2f(0, 0.5)

        glEnd()

        action_manager.update()

    return togl.to_window().create_and_run(
        window_name = "Some Window",
        area = (0, 0, 800, 400),
        opengl_version = (3, 3),

        icon_file_name  = "tests\\assets\\icon.ico",

        # timer_time_interval = 200,

        style = togl.WindowStyleBit.CENTERED,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,
        draw                = draw,

        # do_on_mouse_move        = do_on_mouse_move,
        do_on_mouse_wheel_roll  = do_on_mouse_wheel_roll,
        do_on_key               = do_on_key,
        do_on_text              = do_on_text,
        do_on_resize            = do_on_resize,
        do_on_state_change      = do_on_state_change,
        # do_on_time              = do_on_time,
        do_on_foreground        = do_on_foreground,
    )

example_manager.add_example("run_window", run_window_example)

################################################################################

def _main():
    example_manager.set_default("run_window")
    example_manager.run_examples()

if __name__ == "__main__":
   _main()