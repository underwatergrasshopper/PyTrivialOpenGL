from .FineText  import *
from .Font      import *

class TextAdjuster:
    def __init__(self):
        self._number_of_spaces_in_tab   = 4
        self._wrap_line_width           = 0
        self._width_of_full_tab         = 0     
        self._line_width                = 0

    def reset(self):
        """
        Restores default values.
        """
        self.set_line_wrap_width(0)
        self.set_number_of_spaces_in_tab(4)

    def set_number_of_spaces_in_tab(self, number):
        """
        number : int | SupportsInt
            Default value is 4.
        """
        if not isinstance(number, int):
            try:
                number = int(number)
            except Exception as exception:
                raise ValueError("Value of 'number' is not convertible to int.") from exception

        self._number_of_spaces_in_tab = number

    def set_line_wrap_width(self, width):
        """
        Sets line width in pixels after which words are wrapped.

        width : int | SupportsInt
            Default value is 0. Which means: no line wrap.
        """
        if not isinstance(width, int):
            try:
                width = int(width)
            except Exception as exception:
                raise ValueError("Value of 'width' is not convertible to int.") from exception

        self._wrap_line_width = width


    def adjust_text(self, font, fine_text):
        """
        Adjust text by using word wrapping and replaces tabs with equivalent in length (in pixels) in spaces.

        font        : Font
        fine_text   : FineText
        Returns     : FineText
        """
        if not isinstance(font, Font):
            raise TypeError("Type of 'font' is unexpected.")

        if not isinstance(fine_text, FineText):
            raise TypeError("Type of 'fine_text' is unexpected.")

        adjusted_fine_text = FineText()

        if font.is_loaded():
            self._line_width = 0 # in pixels

            for element in fine_text.to_elements():
                if isinstance(element, Text):
                    adjusted_fine_text += self._prepare_text(font, element.get_content())

                elif isinstance(element, TextHorizontalSpacer):
                    adjusted_fine_text += self._prepare_text_horizontal_spacer(font, element.get_width())

                elif isinstance(element, (ColorB, ColorF)):
                    adjusted_fine_text.append(element)
                else:
                    raise TypeError("'%s' as type of element from 'fine_text' is unexpected." % type(element).__name__)
        else:
            adjusted_fine_text = fine_text

        return adjusted_fine_text

    def _get_sentence_part_pos(self, sentence, current_pos):
        """
        <sentence_part>
            '\t'         # tab
            '\n'         # new line
            ' '          # space
            '[^\t\n ]'   # word (any array of characters which doesn't contain tab, new line or space

        sentence : str
        current_pos : int
        Returns : int | None
        """
        def is_white_space(c):
            return c in [" ", "\t", "\n"]

        for next_sentence_part_pos in range(current_pos, len(sentence)):
            if is_white_space(sentence[next_sentence_part_pos]):
                return next_sentence_part_pos + 1
            if next_sentence_part_pos + 1 < len(sentence) and is_white_space(sentence[next_sentence_part_pos + 1]):
                return next_sentence_part_pos + 1
        
        return None

    def _split_sentence_to_parts(self, sentence):
        """
        sentence : str
        Returns : List[str]
        """
        parts = []

        pos = 0
        while pos < len(sentence):

            next_part_pos = self._get_sentence_part_pos(sentence, pos)

            if next_part_pos is not None:
                part = sentence[pos:next_part_pos]
            else:
                part = sentence[pos:]
                break

            parts.append(part)
            pos = next_part_pos

        return parts

    def _get_sentence_width(self, font, sentence):
        """
        font        : Font
        sentence    : str
        Returns     : int
        """
        width = 0
        is_glyph_before = False

        for c in sentence:
            if c == '\t':
                if is_glyph_before: 
                    width += font.get_distance_between_glyphs()

                width += font.get_glyph_size(' ').width * self._num_of_spaces_in_tab
                if self._num_of_spaces_in_tab > 1:
                   width += font.get_distance_between_glyphs() * self._num_of_spaces_in_tab - 1

                is_glyph_before = True
            elif c == '\n':
                is_glyph_before = False
            else:
                if is_glyph_before: 
                    width += font.get_distance_between_glyphs()

                width += font.get_glyph_size(c).width
                is_glyph_before = True

        return width
    

    def _get_sentence_size(self, font, sentence):
        """
        font        : Font
        sentence    : str
        Returns     : Size
        """
        return Size(self._get_sentence_width(font, sentence), font.get_height())

    def _prepare_text_horizontal_spacer(self, font, text_horizontal_space_width):
        """
        font                        : Font
        text_horizontal_space_width : int
        Returns                     : FineText
        """
        prepared_fine_text = FineText()

        if text_horizontal_space_width + self._line_width > self._wrap_line_width:
            prepared_fine_text.append(Text("\n"))
            self._line_width = 0
        
        prepared_fine_text.append(TextHorizontalSpacer(text_horizontal_space_width))
        self._line_width += text_horizontal_space_width

        return prepared_fine_text

    def _prepare_text(self, font, text):
        """
        font                        : Font
        text                        : str
        Returns                     : FineText
        """
        prepared_fine_text = FineText()
        prepared_text = ""

        sentence_parts = self._split_sentence_to_parts(text)

        is_glyph_before = False

        for part in sentence_parts:
            # Any first glyph in line don't have spacing. Only following ones.
            part_width = self._get_sentence_width(font, part)
            if is_glyph_before:
                part_width += font.get_distance_between_glyphs()

            if part == "\n":
                # New line.
                prepared_text       += part
                self._line_width    = 0

                is_glyph_before = False
            elif part == "\t":
                # Tab.
                width_of_full_tab = part_width

                width_of_tab = width_of_full_tab - (self._line_width % width_of_full_tab)
                if width_of_tab == 0:
                    width_of_tab = width_of_full_tab
                        
                if self._wrap_line_width != 0 and (self._line_width + width_of_full_tab) > self._wrap_line_width:
                    prepared_text       += "\n"
                    self._line_width    = 0

                    width_of_tab = width_of_full_tab

                # To preserve same length of tabs, horizontal spacer is used for custom pixel perfect lengths.
                prepared_fine_text.append(prepared_text, width_of_tab)
                prepared_text = ""

                self._line_width += width_of_tab;

                is_glyph_before = True
            else:
                # Word or Space.
                if self._wrap_line_width != 0 and (self._line_width + part_width) > self._wrap_line_width:
                    # Word or Space is crossing wrap line width. Needs to be moved or split.

                    if part == " ":
                        # Spaces are ignored if they are behind wrap line width.
                        # Current value of is_glyph_before is preserved. 
                        pass
                    else:
                        # Word.
                        if part_width > self._wrap_line_width:
                            # Word is longer than line. Must be split between two or multiple lines.
                            long_part       = part          # str
                            long_part_width = part_width    # int

                            while long_part_width > self._wrap_line_width:
                                line_width_left = self._wrap_line_width - self._line_width 

                                glyph_count = font.get_glyph_count_in_width(long_part, line_width_left)

                                prepared_text   += long_part[0:glyph_count]
                                prepared_text   += "\n"
                                self._line_width      = 0

                                long_part       = long_part[glyph_count:]
                                long_part_width = self._get_sentence_width(font, long_part)
                            

                            prepared_text       += long_part
                            self._line_width    += long_part_width
                        else:
                            # Word is shorter than line. Whole word is moved to next line.
                            prepared_text       += "\n"
                            self._line_width    = 0

                            prepared_text       += part
                            self._line_width    += part_width
                        
                        is_glyph_before = True
                    
                else:
                    # Entire Word or Space fits in line.
                    prepared_text       += part
                    self._line_width    += part_width

                    is_glyph_before = True

        prepared_fine_text.append(prepared_text)

        return prepared_fine_text
