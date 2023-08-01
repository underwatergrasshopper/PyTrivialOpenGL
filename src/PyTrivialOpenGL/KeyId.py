import enum as _enum

__all__ = [
    "KeyboardSideId",
]

class KeyId(_enum.IntEnum):
    """
    Identifier of keyboard key or mouse button.

    Single character string, from ranges '0-9' and 'A-Z', can be used instead of key id for comparisons with '==' and '!='. 
    For example: '0' '1' ... '0' 'A' 'B' ... 'Z'.
    """
    UNKNOWN             = 0

    NUM_0               = ord('0')              # same ids as ascii code points for characters: 0-9
    NUM_1               = _enum.auto()
    NUM_2               = _enum.auto()
    NUM_3               = _enum.auto()
    NUM_4               = _enum.auto()
    NUM_5               = _enum.auto()
    NUM_6               = _enum.auto()
    NUM_7               = _enum.auto()
    NUM_8               = _enum.auto()
    NUM_9               = _enum.auto()

    A                   = ord('A')              # same ids as ascii code points for characters: A-Z
    B                   = _enum.auto()
    C                   = _enum.auto()
    D                   = _enum.auto()
    E                   = _enum.auto()
    F                   = _enum.auto()
    G                   = _enum.auto()
    H                   = _enum.auto()
    I                   = _enum.auto()
    J                   = _enum.auto()
    K                   = _enum.auto()
    L                   = _enum.auto()
    M                   = _enum.auto()
    N                   = _enum.auto()
    O                   = _enum.auto()
    P                   = _enum.auto()
    Q                   = _enum.auto()
    R                   = _enum.auto()
    S                   = _enum.auto()
    T                   = _enum.auto()
    U                   = _enum.auto()
    V                   = _enum.auto()
    W                   = _enum.auto()
    X                   = _enum.auto()
    Y                   = _enum.auto()
    Z                   = _enum.auto()

    ESCAPE              = 256                   # out of ascii scope, no id collision with ascii code points
    ENTER               = _enum.auto()
    CAPS_LOCK           = _enum.auto()
    TAB                 = _enum.auto()
    BACKSPACE           = _enum.auto()
    SPACE               = _enum.auto()

    SHIFT               = _enum.auto()
    CONTROL             = _enum.auto()
    ALT                 = _enum.auto()

    PAGE_UP             = _enum.auto()  
    PAGE_DOWN           = _enum.auto()
    END                 = _enum.auto()
    HOME                = _enum.auto()

    ARROW_LEFT          = _enum.auto()
    ARROW_UP            = _enum.auto()
    ARROW_RIGHT         = _enum.auto()
    ARROW_DOWN          = _enum.auto()

    INSERT              = _enum.auto()
    DELETE              = _enum.auto()
    BREAK               = _enum.auto()
    PAUSE               = _enum.auto()
    PRINT               = _enum.auto()
    PRINT_SCREEN        = _enum.auto()

    NUMPAD_0            = _enum.auto()
    NUMPAD_1            = _enum.auto()
    NUMPAD_2            = _enum.auto()
    NUMPAD_3            = _enum.auto()
    NUMPAD_4            = _enum.auto()
    NUMPAD_5            = _enum.auto()
    NUMPAD_6            = _enum.auto()
    NUMPAD_7            = _enum.auto()
    NUMPAD_8            = _enum.auto()
    NUMPAD_9            = _enum.auto()
    NUMPAD_MULTIPLY     = _enum.auto()
    NUMPAD_ADD          = _enum.auto()
    NUMPAD_SEPARATOR    = _enum.auto()
    NUMPAD_SUBTRACT     = _enum.auto()
    NUMPAD_DECIMAL      = _enum.auto()
    NUMPAD_DIVIDE       = _enum.auto()

    SEMICOLON           = _enum.auto()   # ;
    FORWARD_SLASH       = _enum.auto()   # /
    ACUTE               = _enum.auto()   # `
    OPEN_BRACKET        = _enum.auto()   # [
    BACK_SLASH          = _enum.auto()   # \
    CLOSE_BRACKET       = _enum.auto()   # ]
    APOSTROPHE          = _enum.auto()   # '
    COMMA               = _enum.auto()   # ,
    DOT                 = _enum.auto()   # .
    DASH                = _enum.auto()   # -
    EQUAL               = _enum.auto()   # =

    F1                  = _enum.auto()
    F2                  = _enum.auto()
    F3                  = _enum.auto()
    F4                  = _enum.auto()
    F5                  = _enum.auto()
    F6                  = _enum.auto()
    F7                  = _enum.auto()
    F8                  = _enum.auto()
    F9                  = _enum.auto()
    F10                 = _enum.auto()
    F11                 = _enum.auto()
    F12                 = _enum.auto()
    F13                 = _enum.auto()
    F14                 = _enum.auto()
    F15                 = _enum.auto()
    F16                 = _enum.auto()
    F17                 = _enum.auto()
    F18                 = _enum.auto()
    F19                 = _enum.auto()
    F20                 = _enum.auto()
    F21                 = _enum.auto()
    F22                 = _enum.auto()
    F23                 = _enum.auto()
    F24                 = _enum.auto()

    NUMLOCK             = _enum.auto()
    SCROLL_LOCK         = _enum.auto()

    LEFT_MOUSE_BUTTON   = _enum.auto()
    MIDDLE_MOUSE_BUTTON = _enum.auto()
    RIGHT_MOUSE_BUTTON  = _enum.auto()
    X1_MOUSE_BUTTON     = _enum.auto()
    X2_MOUSE_BUTTON     = _enum.auto()

    def __eq__(self, other):
        """
        Allows comparison with single character string. Ranges: 'A-Z' and '0-9'.
        """
        if isinstance(other, str) and len(other) == 1:
            return int(self) == ord(other)
        return super().__eq__(other)

    def __ne__(self, other):
        """
        Allows comparison with single character string. Ranges: 'A-Z' and '0-9'.
        """
        if isinstance(other, str) and len(other) == 1:
            return int(self) != ord(other)
        return super().__ne__(other)