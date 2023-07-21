from msilib.schema import Icon
from PyTrivialOpenGL._C_WinApi import *
from PyTrivialOpenGL._C_WGL import *
from PyTrivialOpenGL.C_GL import *
from PyTrivialOpenGL.Utility import *
from PyTrivialOpenGL.Key import *
from PyTrivialOpenGL.Key import _vk_code_to_key_id
from PyTrivialOpenGL.Key import _get_mouse_key_id
from PyTrivialOpenGL.Key import _is_mouse_button_down
from PyTrivialOpenGL.Key import _get_keyboard_side_id
from PyTrivialOpenGL.Key import _vk_code_to_str
from PyTrivialOpenGL.Key import _VirtualKeyData
from PyTrivialOpenGL._Debug import _wm_to_str
from PyTrivialOpenGL._WindowAreaCorrector import _WindowAreaCorrector

from ctypes import *
from ..utility.ExampleSupport import *
from ..utility.ExampleManager import ExampleManager
import time
import os
import re

__all__ = ["run"]

def run(name, options):
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

                print("Escape - Close (no prompt)")

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
                if wParam == VK_ESCAPE:
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
    icon_file_name      = get_path_to_assets() + "\\icon.ico"    
    
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