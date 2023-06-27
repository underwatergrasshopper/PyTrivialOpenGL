import enum

from . import _C_WinApi

__all__ = [
    "KeyId",
    "KeyboardSideId",
    "KeyExtra",
    "is_key_toggled",
]

class KeyId(enum.IntEnum):
    """
    Contains ids representing keyboard keys and mouse buttons.

    Single character string, from ranges '0-9' and 'A-Z', can be used instead of key id for comparisons with '==' and '!='. 
    For example: '0' '1' ... '0' 'A' 'B' ... 'Z'.
    """
    UNKNOWN             = 0

    NUM_0               = ord('0')              # same ids as ascii code points for characters: 0-9
    NUM_1               = enum.auto()
    NUM_2               = enum.auto()
    NUM_3               = enum.auto()
    NUM_4               = enum.auto()
    NUM_5               = enum.auto()
    NUM_6               = enum.auto()
    NUM_7               = enum.auto()
    NUM_8               = enum.auto()
    NUM_9               = enum.auto()

    A                   = ord('A')              # same ids as ascii code points for characters: A-Z
    B                   = enum.auto()
    C                   = enum.auto()
    D                   = enum.auto()
    E                   = enum.auto()
    F                   = enum.auto()
    G                   = enum.auto()
    H                   = enum.auto()
    I                   = enum.auto()
    J                   = enum.auto()
    K                   = enum.auto()
    L                   = enum.auto()
    M                   = enum.auto()
    N                   = enum.auto()
    O                   = enum.auto()
    P                   = enum.auto()
    Q                   = enum.auto()
    R                   = enum.auto()
    S                   = enum.auto()
    T                   = enum.auto()
    U                   = enum.auto()
    V                   = enum.auto()
    W                   = enum.auto()
    X                   = enum.auto()
    Y                   = enum.auto()
    Z                   = enum.auto()

    ESCAPE              = 256                   # out of ascii scope, no id collision with ascii code points
    ENTER               = enum.auto()
    CAPS_LOCK           = enum.auto()
    TAB                 = enum.auto()
    BACKSPACE           = enum.auto()
    SPACE               = enum.auto()

    SHIFT               = enum.auto()
    CONTROL             = enum.auto()
    ALT                 = enum.auto()

    PAGE_UP             = enum.auto()  
    PAGE_DOWN           = enum.auto()
    END                 = enum.auto()
    HOME                = enum.auto()

    ARROW_LEFT          = enum.auto()
    ARROW_UP            = enum.auto()
    ARROW_RIGHT         = enum.auto()
    ARROW_DOWN          = enum.auto()

    INSERT              = enum.auto()
    DELETE              = enum.auto()
    BREAK               = enum.auto()
    PAUSE               = enum.auto()
    PRINT               = enum.auto()
    PRINT_SCREEN        = enum.auto()

    NUMPAD_0            = enum.auto()
    NUMPAD_1            = enum.auto()
    NUMPAD_2            = enum.auto()
    NUMPAD_3            = enum.auto()
    NUMPAD_4            = enum.auto()
    NUMPAD_5            = enum.auto()
    NUMPAD_6            = enum.auto()
    NUMPAD_7            = enum.auto()
    NUMPAD_8            = enum.auto()
    NUMPAD_9            = enum.auto()
    NUMPAD_MULTIPLY     = enum.auto()
    NUMPAD_ADD          = enum.auto()
    NUMPAD_SEPARATOR    = enum.auto()
    NUMPAD_SUBTRACT     = enum.auto()
    NUMPAD_DECIMAL      = enum.auto()
    NUMPAD_DIVIDE       = enum.auto()

    SEMICOLON           = enum.auto()   # ;
    FORWARD_SLASH       = enum.auto()   # /
    ACUTE               = enum.auto()   # `
    OPEN_BRACKET        = enum.auto()   # [
    BACK_SLASH          = enum.auto()   # \
    CLOSE_BRACKET       = enum.auto()   # ]
    APOSTROPHE          = enum.auto()   # '
    COMMA               = enum.auto()   # ,
    DOT                 = enum.auto()   # .
    DASH                = enum.auto()   # -
    EQUAL               = enum.auto()   # =

    F1                  = enum.auto()
    F2                  = enum.auto()
    F3                  = enum.auto()
    F4                  = enum.auto()
    F5                  = enum.auto()
    F6                  = enum.auto()
    F7                  = enum.auto()
    F8                  = enum.auto()
    F9                  = enum.auto()
    F10                 = enum.auto()
    F11                 = enum.auto()
    F12                 = enum.auto()
    F13                 = enum.auto()
    F14                 = enum.auto()
    F15                 = enum.auto()
    F16                 = enum.auto()
    F17                 = enum.auto()
    F18                 = enum.auto()
    F19                 = enum.auto()
    F20                 = enum.auto()
    F21                 = enum.auto()
    F22                 = enum.auto()
    F23                 = enum.auto()
    F24                 = enum.auto()

    NUMLOCK             = enum.auto()
    SCROLL_LOCK         = enum.auto()

    LEFT_MOUSE_BUTTON   = enum.auto()
    MIDDLE_MOUSE_BUTTON = enum.auto()
    RIGHT_MOUSE_BUTTON  = enum.auto()
    X1_MOUSE_BUTTON     = enum.auto()
    X2_MOUSE_BUTTON     = enum.auto()

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

class KeyboardSideId(enum.IntEnum):
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
        Note: Used for shift, control, alt keys. For ids: SHIFT, CONTROL, _ALT.
    """
    def __init__(self, count, x, y, keyboard_side_id):
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
            Note: Used for shift, control, alt keys. For ids: SHIFT, CONTROL, _ALT.
        """
        self.count              = count
        self.x                  = x
        self.y                  = y
        self.keyboard_side_id   = keyboard_side_id

_KEY_TOGGLE_BIT = 0x0001

def is_key_toggled(key_id):
    return _C_WinApi.GetKeyState(_key_id_to_vk_code(key_id)) & _KEY_TOGGLE_BIT

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
    return _vk_code_to_key_id(w_param)