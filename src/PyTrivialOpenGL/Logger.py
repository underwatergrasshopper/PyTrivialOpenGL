import enum as _enum

class LogLevel:
    ERROR   = 0
    WARNING = 1
    INFO    = 2
    DEBUG   = 4

class LogMessageTypeId(_enum.Enum):
    DEBUG       = 0
    INFO        = 1
    WARNING     = 2
    ERROR       = 3
    FATAL_ERROR = 4

def default_log_message_to_output(log_message_type_id, prefix, message):
    """
    Logs message to stdout.
    """
    print("%s%s" % (prefix, message), flush = True)

class Logger:
    """
    _log_level              : int
    _log_message_callback   : Callable[[int, str, str], None]
    """

    def __init__(self):
        self._log_level             = LogLevel.INFO
        self._log_message_to_output = default_log_message_to_output

    ### log message ###

    def log_message(self, log_message_type_id, message):
        """
        log_message_type_id : LogMessageTypeId
        message             : str | Any
        """
        if not isinstance(log_message_type_id, LogMessageTypeId):
            raise TypeError("Unexpected type of 'log_message_type_id'.")

        if not isinstance(message, str):
            try:
                message = str(message)
            except Exception as exception:
                raise ValueError("Value of 'message' is not convertible to str.") from exception

        if log_message_type_id == LogMessageTypeId.DEBUG:
            if self.is_log_level_at_least(LogLevel.DEBUG):
                self._log_message_to_output(log_message_type_id, "(TOGL) Debug: ", message)

        elif log_message_type_id == LogMessageTypeId.INFO:
            
            if self.is_log_level_at_least(LogLevel.INFO):
                self._log_message_to_output(log_message_type_id, "(TOGL) Info: ", message)

        elif log_message_type_id == LogMessageTypeId.WARNING:
            if self.is_log_level_at_least(LogLevel.WARNING):
                self._log_message_to_output(log_message_type_id, "(TOGL) Warning: ", message)

        elif log_message_type_id == LogMessageTypeId.ERROR:
            if self.is_log_level_at_least(LogLevel.ERROR):
                self._log_message_to_output(log_message_type_id, "(TOGL) Error: ", message)

        elif log_message_type_id == LogMessageTypeId.FATAL_ERROR:
            if self.is_log_level_at_least(LogLevel.ERROR):
                self._log_message_to_output(log_message_type_id, "(TOGL) Fatal Error: ", message)
                exit(1) # EXIT_FAILURE

    def log_debug(self, message):
        """
        message : str | Any
        """
        if not isinstance(message, str):
            try:
                message = str(message)
            except Exception as exception:
                raise ValueError("Value of 'message' is not convertible to str.") from exception

        self.log_message(LogMessageTypeId.DEBUG, message)

    def log_info(self, message):
        """
        message : str | Any
        """
        if not isinstance(message, str):
            try:
                message = str(message)
            except Exception as exception:
                raise ValueError("Value of 'message' is not convertible to str.") from exception

        self.log_message(LogMessageTypeId.INFO, message)

    def log_warning(self, message):
        """
        message : str | Any
        """
        if not isinstance(message, str):
            try:
                message = str(message)
            except Exception as exception:
                raise ValueError("Value of 'message' is not convertible to str.") from exception

        self.log_message(LogMessageTypeId.WARNING, message)

    def log_error(self, message):
        """
        message : str | Any
        """
        if not isinstance(message, str):
            try:
                message = str(message)
            except Exception as exception:
                raise ValueError("Value of 'message' is not convertible to str.") from exception

        self.log_message(LogMessageTypeId.ERROR, message)

    def log_fatal_error(self, message):
        """
        Exits program after logging message with error code 1.
        message : str | Any
        """
        if not isinstance(message, str):
            try:
                message = str(message)
            except Exception as exception:
                raise ValueError("Value of 'message' is not convertible to str.") from exception

        self.log_message(LogMessageTypeId.FATAL_ERROR, message)

    ### log level ###

    def set_log_level(self, log_level):
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

        self._log_level = log_level

    def get_log_level(self):
        """
        Returns     : int
        """
        return self._log_level

    def is_log_level_at_least(self, log_level):
        """
        Returns     : bool
        """
        if not isinstance(log_level, int):
            try:
                log_level = int(log_level)
            except Exception as exception:
                raise ValueError("Value of 'log_level' is not convertible to int.") from exception

        return log_level <= self._log_level

    ### log message to output ###

    def set_log_message_to_output(self, log_message_to_output):
        """
        Replaces default function which displays log message with custom one (by default it's default_log_message_to_output).
        log_message_to_output : Callable[[int, str, str], None]      
            Is called when any log_{...} method is called as log_message_to_output(log_message_type_id, prefix, message).
            Where:
                log_message_type_id   - LogMessageTypeId.DEBUG, LogMessageTypeId.INFO, LogMessageTypeId.WARNING, 
                                        LogMessageTypeId.ERROR or LogMessageTypeId.FATAL_ERROR.
                prefix                - Log message prefix. Contains default text information about log message type.
                                        For example: "Error: " for error messages.
                message               - Log message.
        """
        if not callable(log_message_to_output):
            raise TypeError("Object assigned to 'log_message_to_output' is not callable.")

        self._log_message_to_output = log_message_to_output








