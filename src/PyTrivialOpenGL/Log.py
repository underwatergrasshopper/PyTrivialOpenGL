# This module and modules imported below are logically part of one module.
from .Logger import *

### inner (do not use) ###

_logger = Logger()

### access to global logger ###

def to_logger():
    """
    Returns     : Logger 
        Reference to global logger instance.
    """
    return _logger

### log message ###

def log_debug(message):
    """
    message : str | Any
    """
    if not isinstance(message, str):
        try:
            message = str(message)
        except Exception as exception:
            raise ValueError("Value of 'message' is not convertible to str.") from exception

    _logger.log_debug(message)

def log_info(message):
    """
    message : str | Any
    """
    if not isinstance(message, str):
        try:
            message = str(message)
        except Exception as exception:
            raise ValueError("Value of 'message' is not convertible to str.") from exception

    _logger.log_info(message)

def log_warning(message):
    """
    message : str | Any
    """
    if not isinstance(message, str):
        try:
            message = str(message)
        except Exception as exception:
            raise ValueError("Value of 'message' is not convertible to str.") from exception

    _logger.log_warning(message)

def log_error(message):
    """
    message : str | Any
    """
    if not isinstance(message, str):
        try:
            message = str(message)
        except Exception as exception:
            raise ValueError("Value of 'message' is not convertible to str.") from exception

    _logger.log_error(message)

def log_fatal_error(message):
    """
    message : str | Any
    """
    if not isinstance(message, str):
        try:
            message = str(message)
        except Exception as exception:
            raise ValueError("Value of 'message' is not convertible to str.") from exception

    _logger.log_fatal_error(message)

### log level ###

def set_log_level(log_level):
    """
    log_level : int | SupportsInt
        Might be: LogLevel.DEBUG, LogLevel.INFO, LogLevel.WARNING or LogLevel.ERROR.
        For:
            LogLevel.DEBUG      - logs debug, info, warning and error messages,
            LogLevel.INFO       - logs info, warning and error messages,
            LogLevel.WARNING    - logs warning and error messages,
            LogLevel.ERROR      - logs error messages only.
    """
    if not isinstance(log_level, int):
        try:
            log_level = int(log_level)
        except Exception as exception:
            raise ValueError("Value of 'log_level' is not convertible to int.") from exception

    _logger.set_log_level(log_level)

def get_log_level():
    """
    Returns     : int
    """
    return _logger.get_log_level()

def is_log_level_at_least(log_level):
    """
    log_level   : int | SupportsInt
    """
    if not isinstance(log_level, int):
        try:
            log_level = int(log_level)
        except Exception as exception:
            raise ValueError("Value of 'log_level' is not convertible to int.") from exception

    return _logger.is_log_level_at_least(log_level)

### custom log ###

def set_log_message_to_output(log_message_to_output):
    """
    Replaces default function which displays log message with custom one (by default it's defautl_log_message_to_output).
    log_message_to_output : Callable[[int, str, str], None]      
        Is called when any log_{...} method is called as log_message_to_output(log_message_type_id, prefix, message).
        Where:
            log_message_type_id   - LogMessageTypeId.DEBUG, LogMessageTypeId.INFO, LogMessageTypeId.WARNING
                                    LogMessageTypeId.ERROR or LogMessageTypeId.FATAL_ERROR.
            prefix                - Log message prefix. Contains default text information about log message type.
                                    For example: "Error: " for error messages.
            message               - Log message.
    """
    if not callable(log_message_to_output):
        raise TypeError("Object assigned to 'log_message_to_output' is not callable.")

    _logger.set_log_message_to_output(log_message_to_output)