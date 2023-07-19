import pytest
import math

from PyTrivialOpenGL.Window import *

__all__ = [
    "run"
]

def test_window_singleton():
    try:
        window = Window()
    except RuntimeError as exception:
        assert str(exception) == "Can not create more than one instance of singleton class 'Window'."
    else:
        assert False, "Should throw an exception."


def run():
    print("test_window start")
    test_window_singleton()
    print("test_window end")

if __name__ == "__main__":
   run()