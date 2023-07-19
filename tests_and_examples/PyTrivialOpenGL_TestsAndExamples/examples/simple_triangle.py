import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

__all__ = [
    "run"
]

def do_on_create():
    glClearColor(0, 0, 0.5, 1)

    print("Escape - Exit")

def do_on_destroy():
    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_TRIANGLES)

    glColor3f(1, 0, 0)
    glVertex2f(0.5, -0.5)

    glColor3f(0, 1, 0)
    glVertex2f(-0.5, -0.5)

    glColor3f(0, 0, 1)
    glVertex2f(0, 0.5)

    glEnd()

def do_on_key(key_id, is_down, extra):
    if key_id == togl.KeyId.ESCAPE:
        if not is_down:
            togl.to_window().request_close()

def do_on_resize(width, height):
    glViewport(0, 0, width, height)

def run():
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Simple Triangle",
        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )

if __name__ == "__main__":
    run()