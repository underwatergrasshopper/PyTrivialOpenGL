from .Logger import Logger, LogLevel, LogMessageTypeId, defautl_log_message_to_output
from .Logger import __all__ as _logger_module__all__

__all__ = [
    "to_logger",

    "log_debug",
    "log_info",
    "log_warning",
    "log_error",
    "log_fatal_error",

    "set_log_level",
    "get_log_level",
    "is_log_level_at_least",

    "set_log_message_to_output",

    *_logger_module__all__
]

### inner (do not use) ###

_logger = Logger()

### access to global logger ###

def to_logger():
    """
    Returns (Logger) reference to global logger instance.
    """
    return _logger

### log message ###

def log_debug(message):
    """
    message : str
    """
    _logger.log_debug(message)

def log_info(message):
    """
    message : str
    """
    _logger.log_info(message)

def log_warning(message):
    """
    message : str
    """
    _logger.log_warning(message)

def log_error(message):
    """
    message : str
    """
    _logger.log_error(message)

def log_fatal_error(message):
    """
    message : str
    """
    _logger.log_fatal_error(message)

### log level ###

def set_log_level(log_level):
    """
    log_level : int
        Might be: LogLevel.DEBUG, LogLevel.INFO, LogLevel.WARNING or LogLevel.ERROR.
    """
    _logger.set_log_level(log_level)

def get_log_level():
    """
    Returns (int).
    """
    return _logger.get_log_level()

def is_log_level_at_least(log_level):
    """
    log_level : int
    """
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
    _logger.set_log_message_to_output(log_message_to_output)