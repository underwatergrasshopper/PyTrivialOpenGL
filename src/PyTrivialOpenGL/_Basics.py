"""
Base functionality and support for PyTrivialOpenGL submodules.
"""

_MIN_U16 = 0
_MAX_U16 = 2**31 - 1

_MIN_I32 = -(2**31)
_MAX_I32 = 2**31 - 1

def clamp(val, min_val, max_val):
    return max(min(val, max_val), min_val)

def is_i32(v):
    return _MIN_I32 <= v and v <= _MAX_I32

def is_u16(v):
    return _MIN_U16 <= v and v <= _MAX_U16

def is_point_i32(p):
    return is_i32(p.x) and is_i32(p.y)

def is_size_u16(s):
    return is_u16(s.width) and is_u16(s.height)

def is_area_i32_u16(a):
    return is_i32(a.x) and is_i32(a.y) and is_u16(a.width) and is_u16(a.height)

def check_i32(v):
    if not is_i32(v):
        raise ValueError("Value is not in rage of 32 bit integer.")

def check_u16(v):
    if not is_u16(v):
        raise ValueError("Value is not in rage of 16 bit unsigned integer.")

def check_point_i32(p):
    if not is_point_i32(p):
        raise ValueError("Point's x and y are not in range of 32 bit integer.")

def check_size_u16(s):
    if not is_size_u16(s):
        raise ValueError("Size's width and height are not in range of 16 bit unsigned integer.")

def check_area_i32_u16(a):
    if not is_area_i32_u16(a):
        raise ValueError("Area's x and y are not in range of 32 bit integer. Area's width and height are not in range of 16 bit unsigned integer.")

