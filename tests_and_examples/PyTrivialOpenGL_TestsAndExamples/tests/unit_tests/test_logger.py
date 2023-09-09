
import os as _os
import sys as _sys

def _get_output(output_path, test_flag):
    test_file_name_no_ext = _os.path.basename(__file__).split(".")[0]
    output_full_file_name = str(output_path) + "/" + test_file_name_no_ext + "_" +  test_flag + ".txt"

    if not _os.path.exists(output_path):
        _os.makedirs(output_path)

    prefix = ""
    for entry in _sys.path:
        prefix += entry + _os.pathsep

    is_64 = _sys.maxsize > 2**32
    platform = "64" if is_64 else "32"
    major = _sys.version_info.major
    minor = _sys.version_info.minor

    _os.system(f"set PYTHONPATH={prefix}%PYTHONPATH% & py -{major}.{minor}-{platform} {__file__ } {test_flag} > {output_full_file_name}")

    with open(output_full_file_name) as file:
        content = file.read()

    return content

def test_logger_log_level():
    from PyTrivialOpenGL.Logger import Logger, LogLevel

    logger = Logger()
    assert logger.get_log_level() == LogLevel.INFO

    ###

    logger.set_log_level(LogLevel.DEBUG)
    assert logger.get_log_level() == LogLevel.DEBUG

    assert logger.is_log_level_at_least(LogLevel.DEBUG)
    assert logger.is_log_level_at_least(LogLevel.INFO)
    assert logger.is_log_level_at_least(LogLevel.WARNING)
    assert logger.is_log_level_at_least(LogLevel.ERROR)

    ###

    logger.set_log_level(LogLevel.INFO)
    assert logger.get_log_level() == LogLevel.INFO

    assert not logger.is_log_level_at_least(LogLevel.DEBUG)
    assert logger.is_log_level_at_least(LogLevel.INFO)
    assert logger.is_log_level_at_least(LogLevel.WARNING)
    assert logger.is_log_level_at_least(LogLevel.ERROR)

    ###

    logger.set_log_level(LogLevel.WARNING)
    assert logger.get_log_level() == LogLevel.WARNING

    assert not logger.is_log_level_at_least(LogLevel.DEBUG)
    assert not logger.is_log_level_at_least(LogLevel.INFO)
    assert logger.is_log_level_at_least(LogLevel.WARNING)
    assert logger.is_log_level_at_least(LogLevel.ERROR)

    ###

    logger.set_log_level(LogLevel.ERROR)
    assert logger.get_log_level() == LogLevel.ERROR

    assert not logger.is_log_level_at_least(LogLevel.DEBUG)
    assert not logger.is_log_level_at_least(LogLevel.INFO)
    assert not logger.is_log_level_at_least(LogLevel.WARNING)
    assert logger.is_log_level_at_least(LogLevel.ERROR)


def test_logger_log_message(tmpdir):
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

    ### log direct ###

    content = _get_output(tmpdir, "log_message_direct_level_default")
    expected_content = (
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = _get_output(tmpdir, "log_message_direct_level_debug")
    expected_content = (
        "(TOGL) Debug: Some debug message.\n"
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = _get_output(tmpdir, "log_message_direct_level_info")
    expected_content = (
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = _get_output(tmpdir, "log_message_direct_level_warning")
    expected_content = (
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = _get_output(tmpdir, "log_message_direct_level_error")
    expected_content = (
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content


def test_logger_custom_log_message(tmpdir):

    content = _get_output(tmpdir, "log_message_custom")
    expected_content = (
        "(TOGL) Debug: --Some debug message.\n"
        "(TOGL) Info: --Some info message.\n"
        "(TOGL) Warning: --Some warning message.\n"
        "(TOGL) Error: --Some error message.\n"
        "(TOGL) Fatal Error: --Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = _get_output(tmpdir, "log_message_direct_custom")
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
    flag : str
    """
    from PyTrivialOpenGL.Logger import Logger, LogLevel, LogMessageTypeId

    if flag == "log_message_level_default":
        logger = Logger()
        logger.log_debug("Some debug message.")
        logger.log_info("Some info message.")
        logger.log_warning("Some warning message.")
        logger.log_error("Some error message.")
        logger.log_fatal_error("Some fatal error message.")
        logger.log_info("This message should not be logged.")

    elif flag == "log_message_level_debug":
        logger = Logger()
        logger.set_log_level(LogLevel.DEBUG)
        logger.log_debug("Some debug message.")
        logger.log_info("Some info message.")
        logger.log_warning("Some warning message.")
        logger.log_error("Some error message.")
        logger.log_fatal_error("Some fatal error message.")
        logger.log_info("This message should not be logged.")

    elif flag == "log_message_level_info":
        logger = Logger()
        logger.set_log_level(LogLevel.INFO)
        logger.log_debug("Some debug message.")
        logger.log_info("Some info message.")
        logger.log_warning("Some warning message.")
        logger.log_error("Some error message.")
        logger.log_fatal_error("Some fatal error message.")
        logger.log_info("This message should not be logged.")

    elif flag == "log_message_level_warning":
        logger = Logger()
        logger.set_log_level(LogLevel.WARNING)
        logger.log_debug("Some debug message.")
        logger.log_info("Some info message.")
        logger.log_warning("Some warning message.")
        logger.log_error("Some error message.")
        logger.log_fatal_error("Some fatal error message.")
        logger.log_info("This message should not be logged.")

    elif flag == "log_message_level_error":
        logger = Logger()
        logger.set_log_level(LogLevel.ERROR)
        logger.log_debug("Some debug message.")
        logger.log_info("Some info message.")
        logger.log_warning("Some warning message.")
        logger.log_error("Some error message.")
        logger.log_fatal_error("Some fatal error message.")
        logger.log_info("This message should not be logged.")

    elif flag == "log_message_direct_level_default":
        logger = Logger()
        logger.log_message(LogMessageTypeId.DEBUG, "Some debug message.")
        logger.log_message(LogMessageTypeId.INFO, "Some info message.")
        logger.log_message(LogMessageTypeId.WARNING, "Some warning message.")
        logger.log_message(LogMessageTypeId.ERROR, "Some error message.")
        logger.log_message(LogMessageTypeId.FATAL_ERROR, "Some fatal error message.")
        logger.log_message(LogMessageTypeId.ERROR, "This message should not be logged.")

    elif flag == "log_message_direct_level_debug":
        logger = Logger()
        logger.set_log_level(LogLevel.DEBUG)
        logger.log_message(LogMessageTypeId.DEBUG, "Some debug message.")
        logger.log_message(LogMessageTypeId.INFO, "Some info message.")
        logger.log_message(LogMessageTypeId.WARNING, "Some warning message.")
        logger.log_message(LogMessageTypeId.ERROR, "Some error message.")
        logger.log_message(LogMessageTypeId.FATAL_ERROR, "Some fatal error message.")
        logger.log_message(LogMessageTypeId.ERROR, "This message should not be logged.")

    elif flag == "log_message_direct_level_info":
        logger = Logger()
        logger.set_log_level(LogLevel.INFO)
        logger.log_message(LogMessageTypeId.DEBUG, "Some debug message.")
        logger.log_message(LogMessageTypeId.INFO, "Some info message.")
        logger.log_message(LogMessageTypeId.WARNING, "Some warning message.")
        logger.log_message(LogMessageTypeId.ERROR, "Some error message.")
        logger.log_message(LogMessageTypeId.FATAL_ERROR, "Some fatal error message.")
        logger.log_message(LogMessageTypeId.ERROR, "This message should not be logged.")

    elif flag == "log_message_direct_level_warning":
        logger = Logger()
        logger.set_log_level(LogLevel.WARNING)
        logger.log_message(LogMessageTypeId.DEBUG, "Some debug message.")
        logger.log_message(LogMessageTypeId.INFO, "Some info message.")
        logger.log_message(LogMessageTypeId.WARNING, "Some warning message.")
        logger.log_message(LogMessageTypeId.ERROR, "Some error message.")
        logger.log_message(LogMessageTypeId.FATAL_ERROR, "Some fatal error message.")
        logger.log_message(LogMessageTypeId.ERROR, "This message should not be logged.")

    elif flag == "log_message_direct_level_error":
        logger = Logger()
        logger.set_log_level(LogLevel.ERROR)
        logger.log_message(LogMessageTypeId.DEBUG, "Some debug message.")
        logger.log_message(LogMessageTypeId.INFO, "Some info message.")
        logger.log_message(LogMessageTypeId.WARNING, "Some warning message.")
        logger.log_message(LogMessageTypeId.ERROR, "Some error message.")
        logger.log_message(LogMessageTypeId.FATAL_ERROR, "Some fatal error message.")
        logger.log_message(LogMessageTypeId.ERROR, "This message should not be logged.")

    elif flag == "log_message_custom":
        logger = Logger()

        def log_message_to_output(log_message_type_id, prefix, message):
            print("%s--%s" % (prefix, message))

        logger.set_log_message_to_output(log_message_to_output)

        logger.set_log_level(LogLevel.DEBUG)
        logger.log_debug("Some debug message.")
        logger.log_info("Some info message.")
        logger.log_warning("Some warning message.")
        logger.log_error("Some error message.")
        logger.log_fatal_error("Some fatal error message.")
        logger.log_info("This message should not be logged.")


    elif flag == "log_message_direct_custom":
        logger = Logger()

        def log_message_to_output(log_message_type_id, prefix, message):
            print("%s--%s" % (prefix, message))

        logger.set_log_message_to_output(log_message_to_output)

        logger.set_log_level(LogLevel.DEBUG)
        logger.log_message(LogMessageTypeId.DEBUG, "Some debug message.")
        logger.log_message(LogMessageTypeId.INFO, "Some info message.")
        logger.log_message(LogMessageTypeId.WARNING, "Some warning message.")
        logger.log_message(LogMessageTypeId.ERROR, "Some error message.")
        logger.log_message(LogMessageTypeId.FATAL_ERROR, "Some fatal error message.")
        logger.log_message(LogMessageTypeId.ERROR, "This message should not be logged.")

def _main(argv):
    """
    argv : list[str]
    """
    if len(argv) > 1:
        flag = argv[1].lower()
        _run(flag)
        
if __name__ == "__main__":
    import sys as _sys
    _main(_sys.argv)


