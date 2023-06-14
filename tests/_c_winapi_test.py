from PyTrivialOpenGL._C_WinApi import *
from ctypes import *

if __name__ == "__main__":
    width   = GetSystemMetrics(SM_CXSCREEN)
    height  = GetSystemMetrics(SM_CYSCREEN)
    print(GetLastError())
    print(width, height)
    
    rc = RECT()
    SystemParametersInfoW(SPI_GETWORKAREA, 0, byref(rc), 0)
    print(rc.left, rc.top, rc.right, rc.bottom)
    print(GetLastError())

    SystemParametersInfoW(11111111, 0, None, 0)
    print(GetLastError())
    
   
