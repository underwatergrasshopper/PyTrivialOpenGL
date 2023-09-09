def test_window_singleton():
    from PyTrivialOpenGL.Window import Window

    try:
        window = Window()
    except RuntimeError as exception:
        assert str(exception) == "Can not create more than one instance of singleton class 'Window'."
    else:
        assert False, "Should throw an exception."
