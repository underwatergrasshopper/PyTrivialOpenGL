from .Font          import *
from .TextAdjuster  import *

from .              import C_GL as _C_GL

class TextDrawer:
    """
    _origin_id              : OringinId
    _orientation_factor_y   : int
    _pos                    : Point
    _base                   : Point
    _color                  : ColorF
    _text                   : FineText()
    """
    def __init__(self):
        self.reset()

    def reset(self):
        self._set_origin(OriginId.LEFT_BOTTOM)
        self._set_pos(Point(0, 0))

        self._color     = ColorF(1, 1, 1, 1)
        self._text      = FineText()

    def set_origin(self, origin_id):
        """
        Sets origin of coordinate system to be in specific place in window area rectangle.

        origin_id : OriginId
        """
        if not isinstance(origin_id, OriginId):
            raise TypeError("Type of 'origin_id' is unexpected.")

        self._set_origin(origin_id)

    def get_origin_id(self):
        """
        Returns : OriginId
        """
        return self._origin_id

    def set_pos(self, x = None , y = None , pos = None):
        """
        Sets start position, for rendering text.

        x : int | SupportsInt | None
        y : int | SupportsInt | None
        pos : Point | Tuple[int | SupportsInt, int | SupportsInt] | None

        Expected combination of arguments:
        When both 'x' and 'y' are None, then 'pos' must be not None.
        When both 'x' and 'y' are not None, then 'pos' must be None.

        Exceptions
            ValueError 
                When unexpected combination of arguments.
            TypeError
                When type of argument is unexpected.
        """
        if (x is not None) and (x is not None) and (pos is None):
            if not isinstance(x, int):
                try:
                    x = int(x)
                except Exception as exception:
                    raise ValueError("Value of 'x' is not convertible to int.") from exception

            if not isinstance(y, int):
                try:
                    y = int(y)
                except Exception as exception:
                    raise ValueError("Value of 'y' is not convertible to int.") from exception

            pos = Point(x, y)

        elif (x is None) and (x is None) and (pos is not None):
            if isinstance(pos, tuple):
                if len(pos) != 2:
                    raise ValueError("Length of 'pos' is unexpected. Should be 2.")

                try:
                    pos = [int(item) for item in pos]
                except Exception as exception:
                    raise ValueError("One of values from 'pos' is not convertible to int.") from exception

                pos = Point(pos[0], pos[1])

            elif not isinstance(pos, Point):
                raise TypeError("Type of 'pos' is unexpected.")

        else:
            if pos is not None:
                if x is not None:
                    raise TypeError("Unexpected combination of arguments. Assignment to 'x' shouldn't be present when assignment to 'pos' is present")
                if y is not None:
                    raise TypeError("Unexpected combination of arguments. Assignment to 'y' shouldn't be present when assignment to 'pos' is present")

            if (x is None) and (x is None):
                    raise TypeError("Unexpected combination of arguments. At least assignment to 'x' and 'y' must be present.")

        self._set_pos(pos)


    def set_color(self, r = None, g = None, b = None, a = None, color = None):
        """
        r : int | SupportsInt | None
            Expected range from 0 to 255.
        g : int | SupportsInt | None
            Expected range from 0 to 255.
        b : int | SupportsInt | None
            Expected range from 0 to 255.
        a : int | SupportsInt | None
            Expected range from 0 to 255.
        color : ColorF | ColorB | Tuple[int | SupportsInt, int | SupportsInt, int | SupportsInt, int | SupportsInt]
            When tuple:
                Contains four channels (red, green, blue, alpha).
                Expected range of each channel from 0 to 255.

        Expected combination of arguments:
        When both 'r', 'g', 'b' and 'a' are None, then 'color' must be not None.
        When both 'r', 'g', 'b' and 'a' are not None, then 'color' must be None.

        Exceptions
            ValueError 
                When unexpected combination of arguments.
            TypeError
                When type of argument is unexpected.
        """
        if (r is not None) and (g is not None) and (b is not None) and (a is not None) and (color is None):
            if not isinstance(r, int):
                try:
                    r = int(r)
                except Exception as exception:
                    raise ValueError("Value of 'r' is not convertible to int.") from exception

            if not isinstance(g, int):
                try:
                    g = int(g)
                except Exception as exception:
                    raise ValueError("Value of 'g' is not convertible to int.") from exception

            if not isinstance(b, int):
                try:
                    b = int(b)
                except Exception as exception:
                    raise ValueError("Value of 'b' is not convertible to int.") from exception

            if not isinstance(a, int):
                try:
                    a = int(a)
                except Exception as exception:
                    raise ValueError("Value of 'a' is not convertible to int.") from exception

            color = ColorF(r, g, b, a)

        elif (r is None) and (g is None) and (b is None) and (a is None) and (color is not None):
            if isinstance(color, tuple):
                if len(color) != 4:
                    raise ValueError("Length of 'color' is unexpected. Should be 4.")

                try:
                    color = [int(item) for item in color]
                except Exception as exception:
                    raise ValueError("One of values from 'color' is not convertible to float.") from exception

                color = ColorF(color[0], color[1])
                
            elif isinstance(color, ColorB):
                color = color.to_color_f()

            elif not isinstance(color, ColorF):
                raise TypeError("Type of 'pos' is unexpected.")

        else:
            if color is not None:
                if r is not None:
                    raise TypeError("Unexpected combination of arguments. Assignment to 'r' shouldn't be present when assignment to 'color' is present")
                if g is not None:
                    raise TypeError("Unexpected combination of arguments. Assignment to 'g' shouldn't be present when assignment to 'color' is present")
                if b is not None:
                    raise TypeError("Unexpected combination of arguments. Assignment to 'b' shouldn't be present when assignment to 'color' is present")
                if a is not None:
                    raise TypeError("Unexpected combination of arguments. Assignment to 'a' shouldn't be present when assignment to 'color' is present")


            if (r is None) and (g is None) and (b is None) and (a is None) :
                    raise TypeError("Unexpected combination of arguments. At least assignment to 'r', 'g', 'b' and 'a' must be present.")

        self._color = color

    def get_text_size(self, font, text):
        """
        font        : Font
        text        : str | FineText
        Returns     : Size
        """
        if not isinstance(font, Font):
            raise TypeError("Type of 'font' is unexpected.")

        if isinstance(text, str):
            fine_text = FineText(text)
        if isinstance(text, FineText):
            fine_text = text
        else:
            try:
                text = str(text)
            except Exception as exception:
                raise ValueError("Value of 'text' is not convertible to str.") from exception

            fine_text = FineText(text)

        size = Size(0, font.get_heigth())
        width = 0

        is_glyph_before = False
    
        if font.is_loaded():
            for element in fine_text.to_elements():
                if isinstance(element, Text):
                    for c in element.get_content():
                        if c == '\n':
                            size.height += font.get_height() + font.get_distance_between_lines()

                            if size.width < width:
                               size.width = width
                            width = 0

                            is_glyph_before = False
                        else:
                            if is_glyph_before:
                                width += font.get_distance_between_glyphs()
                                
                            code_point = ord(c)
                            width += font._get_glyph_size(code_point).width

                            is_glyph_before = True
  
                elif isinstance(element, (ColorB, ColorF)):
                    pass
                
                elif isinstance(element, TextHorizontalSpacer):
                    width += element.get_width()
                    is_glyph_before = False
            
            if size.width < width:
               size.width = width

        return size


    def render_text(self, font, text):
        """
        Renders text. After rendering, sets start position, for drawing text, at the end of rendered text.
        font : Font
        text : str | FineText
        """
        if not isinstance(font, Font):
            raise TypeError("Type of 'font' is unexpected.")

        if isinstance(text, str):
            fine_text = FineText(text)
        if isinstance(text, FineText):
            fine_text = text
        else:
            try:
                text = str(text)
            except Exception as exception:
                raise ValueError("Value of 'text' is not convertible to str.") from exception

            fine_text = FineText(text)

        if font.is_loaded():
            old_origin_id = font.get_origin_id()
            font.set_origin_id(self._origin_id)

            _C_GL.glPushAttrib(_C_GL.GL_CURRENT_BIT)
            c = self._color
            _C_GL.glColor4f(c.r, c.g, c.b, c.a)

            for element in fine_text.to_elements():
                if isinstance(element, Text):
                    font._render_begin()
                    
                    for c in element.get_content():
                        if c == '\n':
                            self._pos.x = self._base.x
                            self._pos.y += (font.get_heigth() + font.get_distance_between_lines()) * self._orientation_factor_y
                        else:
                            _C_GL.glPushMatrix()
                            _C_GL.glTranslatef(self._pos.x, self._pos.y, 0)
    
                            code_point = ord(c)

                            font._render_glyph(code_point)
                            self._pos.x += font._get_glyph_size(code_point).width + font.get_distance_between_glyphs()

                            _C_GL.glPopMatrix()

                    font._render_end()

                elif isinstance(element, ColorB):
                    c = element.to_color_f()
                    _C_GL.glColor4f(c.r, c.g, c.b, c.a)

                elif isinstance(element, ColorF):
                    c = element
                    _C_GL.glColor4f(c.r, c.g, c.b, c.a)
 
                elif isinstance(element, TextHorizontalSpacer):
                    self._pos.x += element.get_width()

            _C_GL.glPopAttrib()

            font.set_origin_id(old_origin_id)

    def _set_origin(self, origin_id):
        """
        origin_id : OriginId
        """
        self._origin_id = origin_id
        self._orientation_factor_y = -1 if self._origin_id == OriginId.LEFT_BOTTOM else 1

    def _set_pos(self, pos):
        """
        pos : Point
        """
        self._pos   = pos.copy()
        self._base  = pos.copy()



