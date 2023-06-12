import pytest
import sys
import os

from PyTrivialOpenGL.Logger import *

__all__ = [
    "run"
]

def gen_test_output(test_file_name, test_flag, output_file_name):
    content = ""

    output_folder_path = "log/tests"

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

def test_logger():
    ### log ###

    content = gen_output("log_default")
    expected_content = (
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = gen_output("log_all_messages")
    expected_content = (
        "(TOGL) Debug: Some debug message.\n"
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = gen_output("log_all_messages_except_debug")
    expected_content = (
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = gen_output("log_only_error")
    expected_content = (
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    ### log raw ###

    content = gen_output("log_default_raw")
    expected_content = (
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = gen_output("log_all_messages_raw")
    expected_content = (
        "(TOGL) Debug: Some debug message.\n"
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = gen_output("log_all_messages_except_debug_raw")
    expected_content = (
        "(TOGL) Info: Some info message.\n"
        "(TOGL) Warning: Some warning message.\n"
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

    content = gen_output("log_only_error_raw")
    expected_content = (
        "(TOGL) Error: Some error message.\n"
        "(TOGL) Fatal Error: Some fatal error message.\n"
    )
    assert content == expected_content, content

def run():
    print("test_logger start")
    test_logger()
    print("test_logger end")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        flag = sys.argv[1].lower()

        if flag == "log_default":
            logger = Logger()
            logger.log_debug("Some debug message.")
            logger.log_info("Some info message.")
            logger.log_warning("Some warning message.")
            logger.log_error("Some error message.")
            logger.log_fatal_error("Some fatal error message.")
            logger.log_info("This message should not be logged.")

        elif flag == "log_all_messages":
            logger = Logger()
            logger.set_log_level(LogLevel.DEBUG)
            logger.log_debug("Some debug message.")
            logger.log_info("Some info message.")
            logger.log_warning("Some warning message.")
            logger.log_error("Some error message.")
            logger.log_fatal_error("Some fatal error message.")
            logger.log_info("This message should not be logged.")

        elif flag == "log_all_messages_except_debug":
            logger = Logger()
            logger.set_log_level(LogLevel.INFO)
            logger.log_debug("Some debug message.")
            logger.log_info("Some info message.")
            logger.log_warning("Some warning message.")
            logger.log_error("Some error message.")
            logger.log_fatal_error("Some fatal error message.")
            logger.log_info("This message should not be logged.")

        elif flag == "log_only_error":
            logger = Logger()
            logger.set_log_level(LogLevel.ERROR)
            logger.log_debug("Some debug message.")
            logger.log_info("Some info message.")
            logger.log_warning("Some warning message.")
            logger.log_error("Some error message.")
            logger.log_fatal_error("Some fatal error message.")
            logger.log_info("This message should not be logged.")

        elif flag == "log_default_raw":
            logger = Logger()
            logger.log_message(LogMessageTypeId.DEBUG, "Some debug message.")
            logger.log_message(LogMessageTypeId.INFO, "Some info message.")
            logger.log_message(LogMessageTypeId.WARNING, "Some warning message.")
            logger.log_message(LogMessageTypeId.ERROR, "Some error message.")
            logger.log_message(LogMessageTypeId.FATAL_ERROR, "Some fatal error message.")
            logger.log_message(LogMessageTypeId.INFO, "This message should not be logged.")

        elif flag == "log_all_messages_raw":
            logger = Logger()
            logger.set_log_level(LogLevel.DEBUG)
            logger.log_message(LogMessageTypeId.DEBUG, "Some debug message.")
            logger.log_message(LogMessageTypeId.INFO, "Some info message.")
            logger.log_message(LogMessageTypeId.WARNING, "Some warning message.")
            logger.log_message(LogMessageTypeId.ERROR, "Some error message.")
            logger.log_message(LogMessageTypeId.FATAL_ERROR, "Some fatal error message.")
            logger.log_message(LogMessageTypeId.INFO, "This message should not be logged.")

        elif flag == "log_all_messages_except_debug_raw":
            logger = Logger()
            logger.set_log_level(LogLevel.INFO)
            logger.log_message(LogMessageTypeId.DEBUG, "Some debug message.")
            logger.log_message(LogMessageTypeId.INFO, "Some info message.")
            logger.log_message(LogMessageTypeId.WARNING, "Some warning message.")
            logger.log_message(LogMessageTypeId.ERROR, "Some error message.")
            logger.log_message(LogMessageTypeId.FATAL_ERROR, "Some fatal error message.")
            logger.log_message(LogMessageTypeId.INFO, "This message should not be logged.")

        elif flag == "log_only_error_raw":
            logger = Logger()
            logger.set_log_level(LogLevel.ERROR)
            logger.log_message(LogMessageTypeId.DEBUG, "Some debug message.")
            logger.log_message(LogMessageTypeId.INFO, "Some info message.")
            logger.log_message(LogMessageTypeId.WARNING, "Some warning message.")
            logger.log_message(LogMessageTypeId.ERROR, "Some error message.")
            logger.log_message(LogMessageTypeId.FATAL_ERROR, "Some fatal error message.")
            logger.log_message(LogMessageTypeId.INFO, "This message should not be logged.")

    else:
        run()