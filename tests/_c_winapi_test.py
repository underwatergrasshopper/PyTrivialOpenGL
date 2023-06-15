from msilib.schema import Icon
from PyTrivialOpenGL._C_WinApi import *
from ctypes import *
import time
import os

def rect_to_str(r):
    return "%d %d %d %d" % (r.left, r.top, r.right, r.bottom)

def rect_diff(a, b):
    return RECT(a.left - b.left, a.top - b.top, a.right - b.right, a.bottom - b.bottom)

count = 0

def run_window():
    def WndProc(hWnd, msg, wParam, lParam):
        global count

        if msg == WM_PAINT:
            return 0;

        if msg == WM_CREATE:
            return 0

        if msg == WM_DESTROY:
            PostQuitMessage(0)
            return 0

        if msg == WM_KEYUP:
            count += 1
            print(count)
            return 0

        if msg == WM_CLOSE:
            # This do not work. Will freeze window.
            #if MessageBoxW(NULL, "Do you want exit?", "Exit", MB_ICONQUESTION | MB_OKCANCEL) == IDOK: 
            #    DestroyWindow(hWnd)

            # Working solution.
            if OwnerlessMessageBox_FromNewThreadWithWait("Do you want exit?", "Exit", MB_ICONQUESTION | MB_OKCANCEL) == IDOK: 
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
    # SetForegroundWindow(hWnd)

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

if __name__ == "__main__":
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

    if False:
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

    result = run_window()
    exit(result)
    
    


    
   
