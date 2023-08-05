import pytest
import math

from PyTrivialOpenGL.Size import *

__all__ = [
    "run"
]

def test_size():

    ### constructor ###

    size = Size(2, 4)
    assert type(size.width) is int
    assert type(size.height) is int
    assert size.width == 2
    assert size.height == 4

    size = Size(2.1, 4.1)
    assert type(size.width) is float
    assert type(size.height) is float
    assert size.width == 2.1
    assert size.height == 4.1

    size = Size(2.1, 4)
    assert type(size.width) is float
    assert type(size.height) is int
    assert size.width == 2.1
    assert size.height == 4

    try:
        size = Size(1, "text")
    except ValueError as e:
        assert(str(e) == "Value of 'height' can not be converted to int.")
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    ### assignment ###

    size = Size(1, 2)
    size.width = 3
    size.height = 4
    assert type(size.width) is int
    assert type(size.height) is int
    assert size.width == 3
    assert size.height == 4

    size = Size(1, 2)
    size.width = 3.0
    size.height = 4.0
    assert type(size.width) is float
    assert type(size.height) is float
    assert size.width == 3.0
    assert size.height == 4.0

    size = Size(1, 2)
    size.width = 3
    size.height = 4.0
    assert type(size.width) is int
    assert type(size.height) is float
    assert size.width == 3
    assert size.height == 4.0

    size = Size(1, 2)
    try:
        size.height = "text"
    except ValueError as e:
        assert(str(e) == "Value of 'height' can not be converted to int.")
    except Exception:
        assert False, "Wrong exception."
    else:
        assert False, "Should throw exception."

    ### comparison ###

    assert not (Size(4, 9) == Size(5, 10))
    assert not (Size(5, 9) == Size(5, 10))
    assert not (Size(4, 10) == Size(5, 10))
    assert Size(5, 10) == Size(5, 10)
    assert not (Size(6, 10) == Size(5, 10))
    assert not (Size(5, 11) == Size(5, 10))
    assert not (Size(6, 11) == Size(5, 10))

    assert Size(4, 9)  != Size(5, 10)
    assert Size(5, 9)  != Size(5, 10)
    assert Size(4, 10) != Size(5, 10)
    assert not (Size(5, 10) != Size(5, 10))
    assert Size(6, 10) != Size(5, 10)
    assert Size(5, 11) != Size(5, 10)
    assert Size(6, 11) != Size(5, 10)

    assert not (Size(4, 9)  > Size(5, 10))
    assert not (Size(5, 9)  > Size(5, 10))
    assert not (Size(4, 10) > Size(5, 10))
    assert not (Size(5, 10) > Size(5, 10))
    assert not Size(6, 10) > Size(5, 10)
    assert not Size(5, 11) > Size(5, 10)
    assert Size(6, 11) > Size(5, 10)

    assert Size(4, 9) < Size(5, 10)
    assert not Size(5, 9)  < Size(5, 10)
    assert not Size(4, 10) < Size(5, 10)
    assert not (Size(5, 10) < Size(5, 10))
    assert not (Size(6, 10) < Size(5, 10))
    assert not (Size(5, 11) < Size(5, 10))
    assert not (Size(6, 11) < Size(5, 10))

    assert not (Size(4, 9)  >= Size(5, 10))
    assert not (Size(5, 9)  >= Size(5, 10))
    assert not (Size(4, 10) >= Size(5, 10))
    assert Size(5, 10) >= Size(5, 10)
    assert Size(6, 10) >= Size(5, 10)
    assert Size(5, 11) >= Size(5, 10)
    assert Size(6, 11) >= Size(5, 10)

    assert Size(4, 9)  <= Size(5, 10)
    assert Size(5, 9)  <= Size(5, 10)
    assert Size(4, 10) <= Size(5, 10)
    assert Size(5, 10) <= Size(5, 10)
    assert not (Size(6, 10) <= Size(5, 10))
    assert not (Size(5, 11) <= Size(5, 10))
    assert not (Size(6, 11) <= Size(5, 10))

    ### arithmetic ###

    assert Size(10, 20) + Size(7, 3) == Size(17, 23)
    assert Size(10, 20) - Size(7, 3) == Size(3, 17)
    assert Size(10, 20) * Size(7, 3) == Size(70, 60)
    assert Size(10, 20) / Size(2, 5) == Size(5, 4)
    assert Size(10, 20) / Size(4, 8) == Size(2.5, 2.5)
    assert Size(10, 20) // Size(4, 8) == Size(2, 2)
    assert Size(10.9, 20.9) // Size(2, 5) == Size(5, 4)

    size = Size(10, 20)
    size += Size(7, 3)
    assert size == Size(17, 23)

    size = Size(10, 20)
    size -= Size(7, 3)
    assert size == Size(3, 17)

    size = Size(10, 20)
    size *= Size(7, 3)
    assert size == Size(70, 60)

    size = Size(10, 20)
    size /= Size(2, 5)
    assert size == Size(5, 4)

    size = Size(10, 20)
    size //= Size(4, 8)
    assert size == Size(2, 2)

    assert Size(10, 20) + 5 == Size(15, 25)
    assert Size(10, 20) - 4 == Size(6, 16)
    assert Size(10, 20) * 5 == Size(50, 100)
    assert Size(10, 20) / 5 == Size(2, 4)
    assert Size(10, 20) / 4 == Size(2.5, 5)
    assert Size(10, 20) // 4 == Size(2, 5)
    assert Size(10.9, 20.9) // 5 == Size(2, 4)

    size = Size(10, 20)
    size += 5
    assert size == Size(15, 25)

    size = Size(10, 20)
    size -= 4
    assert size == Size(6, 16)

    size = Size(10, 20)
    size *= 5
    assert size == Size(50, 100)

    size = Size(10, 20)
    size /= 4
    assert size == Size(2.5, 5)

    size = Size(10, 20)
    size //= 4
    assert size == Size(2, 5)

    ### operations ###

    t = Size(5, 6).to_tuple()
    assert type(t[0]) == int
    assert type(t[1]) == int
    assert t == (5, 6)

    t = Size(5.0, 6).to_tuple()
    assert type(t[0]) == float
    assert type(t[1]) == int
    assert t == (5.0, 6)

    t = Size(5, 6.0).to_tuple()
    assert type(t[0]) == int
    assert type(t[1]) == float
    assert t == (5, 6.0)

    t = Size(5, 6).to_tuple_f()
    assert type(t[0]) == float
    assert type(t[1]) == float
    assert t == (5.0, 6.0)

    t = Size(5.1, 6.1).to_tuple_i()
    assert type(t[0]) == int
    assert type(t[1]) == int
    assert t == (5, 6)

    assert Size(0, 0).is_zero()
    assert not Size(1, 0).is_zero()
    assert not Size(0, 2).is_zero()
    assert not Size(1, 2).is_zero()

    ### auto conversion ###

    assert str(Size(1, 2)) == "1 2"
    assert tuple(Size(1, 2)) == (1, 2)

def run():
    print("test_size start")
    test_size()
    print("test_size end")

if __name__ == "__main__":
   run()