from .Color import *

from copy import deepcopy as _deepcopy

class Text:
    """
    _text : str
    """
    def __init__(self, content):
        """
        content : str | Any
        """
        self.set_content(content)

    def get_content(self):
        """
        returns : str
        """
        return self._text

    def set_content(self, content):
        """
        content : str | Any
        """
        if not isinstance(content, str):
            try:
                content = str(content)
            except Exception as exception:
                raise ValueError("Value of 'content' is not convertible to str.") from exception

        self._text = content


class TextHorizontalSpacer:
    def __init__(self, width):
        """
        width : int | SupportsInt
            Space in pixels.
        """
        self.set_width(width)

    def set_width(self, width):
        """
        width : int | SupportsInt
        """
        if not isinstance(width, int):
            try:
                width = int(width)
            except Exception as exception:
                raise ValueError("Value of 'width' is not convertible to int.") from exception

        self._width = width

    def get_width(self):
        """
        returns : int
        """
        return self._width


class FineText:
    def __init__(self, *elements):
        """
        elements : List[Text | str | TextHorizontalSpacer | int | ColorF | ColorB | Tuple[int | SupportsInt, int | SupportsInt, int | SupportsInt, int | SupportsInt] | Tuple[int | SupportsInt, int | SupportsInt, int | SupportsInt]]
            When type of item from list is:
                Text | str
                    Then it is interpreted as text.
                TextHorizontalSpacer | int
                    Then is interpreted as horizontal space in pixels.
                ColorF 
                    Then is interpreted as color of text with alpha. Value range is from 0.0 to 1.0.
                ColorB
                    Then is interpreted as color of text with alpha. Value range is from 0 to 255.
                Tuple[int | SupportsInt, int | SupportsInt, int | SupportsInt, int | SupportsInt]
                    Then is interpreted as color of text with alpha (rgba). Value range is from 0 to 255.

        """

        self._elements = []

        try:
            self.append(*elements)
        except Exception as e:
            raise e

    def clear(self):
        self._elements.clear()

    def append(self, *elements):
        """
        elements : List[Text | str | TextHorizontalSpacer | int | ColorF | ColorB | Tuple[int | SupportsInt, int | SupportsInt, int | SupportsInt, int | SupportsInt] | Tuple[int | SupportsInt, int | SupportsInt, int | SupportsInt]]
            When type of item from list is:
                Text | str
                    Then it is interpreted as text.
                TextHorizontalSpacer | int
                    Then is interpreted as horizontal space in pixels.
                ColorF 
                    Then is interpreted as color of text with alpha. Value range is from 0.0 to 1.0.
                ColorB
                    Then is interpreted as color of text with alpha. Value range is from 0 to 255.
                Tuple[int | SupportsInt, int | SupportsInt, int | SupportsInt, int | SupportsInt]
                    Then is interpreted as color of text with alpha (rgba). Value range is from 0 to 255.
        """

        if not isinstance(elements, list):
            raise TypeError("Type of 'elements' is not list.")

        index = 0
        for element in elements:
            if isinstance(element, Text):
                self._elements.append(_deepcopy(element))
            elif isinstance(element, str):
                self._elements.append(Text(element))

            elif isinstance(element, TextHorizontalSpacer):
                self._elements.append(_deepcopy(element))
            elif isinstance(element, int):
                self._elements.append(TextHorizontalSpacer(element))

            elif isinstance(element, ColorF):
                self._elements.append(_deepcopy(element))
            elif isinstance(element, ColorB):
                self._elements.append(_deepcopy(element))
            elif isinstance(element, tuple):
                if len(element) == 4: # RGBA
                    try:
                        element = [int(item) for item in element]
                    except Exception as exception:
                        raise ValueError("At %d item of 'elements'. At least on value of tuple is not convertible to int." % index) from exception

                    self._elements.append(ColorB(element[0], element[1], element[2], element[3]))
                elif len(element) == 3: #RGB
                    try:
                        element = [int(item) for item in element]
                    except Exception as exception:
                        raise ValueError("At %d item of 'elements'. At least on value of tuple is not convertible to int." % index) from exception

                    self._elements.append(ColorB(element[0], element[1], element[2], 255))
                else:
                    raise ValueError("At %d item of 'elements'. Unexpected number of items in tuple." % index)

            index += 1


    def to_elements(self):
        """
        Returns : List[Text | TextHorizontalSpacer | ColorF | ColorB]
        """
        return self._elements()

    def __iadd__(self, other):
        if not isinstance(other, FineText):
            raise TypeError("Type of 'other' is unexpected. Only object of FineText is acceptable.")
        self._elements.extend(other)

        