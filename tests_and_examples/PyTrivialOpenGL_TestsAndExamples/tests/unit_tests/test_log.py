import os as _os
import sys as _sys

def _get_output(output_path, test_flag):
    test_file_name_no_ext = _os.path.basename(__file__).split(".")[0]
    output_full_file_name = str(output_path) + "/" + test_file_name_no_ext + "_" +  test_flag + ".txt"

    if not _os.path.exists(output_path):
        _os.makedirs(output_path)

    prefix = ""
    for entry in _sys.path:
        if "PyTrivialOpenGL" in entry:
            prefix += entry + _os.pathsep

    is_64 = _sys.maxsize > 2**32
    platform = "64" if is_64 else "32"
    major = _sys.version_info.major
    minor = _sys.version_info.minor

    _os.system(f"set PYTHONPATH={prefix}%PYTHONPATH% & py -{major}.{minor}-{platform} {__file__ } {test_flag} > {output_full_file_name}")

    with open(output_full_file_name) as file:
        content = file.read()

    return content

def test_log_log_level():
    from PyTrivialOpenGL.Log import LogLevel, get_log_level, set_log_level, is_log_level_at_least

    assert get_log_level() == LogLevel.INFO

    ###

    set_log_level(LogLevel.DEBUG)
    assert get_log_level() == LogLevel.DEBUG

    assert is_log_level_at_least(LogLevel.DEBUG)
    assert is_log_level_at_least(LogLevel.INFO)
    assert is_log_level_at_least(LogLevel.WARNING)
    assert is_log_level_at_least(LogLevel.ERROR)

    ###

    set_log_level(LogLevel.INFO)
    assert get_log_level() == LogLevel.INFO

    assert not is_log_level_at_least(LogLevel.DEBUG)
    assert is_log_level_at_least(LogLevel.INFO)
    assert is_log_level_at_least(LogLevel.WARNING)
    assert is_log_level_at_least(LogLevel.ERROR)

    ###

    set_log_level(LogLevel.WARNING)
    assert get_log_level() == LogLevel.WARNING

    assert not is_log_level_at_least(LogLevel.DEBUG)
    assert not is_log_level_at_least(LogLevel.INFO)
    assert is_log_level_at_least(LogLevel.WARNING)
    assert is_log_level_at_least(LogLevel.ERROR)

    ###

    set_log_level(LogLevel.ERROR)
    assert get_log_level() == LogLevel.ERROR

    assert not is_log_level_at_least(LogLevel.DEBUG)
    assert not is_log_level_at_least(LogLevel.INFO)
    assert not is_log_level_at_least(LogLevel.WARNING)
    assert is_log_level_at_least(LogLevel.ERROR)


def test_log_log_message(tmpdir):
    ### log ###

    content = _get_output(tmpdir, "log_message_level_default")
    expected_content = (
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = _get_output(tmpdir, "log_message_level_debug")
    expected_content = (
        "(TOGL) Debug: Some debug message.\n"
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = _get_output(tmpdir, "log_message_level_info")
    expected_content = (
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = _get_output(tmpdir, "log_message_level_warning")
    expected_content = (
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = _get_output(tmpdir, "log_message_level_error")
    expected_content = (
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content


def test_log_custom_log_message(tmpdir):
    content = _get_output(tmpdir, "log_message_custom")
    expected_content = (
        "(TOGL) Debug: --Some debug message.\n"
        "(TOGL) Info: --Some info message.\n"
        "(TOGL) Warning: --Some warning message.\n"
        "(TOGL) Error: --Some error message.\n"
        "(TOGL) Fatal Error: --Some fatal error message.\n"
    )
    assert content == expected_content, content

def _run(flag):
    """
    flag : list[str]
    """
    from PyTrivialOpenGL.Log import (
        LogLevel, 
        set_log_level, 
        log_debug, log_info, log_warning, log_error, log_fatal_error, 
        set_log_message_to_output
    )

    if flag == "log_message_level_default":
        log_debug("Some debug message.")
        log_info("Some info message.")
        log_warning("Some warning message.")
        log_error("Some error message.")
        log_fatal_error("Some fatal error message.")
        log_info("This message should not be logged.")

    elif flag == "log_message_level_debug":
        set_log_level(LogLevel.DEBUG)
        log_debug("Some debug message.")
        log_info("Some info message.")
        log_warning("Some warning message.")
        log_error("Some error message.")
        log_fatal_error("Some fatal error message.")
        log_info("This message should not be logged.")

    elif flag == "log_message_level_info":
        set_log_level(LogLevel.INFO)
        log_debug("Some debug message.")
        log_info("Some info message.")
        log_warning("Some warning message.")
        log_error("Some error message.")
        log_fatal_error("Some fatal error message.")
        log_info("This message should not be logged.")

    elif flag == "log_message_level_warning":
        set_log_level(LogLevel.WARNING)
        log_debug("Some debug message.")
        log_info("Some info message.")
        log_warning("Some warning message.")
        log_error("Some error message.")
        log_fatal_error("Some fatal error message.")
        log_info("This message should not be logged.")

    elif flag == "log_message_level_error":
        set_log_level(LogLevel.ERROR)
        log_debug("Some debug message.")
        log_info("Some info message.")
        log_warning("Some warning message.")
        log_error("Some error message.")
        log_fatal_error("Some fatal error message.")
        log_info("This message should not be logged.")

    elif flag == "log_message_custom":
        def log_message_to_output(log_message_type_id, prefix, message):
            print("%s--%s" % (prefix, message))

        set_log_message_to_output(log_message_to_output)

        set_log_level(LogLevel.DEBUG)
        log_debug("Some debug message.")
        log_info("Some info message.")
        log_warning("Some warning message.")
        log_error("Some error message.")
        log_fatal_error("Some fatal error message.")
        log_info("This message should not be logged.")

def _main(argv):
    """
    flag : list[str]
    """
    if len(argv) > 1:
        flag = argv[1].lower()
        _run(flag)

if __name__ == "__main__":
    import sys as _sys
    _main(_sys.argv)