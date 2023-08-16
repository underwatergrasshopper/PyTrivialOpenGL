import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

__all__ = [
    "run"
]

def do_on_create(data):
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glViewport(0, 0, data.width, data.height)

    glClearColor(0, 0, 0.5, 1)

    print("Escape - Exit", flush = True)

def do_on_close():
    return togl.run_question_box("Close", "Are you sure?")

def do_on_destroy():
    glPopAttrib()

    print("Bye. Bye.", flush = True)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

def do_on_key(key_id, is_down, extra):
    if key_id == togl.KeyId.ESCAPE:
        if not is_down:
            togl.to_window().request_close()

def do_on_resize(width, height):
    glViewport(0, 0, width, height)

def run():
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Ask on Close",

        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_close         = do_on_close,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )

if __name__ == "__main__":
    run()