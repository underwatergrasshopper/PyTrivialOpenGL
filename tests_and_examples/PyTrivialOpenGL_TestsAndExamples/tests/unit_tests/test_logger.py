import pytest
import sys
import os
import shutil

from PyTrivialOpenGL.Logger import *

__all__ = [
    "run"
]

output_folder_path = "log/tests/logger"

def gen_test_output(test_file_name, test_flag, output_file_name):
    content = ""

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    os.system("python tests/unittests/" + test_file_name + " " + test_flag + " > " + output_folder_path + "/" + output_file_name)

    with open(output_folder_path + "/" + output_file_name) as file:
        content = file.read()

    return content

def gen_output(test_flag):
    test_file_name  = "test_logger.py"
 
    test_file_name_no_ext   = test_file_name.split(".")[0]
    output_file_name        = test_file_name_no_ext + "_" +  test_flag + ".txt"

    return gen_test_output(test_file_name, test_flag, output_file_name)

def test_logger_log_level():
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


def test_logger_log_message():

    ### log ###

    content = gen_output("log_message_level_default")
    expected_content = (
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = gen_output("log_message_level_debug")
    expected_content = (
        "(TOGL) Debug: Some debug message.\n"
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = gen_output("log_message_level_info")
    expected_content = (
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = gen_output("log_message_level_warning")
    expected_content = (
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = gen_output("log_message_level_error")
    expected_content = (
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    ### log direct ###

    content = gen_output("log_message_direct_level_default")
    expected_content = (
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = gen_output("log_message_direct_level_debug")
    expected_content = (
        "(TOGL) Debug: Some debug message.\n"
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = gen_output("log_message_direct_level_info")
    expected_content = (
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = gen_output("log_message_direct_level_warning")
    expected_content = (
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = gen_output("log_message_direct_level_error")
    expected_content = (
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content


def test_logger_custom_log_message():

    content = gen_output("log_message_custom")
    expected_content = (
        "(TOGL) Debug: --Some debug message.\n"
        "(TOGL) Info: --Some info message.\n"
        "(TOGL) Warning: --Some warning message.\n"
        "(TOGL) Error: --Some error message.\n"
        "(TOGL) Fatal Error: --Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = gen_output("log_message_direct_custom")
    expected_content = (
        "(TOGL) Debug: --Some debug message.\n"
        "(TOGL) Info: --Some info message.\n"
        "(TOGL) Warning: --Some warning message.\n"
        "(TOGL) Error: --Some error message.\n"
        "(TOGL) Fatal Error: --Some fatal error message.\n"
    )
    assert content == expected_content, content

def run():
    if os.path.exists(output_folder_path):
        shutil.rmtree(output_folder_path)

    print("test_logger start")
    test_logger_log_level()
    test_logger_log_message()
    test_logger_custom_log_message()
    print("test_logger end")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        flag = sys.argv[1].lower()

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
    else:
        run()