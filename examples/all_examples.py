from ExampleSupport import *

import simple_triangle_example
import window_area_example

################################################################################

example_manager = ExampleManager()
action_chain = ActionChain()

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
        
        scale = area.height if area.height < area.width else area.width
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

            elif key_id == '7':
                togl.to_window().reshape(100, 50, 400, 300)

            elif key_id == '8':
                #togl.to_window().center(600, 300)
                togl.to_window().center()

            elif key_id == '9':
                togl.to_window().center(600, 300, is_draw_area_size = True)

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

    print(area)
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
example_manager.add_example("simple_triangle", simple_triangle_example.run)
example_manager.add_example("window_area", window_area_example.run)

################################################################################

def _main():
    example_manager.set_default("run_window")
    example_manager.run_examples()

if __name__ == "__main__":
   _main()