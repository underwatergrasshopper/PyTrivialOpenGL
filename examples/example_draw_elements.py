import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

__all__ = [
    "run"
]

def do_on_create():
    print("X - Exit")

    glClearColor(0, 0, 0.5, 1)

def do_on_destroy():
    print("Bye. Bye.")

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    vertices = [
        0,      0.5,
        -0.5,   -0.5,
        0.5,    -0.5,
        0.9,      0.5,
    ]

    colors = [
        1, 0, 0,
        0, 1, 0,
        0, 0, 1,
        1, 1, 1,
    ]

    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)

    glVertexPointer(2, GL_FLOAT, 0, vertices)
    glColorPointer(3, GL_FLOAT, 0, colors)

    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, [
        0, 1, 2, 
        0, 2, 3
    ])

    glDisableClientState(GL_VERTEX_ARRAY)
    glDisableClientState(GL_COLOR_ARRAY)

def do_on_key(key_id, is_down, extra):
    if not is_down:
        if key_id == togl.KeyId.ESCAPE:
            togl.to_window().request_close()

def do_on_resize(width, height):
    glViewport(0, 0, width, height)

def run(name, options):
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Draw Elements",
        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )