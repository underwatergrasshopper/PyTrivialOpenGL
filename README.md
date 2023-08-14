# PyTrivialOpenGL
## Description

A simple library which allows to create window with OpenGL rendering context, 
and draw into client area of window (draw area) by using OpenGL functions.

Provides OpenGL 1.1 functions, types, and constant (all optional to use) with and without need to use ctypes module (also optional).
- `PyTrivialOpenGL.GL` - OpenGL functions, types and constants (more readable).
- `PyTrivialOpenGL.C_GL` - OpenGL functions, types and constants with ctypes dependency for using (faster).

No external DLLs are required, other than some defaults provided by system (Kernel32, User32, Dwmapi, Gdi32), python (ctypes) and graphic card vendor (OpenGL32).

No GLUT is required.

## Requirements

|
-|-
Python Version | 3.9 (32bit) or later
Operating System | Window 7/10 

## HowTo: Install
- Go to `Releases` section and download last release package with `whl` extension. 
- Run `pip install PyTrivialOpenGL-<version>-py3-none-win32.whl` in directory where is the package.

*Note: The `<version>` in install command need to be replaced with a version of the package.*

## HowTo: Unistall

- Run `pip uninstall PyTrivialOpenGL`.

## HowTo: Run Unit Tests

- Go to `tests_and_examples` folder.
- Run `python run_unit_tests.py`.

*Note: Local version of package is used, not installed.*

## HowTo: Run Manual Tests

- Go to `tests_and_examples` folder.
- Run `python run_manual_tests.py`.
- Type one of following and press `enter`:
    - name of manual test
    - `l` - which means last used name of manual test
    - `d` - which means default name of manual test
- Type one of following and press `enter`:
    - nothing
    - one or many options names
    - `l` - which means last used options names
    - `d` - which means default options names

*Note: Local version of package is used, not installed.*

## HowTo: Run Debugs

- Go to `tests_and_examples` folder.
- Run `python run_debugs.py`.
- Type one of following and press `enter`:
    - name of debug example
    - `l` - which means last used name of debug example
    - `d` - which means default name of debug example
- Type one of following and press `enter`:
    - nothing
    - one or many options names
    - `l` - which means last used options names
    - `d` - which means default options names

*Note: Local version of package is used, not installed.*

## HowTo: Run Examples

- Go to `tests_and_examples` folder.
- Run `python run_examples.py`.
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

*Note: Local version of package is used, not installed.*

When PyTrivialOpenGL package is installed, all examples can be run individually by going to `tests_and_examples/PyTrivialOpenGL_TestsAndExamples/examples` folder and running `python <example_name>.py` command.

## HowTo: Run All non Unit Tests

- Go to `tests_and_examples` folder.
- Run `python run_all_non_unit_tests.py`.
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
- [Simple Triangle](#simple-triangle)

### Simple Triangle
```python
import PyTrivialOpenGL as togl
from PyTrivialOpenGL.GL import *

__all__ = [
    "run"
]

def do_on_create():
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
- [Back to: Code Examples](#code-examples)