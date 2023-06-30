import pytest
import math

from PyTrivialOpenGL.Key import *
from PyTrivialOpenGL.Key import _vk_code_to_key_id
from PyTrivialOpenGL.Key import _key_id_to_vk_code
from PyTrivialOpenGL._C_WinApi import *

__all__ = [
    "run"
]

def test_key_id():
    key_id = KeyId.V

    assert key_id == KeyId.V
    assert (key_id != KeyId.V) == False

    assert (key_id == KeyId.A) == False
    assert key_id != KeyId.A

    assert key_id == 'V'
    assert (key_id != 'V') == False

    assert (key_id == 'A') == False
    assert key_id != 'A'

def test_vk_code_to_key_id():
    assert _vk_code_to_key_id(VK_F1) == KeyId.F1
    assert _vk_code_to_key_id(-1) == KeyId.UNKNOWN

def test_key_id_to_vk_code():
    assert _key_id_to_vk_code(KeyId.F1) == VK_F1
    assert _key_id_to_vk_code(KeyId.UNKNOWN) == 0

def run():
    print("test_key start")
    test_key_id()
    test_vk_code_to_key_id()
    test_key_id_to_vk_code()
    print("test_key end")

if __name__ == "__main__":
   run()