from ExampleManager import *
from ActionChain import *

import PyTrivialOpenGL as togl
from PyTrivialOpenGL._C_GL import *

import PyTrivialOpenGL._C_WinApi as _C_WinApi
from PyTrivialOpenGL._WindowAreaCorrector import _WindowAreaCorrector

import ctypes
import math

################################################################################

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

example_manager = ExampleManager()
action_chain = ActionChain()

def print_rect(r):
    print("%d %d %d %d" % (r.left, r.top, r.right, r.bottom))

def rect_to_area(r):
    return togl.Area(r.left, r.top, r.right - r.left, r.bottom - r.top)

def display_info():
    print("--- Info ---")

    window_area_corrector = _WindowAreaCorrector()

    window_handle = _C_WinApi.GetForegroundWindow()

    window_area = togl.to_window().get_area()
    print("%-20s: %s" % ("Window Area", window_area))

    draw_area = togl.to_window().get_draw_area()
    print("%-20s: %s" % ("Window Draw Area", draw_area))

    screen_size = togl.get_screen_size()

    print("%-20s: %s" % ("Screen Size", screen_size))

    work_area = togl.get_work_area()

    print("%-20s: %s" % ("Work Area", work_area))

    print("%-20s: %s" % ("is_visible", togl.to_window().is_visible()))

    center_check_size = togl.Size(
        (window_area.x - work_area.x) * 2 + window_area.width,
        (window_area.y - work_area.y) * 2 + window_area.height
    )
    print("%-20s: %s (= %s)" % ("Window Center Check", center_check_size, work_area.get_size()))

    print("---")

def draw_rgb_triangle(x, y, scale, angle):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glRotatef(angle, 0, 0, 1)
    glScalef(scale, scale, 0)

    glBegin(GL_TRIANGLES)

    glColor3f(1, 0, 0)
    angle = 0
    glVertex2f(math.sin(angle), math.cos(angle))

    glColor3f(0, 1, 0)
    angle += math.pi * 2 / 3
    glVertex2f(math.sin(angle), math.cos(angle))
            
    glColor3f(0, 0, 1)
    angle += math.pi * 2 / 3
    glVertex2f(math.sin(angle), math.cos(angle))

    glEnd()

    glPopMatrix()

def draw_rectangle(x, y, width, height):
    glBegin(GL_TRIANGLE_FAN)

    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)

    glEnd()

################################################################################

def run_window_example(name, options):
    togl.set_log_level(togl.LogLevel.DEBUG)
    # togl.to_special_debug().is_full_exit_track_in_callback = True
    # togl.to_special_debug().is_notify_mouse_move = True
    # togl.to_special_debug().is_notify_character_message = True
    # togl.to_special_debug().is_notify_timer = True

    area = togl.Area(0, 0, 800, 400)

    class Data:
        def __init__(self):
            self.angle = 0
    data = Data()

    def do_on_create():
        print("0 - Show -> Hide")
        print("X - Exit")

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, area.width, 0, area.height, 1, -1)

        glClearColor(0, 0, 0.5, 1)

        action_chain.reset()

    def do_on_destroy():
        print("Bye. Bye.")

    def draw():
        glClear(GL_COLOR_BUFFER_BIT)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glColor3f(1, 0, 0)
        draw_rectangle(0, 0, area.width, area.height)

        glColor3f(0, 0, 0.5)
        draw_rectangle(1, 1, area.width - 2, area.height - 2)
        
        scale = area.height if area.height < area.width else area.height
        scale /= 3

        draw_rgb_triangle(area.width / 2, area.height / 2, scale, data.angle)

        action_chain.try_execute()

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

            elif key_id == '1':
                togl.to_window().move_to(10, 10)

            elif key_id == '2':
                togl.to_window().move_to(0, 0)

            elif key_id == '3':
                togl.to_window().move_to(y = 1, is_draw_area = True)

            elif key_id == '4':
                togl.to_window().resize(400, 200, is_draw_area = True)

            elif key_id == '5':
                togl.to_window().resize(800, 400, is_draw_area = True)

            elif key_id == '6':
                togl.to_window().resize(width = 400, is_draw_area = True)

            elif key_id == '0':
                def do():
                    display_info()
                    togl.to_window().hide()
                    display_info()
                action_chain.add(0, do)

                def do():
                    togl.to_window().show()
                    display_info()
                action_chain.add(1, do)

    def do_on_text(text, is_correct):
        # print("do_on_text: text='%s', code_point=%Xh, is_correct=%d" % (text, ord(text), is_correct))
        pass

    def do_on_resize(width, height):
        print("do_on_resize: %d %d" % (width, height))

        glViewport(0, 0, width, height)

        area.width  = width
        area.height = height

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, area.width, 0, area.height, 1, -1)

    def do_on_state_change(state_id):
        print("do_on_state_change: %s" % state_id.name)

    def do_on_time(time_interval):
        # print("time_interval: %dms" % time_interval)

        data.angle += 10 * (time_interval / 1000) # degrees per second

    def do_on_foreground(is_gain):
        text = "gain" if is_gain else "lose"
        print("do_on_forground: %s" % text)

    return togl.to_window().create_and_run(
        window_name         = "Some Window",
        area                = area,
        style               = togl.WindowStyleBit.CENTERED | togl.WindowStyleBit.DRAW_AREA_SIZE,

        opengl_version      = (3, 3),
        timer_time_interval = 20,
        icon_file_name      = "tests\\assets\\icon.ico",

        do_on_create            = do_on_create,
        do_on_destroy           = do_on_destroy,
        draw                    = draw,

        # do_on_mouse_move        = do_on_mouse_move,
        do_on_mouse_wheel_roll  = do_on_mouse_wheel_roll,
        do_on_key               = do_on_key,
        do_on_text              = do_on_text,
        do_on_resize            = do_on_resize,
        do_on_state_change      = do_on_state_change,
        do_on_time              = do_on_time,
        do_on_foreground        = do_on_foreground,
    )

example_manager.add_example("run_window", run_window_example)

################################################################################

def _main():
    example_manager.set_default("run_window")
    example_manager.run_examples()

if __name__ == "__main__":
   _main()