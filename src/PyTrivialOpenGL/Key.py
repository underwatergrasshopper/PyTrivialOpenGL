import enum     as _enum
import ctypes   as _ctypes

from . import _C_WinApi

__all__ = [
    "Key",
    "KeyId",
    "KeyboardSideId",
    "KeyExtra",
    "is_key_toggled",
]

################################################################################

class Key:
    """
    key_id  : KeyId
    is_down : bool
    extra   : KeyExtra
    """
    def __init__(self, key_id, is_down, extra):
        self.key_id     = key_id
        self.is_down    = is_down
        self.extra      = extra

    def check(self, key_id, is_down = True):
        """
        Return (bool).
        """
        return self.key_id == key_id and self.is_down == is_down

    def __str__(self):
        return "key_id=%s, is_down=%s, %s" % (self.key_id, self.is_down, self.extra.name)

    def __repr__(self):
        return self.__str__()


class KeyId(_enum.IntEnum):
    """
    Contains ids representing keyboard keys and mouse buttons.

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

class KeyboardSideId(_enum.IntEnum):
    NONE    = 0
    LEFT    = 1
    RIGHT   = 2

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
        def as_text(is_down):
            if is_down:
                return "DOWN"
            return "UP"
        text = "Shift=%s (L=%s, R=%s), " % (as_text(self.is_shift_down), as_text(self.is_left_shift_down), as_text(self.is_right_shift_down))
        text += "Alt=%s (L=%s, R=%s), " % (as_text(self.is_alt_down), as_text(self.is_left_alt_down), as_text(self.is_right_alt_down))
        text += "Ctrl=%s (L=%s, R=%s)" % (as_text(self.is_ctrl_down), as_text(self.is_left_ctrl_down), as_text(self.is_right_ctrl_down))
        return text

    def __str__(self):
        """
        Returns (str).
        """
        return "count=%d, x=%d, y=%d, keyboard_side_id=%s, %s" % (self.count, self.x, self.y, self.keyboard_side_id.name, self._all_is_down_to_str())

    def __repr__(self):
        """
        Returns (str).
        """
        return self.__str__()

_KEY_TOGGLE_BIT = 0x0001

def is_key_toggled(key_id):
    return _C_WinApi.GetKeyState(_key_id_to_vk_code(key_id)) & _KEY_TOGGLE_BIT

################################################################################

class _VirtualKeyData:
    def __init__(self, l_param):
        self.count          = l_param           & 0x0000FFFF
        self.scan_code      = (l_param >> 16)   & 0x000000FF
        self.is_ext         = (l_param >> 24)   & 0x00000001
        self.reserved1      = (l_param >> 25)   & 0x0000000F
        self.context_code   = (l_param >> 29)   & 0x00000001
        self.prev_state     = (l_param >> 30)   & 0x00000001
        self.trans_state    = (l_param >> 31)   & 0x00000001

    def __str__(self):
        return "c=%u, sc=%u, e=%u, r=%u, cc=%u, ps=%u, ts=%u" % (self.count, self.scan_code, self.is_ext, self.reserved1, self.context_code, self.prev_state, self.trans_state)

    def __repr__(self):
        return self.__str__()

def _key_id_to_vk_code(key_id):
    """
    key_id : KeyId
    Returns (int) 
        virtual key code    - If there is corresponding key id to it,
        0                   - Otherwise.
    """
    return {
        int(KeyId.BREAK)            : _C_WinApi.VK_CANCEL,        
        int(KeyId.BACKSPACE)        : _C_WinApi.VK_BACK,          
        int(KeyId.TAB)              : _C_WinApi.VK_TAB,           
        int(KeyId.ENTER)            : _C_WinApi.VK_RETURN,        
        int(KeyId.SHIFT)            : _C_WinApi.VK_SHIFT,         
        int(KeyId.CONTROL)          : _C_WinApi.VK_CONTROL,       
        int(KeyId.ALT)              : _C_WinApi.VK_MENU,          
                                    
        int(KeyId.PAUSE)            : _C_WinApi.VK_PAUSE,         
        int(KeyId.CAPS_LOCK)        : _C_WinApi.VK_CAPITAL,       
        int(KeyId.ESCAPE)           : _C_WinApi.VK_ESCAPE,        
        int(KeyId.SPACE)            : _C_WinApi.VK_SPACE,         
        int(KeyId.PAGE_UP)          : _C_WinApi.VK_PRIOR,         
        int(KeyId.PAGE_DOWN)        : _C_WinApi.VK_NEXT,          
        int(KeyId.END)              : _C_WinApi.VK_END,           
        int(KeyId.HOME)             : _C_WinApi.VK_HOME,          
        int(KeyId.ARROW_LEFT)       : _C_WinApi.VK_LEFT,          
        int(KeyId.ARROW_UP)         : _C_WinApi.VK_UP,            
        int(KeyId.ARROW_RIGHT)      : _C_WinApi.VK_RIGHT,         
        int(KeyId.ARROW_DOWN)       : _C_WinApi.VK_DOWN,          
        int(KeyId.PRINT)            : _C_WinApi.VK_PRINT,         
        int(KeyId.PRINT_SCREEN)     : _C_WinApi.VK_SNAPSHOT,      
        int(KeyId.INSERT)           : _C_WinApi.VK_INSERT,        
        int(KeyId.DELETE)           : _C_WinApi.VK_DELETE,        
        int(KeyId.NUMPAD_0)         : _C_WinApi.VK_NUMPAD0,       
        int(KeyId.NUMPAD_1)         : _C_WinApi.VK_NUMPAD1,       
        int(KeyId.NUMPAD_2)         : _C_WinApi.VK_NUMPAD2,       
        int(KeyId.NUMPAD_3)         : _C_WinApi.VK_NUMPAD3,       
        int(KeyId.NUMPAD_4)         : _C_WinApi.VK_NUMPAD4,       
        int(KeyId.NUMPAD_5)         : _C_WinApi.VK_NUMPAD5,       
        int(KeyId.NUMPAD_6)         : _C_WinApi.VK_NUMPAD6,       
        int(KeyId.NUMPAD_7)         : _C_WinApi.VK_NUMPAD7,       
        int(KeyId.NUMPAD_8)         : _C_WinApi.VK_NUMPAD8,       
        int(KeyId.NUMPAD_9)         : _C_WinApi.VK_NUMPAD9,       
        int(KeyId.NUMPAD_MULTIPLY)  : _C_WinApi.VK_MULTIPLY,      
        int(KeyId.NUMPAD_ADD)       : _C_WinApi.VK_ADD,           
        int(KeyId.NUMPAD_SEPARATOR) : _C_WinApi.VK_SEPARATOR,     
        int(KeyId.NUMPAD_SUBTRACT)  : _C_WinApi.VK_SUBTRACT,      
        int(KeyId.NUMPAD_DECIMAL)   : _C_WinApi.VK_DECIMAL,       
        int(KeyId.NUMPAD_DIVIDE)    : _C_WinApi.VK_DIVIDE,       
        int(KeyId.F1)               : _C_WinApi.VK_F1,            
        int(KeyId.F2)               : _C_WinApi.VK_F2,            
        int(KeyId.F3)               : _C_WinApi.VK_F3,            
        int(KeyId.F4)               : _C_WinApi.VK_F4,            
        int(KeyId.F5)               : _C_WinApi.VK_F5,            
        int(KeyId.F6)               : _C_WinApi.VK_F6,            
        int(KeyId.F7)               : _C_WinApi.VK_F7,            
        int(KeyId.F8)               : _C_WinApi.VK_F8,            
        int(KeyId.F9)               : _C_WinApi.VK_F9,            
        int(KeyId.F10)              : _C_WinApi.VK_F10,           
        int(KeyId.F11)              : _C_WinApi.VK_F11,           
        int(KeyId.F12)              : _C_WinApi.VK_F12,           
        int(KeyId.F13)              : _C_WinApi.VK_F13,           
        int(KeyId.F14)              : _C_WinApi.VK_F14,           
        int(KeyId.F15)              : _C_WinApi.VK_F15,           
        int(KeyId.F16)              : _C_WinApi.VK_F16,           
        int(KeyId.F17)              : _C_WinApi.VK_F17,           
        int(KeyId.F18)              : _C_WinApi.VK_F18,           
        int(KeyId.F19)              : _C_WinApi.VK_F19,           
        int(KeyId.F20)              : _C_WinApi.VK_F20,           
        int(KeyId.F21)              : _C_WinApi.VK_F21,           
        int(KeyId.F22)              : _C_WinApi.VK_F22,           
        int(KeyId.F23)              : _C_WinApi.VK_F23,           
        int(KeyId.F24)              : _C_WinApi.VK_F24,           
        int(KeyId.NUM_0)            : ord('0'),                   
        int(KeyId.NUM_1)            : ord('1'),                   
        int(KeyId.NUM_2)            : ord('2'),                   
        int(KeyId.NUM_3)            : ord('3'),                   
        int(KeyId.NUM_4)            : ord('4'),                   
        int(KeyId.NUM_5)            : ord('5'),                   
        int(KeyId.NUM_6)            : ord('6'),                   
        int(KeyId.NUM_7)            : ord('7'),                   
        int(KeyId.NUM_8)            : ord('8'),                   
        int(KeyId.NUM_9)            : ord('9'),                   
        int(KeyId.A)                : ord('A'),                   
        int(KeyId.B)                : ord('B'),                   
        int(KeyId.C)                : ord('C'),                   
        int(KeyId.D)                : ord('D'),                   
        int(KeyId.E)                : ord('E'),                   
        int(KeyId.F)                : ord('F'),                   
        int(KeyId.G)                : ord('G'),                   
        int(KeyId.H)                : ord('H'),                   
        int(KeyId.I)                : ord('I'),                   
        int(KeyId.J)                : ord('J'),                   
        int(KeyId.K)                : ord('K'),                   
        int(KeyId.L)                : ord('L'),                   
        int(KeyId.M)                : ord('M'),                   
        int(KeyId.N)                : ord('N'),                   
        int(KeyId.O)                : ord('O'),                   
        int(KeyId.P)                : ord('P'),                   
        int(KeyId.Q)                : ord('Q'),                   
        int(KeyId.R)                : ord('R'),                   
        int(KeyId.S)                : ord('S'),                   
        int(KeyId.T)                : ord('T'),                   
        int(KeyId.U)                : ord('U'),                   
        int(KeyId.V)                : ord('V'),                   
        int(KeyId.W)                : ord('W'),                   
        int(KeyId.X)                : ord('X'),                   
        int(KeyId.Y)                : ord('Y'),                   
        int(KeyId.Z)                : ord('Z'),                   
                                    
        int(KeyId.SEMICOLON)        : _C_WinApi.VK_OEM_1,         
        int(KeyId.FORWARD_SLASH)    : _C_WinApi.VK_OEM_2,         
        int(KeyId.ACUTE)            : _C_WinApi.VK_OEM_3,         
        int(KeyId.OPEN_BRACKET)     : _C_WinApi.VK_OEM_4,         
        int(KeyId.BACK_SLASH)       : _C_WinApi.VK_OEM_5,         
        int(KeyId.CLOSE_BRACKET)    : _C_WinApi.VK_OEM_6,         
        int(KeyId.APOSTROPHE)       : _C_WinApi.VK_OEM_7,         
        int(KeyId.COMMA)            : _C_WinApi.VK_OEM_COMMA,     
        int(KeyId.DOT)              : _C_WinApi.VK_OEM_PERIOD,    
        int(KeyId.DASH)             : _C_WinApi.VK_OEM_MINUS,     
        int(KeyId.EQUAL)            : _C_WinApi.VK_OEM_PLUS,     
                                    
        int(KeyId.NUMLOCK)          : _C_WinApi.VK_NUMLOCK,       
        int(KeyId.SCROLL_LOCK)      : _C_WinApi.VK_SCROLL,
    }.get(int(key_id), 0)

def _vk_code_to_key_id(vk_code):
    """
    vk_code : int
    Returns (KeyId) 
        key id          - If there is corresponding virtual key code to it,
        KeyId.UNKNOWN   - Otherwise.
    """
    return {
        _C_WinApi.VK_CANCEL         : KeyId.BREAK,                  
        _C_WinApi.VK_BACK           : KeyId.BACKSPACE,              
        _C_WinApi.VK_TAB            : KeyId.TAB,                    
        _C_WinApi.VK_RETURN         : KeyId.ENTER, 
        _C_WinApi.VK_SHIFT          : KeyId.SHIFT, 
        _C_WinApi.VK_CONTROL        : KeyId.CONTROL, 
        _C_WinApi.VK_MENU           : KeyId.ALT, 

        _C_WinApi.VK_PAUSE          : KeyId.PAUSE,                  
        _C_WinApi.VK_CAPITAL        : KeyId.CAPS_LOCK,              
        _C_WinApi.VK_ESCAPE         : KeyId.ESCAPE,                 
        _C_WinApi.VK_SPACE          : KeyId.SPACE,                  
        _C_WinApi.VK_PRIOR          : KeyId.PAGE_UP,                
        _C_WinApi.VK_NEXT           : KeyId.PAGE_DOWN,              
        _C_WinApi.VK_END            : KeyId.END,                    
        _C_WinApi.VK_HOME           : KeyId.HOME,                   
        _C_WinApi.VK_LEFT           : KeyId.ARROW_LEFT,             
        _C_WinApi.VK_UP             : KeyId.ARROW_UP,               
        _C_WinApi.VK_RIGHT          : KeyId.ARROW_RIGHT,            
        _C_WinApi.VK_DOWN           : KeyId.ARROW_DOWN,             
        _C_WinApi.VK_PRINT          : KeyId.PRINT,                  
        _C_WinApi.VK_SNAPSHOT       : KeyId.PRINT_SCREEN,           
        _C_WinApi.VK_INSERT         : KeyId.INSERT,                 
        _C_WinApi.VK_DELETE         : KeyId.DELETE,                 
        _C_WinApi.VK_NUMPAD0        : KeyId.NUMPAD_0,               
        _C_WinApi.VK_NUMPAD1        : KeyId.NUMPAD_1,               
        _C_WinApi.VK_NUMPAD2        : KeyId.NUMPAD_2,               
        _C_WinApi.VK_NUMPAD3        : KeyId.NUMPAD_3,               
        _C_WinApi.VK_NUMPAD4        : KeyId.NUMPAD_4,               
        _C_WinApi.VK_NUMPAD5        : KeyId.NUMPAD_5,               
        _C_WinApi.VK_NUMPAD6        : KeyId.NUMPAD_6,               
        _C_WinApi.VK_NUMPAD7        : KeyId.NUMPAD_7,               
        _C_WinApi.VK_NUMPAD8        : KeyId.NUMPAD_8,               
        _C_WinApi.VK_NUMPAD9        : KeyId.NUMPAD_9,               
        _C_WinApi.VK_MULTIPLY       : KeyId.NUMPAD_MULTIPLY,        
        _C_WinApi.VK_ADD            : KeyId.NUMPAD_ADD,             
        _C_WinApi.VK_SEPARATOR      : KeyId.NUMPAD_SEPARATOR,       
        _C_WinApi.VK_SUBTRACT       : KeyId.NUMPAD_SUBTRACT,        
        _C_WinApi.VK_DECIMAL        : KeyId.NUMPAD_DECIMAL,         
        _C_WinApi.VK_DIVIDE         : KeyId.NUMPAD_DIVIDE,          
        _C_WinApi.VK_F1             : KeyId.F1,                     
        _C_WinApi.VK_F2             : KeyId.F2,                     
        _C_WinApi.VK_F3             : KeyId.F3,                     
        _C_WinApi.VK_F4             : KeyId.F4,                     
        _C_WinApi.VK_F5             : KeyId.F5,                     
        _C_WinApi.VK_F6             : KeyId.F6,                     
        _C_WinApi.VK_F7             : KeyId.F7,                     
        _C_WinApi.VK_F8             : KeyId.F8,                     
        _C_WinApi.VK_F9             : KeyId.F9,                     
        _C_WinApi.VK_F10            : KeyId.F10,                    
        _C_WinApi.VK_F11            : KeyId.F11,                    
        _C_WinApi.VK_F12            : KeyId.F12,                    
        _C_WinApi.VK_F13            : KeyId.F13,                    
        _C_WinApi.VK_F14            : KeyId.F14,                    
        _C_WinApi.VK_F15            : KeyId.F15,                    
        _C_WinApi.VK_F16            : KeyId.F16,                    
        _C_WinApi.VK_F17            : KeyId.F17,                    
        _C_WinApi.VK_F18            : KeyId.F18,                    
        _C_WinApi.VK_F19            : KeyId.F19,                    
        _C_WinApi.VK_F20            : KeyId.F20,                    
        _C_WinApi.VK_F21            : KeyId.F21,                    
        _C_WinApi.VK_F22            : KeyId.F22,                    
        _C_WinApi.VK_F23            : KeyId.F23,                    
        _C_WinApi.VK_F24            : KeyId.F24,   
        ord('0')                    : KeyId.NUM_0,    
        ord('1')                    : KeyId.NUM_1,    
        ord('2')                    : KeyId.NUM_2,    
        ord('3')                    : KeyId.NUM_3,    
        ord('4')                    : KeyId.NUM_4,    
        ord('5')                    : KeyId.NUM_5,    
        ord('6')                    : KeyId.NUM_6,    
        ord('7')                    : KeyId.NUM_7,    
        ord('8')                    : KeyId.NUM_8,    
        ord('9')                    : KeyId.NUM_9,    
        ord('A')                    : KeyId.A,    
        ord('B')                    : KeyId.B,    
        ord('C')                    : KeyId.C,    
        ord('D')                    : KeyId.D,    
        ord('E')                    : KeyId.E,    
        ord('F')                    : KeyId.F,    
        ord('G')                    : KeyId.G,    
        ord('H')                    : KeyId.H,    
        ord('I')                    : KeyId.I,    
        ord('J')                    : KeyId.J,    
        ord('K')                    : KeyId.K,    
        ord('L')                    : KeyId.L,    
        ord('M')                    : KeyId.M,    
        ord('N')                    : KeyId.N,    
        ord('O')                    : KeyId.O,    
        ord('P')                    : KeyId.P,    
        ord('Q')                    : KeyId.Q,    
        ord('R')                    : KeyId.R,    
        ord('S')                    : KeyId.S,    
        ord('T')                    : KeyId.T,    
        ord('U')                    : KeyId.U,    
        ord('V')                    : KeyId.V,    
        ord('W')                    : KeyId.W,    
        ord('X')                    : KeyId.X,    
        ord('Y')                    : KeyId.Y,    
        ord('Z')                    : KeyId.Z,

        _C_WinApi.VK_OEM_1          : KeyId.SEMICOLON,       # ;
        _C_WinApi.VK_OEM_2          : KeyId.FORWARD_SLASH,   # /
        _C_WinApi.VK_OEM_3          : KeyId.ACUTE,           # `
        _C_WinApi.VK_OEM_4          : KeyId.OPEN_BRACKET,    # [
        _C_WinApi.VK_OEM_5          : KeyId.BACK_SLASH,      # \
        _C_WinApi.VK_OEM_6          : KeyId.CLOSE_BRACKET,   # ]
        _C_WinApi.VK_OEM_7          : KeyId.APOSTROPHE,      # '
        _C_WinApi.VK_OEM_COMMA      : KeyId.COMMA,           # ,
        _C_WinApi.VK_OEM_PERIOD     : KeyId.DOT,             # .
        _C_WinApi.VK_OEM_MINUS      : KeyId.DASH,            # -
        _C_WinApi.VK_OEM_PLUS       : KeyId.EQUAL,           # =

        _C_WinApi.VK_NUMLOCK        : KeyId.NUMLOCK,                
        _C_WinApi.VK_SCROLL         : KeyId.SCROLL_LOCK,      
    }.get(vk_code, KeyId.UNKNOWN)

def _get_key_id_from_w_param(w_param):
    """
    w_param : int
    Returns (KeyId).
    """
    return _vk_code_to_key_id(w_param)

def _get_mouse_key_id(message, w_param):
    """
    message : int
    w_param : int
    Returns (KeyId).
    """
    key_id = {
        _C_WinApi.WM_LBUTTONDOWN    : KeyId.LEFT_MOUSE_BUTTON,
        _C_WinApi.WM_LBUTTONUP      : KeyId.LEFT_MOUSE_BUTTON,

        _C_WinApi.WM_RBUTTONDOWN    : KeyId.RIGHT_MOUSE_BUTTON,
        _C_WinApi.WM_RBUTTONUP      : KeyId.RIGHT_MOUSE_BUTTON,

        _C_WinApi.WM_MBUTTONDOWN    : KeyId.MIDDLE_MOUSE_BUTTON,
        _C_WinApi.WM_MBUTTONUP      : KeyId.MIDDLE_MOUSE_BUTTON,
    }.get(int(message), None)

    if key_id is not None:
        return key_id

    if int(message) in (_C_WinApi.WM_XBUTTONDOWN, _C_WinApi.WM_XBUTTONUP):
        if _C_WinApi.HIWORD(w_param).value == _C_WinApi.XBUTTON1:
            return KeyId.X1_MOUSE_BUTTON
        if _C_WinApi.HIWORD(w_param).value == _C_WinApi.XBUTTON2:
            return KeyId.X2_MOUSE_BUTTON

    return KeyId.UNKNOWN

def _is_mouse_button_down(message):
    """
    message : int
    Returns (bool).
    """
    return int(message) in (_C_WinApi.WM_LBUTTONDOWN, _C_WinApi.WM_RBUTTONDOWN, _C_WinApi.WM_MBUTTONDOWN, _C_WinApi.WM_XBUTTONDOWN)

def _get_keyboard_side_id(key_id, virtual_key_data):
    """
    key_id : KeyId
    virtual_key_data : _VirtualKeyData
    Returns (KeyboardSideId).
    """
    if key_id == KeyId.SHIFT:
        vk_code_ext = _C_WinApi.MapVirtualKeyA(virtual_key_data.scan_code, _C_WinApi.MAPVK_VSC_TO_VK_EX)
        if vk_code_ext == _C_WinApi.VK_LSHIFT:
            return KeyboardSideId.LEFT
        if vk_code_ext == _C_WinApi.VK_RSHIFT:
            return KeyboardSideId.RIGHT
        return KeyboardSideId.NONE

    if key_id in (KeyId.CONTROL, KeyId.ALT):
        if virtual_key_data.is_ext:
            return KeyboardSideId.RIGHT
        return KeyboardSideId.LEFT

    return KeyboardSideId.NONE

def _vk_code_to_str(vk_code):
    text = {
        _C_WinApi.VK_CANCEL           : "VK_CANCEL",
        _C_WinApi.VK_BACK             : "VK_BACK",
        _C_WinApi.VK_TAB              : "VK_TAB",
        _C_WinApi.VK_RETURN           : "VK_RETURN",
        _C_WinApi.VK_SHIFT            : "VK_SHIFT",
        _C_WinApi.VK_CONTROL          : "VK_CONTROL",
        _C_WinApi.VK_MENU             : "VK_MENU",
        _C_WinApi.VK_PAUSE            : "VK_PAUSE",
        _C_WinApi.VK_CAPITAL          : "VK_CAPITAL",
        _C_WinApi.VK_ESCAPE           : "VK_ESCAPE",
        _C_WinApi.VK_SPACE            : "VK_SPACE",
        _C_WinApi.VK_PRIOR            : "VK_PRIOR",
        _C_WinApi.VK_NEXT             : "VK_NEXT",
        _C_WinApi.VK_END              : "VK_END",
        _C_WinApi.VK_HOME             : "VK_HOME",
        _C_WinApi.VK_LEFT             : "VK_LEFT",
        _C_WinApi.VK_UP               : "VK_UP",
        _C_WinApi.VK_RIGHT            : "VK_RIGHT",
        _C_WinApi.VK_DOWN             : "VK_DOWN",
        _C_WinApi.VK_PRINT            : "VK_PRINT",
        _C_WinApi.VK_SNAPSHOT         : "VK_SNAPSHOT",
        _C_WinApi.VK_INSERT           : "VK_INSERT",
        _C_WinApi.VK_DELETE           : "VK_DELETE",
        _C_WinApi.VK_NUMPAD0          : "VK_NUMPAD0",
        _C_WinApi.VK_NUMPAD1          : "VK_NUMPAD1",
        _C_WinApi.VK_NUMPAD2          : "VK_NUMPAD2",
        _C_WinApi.VK_NUMPAD3          : "VK_NUMPAD3",
        _C_WinApi.VK_NUMPAD4          : "VK_NUMPAD4",
        _C_WinApi.VK_NUMPAD5          : "VK_NUMPAD5",
        _C_WinApi.VK_NUMPAD6          : "VK_NUMPAD6",
        _C_WinApi.VK_NUMPAD7          : "VK_NUMPAD7",
        _C_WinApi.VK_NUMPAD8          : "VK_NUMPAD8",
        _C_WinApi.VK_NUMPAD9          : "VK_NUMPAD9",
        _C_WinApi.VK_MULTIPLY         : "VK_MULTIPLY",
        _C_WinApi.VK_ADD              : "VK_ADD",
        _C_WinApi.VK_SEPARATOR        : "VK_SEPARATOR",
        _C_WinApi.VK_SUBTRACT         : "VK_SUBTRACT",
        _C_WinApi.VK_DECIMAL          : "VK_DECIMAL",
        _C_WinApi.VK_DIVIDE           : "VK_DIVIDE",
        _C_WinApi.VK_F1               : "VK_F1",
        _C_WinApi.VK_F2               : "VK_F2",
        _C_WinApi.VK_F3               : "VK_F3",
        _C_WinApi.VK_F4               : "VK_F4",
        _C_WinApi.VK_F5               : "VK_F5",
        _C_WinApi.VK_F6               : "VK_F6",
        _C_WinApi.VK_F7               : "VK_F7",
        _C_WinApi.VK_F8               : "VK_F8",
        _C_WinApi.VK_F9               : "VK_F9",
        _C_WinApi.VK_F10              : "VK_F10",
        _C_WinApi.VK_F11              : "VK_F11",
        _C_WinApi.VK_F12              : "VK_F12",
        _C_WinApi.VK_F13              : "VK_F13",
        _C_WinApi.VK_F14              : "VK_F14",
        _C_WinApi.VK_F15              : "VK_F15",
        _C_WinApi.VK_F16              : "VK_F16",
        _C_WinApi.VK_F17              : "VK_F17",
        _C_WinApi.VK_F18              : "VK_F18",
        _C_WinApi.VK_F19              : "VK_F19",
        _C_WinApi.VK_F20              : "VK_F20",
        _C_WinApi.VK_F21              : "VK_F21",
        _C_WinApi.VK_F22              : "VK_F22",
        _C_WinApi.VK_F23              : "VK_F23",
        _C_WinApi.VK_F24              : "VK_F24",

        _C_WinApi.VK_OEM_1            : "VK_OEM_1",
        _C_WinApi.VK_OEM_2            : "VK_OEM_2",
        _C_WinApi.VK_OEM_3            : "VK_OEM_3",
        _C_WinApi.VK_OEM_4            : "VK_OEM_4",
        _C_WinApi.VK_OEM_5            : "VK_OEM_5",
        _C_WinApi.VK_OEM_6            : "VK_OEM_6",
        _C_WinApi.VK_OEM_7            : "VK_OEM_7",
        _C_WinApi.VK_OEM_COMMA        : "VK_OEM_COMMA",
        _C_WinApi.VK_OEM_PERIOD       : "VK_OEM_PERIOD",
        _C_WinApi.VK_OEM_MINUS        : "VK_OEM_MINUS",
        _C_WinApi.VK_OEM_PLUS         : "VK_OEM_PLUS",

        _C_WinApi.VK_NUMLOCK          : "VK_NUMLOCK",
        _C_WinApi.VK_SCROLL           : "VK_SCROLL",
        _C_WinApi.VK_LSHIFT           : "VK_LSHIFT",
        _C_WinApi.VK_RSHIFT           : "VK_RSHIFT",
        _C_WinApi.VK_LCONTROL         : "VK_LCONTROL",
        _C_WinApi.VK_RCONTROL         : "VK_RCONTROL",
        _C_WinApi.VK_LMENU            : "VK_LMENU",
        _C_WinApi.VK_RMENU            : "VK_RMENU",
    }.get(vk_code, None)

    if text is None:
        if (vk_code >= ord('0') and vk_code <= ord('9')) or (vk_code >= ord('A') and vk_code <= ord('Z')):
            return chr(vk_code)
        return "(%u)" % (vk_code)

    return text

def _is_mw_mouse_button(window_message):
    return window_message in [
        _C_WinApi.WM_LBUTTONDOWN,
        _C_WinApi.WM_LBUTTONUP,
        _C_WinApi.WM_RBUTTONDOWN,
        _C_WinApi.WM_RBUTTONUP,
        _C_WinApi.WM_MBUTTONDOWN,
        _C_WinApi.WM_MBUTTONUP,
        _C_WinApi.WM_XBUTTONDOWN,
        _C_WinApi.WM_XBUTTONUP
    ]

def _is_mw_mouse_button_x(window_message):
    return window_message in [
        _C_WinApi.WM_XBUTTONDOWN,
        _C_WinApi.WM_XBUTTONUP
    ]

