import pytest
import math

from PyTrivialOpenGL.Size   import Size
from PyTrivialOpenGL.Point  import Point
from PyTrivialOpenGL.Area   import Area

__all__ = [
    "run"
]

def test_area():

    ### constructor ###

    area = Area(1, 2, 3, 4)
    assert type(area.x)         is int
    assert type(area.y)         is int
    assert type(area.width)     is int
    assert type(area.height)    is int
    assert area.x       == 1
    assert area.y       == 2
    assert area.width   == 3
    assert area.height  == 4

    area = Area(1, 2.1, 3, 4.1)
    assert type(area.x)         is int
    assert type(area.y)         is float
    assert type(area.width)     is int
    assert type(area.height)    is float
    assert area.x       == 1
    assert area.y       == 2.1
    assert area.width   == 3
    assert area.height  == 4.1

    area = Area(1.1, 2.1, 3.1, 4.1)
    assert type(area.x)         is float
    assert type(area.y)         is float
    assert type(area.width)     is float
    assert type(area.height)    is float
    assert area.x       == 1.1
    assert area.y       == 2.1
    assert area.width   == 3.1
    assert area.height  == 4.1

    try:
        area = Area(1, "text", 3, 4)
    except TypeError as e:
        assert(str(e) == "Value of 'y' can not be converted to int.")
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    ### assignment ###

    area = Area(1, 2, 3, 4)
    area.y = 22
    assert type(area.x)         is int
    assert type(area.y)         is int
    assert type(area.width)     is int
    assert type(area.height)    is int
    assert area.x       == 1
    assert area.y       == 22
    assert area.width   == 3
    assert area.height  == 4

    area = Area(1, 2, 3, 4)
    area.y = 2.1
    assert type(area.x)         is int
    assert type(area.y)         is float
    assert type(area.width)     is int
    assert type(area.height)    is int
    assert area.x       == 1
    assert area.y       == 2.1
    assert area.width   == 3
    assert area.height  == 4

    area = Area(1.1, 2.1, 3.1, 4.1)
    area.y = 2
    assert type(area.x)         is float
    assert type(area.y)         is int
    assert type(area.width)     is float
    assert type(area.height)    is float
    assert area.x       == 1.1
    assert area.y       == 2
    assert area.width   == 3.1
    assert area.height  == 4.1

    area = Area(1, 2, 3, 4)
    try:
        area.y = "text"
    except TypeError as e:
        assert(str(e) == "Value of 'y' can not be converted to int.")
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    ### comparison ###
    
    assert not (Area(10, 20, 30 ,39) == Area(10, 20, 30 ,40))
    assert not (Area(10, 20, 29 ,40) == Area(10, 20, 30 ,40))
    assert not (Area(10, 19, 30 ,40) == Area(10, 20, 30 ,40))
    assert not (Area(9, 20, 30 ,40) == Area(10, 20, 30 ,40))
    assert Area(10, 20, 30 ,40) == Area(10, 20, 30 ,40)
    assert not (Area(10, 20, 30 ,40) == Area(9, 20, 30 ,40))
    assert not (Area(10, 20, 30 ,40) == Area(10, 19, 30 ,40))
    assert not (Area(10, 20, 30 ,40) == Area(10, 20, 29 ,40))
    assert not (Area(10, 20, 30 ,40) == Area(10, 20, 30 ,39))

    assert Area(10, 20, 30 ,39) != Area(10, 20, 30 ,40)
    assert Area(10, 20, 29 ,40) != Area(10, 20, 30 ,40)
    assert Area(10, 19, 30 ,40) != Area(10, 20, 30 ,40)
    assert Area(9, 20, 30 ,40) != Area(10, 20, 30 ,40)
    assert not (Area(10, 20, 30 ,40) != Area(10, 20, 30 ,40))
    assert Area(10, 20, 30 ,40) != Area(9, 20, 30 ,40)
    assert Area(10, 20, 30 ,40) != Area(10, 19, 30 ,40)
    assert Area(10, 20, 30 ,40) != Area(10, 20, 29 ,40)
    assert Area(10, 20, 30 ,40) != Area(10, 20, 30 ,39)

    ### arithmetic ###
   
    assert Area(10, 20, 30, 40) + Area(1, 2, 3, 4) == Area(11, 22, 33, 44)
    assert Area(10, 20, 30, 40) - Area(1, 2, 3, 4) == Area(9, 18, 27, 36)

    area = Area(10, 20, 30, 40)
    area += Area(1, 2, 3, 4)
    assert area == Area(11, 22, 33, 44)

    area = Area(10, 20, 30, 40)
    area -= Area(1, 2, 3, 4)
    assert area == Area(9, 18, 27, 36)

    assert Area(10, 20, 30, 40) + Point(1, 2) == Area(11, 22, 30, 40)
    assert Area(10, 20, 30, 40) - Point(1, 2) == Area(9, 18, 30, 40)

    area = Area(10, 20, 30, 40)
    area += Point(1, 2)
    assert area == Area(11, 22, 30, 40)

    area = Area(10, 20, 30, 40)
    area -= Point(1, 2)
    assert area == Area(9, 18, 30, 40)

    assert Area(10, 20, 30, 40) + Size(3, 4) == Area(10, 20, 33, 44)
    assert Area(10, 20, 30, 40) - Size(3, 4) == Area(10, 20, 27, 36)

    area = Area(10, 20, 30, 40)
    area += Size(3, 4)
    assert area == Area(10, 20, 33, 44)

    area = Area(10, 20, 30, 40)
    area -= Size(3, 4)
    assert area == Area(10, 20, 27, 36)

    ### to_tuple ###

    t = Area(1, 2, 3, 4).to_tuple()
    assert type(t[0]) == int
    assert type(t[1]) == int
    assert type(t[2]) == int
    assert type(t[3]) == int
    assert t == (1, 2, 3, 4)

    t = Area(1, 2, 3.0, 4).to_tuple()
    assert type(t[0]) == int
    assert type(t[1]) == int
    assert type(t[2]) == float
    assert type(t[3]) == int
    assert t == (1, 2, 3.0, 4)

    t = Area(1, 2, 3, 4).to_tuple_f()
    assert type(t[0]) == float
    assert type(t[1]) == float
    assert type(t[2]) == float
    assert type(t[3]) == float
    assert t == (1.0, 2.0, 3.0, 4.0)

    t = Area(1.0, 2.0, 3.0, 4.0).to_tuple_i()
    assert type(t[0]) == int
    assert type(t[1]) == int
    assert type(t[2]) == int
    assert type(t[3]) == int
    assert t == (1, 2, 3, 4)

    ### is_zero ###

    assert Area(0, 0, 0, 0).is_zero()
    assert not Area(1, 0, 0, 0).is_zero()
    assert not Area(0, 2, 0, 0).is_zero()
    assert not Area(0, 0, 3, 0).is_zero()
    assert not Area(0, 0, 0, 4).is_zero()
    assert not Area(1, 2, 3, 4).is_zero()

    ### get_pos ###

    pos = Area(1, 2, 3, 4).get_pos()
    assert type(pos) is Point
    assert pos == Point(1, 2)

    ### get_size ###

    size = Area(1, 2, 3, 4).get_size()
    assert type(size) is Size
    assert size == Size(3, 4)

    ### is_in ###

    assert Area(10, 20, 50, 100).is_in(Point(10, 20))
    assert not Area(10, 20, 50, 100).is_in(Point(9, 20))
    assert not Area(10, 20, 50, 100).is_in(Point(10, 19))
    assert Area(10, 20, 50, 100).is_in(Point(59, 119))
    assert not Area(10, 20, 50, 100).is_in(Point(59, 120))
    assert not Area(10, 20, 50, 100).is_in(Point(60, 119))

    ### to_area_i ###
    assert Area(10.1, 20.1, 50.1, 100.1).get_area_i() == Area(10, 20, 50, 100)

def run():
    print("test_area start")
    test_area()
    print("test_area end")

if __name__ == "__main__":
   run()