import enum     as _enum
import ctypes   as _ctypes

from ._Private import C_WinApi      as _C_WinApi
from ._Private import KeySupport    as _KeySupport

# Same level modules.
from .KeyId             import KeyId
from .KeyboardSideId    import KeyboardSideId

class KeyExtra:
    """
    count               : int
        Repeat count of key stroke.
    x                   : int
        Cursor x position in window draw area.
    y                   : int
        Cursor y position in window draw area.
    keyboard_side_id    : KeyboardSideId
        Stores information that, on which side of keyboard is used key (left or right).
        If side of keyboard doesn't matter or when key exists only on one side, then contains KeyBoardSideId_NONE. 
        Note: Used for shift, control, alt keys. For ids: SHIFT, CONTROL, ALT.
    is_shift_down       : bool
    is_alt_down         : bool
    is_ctrl_down        : bool
                    
    is_left_shift_down  : bool
    is_left_alt_down    : bool
    is_left_ctrl_down   : bool
                      
    is_right_shift_down : bool
    is_right_alt_down   : bool
    is_right_ctrl_down  : bool
    """
    def __init__(self, count, x, y, keyboard_side_id):
        self.count                  = count
        self.x                      = x
        self.y                      = y
        self.keyboard_side_id       = keyboard_side_id

        self.is_shift_down          = False
        self.is_alt_down            = False
        self.is_ctrl_down           = False

        self.is_left_shift_down     = False
        self.is_left_alt_down       = False
        self.is_left_ctrl_down      = False

        self.is_right_shift_down    = False
        self.is_right_alt_down      = False
        self.is_right_ctrl_down     = False

    def _all_is_down_to_str(self):
        """
        Returns     : str
        """
        def as_text(is_down):
            if is_down:
                return "DOWN"
            return "UP"
        text = "Shift=%s (L=%s, R=%s), " % (as_text(self.is_shift_down), as_text(self.is_left_shift_down), as_text(self.is_right_shift_down))
        text += "Alt=%s (L=%s, R=%s), " % (as_text(self.is_alt_down), as_text(self.is_left_alt_down), as_text(self.is_right_alt_down))
        text += "Ctrl=%s (L=%s, R=%s)" % (as_text(self.is_ctrl_down), as_text(self.is_left_ctrl_down), as_text(self.is_right_ctrl_down))
        return text

    def __str__(self):
        return "count=%d, x=%d, y=%d, keyboard_side_id=%s, %s" % (self.count, self.x, self.y, self.keyboard_side_id.name, self._all_is_down_to_str())

    def __repr__(self):
        return self.__str__()

_KEY_TOGGLE_BIT = 0x0001

def is_key_toggled(key_id):
    """
    key_id  : KeyId
    Returns : bool
    """
    if not isinstance(key_id, KeyId):
        raise TypeError("Unexpected type of 'key_id'.")

    return _C_WinApi.GetKeyState(_KeySupport.key_id_to_vk_code(key_id)) & _KEY_TOGGLE_BIT

