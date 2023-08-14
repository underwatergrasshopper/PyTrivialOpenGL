import pytest
import sys
import os
import shutil

_path_to_src = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../../../../src")
sys.path.insert(0, _path_to_src)

from PyTrivialOpenGL.Log import *

__all__ = [
    "run"
]
_path_to_project = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/../../../..")

output_folder_path = _path_to_project + "/log/tests/log"

def gen_test_output(test_file_name, test_flag, output_file_name):
    content = ""

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    os.system("python " + _path_to_project + "/tests_and_examples/PyTrivialOpenGL_TestsAndExamples/tests/unit_tests/" + test_file_name + " " + test_flag + " > " + output_folder_path + "/" + output_file_name)

    with open(output_folder_path + "/" + output_file_name) as file:
        content = file.read()

    return content

def gen_output(test_flag):
    test_file_name  = "test_log.py"
 
    test_file_name_no_ext   = test_file_name.split(".")[0]
    output_file_name        = test_file_name_no_ext + "_" +  test_flag + ".txt"

    return gen_test_output(test_file_name, test_flag, output_file_name)

def test_log_log_level():

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


def test_log_log_message():

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


def test_log_custom_log_message():

    content = gen_output("log_message_custom")
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

    print("test_log start")
    test_log_log_level()
    test_log_log_message()
    test_log_custom_log_message()
    print("test_log end")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        flag = sys.argv[1].lower()

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

    else:
        run()