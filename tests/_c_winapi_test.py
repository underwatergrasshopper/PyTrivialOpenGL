from PyTrivialOpenGL._C_WinApi import *
from ctypes import *

if __name__ == "__main__":
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


    
   
