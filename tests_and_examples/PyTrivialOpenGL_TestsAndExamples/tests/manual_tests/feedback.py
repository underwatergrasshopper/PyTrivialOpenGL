import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *
import ctypes

from ...utility.ExampleSupport import is_close

__all__ = [
    "run"
]

class Feedback:
    def __init__(self):
        self._list      = []

    def generate(self, buffer):
        index = 0

        def get():
            nonlocal index
            value = buffer[index]
            index += 1
            return value

        def get_vertex():
            return ((get(), get(), get()), (get(), get(), get(), get())) # vertex + color

        list_ = []
        while index < len(buffer):
            token = int(get())
            
            if token == GL_POINT_TOKEN :
                list_.append("GL_POINT_TOKEN")
                list_.append(get_vertex())
            elif token == GL_LINE_TOKEN:
                list_.append("GL_LINE_TOKEN")
                list_.append(get_vertex())
                list_.append(get_vertex())
            elif token == GL_LINE_RESET_TOKEN:
                list_.append("GL_LINE_RESET_TOKEN")
                list_.append(get_vertex())
                list_.append(get_vertex())
            elif token == GL_POLYGON_TOKEN:
                list_.append("GL_POLYGON_TOKEN")
                n = int(get())
                list_.append(n)
                for _ in range(n):
                    list_.append(get_vertex())
            elif token == GL_DRAW_PIXEL_TOKEN:
                list_.append("GL_DRAW_PIXEL_TOKEN")
                list_.append(get_vertex())
            elif token == GL_COPY_PIXEL_TOKEN:
                list_.append("GL_COPY_PIXEL_TOKEN")
                list_.append(get_vertex())
            elif token == GL_PASS_THROUGH_TOKEN:
                list_.append("GL_PASS_THROUGH_TOKEN")
                list_.append(get())
            else:
                raise RuntimeError("Unknown OpenGL Feedback Token (%f)." % token)

        self._list = list_

    def get_list(self):
        return self._list

_feedback = Feedback()

def check():
    feedback_list = _feedback.get_list()

    index = 0
    def get():
        nonlocal index
        item = feedback_list[index]
        index += 1
        return item

    assert len(feedback_list) == 31
            
    assert get() == "GL_PASS_THROUGH_TOKEN"
    assert is_close(get(), 1.0)
    assert get() == "GL_POLYGON_TOKEN"
    assert get() == 3
    assert is_close(get(), ((200.0, 100.0, 0.5), (1.0, 0.0, 0.0, 1.0)))
    assert is_close(get(), ((600.0, 100.0, 0.5), (1.0, 0.0, 0.0, 1.0)))
    assert is_close(get(), ((600.0, 300.0, 0.5), (1.0, 0.0, 0.0, 1.0)))
    assert get() == "GL_POLYGON_TOKEN"
    assert get() == 3
    assert is_close(get(), ((200.0, 100.0, 0.5), (1.0, 0.0, 0.0, 1.0)))
    assert is_close(get(), ((600.0, 300.0, 0.5), (1.0, 0.0, 0.0, 1.0)))
    assert is_close(get(), ((200.0, 300.0, 0.5), (1.0, 0.0, 0.0, 1.0)))
    assert get() == "GL_PASS_THROUGH_TOKEN"
    assert is_close(get(), 2.0)
    assert get() == "GL_POLYGON_TOKEN"
    assert get() == 3
    assert is_close(get(), ((240.0, 0.0, 0.5), (0.0, 1.0, 0.0, 1.0)))
    assert is_close(get(), ((240.0, 120.0, 0.5), (0.0, 1.0, 0.0, 1.0)))
    assert is_close(get(), ((0.0, 0.0, 0.5), (0.0, 1.0, 0.0, 1.0)))
    assert get() == "GL_POLYGON_TOKEN"
    assert get() == 3
    assert is_close(get(), ((240.0, 0.0, 0.5), (0.0, 1.0, 0.0, 1.0)))
    assert is_close(get(), ((0.0, 0.0, 0.5), (0.0, 1.0, 0.0, 1.0)))
    assert is_close(get(), ((0.0, 0.0, 0.5), (0.0, 1.0, 0.0, 1.0)))
    assert get() == "GL_POLYGON_TOKEN"
    assert get() == 3
    assert is_close(get(), ((0.0, 120.0, 0.5), (0.0, 1.0, 0.0, 1.0)))
    assert is_close(get(), ((0, 0.0, 0.5), (0.0, 1.0, 0.0, 1.0)))
    assert is_close(get(), ((240.0, 120.0, 0.5), (0.0, 1.0, 0.0, 1.0)))
    assert get() == "GL_PASS_THROUGH_TOKEN"
    assert is_close(get(), 3.0)

    print("Ok")

def do_on_create():
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glClearColor(0, 0, 0.5, 1)

    print("F        - Display Feedback List")
    print("C        - Check Feedback List")
    print("Escape   - Exit")

def do_on_destroy():
    glPopAttrib()

    print("Bye. Bye.")

def draw_scene(is_pass_throug = False):
    if is_pass_throug: glPassThrough(1.0)
    glColor3f(1, 0, 0)
    glRectd(-0.5, -0.5, 0.5, 0.5)
    
    if is_pass_throug: glPassThrough(2.0)
    glColor3f(0, 1, 0)
    glRectd(-1.2, -1.2, -0.4, -0.4)
    
    # is out of view, won't hit
    if is_pass_throug: glPassThrough(3.0)
    glColor3f(1, 1, 0)
    glRectd(-2, -2, -1.2, -1.2)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    LENGTH = 512
    glFeedbackBuffer(LENGTH, GL_3D_COLOR)
    glRenderMode(GL_FEEDBACK)

    draw_scene(is_pass_throug = True)

    glFlush()
    length = glRenderMode(GL_RENDER)

    buffer = glFeedbackBuffer()[:length]

    _feedback.generate(buffer)

    draw_scene()

def do_on_key(key_id, is_down, extra):
    if not is_down:
        if key_id == togl.KeyId.ESCAPE:
            togl.to_window().request_close()
        elif key_id == 'F':
            print("--- Feedback List ---")
            for item in _feedback.get_list():
                print(item)
            print("---")
        elif key_id == 'C':
            check()

def do_on_resize(width, height):
    glViewport(0, 0, width, height)

def run(name, options):
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Feedback",
        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )