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
from ExampleManager import ExampleManager
import time
import os
import re

################################################################################

def print_point(p):
    print(p.x, p.y)

def print_size(s):
    print(s.width, s.height)

def print_area(a):
    print(a.x, a.y, a.width, a.height)

def print_bin_32(val):
    val = int(val) & 0xFFFFFFFF

    for ix in range(0, 32):
        if ix > 0 and ix % 4 == 0:
            print("`", end = "")

        if val & (0x1 << (31 - ix)):
            print("1", end = "")
        else:
            print("0", end = "")

    print("")


################################################################################
# basics
################################################################################




################################################################################
# simple_window
################################################################################



################################################################################
# opengl_window
################################################################################




################################################################################
# main
################################################################################

if __name__ == "__main__":
    example_manager.set_default("opengl_window")
    example_manager.run_examples()

    
    


    
   
