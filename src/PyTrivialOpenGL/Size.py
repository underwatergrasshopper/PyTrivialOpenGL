__all__ = [
    "Size",
]

class Size:
    """
    width   : int | float
    height  : int | float

    Exceptions
        ValueError
            When to x or y is assigned value which is neither int or float.
    """
    def __init__(self, width, height):
        """
        width   : int | float | SupportsInt
        height  : int | float | SupportsInt

        Exceptions
            ValueError
                When x or y is neither int or float.
        """
        self.width  = width
        self.height = height

    def is_zero(self):
        """
        Returns : bool
            True - when both x and y are equal to 0.
        """
        return self.width == 0 and self.height == 0

    def to_tuple(self):
        """
        Returns : Tuple[T, T]
            (x, y).
        """
        return (self.width, self.height)

    def to_tuple_i(self):
        """
        Returns : Tuple[int, int] 
            (x, y).
        """
        return (int(self.width), int(self.height))

    def to_tuple_f(self):
        """
        Returns : Tuple[float, float]
            (x, y).
        """
        return (float(self.width), float(self.height))

    ### logic ###

    def __eq__(self, other): # ==
        return self.width == other.width and self.height == other.height

    def __ne__(self, other): # !=
        return self.width != other.width or self.height != other.height

    def __gt__(self, other): # >
        return self.width > other.width and self.height > other.height

    def __lt__(self, other): # <
        return self.width < other.width and self.height < other.height

    def __ge__(self, other): # >=
        return self.width >= other.width and self.height >= other.height

    def __le__(self, other): # <=
        return self.width <= other.width and self.height <= other.height  

    ### arithmetic ###

    def __add__(self, other): # +
        if isinstance(other, Size):
            return Size(self.width + other.width, self.height + other.height)
        return Size(self.width + other, self.height + other)

    def __sub__(self, other): # -
        if isinstance(other, Size):
            return Size(self.width - other.width, self.height - other.height)
        return Size(self.width - other, self.height - other)

    def __mul__(self, other): # *
        if isinstance(other, Size):
            return Size(self.width * other.width, self.height * other.height)
        return Size(self.width * other, self.height * other)

    def __truediv__(self, other): # /
        if isinstance(other, Size):
            return Size(self.width / other.width, self.height / other.height)
        return Size(self.width / other, self.height / other)

    def __floordiv__(self, other): # //
        if isinstance(other, Size):
            return Size(self.width // other.width, self.height // other.height)
        return Size(self.width // other, self.height // other)

    def __div__(self, other): # /
        if isinstance(other, Size):
            return Size(self.width / other.width, self.height / other.height)
        return Size(self.width / other, self.height / other)

    def __setattr__(self, name, value):
        if isinstance(value, (int, float)):
            self.__dict__[name] = value
        else:
            try:
                value = int(value)
            except:
                raise ValueError("Value of '%s' can not be converted to int." % (name))

            self.__dict__[name] = value

    ### 

    def __str__(self):
        return "%s %s" % (self.width, self.height)

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield self.width
        yield self.height
