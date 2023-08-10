import pytest
import math

from PyTrivialOpenGL.Point import Point
from PyTrivialOpenGL.Size import Size

__all__ = [
    "run"
]

def test_point():

    ### constructor ###

    point = Point(2, 4)
    assert type(point.x) is int
    assert type(point.y) is int
    assert point.x == 2
    assert point.y == 4

    point = Point(2.1, 4.1)
    assert type(point.x) is float
    assert type(point.y) is float
    assert point.x == 2.1
    assert point.y == 4.1

    point = Point(2.1, 4)
    assert type(point.x) is float
    assert type(point.y) is int
    assert point.x == 2.1
    assert point.y == 4

    try:
        point = Point(1, "text")
    except ValueError as e:
        assert(str(e) == "Value of 'y' can not be converted to int.")
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    ### assignment ###

    point = Point(1, 2)
    point.x = 3
    point.y = 4
    assert type(point.x) is int
    assert type(point.y) is int
    assert point.x == 3
    assert point.y == 4

    point = Point(1, 2)
    point.x = 3.0
    point.y = 4.0
    assert type(point.x) is float
    assert type(point.y) is float
    assert point.x == 3.0
    assert point.y == 4.0

    point = Point(1, 2)
    point.x = 3
    point.y = 4.0
    assert type(point.x) is int
    assert type(point.y) is float
    assert point.x == 3
    assert point.y == 4.0

    point = Point(1, 2)
    try:
        point.y = "text"
    except ValueError as e:
        assert(str(e) == "Value of 'y' can not be converted to int.")
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    ### comparison ###

    assert not (Point(4, 9) == Point(5, 10))
    assert not (Point(5, 9) == Point(5, 10))
    assert not (Point(4, 10) == Point(5, 10))
    assert Point(5, 10) == Point(5, 10)
    assert not (Point(6, 10) == Point(5, 10))
    assert not (Point(5, 11) == Point(5, 10))
    assert not (Point(6, 11) == Point(5, 10))

    assert Point(4, 9)  != Point(5, 10)
    assert Point(5, 9)  != Point(5, 10)
    assert Point(4, 10) != Point(5, 10)
    assert not (Point(5, 10) != Point(5, 10))
    assert Point(6, 10) != Point(5, 10)
    assert Point(5, 11) != Point(5, 10)
    assert Point(6, 11) != Point(5, 10)

    assert not (Point(4, 9)  > Point(5, 10))
    assert not (Point(5, 9)  > Point(5, 10))
    assert not (Point(4, 10) > Point(5, 10))
    assert not (Point(5, 10) > Point(5, 10))
    assert not Point(6, 10) > Point(5, 10)
    assert not Point(5, 11) > Point(5, 10)
    assert Point(6, 11) > Point(5, 10)

    assert Point(4, 9)  < Point(5, 10)
    assert not Point(5, 9)  < Point(5, 10)
    assert not Point(4, 10) < Point(5, 10)
    assert not (Point(5, 10) < Point(5, 10))
    assert not (Point(6, 10) < Point(5, 10))
    assert not (Point(5, 11) < Point(5, 10))
    assert not (Point(6, 11) < Point(5, 10))

    assert not (Point(4, 9)  >= Point(5, 10))
    assert not (Point(5, 9)  >= Point(5, 10))
    assert not (Point(4, 10) >= Point(5, 10))
    assert Point(5, 10) >= Point(5, 10)
    assert Point(6, 10) >= Point(5, 10)
    assert Point(5, 11) >= Point(5, 10)
    assert Point(6, 11) >= Point(5, 10)

    assert Point(4, 9)  <= Point(5, 10)
    assert Point(5, 9)  <= Point(5, 10)
    assert Point(4, 10) <= Point(5, 10)
    assert Point(5, 10) <= Point(5, 10)
    assert not (Point(6, 10) <= Point(5, 10))
    assert not (Point(5, 11) <= Point(5, 10))
    assert not (Point(6, 11) <= Point(5, 10))

    ### arithmetic ###

    assert Point(10, 20) + Point(7, 3) == Point(17, 23)
    assert Point(10, 20) - Point(7, 3) == Point(3, 17)
    assert Point(10, 20) * Point(7, 3) == Point(70, 60)
    assert Point(10, 20) / Point(2, 5) == Point(5, 4)
    assert Point(10, 20) / Point(4, 8) == Point(2.5, 2.5)
    assert Point(10, 20) // Point(4, 8) == Point(2, 2)
    assert Point(10.9, 20.9) // Point(2, 5) == Point(5, 4)

    point = Point(10, 20)
    point += Point(7, 3)
    assert point == Point(17, 23)

    point = Point(10, 20)
    point -= Point(7, 3)
    assert point == Point(3, 17)

    point = Point(10, 20)
    point *= Point(7, 3)
    assert point == Point(70, 60)

    point = Point(10, 20)
    point /= Point(2, 5)
    assert point == Point(5, 4)

    point = Point(10, 20)
    point //= Point(4, 8)
    assert point == Point(2, 2)

    assert Point(10, 20) + Size(7, 3) == Point(17, 23)
    assert Point(10, 20) - Size(7, 3) == Point(3, 17)
    assert Point(10, 20) * Size(7, 3) == Point(70, 60)
    assert Point(10, 20) / Size(2, 5) == Point(5, 4)
    assert Point(10, 20) / Size(4, 8) == Point(2.5, 2.5)
    assert Point(10, 20) // Size(4, 8) == Point(2, 2)
    assert Point(10.9, 20.9) // Size(2, 5) == Point(5, 4)

    point = Point(10, 20)
    point += Size(7, 3)
    assert point == Point(17, 23)

    point = Point(10, 20)
    point -= Size(7, 3)
    assert point == Point(3, 17)

    point = Point(10, 20)
    point *= Size(7, 3)
    assert point == Point(70, 60)

    point = Point(10, 20)
    point /= Size(2, 5)
    assert point == Point(5, 4)

    point = Point(10, 20)
    point //= Size(4, 8)
    assert point == Point(2, 2)

    assert Point(10, 20) + 5 == Point(15, 25)
    assert Point(10, 20) - 4 == Point(6, 16)
    assert Point(10, 20) * 5 == Point(50, 100)
    assert Point(10, 20) / 5 == Point(2, 4)
    assert Point(10, 20) / 4 == Point(2.5, 5)
    assert Point(10, 20) // 4 == Point(2, 5)
    assert Point(10.9, 20.9) // 5 == Point(2, 4)

    point = Point(10, 20)
    point += 5
    assert point == Point(15, 25)

    point = Point(10, 20)
    point -= 4
    assert point == Point(6, 16)

    point = Point(10, 20)
    point *= 5
    assert point == Point(50, 100)

    point = Point(10, 20)
    point /= 4
    assert point == Point(2.5, 5)

    point = Point(10, 20)
    point //= 4
    assert point == Point(2, 5)

    ### to_tuple{_f|_i} ###

    t = Point(5, 6).to_tuple()
    assert type(t[0]) == int
    assert type(t[1]) == int
    assert t == (5, 6)

    t = Point(5.0, 6).to_tuple()
    assert type(t[0]) == float
    assert type(t[1]) == int
    assert t == (5.0, 6)

    t = Point(5, 6.0).to_tuple()
    assert type(t[0]) == int
    assert type(t[1]) == float
    assert t == (5, 6.0)

    t = Point(5, 6).to_tuple_f()
    assert type(t[0]) == float
    assert type(t[1]) == float
    assert t == (5.0, 6.0)

    t = Point(5.1, 6.1).to_tuple_i()
    assert type(t[0]) == int
    assert type(t[1]) == int
    assert t == (5, 6)

    ### is_zero ###

    assert Point(0, 0).is_zero()
    assert not Point(1, 0).is_zero()
    assert not Point(0, 2).is_zero()
    assert not Point(1, 2).is_zero()

    ### is_between ###

    assert Point(0, 0).is_between(Point(-1, -1), Point(1, 1))
    assert not Point(1, 0).is_between(Point(-1, -1), Point(1, 1))
    assert Point(-1, 0).is_between(Point(-1, -1), Point(1, 1))
    assert not Point(0, 1).is_between(Point(-1, -1), Point(1, 1))
    assert Point(0, -1).is_between(Point(-1, -1), Point(1, 1))
    assert not Point(1, 1).is_between(Point(-1, -1), Point(1, 1))
    assert Point(-1, -1).is_between(Point(-1, -1), Point(1, 1))
    
    assert not Point(-2, -1).is_between(Point(-1, -1), Point(1, 1))
    assert not Point(-1, -2).is_between(Point(-1, -1), Point(1, 1))
    assert not Point(-2, -2).is_between(Point(-1, -1), Point(1, 1))
    
    assert not Point(2, 1).is_between(Point(-1, -1), Point(1, 1))
    assert not Point(1, 2).is_between(Point(-1, -1), Point(1, 1))
    assert not Point(2, 2).is_between(Point(-1, -1), Point(1, 1))

    ### auto conversion ###

    assert str(Point(1, 2)) == "1 2"
    assert tuple(Point(1, 2)) == (1, 2)

    ### copy ###
    p = Point(1, 2)
    p2 = p.copy()
    assert p == p2
    assert p is not p2

def run():
    print("test_point start")
    test_point()
    print("test_point end")

if __name__ == "__main__":
   run()