__all__ = [
    "ColorF",
    "ColorB",
]

################################################################################
# Color
################################################################################

class ColorB:
    """
    Represent color with three color channels and one alpha channel. 
    Each channel value can fit in one byte.
    r : int         Red color channel. Valid value range 0..255.       
    g : int         Green color channel. Valid value range 0..255.  
    b : int         Blue color channel. Valid value range 0..255.  
    a : int         Alpha channel. Valid value range 0..255.  
    """

    def __init__(self, r, g, b, a = 255):
        """
        r : int         Red color channel. Valid value range 0..255.       
        g : int         Green color channel. Valid value range 0..255.  
        b : int         Blue color channel. Valid value range 0..255.  
        a : int         Alpha channel. Valid value range 0..255.  
        """
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def rgba(self):
        """
        Converts to tuple[int, int, int, int] Where tuple is (r, g, b, a).
        """
        return (self.r, self.g, self.b, self.a)

    def to_color_b(self):
        """
        Converts to ColorB. Value ranges are not changed.
        """
        return self

    def to_color_f(self):
        """
        Converts to ColorF. Changes remap value range from 0..255 to 0..1 for each channel.
        """
        return ColorF(self.r / 255.0, self.g / 255.0, self.b / 255.0, self.a / 255.0)

    def __setattr__(self, name, value):
        try:
            value = int(value)
        except:
            raise ValueError("Value of '%s' can not be converted to int." % (name))

        if not (0 <= value and value <= 255):
            raise ValueError("Value of '%s' is out of acceptable range 0..255." % (name))

        self.__dict__[name] = value

class ColorF:
    """
    Represent color with three color channels and one alpha channel.
    r : float       Red color channel. Valid value range 0..1.       
    g : float       Green color channel. Valid value range 0..1.  
    b : float       Blue color channel. Valid value range 0..1.  
    a : float       Alpha channel. Valid value range 0..1.  
    """

    def __init__(self, r, g, b, a = 1):
        """
        r : float       Red color channel. Valid value range 0..1.       
        g : float       Green color channel. Valid value range 0..1.  
        b : float       Blue color channel. Valid value range 0..1.  
        a : float       Alpha channel. Valid value range 0..1.  
        """
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def rgba(self):
        """
        Converts to tuple[float, float, float, float]. Where tuple is (r, g, b, a).
        """
        return (self.r, self.g, self.b, self.a)

    def to_color_b(self):
        """
        Converts to ColorB. Changes remap value range from 0..1 to 0..255 for each channel.
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
            raise ValueError("Value of '%s' can not be converted to float." % (name))

        if not (0.0 <= value and value <= 1.0):
            raise ValueError("Value of '%s' is out of acceptable range 0..1." % (name))

        self.__dict__[name] = value



################################################################################
# Inner Support
################################################################################

def clamp(val, min_val, max_val):
    return max(min(val, max_val), min_val)

def clamp_u8(val):
    return clamp(int(val), 0, 255)



