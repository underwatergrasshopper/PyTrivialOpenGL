__all__ = [
    "SpecialDebug",
    "to_special_debug",
]

class SpecialDebug:
    """                         
    is_notify_any_message       : bool
    is_notify_draw_call         : bool
    is_notify_mouse_move        : bool
    is_notify_key_message       : bool
    is_notify_character_message : bool
    """
    def __init_(self):
        self.is_notify_any_message          = False
        self.is_notify_draw_call            = False
        self.is_notify_mouse_move           = False
        self.is_notify_key_message          = False
        self.is_notify_character_message    = False

_special_debug = SpecialDebug()

def to_special_debug():
    """
    Returns (SpecialDebug).
    """
    return _special_debug