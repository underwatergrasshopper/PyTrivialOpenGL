from .Size import Size

__all__ = [
    "Point",
]

class Point:
    """
    x : int | float
    y : int | float

    Exceptions: ValueError - When to x or y is assigned value which is neither int or float.
    """
    def __init__(self, x, y):
        """
        x : int | float
        y : int | float
        Exceptions: ValueError - When x or y is neither int or float.
        """
        self.x = x
        self.y = y

    def is_zero(self):
        """
        Returns (bool) True - when both x and y are equal to 0.
        """
        return self.x == 0 and self.y == 0

    def to_tuple(self):
        """
        Returns (tuple[T, T]) (x, y).
        """
        return (self.x, self.y)

    def to_tuple_i(self):
        """
        Returns (tuple[int, int]) (x, y).
        """
        return (int(self.x), int(self.y))

    def to_tuple_f(self):
        """
        Returns (tuple[float, float]) (x, y).
        """
        return (float(self.x), float(self.y))

    ### logic ###

    def __eq__(self, other): # ==
        return self.x == other.x and self.y == other.y

    def __ne__(self, other): # !=
        return self.x != other.x or self.y != other.y

    def __gt__(self, other): # >
        return (self.x > other.x and self.y >= other.y) or (self.x == other.x and self.y > other.y)

    def __lt__(self, other): # <
        return (self.x < other.x and self.y <= other.y) or (self.x == other.x and self.y < other.y)

    def __ge__(self, other): # >=
        return self.x >= other.x and self.y >= other.y

    def __le__(self, other): # <=
        return self.x <= other.x and self.y <= other.y  

    ### arithmetic ###

    def __add__(self, other): # +
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        if isinstance(other, Size):
            return Point(self.x + other.width, self.y + other.height)
        return Point(self.x + other, self.y + other)

    def __sub__(self, other): # -
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        if isinstance(other, Size):
            return Point(self.x - other.width, self.y - other.height)
        return Point(self.x - other, self.y - other)

    def __mul__(self, other): # *
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        if isinstance(other, Size):
            return Point(self.x * other.width, self.y * other.height)
        return Point(self.x * other, self.y * other)

    def __truediv__(self, other): # /
        if isinstance(other, Point):
            return Point(self.x / other.x, self.y / other.y)
        if isinstance(other, Size):
            return Point(self.x / other.width, self.y / other.height)
        return Point(self.x / other, self.y / other)

    def __floordiv__(self, other): # //
        if isinstance(other, Point):
            return Point(self.x // other.x, self.y // other.y)
        if isinstance(other, Size):
            return Point(self.x // other.width, self.y // other.height)
        return Point(self.x // other, self.y // other)

    def __div__(self, other): # /
        if isinstance(other, Point):
            return Point(self.x / other.x, self.y / other.y)
        if isinstance(other, Size):
            return Point(self.x / other.width, self.y / other.height)
        return Point(self.x / other, self.y / other)

    def __setattr__(self, name, value):
        if isinstance(value, (int, float)):
            self.__dict__[name] = value
        else:
            try:
                value = int(value)
            except:
                raise TypeError("Value of '%s' can not be converted to int." % (name))

            self.__dict__[name] = value