import pytest
import math

from PyTrivialOpenGL.Size import Size
from PyTrivialOpenGL.Area import Area
from PyTrivialOpenGL.Point import Point
from PyTrivialOpenGL._Basics import *

__all__ = [
    "run"
]

def test_basics():
    ### is_i32, check_i32 ###

    assert is_i32(MIN_I32)
    assert is_i32(MAX_I32)

    assert not is_i32(MIN_I32 - 1)
    assert not is_i32(MAX_I32 + 1)

    try:
        check_i32(MIN_I32)
    except Exception:
        assert False, "Should not throw exception."

    try:
        check_i32(MAX_I32)
    except Exception:
        assert False, "Should not throw exception."

    try:
        check_i32(MIN_I32 - 1)
    except ValueError as e:
        assert str(e) == "Value is not in rage of 32 bit integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    try:
        check_i32(MAX_I32 + 1)
    except ValueError as e:
        assert str(e) == "Value is not in rage of 32 bit integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    ### is_u16, check_u16 ###

    assert is_u16(MIN_U16)
    assert is_u16(MAX_U16)

    assert not is_u16(MIN_U16 - 1)
    assert not is_u16(MAX_U16 + 1)

    try:
        check_u16(MIN_U16)
    except Exception:
        assert False, "Should not throw exception."

    try:
        check_u16(MAX_U16)
    except Exception:
        assert False, "Should not throw exception."

    try:
        check_u16(MIN_U16 - 1)
    except ValueError as e:
        assert str(e) == "Value is not in rage of 16 bit unsigned integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    try:
        check_u16(MAX_U16 + 1)
    except ValueError as e:
        assert str(e) == "Value is not in rage of 16 bit unsigned integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    ### is_size_u16, check_size_u16 ###

    assert is_size_u16(Size(MIN_U16, MIN_U16))
    assert is_size_u16(Size(MAX_U16, MAX_U16))

    assert not is_size_u16(Size(MIN_U16 - 1, MIN_U16))
    assert not is_size_u16(Size(MIN_U16, MIN_U16 - 1))
    assert not is_size_u16(Size(MAX_U16 + 1, MAX_U16))
    assert not is_size_u16(Size(MAX_U16, MAX_U16 + 1))

    try:
        check_size_u16(Size(MIN_U16, MIN_U16))
    except Exception:
        assert False, "Should not throw exception."

    try:
        check_size_u16(Size(MAX_U16, MAX_U16))
    except Exception:
        assert False, "Should not throw exception."

    try:
        check_size_u16(Size(MIN_U16 - 1, MIN_U16))
    except ValueError as e:
        assert str(e) == "Size's value 'width' are not in range of 16 bit unsigned integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    try:
        check_size_u16(Size(MIN_U16, MIN_U16 - 1))
    except ValueError as e:
        assert str(e) == "Size's value 'height' are not in range of 16 bit unsigned integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    try:
        check_size_u16(Size(MAX_U16 + 1, MAX_U16))
    except ValueError as e:
        assert str(e) == "Size's value 'width' are not in range of 16 bit unsigned integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    try:
        check_size_u16(Size(MAX_U16, MAX_U16 + 1))
    except ValueError as e:
        assert str(e) == "Size's value 'height' are not in range of 16 bit unsigned integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    ### is_point_i32, check_point_i32 ###

    assert is_point_i32(Point(MIN_I32, MIN_I32))
    assert is_point_i32(Point(MAX_I32, MAX_I32))

    assert not is_point_i32(Point(MIN_I32 - 1, MIN_I32))
    assert not is_point_i32(Point(MIN_I32, MIN_I32 - 1))
    assert not is_point_i32(Point(MAX_I32 + 1, MAX_I32))
    assert not is_point_i32(Point(MAX_I32, MAX_I32 + 1))

    try:
        check_point_i32(Point(MIN_I32, MIN_I32))
    except Exception:
        assert False, "Should not throw exception."

    try:
        check_point_i32(Point(MAX_I32, MAX_I32))
    except Exception:
        assert False, "Should not throw exception."

    try:
        check_point_i32(Point(MIN_I32 - 1, MIN_I32))
    except ValueError as e:
        assert str(e) == "Point's value 'x' are not in range of 32 bit integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    try:
        check_point_i32(Point(MIN_I32, MIN_I32 - 1))
    except ValueError as e:
        assert str(e) == "Point's value 'y' are not in range of 32 bit integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    try:
        check_point_i32(Point(MAX_I32 + 1, MAX_I32))
    except ValueError as e:
        assert str(e) == "Point's value 'x' are not in range of 32 bit integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    try:
        check_point_i32(Point(MAX_I32, MAX_I32 + 1))
    except ValueError as e:
        assert str(e) == "Point's value 'y' are not in range of 32 bit integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    ### is_area_i32_u16, check_area_i32_u16 ###
    
    assert is_area_i32_u16(Area(MIN_I32, MIN_I32, MIN_U16, MIN_U16))
    assert is_area_i32_u16(Area(MAX_I32, MAX_I32, MAX_U16, MAX_U16))
    
    assert not is_area_i32_u16(Area(MIN_I32 - 1, MIN_I32, MIN_U16, MIN_U16))
    assert not is_area_i32_u16(Area(MIN_I32, MIN_I32 - 1, MIN_U16, MIN_U16))
    assert not is_area_i32_u16(Area(MIN_I32, MIN_I32, MIN_U16 - 1, MIN_U16))
    assert not is_area_i32_u16(Area(MIN_I32, MIN_I32, MIN_U16, MIN_U16 - 1))
    assert not is_area_i32_u16(Area(MAX_I32 + 1, MAX_I32, MAX_U16, MAX_U16))
    assert not is_area_i32_u16(Area(MAX_I32, MAX_I32 + 1, MAX_U16, MAX_U16))
    assert not is_area_i32_u16(Area(MAX_I32, MAX_I32, MAX_U16 + 1, MAX_U16))
    assert not is_area_i32_u16(Area(MAX_I32, MAX_I32, MAX_U16, MAX_U16 + 1))
    
    try:
        check_area_i32_u16(Area(MIN_I32, MIN_I32, MIN_U16, MIN_U16))
    except Exception:
        assert False, "Should not throw exception."
    
    try:
        check_area_i32_u16(Area(MAX_I32, MAX_I32, MAX_U16, MAX_U16))
    except Exception:
        assert False, "Should not throw exception."
    
    try:
        check_area_i32_u16(Area(MIN_I32 - 1, MIN_I32, MIN_U16, MIN_U16))
    except ValueError as e:
        assert str(e) == "Area's value 'x' are not in range of 32 bit integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    try:
        check_area_i32_u16(Area(MIN_I32, MIN_I32 - 1, MIN_U16, MIN_U16))
    except ValueError as e:
        assert str(e) == "Area's value 'y' are not in range of 32 bit integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    try:
        check_area_i32_u16(Area(MIN_I32, MIN_I32, MIN_U16 - 1, MIN_U16))
    except ValueError as e:
        assert str(e) == "Area's value 'width' are not in range of 16 bit unsigned integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    try:
        check_area_i32_u16(Area(MIN_I32, MIN_I32, MIN_U16, MIN_U16 - 1))
    except ValueError as e:
        assert str(e) == "Area's value 'height' are not in range of 16 bit unsigned integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."
    
    try:
        check_area_i32_u16(Area(MAX_I32 + 1, MAX_I32, MAX_U16, MAX_U16))
    except ValueError as e:
        assert str(e) == "Area's value 'x' are not in range of 32 bit integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."
    
    try:
        check_area_i32_u16(Area(MAX_I32, MAX_I32 + 1, MAX_U16, MAX_U16))
    except ValueError as e:
        assert str(e) == "Area's value 'y' are not in range of 32 bit integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."
    
    try:
        check_area_i32_u16(Area(MAX_I32, MAX_I32, MAX_U16 + 1, MAX_U16))
    except ValueError as e:
        assert str(e) == "Area's value 'width' are not in range of 16 bit unsigned integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."
    
    try:
        check_area_i32_u16(Area(MAX_I32, MAX_I32, MAX_U16, MAX_U16 + 1))
    except ValueError as e:
        assert str(e) == "Area's value 'height' are not in range of 16 bit unsigned integer."
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

def run():
    print("test_basics start")
    test_basics()

    print("test_basics end")

if __name__ == "__main__":
   run()