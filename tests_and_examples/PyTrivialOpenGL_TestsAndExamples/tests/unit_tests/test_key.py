def test_key_id():
    from PyTrivialOpenGL.Key import KeyId

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
    from PyTrivialOpenGL.Key                    import KeyId
    from PyTrivialOpenGL._Private.KeySupport    import vk_code_to_key_id
    from PyTrivialOpenGL._Private.C_WinApi      import VK_F1

    assert vk_code_to_key_id(VK_F1) == KeyId.F1
    assert vk_code_to_key_id(-1) == KeyId.UNKNOWN

def test_key_id_to_vk_code():
    from PyTrivialOpenGL.Key                    import KeyId
    from PyTrivialOpenGL._Private.KeySupport    import key_id_to_vk_code
    from PyTrivialOpenGL._Private.C_WinApi      import VK_F1

    assert key_id_to_vk_code(KeyId.F1) == VK_F1
    assert key_id_to_vk_code(KeyId.UNKNOWN) == 0