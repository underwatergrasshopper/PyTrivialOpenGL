import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *
from PyTrivialOpenGL import C_GL
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
    C_GL.glPushAttrib(GL_ALL_ATTRIB_BITS)

    C_GL.glClearColor(0, 0, 0.5, 1)

    print("F        - Display Feedback List")
    print("C        - Check Feedback List")
    print("Escape   - Exit")

def do_on_destroy():
    C_GL.glPopAttrib()

    print("Bye. Bye.")

def draw_scene(is_pass_throug = False):
    if is_pass_throug: C_GL.glPassThrough(1.0)
    C_GL.glColor3f(1, 0, 0)
    C_GL.glRectd(-0.5, -0.5, 0.5, 0.5)
    
    if is_pass_throug: C_GL.glPassThrough(2.0)
    C_GL.glColor3f(0, 1, 0)
    C_GL.glRectd(-1.2, -1.2, -0.4, -0.4)
    
    # is out of view, won't hit
    if is_pass_throug: C_GL.glPassThrough(3.0)
    C_GL.glColor3f(1, 1, 0)
    C_GL.glRectd(-2, -2, -1.2, -1.2)

def draw():
    C_GL.glClear(GL_COLOR_BUFFER_BIT)

    LENGTH = 512
    c_buffer = (C_GL.GLfloat * LENGTH)()
    C_GL.glFeedbackBuffer(LENGTH, GL_3D_COLOR, c_buffer)
    C_GL.glRenderMode(GL_FEEDBACK)

    # Note: They all fail. GL_INVALID_ENUM is issued.
    # c_ptr = ctypes.c_void_p(None)
    # C_GL.glGetPointerv(GL_FEEDBACK_BUFFER_POINTER, ctypes.byref(c_ptr))
    # print(c_ptr.value)
    # print(togl.get_gl_error_str(C_GL.glGetError()))
    # 
    # c_size = C_GL.GLint(0)
    # C_GL.glGetIntegerv(GL_FEEDBACK_BUFFER_SIZE, ctypes.byref(c_size))
    # print(c_size.value)
    # print(togl.get_gl_error_str(C_GL.glGetError()))
    # 
    # c_type = C_GL.GLint(0)
    # C_GL.glGetIntegerv(GL_FEEDBACK_BUFFER_TYPE, ctypes.byref(c_type))
    # print(c_type.value)
    # print(togl.get_gl_error_str(C_GL.glGetError()))

    draw_scene(is_pass_throug = True)

    C_GL.glFlush()
    length = C_GL.glRenderMode(GL_RENDER)

    buffer = [float(c_buffer[index]) for index in range(length)]
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
    C_GL.glViewport(0, 0, width, height)

def run(name, options):
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "C Feedback",
        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )