import enum     as _enum
import ctypes   as _ctypes

from . import C_WinApi as _C_WinApi

from ..KeyId import KeyId
from ..KeyboardSideId import KeyboardSideId

class VirtualKeyData:
    """
    count           : int
    scan_code       : int
    is_ext          : int
    reserved1       : int
    context_code    : int
    prev_state      : int
    trans_state     : int
    """
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

def key_id_to_vk_code(key_id):
    """
    key_id : KeyId
    Returns (int) 
        virtual key code    - If there is corresponding key id to it,
        0                   - Otherwise.
    """
    return {
        KeyId.BREAK             : _C_WinApi.VK_CANCEL,        
        KeyId.BACKSPACE         : _C_WinApi.VK_BACK,          
        KeyId.TAB               : _C_WinApi.VK_TAB,           
        KeyId.ENTER             : _C_WinApi.VK_RETURN,        
        KeyId.SHIFT             : _C_WinApi.VK_SHIFT,         
        KeyId.CONTROL           : _C_WinApi.VK_CONTROL,       
        KeyId.ALT               : _C_WinApi.VK_MENU,          
                                 
        KeyId.PAUSE             : _C_WinApi.VK_PAUSE,         
        KeyId.CAPS_LOCK         : _C_WinApi.VK_CAPITAL,       
        KeyId.ESCAPE            : _C_WinApi.VK_ESCAPE,        
        KeyId.SPACE             : _C_WinApi.VK_SPACE,         
        KeyId.PAGE_UP           : _C_WinApi.VK_PRIOR,         
        KeyId.PAGE_DOWN         : _C_WinApi.VK_NEXT,          
        KeyId.END               : _C_WinApi.VK_END,           
        KeyId.HOME              : _C_WinApi.VK_HOME,          
        KeyId.ARROW_LEFT        : _C_WinApi.VK_LEFT,          
        KeyId.ARROW_UP          : _C_WinApi.VK_UP,            
        KeyId.ARROW_RIGHT       : _C_WinApi.VK_RIGHT,         
        KeyId.ARROW_DOWN        : _C_WinApi.VK_DOWN,          
        KeyId.PRINT             : _C_WinApi.VK_PRINT,         
        KeyId.PRINT_SCREEN      : _C_WinApi.VK_SNAPSHOT,      
        KeyId.INSERT            : _C_WinApi.VK_INSERT,        
        KeyId.DELETE            : _C_WinApi.VK_DELETE,        
        KeyId.NUMPAD_0          : _C_WinApi.VK_NUMPAD0,       
        KeyId.NUMPAD_1          : _C_WinApi.VK_NUMPAD1,       
        KeyId.NUMPAD_2          : _C_WinApi.VK_NUMPAD2,       
        KeyId.NUMPAD_3          : _C_WinApi.VK_NUMPAD3,       
        KeyId.NUMPAD_4          : _C_WinApi.VK_NUMPAD4,       
        KeyId.NUMPAD_5          : _C_WinApi.VK_NUMPAD5,       
        KeyId.NUMPAD_6          : _C_WinApi.VK_NUMPAD6,       
        KeyId.NUMPAD_7          : _C_WinApi.VK_NUMPAD7,       
        KeyId.NUMPAD_8          : _C_WinApi.VK_NUMPAD8,       
        KeyId.NUMPAD_9          : _C_WinApi.VK_NUMPAD9,       
        KeyId.NUMPAD_MULTIPLY   : _C_WinApi.VK_MULTIPLY,      
        KeyId.NUMPAD_ADD        : _C_WinApi.VK_ADD,           
        KeyId.NUMPAD_SEPARATOR  : _C_WinApi.VK_SEPARATOR,     
        KeyId.NUMPAD_SUBTRACT   : _C_WinApi.VK_SUBTRACT,      
        KeyId.NUMPAD_DECIMAL    : _C_WinApi.VK_DECIMAL,       
        KeyId.NUMPAD_DIVIDE     : _C_WinApi.VK_DIVIDE,       
        KeyId.F1                : _C_WinApi.VK_F1,            
        KeyId.F2                : _C_WinApi.VK_F2,            
        KeyId.F3                : _C_WinApi.VK_F3,            
        KeyId.F4                : _C_WinApi.VK_F4,            
        KeyId.F5                : _C_WinApi.VK_F5,            
        KeyId.F6                : _C_WinApi.VK_F6,            
        KeyId.F7                : _C_WinApi.VK_F7,            
        KeyId.F8                : _C_WinApi.VK_F8,            
        KeyId.F9                : _C_WinApi.VK_F9,            
        KeyId.F10               : _C_WinApi.VK_F10,           
        KeyId.F11               : _C_WinApi.VK_F11,           
        KeyId.F12               : _C_WinApi.VK_F12,           
        KeyId.F13               : _C_WinApi.VK_F13,           
        KeyId.F14               : _C_WinApi.VK_F14,           
        KeyId.F15               : _C_WinApi.VK_F15,           
        KeyId.F16               : _C_WinApi.VK_F16,           
        KeyId.F17               : _C_WinApi.VK_F17,           
        KeyId.F18               : _C_WinApi.VK_F18,           
        KeyId.F19               : _C_WinApi.VK_F19,           
        KeyId.F20               : _C_WinApi.VK_F20,           
        KeyId.F21               : _C_WinApi.VK_F21,           
        KeyId.F22               : _C_WinApi.VK_F22,           
        KeyId.F23               : _C_WinApi.VK_F23,           
        KeyId.F24               : _C_WinApi.VK_F24,           
        KeyId.NUM_0             : ord('0'),                   
        KeyId.NUM_1             : ord('1'),                   
        KeyId.NUM_2             : ord('2'),                   
        KeyId.NUM_3             : ord('3'),                   
        KeyId.NUM_4             : ord('4'),                   
        KeyId.NUM_5             : ord('5'),                   
        KeyId.NUM_6             : ord('6'),                   
        KeyId.NUM_7             : ord('7'),                   
        KeyId.NUM_8             : ord('8'),                   
        KeyId.NUM_9             : ord('9'),                   
        KeyId.A                 : ord('A'),                   
        KeyId.B                 : ord('B'),                   
        KeyId.C                 : ord('C'),                   
        KeyId.D                 : ord('D'),                   
        KeyId.E                 : ord('E'),                   
        KeyId.F                 : ord('F'),                   
        KeyId.G                 : ord('G'),                   
        KeyId.H                 : ord('H'),                   
        KeyId.I                 : ord('I'),                   
        KeyId.J                 : ord('J'),                   
        KeyId.K                 : ord('K'),                   
        KeyId.L                 : ord('L'),                   
        KeyId.M                 : ord('M'),                   
        KeyId.N                 : ord('N'),                   
        KeyId.O                 : ord('O'),                   
        KeyId.P                 : ord('P'),                   
        KeyId.Q                 : ord('Q'),                   
        KeyId.R                 : ord('R'),                   
        KeyId.S                 : ord('S'),                   
        KeyId.T                 : ord('T'),                   
        KeyId.U                 : ord('U'),                   
        KeyId.V                 : ord('V'),                   
        KeyId.W                 : ord('W'),                   
        KeyId.X                 : ord('X'),                   
        KeyId.Y                 : ord('Y'),                   
        KeyId.Z                 : ord('Z'),                   
                                 
        KeyId.SEMICOLON         : _C_WinApi.VK_OEM_1,         
        KeyId.FORWARD_SLASH     : _C_WinApi.VK_OEM_2,         
        KeyId.ACUTE             : _C_WinApi.VK_OEM_3,         
        KeyId.OPEN_BRACKET      : _C_WinApi.VK_OEM_4,         
        KeyId.BACK_SLASH        : _C_WinApi.VK_OEM_5,         
        KeyId.CLOSE_BRACKET     : _C_WinApi.VK_OEM_6,         
        KeyId.APOSTROPHE        : _C_WinApi.VK_OEM_7,         
        KeyId.COMMA             : _C_WinApi.VK_OEM_COMMA,     
        KeyId.DOT               : _C_WinApi.VK_OEM_PERIOD,    
        KeyId.DASH              : _C_WinApi.VK_OEM_MINUS,     
        KeyId.EQUAL             : _C_WinApi.VK_OEM_PLUS,     
                                 
        KeyId.NUMLOCK           : _C_WinApi.VK_NUMLOCK,       
        KeyId.SCROLL_LOCK       : _C_WinApi.VK_SCROLL,
    }.get(int(key_id), 0)

def vk_code_to_key_id(vk_code):
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

def get_key_id_from_w_param(w_param):
    """
    w_param : int
    Returns (KeyId).
    """
    return vk_code_to_key_id(w_param)

def get_mouse_key_id(message, w_param):
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

def is_mouse_button_down(message):
    """
    message : int
    Returns (bool).
    """
    return int(message) in (_C_WinApi.WM_LBUTTONDOWN, _C_WinApi.WM_RBUTTONDOWN, _C_WinApi.WM_MBUTTONDOWN, _C_WinApi.WM_XBUTTONDOWN)

def get_keyboard_side_id(key_id, virtual_key_data):
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

def vk_code_to_str(vk_code):
    """
    Returns (str).
    """
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

def is_mw_mouse_button(window_message):
    """
    Returns (bool).
    """
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

def is_mw_mouse_button_x(window_message):
    """
    Returns (bool).
    """
    return window_message in [
        _C_WinApi.WM_XBUTTONDOWN,
        _C_WinApi.WM_XBUTTONUP
    ]

