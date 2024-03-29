# This module and modules imported below are logically part of one module.
from .Size  import *
from .Point import *

class Area:
    """
    Represents area from position (x, y) and size (width, height).

    x       : int | float | SupportsInt
    y       : int | float | SupportsInt
    width   : int | float | SupportsInt
    height  : int | float | SupportsInt
    """
    def __init__(self, x, y, width, height):
        """
        x       : int | float | SupportsInt
        y       : int | float | SupportsInt
        width   : int | float | SupportsInt
        height  : int | float | SupportsInt

        Exceptions
            ValueError
                When x, y width or height is neither int or float or can not be converted to int.
        """
        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height

    def is_zero(self):
        """
        Returns     : bool
            True - when both x, y width and height are equal to 0.
        """
        return self.x == 0 and self.y == 0 and self.width == 0 and self.height == 0

    def to_tuple(self):
        """
        Returns     : Tuple[T, T, T, T]
            (x, y, width, height).
        """
        return (self.x, self.y, self.width, self.height)

    def to_tuple_i(self):
        """
        Returns     : Tuple[int, int, int, int]) 
            (x, y, width, height).
        """
        return (int(self.x), int(self.y), int(self.width), int(self.height))

    def to_tuple_f(self):
        """
        Returns     : Tuple[float, float, float, float] 
            (x, y, width, height).
        """
        return (float(self.x), float(self.y), float(self.width), float(self.height))

    def get_pos(self):
        """
        Returns     : Point
        """
        return Point(self.x, self.y)

    def get_size(self):
        """
        Returns     : Size
        """
        return Size(self.width, self.height)

    def is_in(self, pos):
        """
        pos         : Point
        Returns     : bool
            True - When pos is in area.
        """
        if not isinstance(pos, Point):
            raise TypeError("Unexpected type of 'pos'.")

        return pos.is_between(self.get_pos(), self.get_pos() + self.get_size())

    def get_area_i(self):
        """
        Converts all variables to int.

        Returns     : Area
        """
        return Area(
            x = int(self.x),
            y = int(self.y),
            width = int(self.width),
            height = int(self.height)
        )

    def __str__(self):
        return "%s %s %s %s" % (self.x, self.y, self.width, self.height)

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.width
        yield self.height

    ### logic ###

    def __eq__(self, other): # ==
        return self.x == other.x and self.y == other.y and self.width == other.width and self.height == other.height

    def __ne__(self, other): # !=
        return self.x != other.x or self.y != other.y or self.width != other.width or self.height != other.height

    ### arithmetic ###

    def __add__(self, other): # +
        if isinstance(other, Point):
            return Area(self.x + other.x, self.y + other.y, self.width, self.height)
        if isinstance(other, Size):
            return Area(self.x, self.y, self.width + other.width, self.height + other.height)
        return Area(self.x + other.x, self.y + other.y, self.width + other.width, self.height + other.height)

    def __sub__(self, other): # -
        if isinstance(other, Point):
            return Area(self.x - other.x, self.y - other.y, self.width, self.height)
        if isinstance(other, Size):
            return Area(self.x, self.y, self.width - other.width, self.height - other.height)
        return Area(self.x - other.x, self.y - other.y, self.width - other.width, self.height - other.height)

    def __setattr__(self, name, value):
        if isinstance(value, (int, float)):
            self.__dict__[name] = value
        else:
            try:
                value = int(value)
            except:
                raise ValueError("Value of '%s' can not be converted to int." % (name))

            self.__dict__[name] = value