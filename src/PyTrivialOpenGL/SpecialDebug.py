__all__ = [
    "SpecialDebug",
    "to_special_debug",
]

class SpecialDebug:
    """                         
    is_notify_remaining_messages    : bool
    is_notify_draw_call             : bool
    is_notify_mouse_move            : bool
    is_notify_key_message           : bool
    is_notify_character_message     : bool
    is_full_exit_track_in_callback  : bool
    """
    def __init__(self):
        self.reset()

    def reset(self):
        self.is_notify_remaining_messages   = False
        self.is_notify_draw_call            = False
        self.is_notify_mouse_move           = False
        self.is_notify_key_message          = False
        self.is_notify_character_message    = False
        self.is_notify_timer                = False
        self.is_full_exit_track_in_callback = False

_special_debug = SpecialDebug()

def to_special_debug():
    """
    Returns (SpecialDebug).
    """
    return _special_debug