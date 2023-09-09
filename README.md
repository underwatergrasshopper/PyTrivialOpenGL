# PyTrivialOpenGL
## Description

A simple library which allows to create window with OpenGL rendering context, 
and draw into client area of window (draw area) by using OpenGL functions.

Provides OpenGL 1.1 functions, types, and constant (all optional to use) with and without need to use ctypes module (also optional).
- `PyTrivialOpenGL.GL` - OpenGL functions, types and constants (more readable).
- `PyTrivialOpenGL.C_GL` - OpenGL functions, types and constants with ctypes dependency for using (faster).

Provides some very basic functionality to draw text (optional).
- `PyTrivialOpenGL.Font`
- `PyTrivialOpenGL.TextDrawer`

No external DLLs are required, other than some defaults provided by system (Kernel32, User32, Dwmapi, Gdi32), python (ctypes) and graphic card vendor (OpenGL32).

No GLUT is required.

*Current Problems:*
- *Speed of `Font` and `TextDrawer`.*
- *No python `typing` and python `match-case`. Requires moving to python versions 3.10, at least.*
- *Small number of examples. Having some 3D examples would be nice.*
- *No game as example.*

## Requirements

|
-|-
Python Version | 3.9 (32bit) or later
py launcher | Yes
Operating System | Window 10 

## HowTo: Install
- Go to `Releases` section an `PyTrivialOpenGL` github page and download last release package with `whl` extension. 
- Run `py -m pip install PyTrivialOpenGL-<version>-py3-none-win32.whl` in directory where is the package.

*Note: The `<version>` in install command need to be replaced with a version of the package.*

## HowTo: Uninstall
- Run `py -m pip uninstall PyTrivialOpenGL`.

## HowTo: Install required packages for Tests and Examples
- Run `py -m pip install -r tests_and_examples_requirements.txt`.

## HowTo: Run Unit Tests
- [HowTo: Install required packages for tests and examples](#howto-install-required-packages-for-tests-and-examples), if not done before.
- Run `py -m pip install -r tests_and_examples_requirements.txt` to install needed packges (only first time).
- Go to `tests_and_examples` folder.
- Run `py run_unit_tests.py`.

*Note: Local version of PyTrivialOpenGl package will be used, not installed.*

## HowTo: Run Manual Tests
- [HowTo: Install required packages for tests and examples](#howto-install-required-packages-for-tests-and-examples), if not done before.
- Go to `tests_and_examples` folder.
- Run `py run_unit_tests.py`.
- Type one of following and press `enter`:
    - name of manual test
    - `l` - which means last used name of manual test
    - `d` - which means default name of manual test
- Type one of following and press `enter`:
    - nothing
    - one or many options names
    - `l` - which means last used options names
    - `d` - which means default options names

*Note: Local version of PyTrivialOpenGl package will be used, not installed.*

## HowTo: Run Debugs
- [HowTo: Install required packages for tests and examples](#howto-install-required-packages-for-tests-and-examples), if not done before.
- Go to `tests_and_examples` folder.
- Run `py run_debugs.py`.
- Type one of following and press `enter`:
    - name of debug example
    - `l` - which means last used name of debug example
    - `d` - which means default name of debug example
- Type one of following and press `enter`:
    - nothing
    - one or many options names
    - `l` - which means last used options names
    - `d` - which means default options names

*Note: Local version of PyTrivialOpenGl package will be used, not installed.*

## HowTo: Run Examples
- [HowTo: Install required packages for tests and examples](#howto-install-required-packages-for-tests-and-examples), if not done before.
- Go to `tests_and_examples` folder.
- Run `py run_examples.py`.
- Type one of following and press `enter`:
    - name of example
    - `l` - which means last used name of example
    - `d` - which means default name of example
- Type one of following and press `enter`:
    - nothing
    - one or many options names
    - `l` - which means last used options names
    - `d` - which means default options names

Examples with `c_` prefix are using `C_GL` module instead of `GL` module.

*Note: Local version of PyTrivialOpenGl package will be used, not installed.*

When PyTrivialOpenGL package is installed, all examples can be run individually by going to `tests_and_examples/PyTrivialOpenGL_TestsAndExamples/examples` folder and running `py <example_name>.py` command.

## HowTo: Run All non Unit Tests
- [HowTo: Install required packages for tests and examples](#howto-install-required-packages-for-tests-and-examples), if not done before.
- Go to `tests_and_examples` folder.
- Run `py run_all_non_unit_tests.py`.
- Type one of following and press `enter`:
    - name of example
    - `l` - which means last used name of example
    - `d` - which means default name of example
- Type one of following and press `enter`:
    - nothing
    - one or many options names
    - `l` - which means last used options names
    - `d` - which means default options names

*Note: Local version of package is used, not installed.*

## Code Examples
- [Custom Icon](#custom-icon)
- [Specific OpenGL Version](#specific-opengl-version)
- [Timer](#timer)
- [Ask on Close](#ask-on-close)
- [Simple Triangle](#simple-triangle)
- [Animated Triangle](#animated-triangle)

For more examples go to `tests_and_examples/PyTrivialOpenGL_TestsAndExamples/examples` folder.

### Custom Icon

Loads icon image from file.
Loaded icon image will be displayed on task bar and window title bar.

```python
import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

__all__ = [
    "run"
]

def do_on_create(data):    
    glViewport(0, 0, data.width, data.height)

    glClearColor(0, 0, 0.5, 1)

    print("Escape - Exit", flush = True)

def do_on_destroy():
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
        window_name         = "Custom Icon",
        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        icon_file_name      = "icon.ico",

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )

if __name__ == "__main__":
    run()
```
[Back to: Code Examples](#code-examples)

### Specific OpenGL Version
This example crates OpenGL Rendering Context for at least version 3.3 with Compatibility Profile.

```python
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
        window_name         = "OpenGL Version",

        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        opengl_version      = (3, 3),

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )

if __name__ == "__main__":
    run()
```
[Back to: Code Examples](#code-examples)

### Timer
Displays a message each 500ms.

```python
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

def do_on_destroy():
    glPopAttrib()

    print("Bye. Bye.", flush = True)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

def do_on_time(time_interval):
    print("500ms", flush = True)

def do_on_key(key_id, is_down, extra):
    if key_id == togl.KeyId.ESCAPE:
        if not is_down:
            togl.to_window().request_close()

def do_on_resize(width, height):
    glViewport(0, 0, width, height)

def run():
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Timer",

        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,
        timer_time_interval = 500,
        

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,
        do_on_time          = do_on_time,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )

if __name__ == "__main__":
    run()
```
[Back to: Code Examples](#code-examples)

### Ask on Close
Displays message box when pressing close button on window title bar, with question about close.

```python
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
```
[Back to: Code Examples](#code-examples)


### Simple Triangle

Draws simple triangle.

```python
import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

__all__ = [
    "run"
]

def do_on_create(data):    
    glViewport(0, 0, data.width, data.height)

    glClearColor(0, 0, 0.5, 1)

    print("Escape - Exit", flush = True)

def do_on_destroy():
    print("Bye. Bye.", flush = True)

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

        # Sets width and height of windows draw area.
        area                = (800, 400),

        # Interprets size from 'area' parameter as size of draw area of window.
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )

if __name__ == "__main__":
    run()
```
[Back to: Code Examples](#code-examples)

### Animated Triangle
Displays rotating triangle.

```python
import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

import math

__all__ = [
    "run"
]

def draw_rgb_triangle():
    glPushMatrix()

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

class AnimatedTriangle:
    def __init__(self, x, y, scale, rotation_speed):
        """
        x               : int
        y               : int
        scale           : float
        rotation_speed  : float
            In degrees per second.
        """
        self.set_pos(x, y)
        self.set_scale(scale)
        self.set_rotation_speed(rotation_speed)

        self._angle = 0.0
      
    def set_pos(self, x, y):
        """
        x               : int
        y               : int
        """
        self._x     = x
        self._y     = y

    def set_scale(self, scale):
        """
        scale          : float
        """
        self._scale  = scale

    def set_rotation_speed(self, rotation_speed):
        """
        rotation_speed  : float
            In degrees per second.
        """
        self._rotation_speed = rotation_speed

    def draw(self):
        glPushMatrix()

        glTranslatef(self._x, self._y, 0)
        glRotatef(self._angle, 0, 0, 1)
        glScalef(self._scale, self._scale, 1)

        draw_rgb_triangle()

        glPopMatrix()

    def update(self, delta_time):
        """
        delta_time : float
            In seconds.
        """
        self._angle += self._rotation_speed * delta_time
        self._angle %= 360

_animated_triangle = AnimatedTriangle(0, 0, 100.0, 20.0)

def resize(width, height):
    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, 1, -1)

    _animated_triangle.set_pos(width // 2, height // 2)

    scale = width if width < height else height
    scale *= 0.5

    _animated_triangle.set_scale(scale)

def do_on_create(data):
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    resize(data.width, data.height)

    glClearColor(0, 0, 0.5, 1)

    print("Escape - Exit", flush = True)

def do_on_destroy():
    glPopAttrib()

    print("Bye. Bye.", flush = True)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    _animated_triangle.draw()

def do_on_time(time_interval):
    _animated_triangle.update(time_interval / 1000)

def do_on_key(key_id, is_down, extra):
    if key_id == togl.KeyId.ESCAPE:
        if not is_down:
            togl.to_window().request_close()

def do_on_resize(width, height):
    resize(width, height)

def run():
    togl.set_log_level(togl.LogLevel.INFO)

    return togl.to_window().create_and_run(
        window_name         = "Animated Triangle",

        area                = (800, 400),
        style               = togl.WindowStyleBit.DRAW_AREA_SIZE,
        timer_time_interval = 20,
        

        do_on_create        = do_on_create,
        do_on_destroy       = do_on_destroy,
        do_on_time          = do_on_time,

        draw                = draw,

        do_on_key           = do_on_key,
        do_on_resize        = do_on_resize,
    )

if __name__ == "__main__":
    run()
```
[Back to: Code Examples](#code-examples)

