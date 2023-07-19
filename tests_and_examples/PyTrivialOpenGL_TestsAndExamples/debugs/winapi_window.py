from msilib.schema import Icon
from PyTrivialOpenGL._C_WinApi import *
from PyTrivialOpenGL._C_WGL import *
from PyTrivialOpenGL._C_GL import *
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
from ..utility.ExampleManager import ExampleManager
import time
import os
import re

__all__ = ["run"]

wm_paint_count = 0

def run(name, options):
    def WndProc(hWnd, msg, wParam, lParam):
        global wm_paint_count

        if "all_wm" in options:
            if msg == WM_PAINT:
                if wm_paint_count == 0:
                    print(_wm_to_str(msg))
                elif wm_paint_count == 1:
                    print("...")
                wm_paint_count += 1
            else:
                if wm_paint_count > 2:
                    print("WM_PAINT x%u" % (wm_paint_count - 1))
                elif wm_paint_count > 1:
                    print("WM_PAINT")
                else:
                    print(_wm_to_str(msg))
                wm_paint_count = 0
    
        if msg == WM_CREATE:
            print("Escape - Close (no prompt)")
            print("0 - Test _WindowAreaCorrector (simulates maximize)")
            print("Hold LMB + RMB - Display Mouse Position")
            return 0
    
        elif msg == WM_DESTROY:
            print("Bye. Bye.")
            PostQuitMessage(0)
            return 0

        elif msg == WM_PAINT:
            return 0;

        elif msg == WM_KEYDOWN:
            key_id = _vk_code_to_key_id(wParam)
            print(key_id, _get_keyboard_side_id(key_id, _VirtualKeyData(lParam)))
            #print(bin(lParam & 0xFFFFFFFF))
            print(_vk_code_to_str(wParam))


            #print_bin_32(lParam)
            #print(_VirtualKeyData(lParam))

            return 0
    
        elif msg == WM_KEYUP:
            key_id = _vk_code_to_key_id(wParam)
            print(key_id, _get_keyboard_side_id(key_id, _VirtualKeyData(lParam)))
            print(_vk_code_to_str(wParam))
            #key_id = _vk_code_to_key_id(wParam)
            #data = WPARAM(wParam)
            #ptr = cast(byref(data), POINTER(_C_VirtualKeyData))
            #
            #print(key_id, _get_keyboard_side_id(key_id, ptr))
            #print(bin(lParam & 0xFFFFFFFF))
            #print_bin_32(lParam)
            #print(_VirtualKeyData(lParam))

            if wParam == VK_ESCAPE:
                DestroyWindow(hWnd)
            elif wParam == ord("0"):
                # _WindowAreaCorrector test
                area = get_work_area()
                window_area_corrector = _WindowAreaCorrector()
                area = window_area_corrector.add_invisible_frame_to_area(area, hWnd)
                SetWindowPos(hWnd, HWND_TOP, area.x, area.y, area.width, area.height, 0)

            return 0

        elif msg == WM_SYSKEYDOWN:
            key_id = _vk_code_to_key_id(wParam)
            print(key_id, _get_keyboard_side_id(key_id, _VirtualKeyData(lParam)))
            print(_vk_code_to_str(wParam))

            return 0

        elif msg == WM_SYSKEYUP:
            key_id = _vk_code_to_key_id(wParam)
            print(key_id, _get_keyboard_side_id(key_id, _VirtualKeyData(lParam)))

            return 0

        elif msg == WM_LBUTTONDOWN:
            print(_get_mouse_key_id(msg, wParam), _is_mouse_button_down(msg))
            print(_vk_code_to_str(wParam))

            if GetCapture() != hWnd:
                SetCapture(hWnd)
            return 0
    
        elif msg == WM_LBUTTONUP:
            print(_get_mouse_key_id(msg, wParam), _is_mouse_button_down(msg))

            if GetCapture() == hWnd:
                ReleaseCapture()
            return 0

        elif msg == WM_RBUTTONDOWN:
            print(_get_mouse_key_id(msg, wParam), _is_mouse_button_down(msg))

            return 0
    
        elif msg == WM_RBUTTONUP:
            print(_get_mouse_key_id(msg, wParam), _is_mouse_button_down(msg))

            pos = POINT()
            GetCursorPos(byref(pos))
            ScreenToClient(hWnd, byref(pos))
            print(pos.x, pos.y)

            return 0

        elif msg == WM_MBUTTONDOWN:
            print(_get_mouse_key_id(msg, wParam), _is_mouse_button_down(msg))

            return 0
    
        elif msg == WM_MBUTTONUP:
            print(_get_mouse_key_id(msg, wParam), _is_mouse_button_down(msg))

            return 0

        elif msg == WM_XBUTTONDOWN:
            print(_get_mouse_key_id(msg, wParam), _is_mouse_button_down(msg))

            return 0
    
        elif msg == WM_XBUTTONUP:
            print(_get_mouse_key_id(msg, wParam), _is_mouse_button_down(msg))

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