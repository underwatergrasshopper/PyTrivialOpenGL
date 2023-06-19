from msilib.schema import Icon
from PyTrivialOpenGL._C_WinApi import *
from PyTrivialOpenGL._C_WGL import *
from PyTrivialOpenGL._C_GL import *
from ctypes import *
import time
import os
import re

################################################################################

class Example:
    def __init__(self, name, function, possible_options, default_options):
        """
        name                : str
        function            : Callable[[str, set[str]], NoneType]
        possible_options    : set[str]
        possible_options    : set[str]
        """
        self.name               = name
        self.function           = function
        self.possible_options   = possible_options
        self.default_options    = default_options

    def def_opt_to_str(self):
        text = ""
        for option in self.default_options:
            if text != "":
                text += " "
            text += option
        return text

class ExampleManager:
    """
    examples                : dict[str, Example]
    default_example_name    : str
    """
    def __init__(self):
        self.examples               = {}
        self.default_example_name   = ""

    def set_default(self, default_example_name):
        """
        default_example_name    : str
        """
        self.default_example_name = default_example_name

    def add_example(self, name, function, possible_options = None, default_options = None):
        """
        name                : str
        function            : Callable[[str, set[str]], NoneType]
        possible_options    : set[str]
        possible_options    : set[str]
        """
        
        if possible_options == None:
            possible_options = set()
        else:
            possible_options = set(possible_options)

        if default_options == None:
            default_options = set()
        else:
            default_options = set(default_options)

        self.examples[name] = Example(name, function, possible_options, default_options)

    def _display_examples(self):
        count = 0
        for example_name in self.examples.keys():
            print("% 19s, " % example_name, end = "")
            count +=1
            if count % 4 == 0:
                print("")
        print("")

    def _display_possible_options(self, example):
        count = 0
        for option in example.possible_options:
            print("% 19s, " % option, end = "")
            count +=1
            if count % 4 == 0:
                print("")
        print("")

    def run_examples(self):
        while True:
            print("--- Example Manager ---")
            print("Examples:")
            self._display_examples()
            print("")

            print("(e=Exit, d=%s)" % self.default_example_name)
            example_name = input("select example: ")
            print("")

            if example_name == "e":
                exit(0)

            elif example_name == "d":
                example_name = self.default_example_name

            example = self.examples.get(example_name, None)
            if example:
                print("Options:")
                self._display_possible_options(example)
                print("")

                print("(e=Exit, d=%s)" % example.def_opt_to_str())
                raw_options = input("select options: ")
                print("")

                raw_options = re.split(r"[\t\n ]+", raw_options)

                options = set()
                
                if raw_options == ["e"]:
                    exit(0)

                elif raw_options == ["d"]:
                    options = example.default_options

                elif raw_options != [""]:
                    options = set(raw_options)

                is_valid_option = True
                for option in options:
                    if option not in example.possible_options:
                        is_valid_option = False
                        print("Error: Option '%s' does not exist." % option)
                        break

                if is_valid_option:
                    result = example.function(example_name, options)
                    print("")
                    print("Example ended with result code: %d." % result)
            else:
                print("Error: Example '%s' do not exist in expected options." % example_name)
                
            print("")

example_manager = ExampleManager()

if False: # ExampleManager test
    def example_1(name, options):
        print(name, options)
        return 0

    def example_2(name, options):
        print(name, options)
        return 0

    def example_3(name, options):
        print(name, options)
        return 0

    def example_4(name, options):
        print(name, options)
        return 0

    def example_5(name, options):
        print(name, options)
        return 0
        
    example_manager.set_default("example_2")

    example_manager.add_example("example_1", example_1)
    example_manager.add_example("example_2", example_2, ["a"])
    example_manager.add_example("example_3", example_3, ["a", "c", "d", "e", "f"])
    example_manager.add_example("example_4", example_4, ["a", "c", "d", "e", "f"], ["a", "d"])
    example_manager.add_example("example_5", example_5)

    example_manager.run_examples()

    exit(1)

################################################################################
# basics
################################################################################

def basics(name, options):
    def rect_to_str(r):
        return "%d %d %d %d" % (r.left, r.top, r.right, r.bottom)

    def rect_diff(a, b):
        return RECT(a.left - b.left, a.top - b.top, a.right - b.right, a.bottom - b.bottom)

    ### Window Function Scenarios ####
    width   = GetSystemMetrics(SM_CXSCREEN)
    height  = GetSystemMetrics(SM_CYSCREEN)
    print(width, height)

    rc = RECT()
    if not SystemParametersInfoW(SPI_GETWORKAREA, 0, byref(rc), 0):
        print("Error Code: %d" % GetLastError())
    print(rc.left, rc.top, rc.right, rc.bottom)

    NOT_WORKING_CODE = 11111111
    if not SystemParametersInfoW(NOT_WORKING_CODE, 0, None, 0):
        print("Error Code: %d" % GetLastError())
        print(FormatError(GetLastError()))
        

    window_handle = GetForegroundWindow()
    print(window_handle)

    window_rect = RECT()
    GetWindowRect(window_handle, byref(window_rect))
    print(rect_to_str(window_rect))

    actual_window_rect = RECT()
    DwmGetWindowAttribute(window_handle, DWMWA_EXTENDED_FRAME_BOUNDS, byref(actual_window_rect), sizeof(RECT))
    print(rect_to_str(actual_window_rect))
    print(rect_to_str(rect_diff(actual_window_rect, window_rect)))

    client_rect = RECT()
    GetClientRect(window_handle, byref(client_rect))
    print(rect_to_str(client_rect))

    points = cast(byref(client_rect), LPPOINT)

    ClientToScreen(window_handle, points)
    ClientToScreen(window_handle, byref(points[1]))

    print(rect_to_str(client_rect))

    ScreenToClient(window_handle, points)
    ScreenToClient(window_handle, byref(points[1]))

    print(rect_to_str(client_rect))

    ### get window name ###

    num_of_chars = GetWindowTextLengthW(window_handle)
    length = num_of_chars + 1
    buffer = (c_wchar * length)()
    GetWindowTextW(window_handle, buffer, length)

    window_name = cast(buffer, c_wchar_p).value
    print(window_name)

    this_window_handle = window_handle

    ### 

    window_handle = FindWindowW(None, "Untitled - Notepad")
    if window_handle:
        if not SetForegroundWindow(window_handle):
            print(FormatError(GetLastError()))
        
        print("Window 'Untitled - Notepad' moved to foreground.")

    window_handle = FindWindowW(None, "*Untitled - Notepad")
    if window_handle:
        if not SetForegroundWindow(window_handle):
            print(FormatError(GetLastError()))
        
        print("Focused on '*Untitled - Notepad'.")

    if not SetWindowLongPtrW(window_handle, GWL_STYLE, WS_POPUPWINDOW):
        print(FormatError(GetLastError()))

    pos = POINT()
    GetCursorPos(byref(pos))
    print("%d %d" % (pos.x, pos.y))

    SetWindowPos(this_window_handle, HWND_TOP, 0, 0, 1200, 600, SWP_NOMOVE)

    ###

    if "min_max" in options:
        assert IsMaximized(this_window_handle) == False
        assert IsMinimized(this_window_handle) == False

        ShowWindow(this_window_handle, SW_MINIMIZE)

        assert IsMaximized(this_window_handle) == False
        assert IsMinimized(this_window_handle) == True

        time.sleep(0.2)

        ShowWindow(this_window_handle, SW_MAXIMIZE)

        assert IsMaximized(this_window_handle) == True
        assert IsMinimized(this_window_handle) == False

        time.sleep(0.2)

        ShowWindow(this_window_handle, SW_SHOWNORMAL)
    
        assert IsMaximized(this_window_handle) == False
        assert IsMinimized(this_window_handle) == False

    ### Macro Check ###
    if sizeof(c_void_p) == 4:
        assert ULONG is ULONG_PTR
    else:
        assert ULONG is not ULONG_PTR

    i = MAKEINTRESOURCEW(0x12345678)
    p = cast(byref(i), POINTER(c_short))
    assert p[0] == 0x5678

    assert HIWORD(0x12345678).value == 0x1234
    assert LOWORD(0x12345678).value == 0x5678

    assert GET_X_LPARAM(0xFF12FF34).value == -204
    assert GET_Y_LPARAM(0xFF12FF34).value == -238

    assert GET_WHEEL_DELTA_WPARAM(0xFF12FF34).value == -238
    assert GET_KEYSTATE_WPARAM(0x12345678).value == 0x5678

    return 0
example_manager.add_example("basics", basics, ["min_max"])

################################################################################
# simple_window
################################################################################
count       = 0

def simple_window(name, options):

    def WndProc(hWnd, msg, wParam, lParam):
        global count
    
        if msg == WM_CREATE:
            print("X - Close (no prompt)")
            print("Hold LMB + RMB - Display Mouse Position")
            return 0
    
        elif msg == WM_DESTROY:
            print("Bye. Bye.")
            PostQuitMessage(0)
            return 0

        elif msg == WM_PAINT:
            return 0;

        elif msg == WM_KEYDOWN:
            return 0
    
        elif msg == WM_KEYUP:
            count += 1
            print(count)

            if wParam == ord("X"):
                DestroyWindow(hWnd)
            return 0

        elif msg == WM_LBUTTONDOWN:
            if GetCapture() != hWnd:
                SetCapture(hWnd)
            return 0
    
        elif msg == WM_LBUTTONUP:
            if GetCapture() == hWnd:
                ReleaseCapture()
            return 0

        elif msg == WM_RBUTTONDOWN:
            return 0
    
        elif msg == WM_RBUTTONUP:
            pos = POINT()
            GetCursorPos(byref(pos))
            ScreenToClient(hWnd, byref(pos))
            print(pos.x, pos.y)

            return 0

        elif msg == WM_CLOSE:
            # This do not work. Will freeze window.
            #if MessageBoxW(NULL, "Are you sure?", "Exit", MB_ICONQUESTION | MB_OKCANCEL) == IDOK: 
            #    DestroyWindow(hWnd)
    
            # Working solution.
            if OwnerlessMessageBox_FromNewThreadWithWait("Are you sure?", "Exit", MB_ICONQUESTION | MB_OKCANCEL) == IDOK: 
                DestroyWindow(hWnd)
    
            return 0
    
        return DefWindowProcW(hWnd, msg, wParam, lParam)
    
    WndProc = WNDPROC(WndProc)
    
    window_name         = "Trivial Window"
    window_class_name   = window_name + " Class"
    icon_file_name      = "tests\\assets\\icon.ico"    
    
    hInstance = GetModuleHandleW(NULL)
        
    wc = WNDCLASSEXW()
    wc.cbSize           = sizeof(WNDCLASSEXW)
    wc.style            = CS_HREDRAW | CS_VREDRAW | CS_OWNDC
    wc.lpfnWndProc      = WndProc
    wc.cbClsExtra       = 0
    wc.cbWndExtra       = 0
    wc.hInstance        = hInstance
    wc.hIcon            = LoadImageW(
        NULL,
        icon_file_name,
        IMAGE_ICON,
        0, 0,
        LR_LOADFROMFILE | LR_DEFAULTSIZE | LR_SHARED
    )
    wc.hCursor          = LoadCursorW(NULL, IDC_ARROW)
    wc.hbrBackground    = COLOR_WINDOW
    wc.lpszMenuName     = NULL
    wc.lpszClassName    = window_class_name
    wc.hIconSm          = NULL
    
    if not RegisterClassExW(byref(wc)):
        print("Error: Cannot create window class.")
        exit(EXIT_FAILURE)
    
    hWnd = CreateWindowExW(
        0,
        window_class_name,
        window_name,
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT,
        NULL,
        NULL,
        hInstance,
        NULL
    )
    
    if not hWnd:
        print("Error: Cannot create window.")
        exit(EXIT_FAILURE)
            
    UpdateWindow(hWnd)
    ShowWindow(hWnd, SW_SHOW)
    SetForegroundWindow(hWnd)
    
    def execute_main_loop():
        is_peek = True

        if is_peek:
            msg = MSG()
            while True:
                while PeekMessageW(byref(msg), NULL, 0, 0, PM_REMOVE):
                    if msg.message == WM_QUIT:
                        return msg.wParam
    
                    TranslateMessage(byref(msg))
                    DispatchMessageW(byref(msg))
    
                # ... render, update ...
        else:
            msg = MSG()
            while GetMessageW(byref(msg), NULL, 0, 0):
                TranslateMessage(byref(msg))
                DispatchMessageW(byref(msg))
            return msg.wParam

    result = execute_main_loop()
    UnregisterClassW(window_class_name, hInstance)
    return result

example_manager.add_example("simple_window", simple_window)

################################################################################
# opengl_window
################################################################################
def opengl_window(name, options):
    TIMER_ID    = 1000
    TIMER_DELAY = 20 # in milliseconds

    class Data:
        hDC     = NULL
        hRC     = NULL
        angle   = 0.0
    data = Data()

    def initialize():
        glClearColor(0.0, 0.0, 0.5, 1.0)

    def render():
        glClear(GL_COLOR_BUFFER_BIT)

        glPushMatrix()
        glRotatef(data.angle, 0, 0, 1)

        glBegin(GL_TRIANGLES)
        glColor3f(1, 0, 0)
        glVertex2f(0, 0.5)

        glColor3f(0, 1, 0)
        glVertex2f(0.5, -0.5)

        glColor3f(0, 0, 1)
        glVertex2f(-0.5, -0.5)
        glEnd()

        glPopMatrix()

    def MessageError(err_msg):
        print(err_msg)
        exit(EXIT_FAILURE)

    def PixelTypeToStr(iPixelType):
        return {
            PFD_TYPE_RGBA : "PFD_TYPE_RGBA",
            PFD_TYPE_COLORINDEX : "PFD_TYPE_COLORINDEX",
        }.get(iPixelType, "")
    
    def FlagsToStr(dwFlags):
        text = ""
        text += "PFD_DOUBLEBUFFER, "         if dwFlags & PFD_DOUBLEBUFFER else ""
        text += "PFD_STEREO, "               if dwFlags & PFD_STEREO else ""
        text += "PFD_DRAW_TO_WINDOW, "       if dwFlags & PFD_DRAW_TO_WINDOW else ""
        text += "PFD_DRAW_TO_BITMAP, "       if dwFlags & PFD_DRAW_TO_BITMAP else ""
        text += "PFD_SUPPORT_GDI, "          if dwFlags & PFD_SUPPORT_GDI else ""
        text += "PFD_SUPPORT_OPENGL, "       if dwFlags & PFD_SUPPORT_OPENGL else ""
        text += "PFD_GENERIC_FORMAT, "       if dwFlags & PFD_GENERIC_FORMAT else ""
        text += "PFD_NEED_PALETTE, "         if dwFlags & PFD_NEED_PALETTE else ""
        text += "PFD_NEED_SYSTEM_PALETTE, "  if dwFlags & PFD_NEED_SYSTEM_PALETTE else ""
        text += "PFD_SWAP_EXCHANGE, "        if dwFlags & PFD_SWAP_EXCHANGE else ""
        text += "PFD_SWAP_COPY, "            if dwFlags & PFD_SWAP_COPY else ""
        text += "PFD_SWAP_LAYER_BUFFERS, "   if dwFlags & PFD_SWAP_LAYER_BUFFERS else ""
        text += "PFD_GENERIC_ACCELERATED, "  if dwFlags & PFD_GENERIC_ACCELERATED else ""
        text += "PFD_SUPPORT_DIRECTDRAW, "   if dwFlags & PFD_SUPPORT_DIRECTDRAW else ""
        text += "PFD_DIRECT3D_ACCELERATED, " if dwFlags & PFD_DIRECT3D_ACCELERATED else ""
        text += "PFD_SUPPORT_COMPOSITION, "  if dwFlags & PFD_SUPPORT_COMPOSITION else ""
        return text

    def ViewPFD(pfi, pfd):
        print("I:%4d C:%2d R:%2d G:%2d B:%2d A:%2d D:%2d S:%2d P:%s F:%s" % (
            pfi,
            pfd.cColorBits,
            pfd.cRedBits,
            pfd.cGreenBits,
            pfd.cBlueBits,
            pfd.cAlphaBits,
            pfd.cDepthBits,
            pfd.cStencilBits,
            PixelTypeToStr(pfd.iPixelType),
            FlagsToStr(pfd.dwFlags)
        ))

    def WndProc(hWnd, msg, wParam, lParam):
        try:
            if msg == WM_CREATE:
                pfd = PIXELFORMATDESCRIPTOR()
                memset(byref(pfd), 0, sizeof(PIXELFORMATDESCRIPTOR))
        
                pfd.nSize           = sizeof(PIXELFORMATDESCRIPTOR)
                pfd.nVersion        = 1
                pfd.dwFlags         = PFD_DRAW_TO_WINDOW | PFD_SUPPORT_OPENGL | PFD_DOUBLEBUFFER
                pfd.iPixelType      = PFD_TYPE_RGBA
                pfd.cColorBits      = 24
                pfd.cAlphaBits      = 8
                pfd.cDepthBits      = 32
                pfd.cStencilBits    = 8
                pfd.iLayerType      = PFD_MAIN_PLANE
        
                data.hDC = GetDC(hWnd);
                if not data.hDC:
                    MessageError("Can not get device context.");

                pfi = ChoosePixelFormat(data.hDC, byref(pfd))
                if not pfi:
                    MessageError("Can not choose pixel format. (windows error code: %d)" % GetLastError())
        
                result = SetPixelFormat(data.hDC, pfi, byref(pfd))
                if not result:
                    MessageError("Can not set pixel format. (windows error code: %d)" % GetLastError())

                # --- Just getting info --- 
                memset(byref(pfd), 0, sizeof(PIXELFORMATDESCRIPTOR))
                max_pfi = DescribePixelFormat(data.hDC, pfi, sizeof(PIXELFORMATDESCRIPTOR), byref(pfd));
                if not max_pfi:
                    MessageError("Can not get pixel format. (windows error code: %d)" % GetLastError())
            
                print("cColorBits   =", pfd.cColorBits)
                print("cRedBits     =", pfd.cRedBits)
                print("cGreenBits   =", pfd.cGreenBits)
                print("cBlueBits    =", pfd.cBlueBits)
                print("cAlphaBits   =", pfd.cAlphaBits)
                print("cDepthBits   =", pfd.cDepthBits)
                print("cStencilBits =", pfd.cStencilBits)
            
                if "list_pixel_formats" in options:
                    max_pfi = DescribePixelFormat(data.hDC, 0, 0, NULL)
                    print("max_pfi:", max_pfi)
            
                    for pfi in range(0, max_pfi + 1):
                        memset(byref(pfd), 0, sizeof(PIXELFORMATDESCRIPTOR))
                        DescribePixelFormat(data.hDC, pfi, sizeof(PIXELFORMATDESCRIPTOR), byref(pfd))
                
                        ViewPFD(pfi, pfd)
                # ---
        
                data.hRC = wglCreateContext(data.hDC)
                if not data.hRC:
                    MessageError("Can not create OpenGL Rendering Context. (windows error code: %d)" % GetLastError())
        
                wglMakeCurrent(data.hDC, data.hRC)

                gl_version_major = 3
                gl_version_minor = 0

                attribute_list = [
                    WGL_CONTEXT_MAJOR_VERSION_ARB, gl_version_major,
                    WGL_CONTEXT_MINOR_VERSION_ARB, gl_version_minor,
                    WGL_CONTEXT_FLAGS_ARB, WGL_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB,
                    0
                ]
                attribute_list = (c_int * len(attribute_list))(*(attribute for attribute in attribute_list))

                wglCreateContextAttribsARB = PFNWGLCREATECONTEXTATTRIBSARBPROC(wglGetProcAddress(b"wglCreateContextAttribsARB"))

                data.hRC = wglCreateContextAttribsARB(data.hDC, data.hRC, attribute_list)
                if not data.hRC:
                    MessageError("Can not create OpenGL %d.%d Rendering Context. (windows error code: %d)" % (gl_version_major, gl_version_minor, GetLastError()))

                wglMakeCurrent(data.hDC, data.hRC)
        
                # --- Just getting info --- 
                version_string = cast(glGetString(GL_VERSION), c_char_p).value.decode("utf-8")
                print("GL_VERSION: %s\n" % version_string, flush = True)

                # ---

                initialize()

                # ---

                print("X - Close (no prompt)")

                return 0
    
            if msg == WM_DESTROY:
                print("Bye. Bye.")

                wglMakeCurrent(NULL, NULL)
                wglDeleteContext(data.hRC)
                ReleaseDC(hWnd, data.hDC)

                PostQuitMessage(0)

                return 0

            if msg == WM_PAINT:
                render()
                SwapBuffers(data.hDC)
                ValidateRect(hWnd, NULL)
                return 0;

            if msg == WM_ERASEBKGND:
                # Tells DefWindowProc to not erase background. It's unnecessary since background is handled by OpenGL.
                return 1

            if msg == WM_TIMER:
                if wParam == TIMER_ID:
                    # 15 degrees per second
                    data.angle += 15 * (TIMER_DELAY / 1000.0)
                return 0

            if msg == WM_SIZE:
                glViewport(0, 0, LOWORD(lParam).value, HIWORD(lParam).value)
                return 0

            if msg == WM_KEYUP:
                if wParam == ord("X"):
                    DestroyWindow(hWnd)
                return 0

            if msg == WM_CLOSE:
                DestroyWindow(hWnd)
                return 0
    
            return DefWindowProcW(hWnd, msg, wParam, lParam)

        except Exception as e:
            DestroyWindow(hWnd)
            raise e
    
    WndProc = WNDPROC(WndProc)
    
    window_name         = "OpenGL Window"
    window_class_name   = window_name + " Class"
    icon_file_name      = "tests\\assets\\icon.ico"    
    
    hInstance = GetModuleHandleW(NULL)
        
    wc = WNDCLASSEXW()
    wc.cbSize           = sizeof(WNDCLASSEXW)
    wc.style            = CS_HREDRAW | CS_VREDRAW | CS_OWNDC
    wc.lpfnWndProc      = WndProc
    wc.hInstance        = hInstance
    wc.hIcon            = LoadImageW(
        NULL,
        icon_file_name,
        IMAGE_ICON,
        0, 0,
        LR_LOADFROMFILE | LR_DEFAULTSIZE | LR_SHARED
    )
    wc.hCursor          = LoadCursorW(NULL, IDC_ARROW)
    wc.lpszClassName    = window_class_name
    
    if not RegisterClassExW(byref(wc)):
        print("Error: Cannot create window class.")
        exit(EXIT_FAILURE)

    work_area_rect = RECT()
    SystemParametersInfoW(SPI_GETWORKAREA, 0, byref(work_area_rect), 0)
    work_area_width     = work_area_rect.right - work_area_rect.left
    work_area_height    = work_area_rect.bottom - work_area_rect.top

    width = work_area_width // 2
    height = work_area_height // 2
    x = (work_area_width - width) // 2
    y = (work_area_height - height) // 2
    
    hWnd = CreateWindowExW(
        0,
        window_class_name,
        window_name,
        WS_OVERLAPPEDWINDOW,
        x, y, width, height,
        NULL,
        NULL,
        hInstance,
        NULL
    )
    
    if not hWnd:
        print("Error: Cannot create window.")
        exit(EXIT_FAILURE)

    SetTimer(hWnd, TIMER_ID, TIMER_DELAY, TIMERPROC(0))
            
    UpdateWindow(hWnd)
    ShowWindow(hWnd, SW_SHOW)
    SetForegroundWindow(hWnd)
    
    def execute_main_loop():
        is_peek = True

        if is_peek:
            msg = MSG()
            while True:
                while PeekMessageW(byref(msg), NULL, 0, 0, PM_REMOVE):
                    if msg.message == WM_QUIT:
                        return msg.wParam
    
                    TranslateMessage(byref(msg))
                    DispatchMessageW(byref(msg))
    
                render()
                SwapBuffers(data.hDC)
        else:
            msg = MSG()
            while GetMessageW(byref(msg), NULL, 0, 0):
                TranslateMessage(byref(msg))
                DispatchMessageW(byref(msg))
            return msg.wParam

    result = execute_main_loop()
    UnregisterClassW(window_class_name, hInstance)
    return result

example_manager.add_example("opengl_window", opengl_window, ["list_pixel_formats"])

################################################################################
# main
################################################################################

if __name__ == "__main__":
    example_manager.set_default("opengl_window")
    example_manager.run_examples()

    
    


    
   
