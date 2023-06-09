__all__ = [
    "Color4",
    "Color4U8",
    "Color4F",
]

################################################################################
# Color
################################################################################

class Color4:
    """
    Abstract class for representing four channel color (red, green, blue, alpha)
    """

    def rgba(self):
        """
        Returns tuple containing each color channel.
        """
        raise Exception("Abstract method is not defined.")

    def to_color4u8(self):
        """
        Returns color where all channels are converted to int on range 0..255.
        """
        raise Exception("Abstract method is not defined.")

    def to_color4f(self):
        """
        Returns color where all channels are converted to float on range 0..1.
        """
        raise Exception("Abstract method is not defined.")


class Color4U8:
    """
    Represents four channel color.

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
        Returns tuple[int, int, int, int]       Value range of each channel: 0..255.
        """
        return (self.r, self.g, self.b, self.a)

    def to_color4u8(self):
        """
        Returns color where all channels are converted to int on range 0..255.
        """
        return self

    def to_color4f(self):
        """
        Returns color where all channels are converted to float on range 0..1.
        """
        return Color4F(self.r / 255.0, self.g / 255.0, self.b / 255.0, self.a / 255.0)

    def __setattr__(self, name, value):
        try:
            value = int(value)
        except:
            raise ValueError("Value of '%s' can not be converted to int." % (name))

        if not (0 <= value and value <= 255):
            raise ValueError("Value of '%s' is out of acceptable range 0..255." % (name))

        self.__dict__[name] = value

class Color4F:
    """
    Represents four channel color.

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
        Returns tuple[float, float, float, float]       Value range of each channel: 0..1.
        """
        return (self.r, self.g, self.b, self.a)

    def to_color4u8(self):
        """
        Returns color where all channels are converted to int on range 0..255.
        """
        return Color4U8(self.r * 255, self.g * 255, self.b * 255, self.a * 255)

    def to_color4f(self):
        """
        Returns color where all channels are converted to float on range 0..1.
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



