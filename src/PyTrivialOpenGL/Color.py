from .Basics import clamp

__all__ = [
    "Color",
    "ColorF",
    "ColorB",
]

################################################################################
# Color
################################################################################

class Color:
    """
    Abstract class.
    Should contain color with three color channels and one alpha channel. 
    """

    def __init__(self):
        raise NotImplementedError("Can not create object of abstract class 'Color'.")

    def rgba(self):
        """
        Abstract method.
        Should converts to tuple[T, T, T, T] Where tuple is (r, g, b, a).
        """
        raise NotImplementedError("Call of not implemented abstract method.")

    def to_color_b(self):
        """
        Abstract method.
        Should converts to ColorB.
        """
        raise NotImplementedError("Call of not implemented abstract method.")

    def to_color_f(self):
        """
        Abstract method.
        Should converts to ColorF.
        """
        raise NotImplementedError("Call of not implemented abstract method.")

class ColorB(Color):
    """
    Contains color with three color channels and one alpha channel. 
    Each channel value can fit in one byte.

    r : int       Red color channel. Valid value range 0..255.       
    g : int       Green color channel. Valid value range 0..255.  
    b : int       Blue color channel. Valid value range 0..255.  
    a : int       Alpha channel. Valid value range 0..255. 
    
    Assignment out of valid range to any of those variables will throw ValueError exception.
    """

    def __init__(self, r, g, b, a = 255, is_clamp = False):
        """
        r           : int       Red color channel. Valid value range 0..255.       
        g           : int       Green color channel. Valid value range 0..255.  
        b           : int       Blue color channel. Valid value range 0..255.  
        a           : int       (optional, default = 255) Alpha channel. Valid value range 0..255.  
        is_clamp    : bool      (optional, default = False) When true, then clamp values of r, g, b and a variables to valid range.
                                When false, then throws ValueError exception if any values of r, g, b or a variable is out of valid range.
        Exceptions:             ValueError - If any value of r, g, b or a variable is out of valid range.
        """
        if is_clamp:
            self.r = clamp(r, 0, 255)
            self.g = clamp(g, 0, 255)
            self.b = clamp(b, 0, 255)
            self.a = clamp(a, 0, 255)
        else:
            self.r = r
            self.g = g
            self.b = b
            self.a = a

    def rgba(self):
        """
        Converts to tuple[int, int, int, int] Where tuple is (r, g, b, a). 
        Value ranges are not changed.
        """
        return (self.r, self.g, self.b, self.a)

    def to_color_b(self):
        """
        Converts to ColorB. Value ranges are not changed.
        """
        return self

    def to_color_f(self):
        """
        Converts to ColorF. Remaps value range from 0..255 to 0..1 for each channel.
        """
        return ColorF(self.r / 255.0, self.g / 255.0, self.b / 255.0, self.a / 255.0)

    def __setattr__(self, name, value):
        try:
            value = int(value)
        except:
            raise TypeError("Value of '%s' can not be converted to int." % (name))

        if not (0 <= value and value <= 255):
            raise ValueError("Value of '%s' is out of acceptable range 0..255." % (name))

        self.__dict__[name] = value

class ColorF(Color):
    """
    Contains color with three color channels and one alpha channel.

    r : float     Red color channel. Valid value range 0..1.       
    g : float     Green color channel. Valid value range 0..1.  
    b : float     Blue color channel. Valid value range 0..1.  
    a : float     Alpha channel. Valid value range 0..1.  

    Assignment out of valid range to any of those variables will throw ValueError exception.
    """

    def __init__(self, r, g, b, a = 1, is_clamp = False):
        """
        r           : float     Red color channel. Valid value range 0..1.       
        g           : float     Green color channel. Valid value range 0..1.  
        b           : float     Blue color channel. Valid value range 0..1.  
        a           : float     (optional, default = 255)  Alpha channel. Valid value range 0..1.  
        is_clamp    : bool      (optional, default = False) When true, then clamp values of r, g, b and a variables to valid range.
                                When false, then throws ValueError exception if any values of r, g, b or a variable is out of valid range.
        Exceptions:             ValueError - If any value of r, g, b or a variable is out of valid range.
        """
        if is_clamp:
            self.r = clamp(r, 0.0, 1.0)
            self.g = clamp(g, 0.0, 1.0)
            self.b = clamp(b, 0.0, 1.0)
            self.a = clamp(a, 0.0, 1.0)
        else:
            self.r = r
            self.g = g
            self.b = b
            self.a = a

    def rgba(self):
        """
        Converts to tuple[float, float, float, float]. Where tuple is (r, g, b, a). 
        Value ranges are not changed.
        """
        return (self.r, self.g, self.b, self.a)

    def to_color_b(self):
        """
        Converts to ColorB. Remaps value range from 0..1 to 0..255 for each channel.
        """
        return ColorB(self.r * 255, self.g * 255, self.b * 255, self.a * 255)

    def to_color_f(self):
        """
        Converts to ColorF. Value ranges are not changed.
        """
        return self

    def __setattr__(self, name, value):
        try:
            value = float(value)
        except:
            raise TypeError("Value of '%s' can not be converted to float." % (name))

        if not (0.0 <= value and value <= 1.0):
            raise ValueError("Value of '%s' is out of acceptable range 0..1." % (name))

        self.__dict__[name] = value




