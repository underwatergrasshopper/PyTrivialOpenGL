import pytest
import math

from PyTrivialOpenGL.Color import *

def test_ColorB():
    ### constructor ###

    color = ColorB(0, 0, 0, 0)
    assert(color.r == 0)
    assert(color.g == 0)
    assert(color.b == 0)
    assert(color.a == 0)

    color = ColorB(0, 0, 0)
    assert(color.r == 0)
    assert(color.g == 0)
    assert(color.b == 0)
    assert(color.a == 255)

    color = ColorB(11, 22, 33, 44)
    assert(color.r == 11)
    assert(color.g == 22)
    assert(color.b == 33)
    assert(color.a == 44)

    color = ColorB(11, 300, 33, 44, is_clamp = True)
    assert(color.r == 11)
    assert(color.g == 255)
    assert(color.b == 33)
    assert(color.a == 44)

    color = ColorB(-1, 300, 400, 500, is_clamp = True)
    assert(color.r == 0)
    assert(color.g == 255)
    assert(color.b == 255)
    assert(color.a == 255)

    ### access ###

    color = ColorB(11, 22, 33, 44)
    assert(color.rgba() == (11, 22, 33, 44))

    ### assign ###

    color.r = 0
    assert(color.r == 0)

    color.r = 255
    assert(color.r == 255)

    ### conversion ###

    color = ColorB(11, 22, 33, 44).to_color_b()
    assert(color.r == 11)
    assert(color.g == 22)
    assert(color.b == 33)
    assert(color.a == 44)

    color = ColorB(255, 255, 255, 255).to_color_f()
    assert(math.isclose(color.r, 1.0, rel_tol = 0.0001))
    assert(math.isclose(color.g, 1.0, rel_tol = 0.0001))
    assert(math.isclose(color.b, 1.0, rel_tol = 0.0001))
    assert(math.isclose(color.a, 1.0, rel_tol = 0.0001))

    color = ColorB(127, 127, 127, 127).to_color_f()
    assert(math.isclose(color.r, 0.5, rel_tol = 0.01))
    assert(math.isclose(color.g, 0.5, rel_tol = 0.01))
    assert(math.isclose(color.b, 0.5, rel_tol = 0.01))
    assert(math.isclose(color.a, 0.5, rel_tol = 0.01))

    color = ColorB(0, 0, 0, 0).to_color_f()
    assert(math.isclose(color.r, 0, rel_tol = 0.0001))
    assert(math.isclose(color.g, 0, rel_tol = 0.0001))
    assert(math.isclose(color.b, 0, rel_tol = 0.0001))
    assert(math.isclose(color.a, 0, rel_tol = 0.0001))

    color = ColorB(0, 63, 127, 255).to_color_f()
    assert(math.isclose(color.r, 0.0, rel_tol = 0.0001))
    assert(math.isclose(color.g, 0.25, rel_tol = 0.1))
    assert(math.isclose(color.b, 0.5, rel_tol = 0.01))
    assert(math.isclose(color.a, 1.0, rel_tol = 0.0001))

    ### wrong value type ###

    try:
        color = ColorB(11, 22, "text", 44)
    except Exception as e:
        assert(str(e) == "Value of 'b' can not be converted to int.")
    else:
        assert False, "Should throw exception."

    color = ColorB(11, 22, 33, 44)
    try:
        color.b = "text"
    except Exception as e:
        assert(str(e) == "Value of 'b' can not be converted to int.")
    else:
        assert False, "Should throw exception."

    ### wrong value range ###

    try:
        color = ColorB(11, 22, 330, 44)
    except Exception as e:
        assert(str(e) == "Value of 'b' is out of acceptable range 0..255.")
    else:
        assert False, "Should throw exception."
        
    color = ColorB(11, 22, 33, 44)
    try:
        color.b = 256
    except Exception as e:
        assert(str(e) == "Value of 'b' is out of acceptable range 0..255.")
    else:
        assert False, "Should throw exception."

    color = ColorB(11, 22, 33, 44)
    try:
        color.b = -1
    except Exception as e:
        assert(str(e) == "Value of 'b' is out of acceptable range 0..255.")
    else:
        assert False, "Should throw exception."

    ### abstract check ###

    try:
        color = Color()
    except NotImplementedError as e:
        assert str(e) == "Can not create object of abstract class 'Color'."
    else:
        assert False, "Should throw exception."

    ### type check ###

    color_b = ColorB(255, 255, 255)
    assert isinstance(color_b, Color)
    assert isinstance(color_b, ColorB)
    assert not isinstance(color_b, ColorF)


def test_ColorF():
    ### constructor ###

    color = ColorF(0, 0, 0, 0)
    assert(color.r == 0)
    assert(color.g == 0)
    assert(color.b == 0)
    assert(color.a == 0)

    color = ColorF(0, 0, 0)
    assert(color.r == 0)
    assert(color.g == 0)
    assert(color.b == 0)
    assert(color.a == 1)

    color = ColorF(0.1, 0.2, 0.3, 0.4)
    assert(color.r == 0.1)
    assert(color.g == 0.2)
    assert(color.b == 0.3)
    assert(color.a == 0.4)

    color = ColorF(0.1, 1.2, 0.3, 0.4, is_clamp = True)
    assert(color.r == 0.1)
    assert(color.g == 1.0)
    assert(color.b == 0.3)
    assert(color.a == 0.4)

    color = ColorF(-0.1, 1.2, -0.3, 1.4, is_clamp = True)
    assert(color.r == 0.0)
    assert(color.g == 1.0)
    assert(color.b == 0.0)
    assert(color.a == 1.0)

    ### access ###

    color = ColorF(0.1, 0.2, 0.3, 0.4)
    assert(color.rgba() == (0.1, 0.2, 0.3, 0.4))

    ### assign ###

    color.r = 0
    assert(color.r == 0)

    color.r = 1
    assert(color.r == 1)

    ### conversion ###

    color = ColorF(0.1, 0.2, 0.3, 0.4).to_color_f()
    assert(color.r == 0.1)
    assert(color.g == 0.2)
    assert(color.b == 0.3)
    assert(color.a == 0.4)

    color = ColorF(1, 1, 1, 1).to_color_b()
    assert(color.r == 255)
    assert(color.g == 255)
    assert(color.b == 255)
    assert(color.a == 255)

    color = ColorF(0.5, 0.5, 0.5, 0.5).to_color_b()
    assert(color.r == 127)
    assert(color.g == 127)
    assert(color.b == 127)
    assert(color.a == 127)

    color = ColorF(0, 0, 0, 0).to_color_b()
    assert(color.r == 0)
    assert(color.g == 0)
    assert(color.b == 0)
    assert(color.a == 0)

    color = ColorF(0, 0.25, 0.5, 1).to_color_b()
    assert(color.r == 0)
    assert(color.g == 63)
    assert(color.b == 127)
    assert(color.a == 255)

    ### wrong value type ###

    try:
        color = ColorF(0.1, 0.2, "text", 0.3)
    except Exception as e:
        assert(str(e) == "Value of 'b' can not be converted to float.")
    else:
        assert False, "Should throw exception."

    color = ColorF(0.1, 0.2, 0.3, 0.4)
    try:
        color.b = "text"
    except Exception as e:
        assert(str(e) == "Value of 'b' can not be converted to float.")
    else:
        assert False, "Should throw exception."

    ### wrong value range ###

    try:
        color = ColorF(0.1, 0.2, 1.1, 0.4)
    except Exception as e:
        assert(str(e) == "Value of 'b' is out of acceptable range 0..1.")
    else:
        assert False, "Should throw exception."
        
    color = ColorF(0.1, 0.2, 0.3, 0.4)
    try:
        color.b = 1.1
    except Exception as e:
        assert(str(e) == "Value of 'b' is out of acceptable range 0..1.")
    else:
        assert False, "Should throw exception."

    color = ColorF(0.1, 0.2, 0.3, 0.4)
    try:
        color.b = -0.1
    except Exception as e:
        assert(str(e) == "Value of 'b' is out of acceptable range 0..1.")
    else:
        assert False, "Should throw exception."

    ### type check ###

    color_f = ColorF(1, 1, 1)
    assert isinstance(color_f, Color)
    assert not isinstance(color_f, ColorB)
    assert isinstance(color_f, ColorF)

if __name__ == "__main__":
    print("test_color start")
    test_ColorB()
    test_ColorF()
    print("test_color end")