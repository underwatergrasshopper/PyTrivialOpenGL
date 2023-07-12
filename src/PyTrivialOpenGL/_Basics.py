"""
This is an internal module! Shouldn't by imported outside of PyTrivialOpenGL package.

Contains functionality and support for PyTrivialOpenGL submodules.
"""

MIN_U16 = 0
MAX_U16 = 2**31 - 1

MIN_I32 = -(2**31)
MAX_I32 = 2**31 - 1

def clamp(val, min_val, max_val):
    return max(min(val, max_val), min_val)

def is_i32(v):
    return MIN_I32 <= v and v <= MAX_I32

def is_u16(v):
    return MIN_U16 <= v and v <= MAX_U16

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
    if not is_i32(p.x):
        raise ValueError("Point's value 'x' are not in range of 32 bit integer.")

    if not is_i32(p.y):
        raise ValueError("Point's value 'y' are not in range of 32 bit integer.")

def check_size_u16(s):
    if not is_u16(s.width):
        raise ValueError("Size's value 'width' are not in range of 16 bit unsigned integer.")

    if not is_u16(s.height):
        raise ValueError("Size's value 'height' are not in range of 16 bit unsigned integer.")

def check_area_i32_u16(a):
    if not is_i32(a.x):
        raise ValueError("Area's value 'x' are not in range of 32 bit integer.")

    if not is_i32(a.y):
        raise ValueError("Area's value 'y' are not in range of 32 bit integer.")

    if not is_u16(a.width):
        raise ValueError("Area's value 'width' are not in range of 16 bit unsigned integer.")

    if not is_u16(a.height):
        raise ValueError("Area's value 'height' are not in range of 16 bit unsigned integer.")

