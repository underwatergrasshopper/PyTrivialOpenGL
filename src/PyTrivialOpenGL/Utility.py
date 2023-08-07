from .Point         import Point
from .Size          import Size
from .Area          import Area
from ._Private      import C_WinApi as _C_WinApi
from .              import C_GL     as _C_GL
from .GL._Private   import Support  as _gl_support

import ctypes as _ctypes

__all__ = [
    "MIN_U16",
    "MAX_U16",
    "MIN_I32",
    "MAX_I32",
    "OpenGL_Version",
    "get_work_area",
    "get_screen_size",
    "get_cursor_pos_in_screen",
    "run_question_box",
    "save_as_bmp",
    "save_texture_as_bmp",
    "is_defined_in_gl",
    "is_defined_in_c_gl",
    "get_gl_error_str",
]

################################################################################

MIN_U16 = 0
MAX_U16 = 2**31 - 1

MIN_I32 = -(2**31)
MAX_I32 = 2**31 - 1

################################################################################

class OpenGL_Version:
    """
    major : int
    minor : int
    """
    def __init__(self, major, minor):
        """
        major : int | SupportsInt
        minor : int | SupportsInt
        """
        self.major = major
        self.minor = minor

    def __setattr__(self, name, value):
        if isinstance(value, int):
            self.__dict__[name] = value
        else:
            try:
                value = int(value)
            except:
                raise TypeError("Value of '%s' can not be converted to int." % (name))

            self.__dict__[name] = value

    def __str__(self):
        return "%d.%d" % (self.major, self.minor)

    def __repr__(self):
        return self.__str__()

################################################################################

def get_work_area():
    """
    Returns : Area
        Desktop area without task bar.
    """
    rc = _C_WinApi.RECT()
    _C_WinApi.SystemParametersInfoW(_C_WinApi.SPI_GETWORKAREA, 0, _ctypes.byref(rc), 0)
    return Area(rc.left, rc.top, rc.right - rc.left, rc.bottom - rc.top)


def get_work_area():
    """
    Returns : Area
    """
    rc = _C_WinApi.RECT()
    _C_WinApi.SystemParametersInfoW(_C_WinApi.SPI_GETWORKAREA, 0, _ctypes.byref(rc), 0)
    return Area(rc.left, rc.top, rc.right - rc.left, rc.bottom - rc.top)

def get_screen_size():
    """
    Returns : Size
    """
    width   = _C_WinApi.GetSystemMetrics(_C_WinApi.SM_CXSCREEN)
    height  = _C_WinApi.GetSystemMetrics(_C_WinApi.SM_CYSCREEN)
    return Size(width, height)

def get_cursor_pos_in_screen():
    """
    Returns : Point
    """
    pt = _C_WinApi.POINT()
    if _C_WinApi.GetCursorPos(_ctypes.byref(pt)):
        return Point(pt.x, pt.y)
    return Point(0, 0)

################################################################################

def run_question_box(title = None, message = None):
    """
    Run question box and waits for answer.
    title   : str | Any | None
    message : str | Any | None
    Returns : bool
        True, when 'Yes' was pressed. 
        False, when 'No' was pressed.
    """
    if title is None:
        title = ""
    elif not isinstance(title, str):
        try:
            title = str(title)
        except Exception as exception:
            raise ValueError("Value of 'title' is not convertible to str.") from exception

    if message is None:
        message = ""
    elif not isinstance(message, str):
        try:
            message = str(message)
        except Exception as exception:
            raise ValueError("Value of 'message' is not convertible to str.") from exception

    result = _C_WinApi.OwnerlessMessageBox_FromNewThreadWithWait(message, title, _C_WinApi.MB_ICONQUESTION | _C_WinApi.MB_YESNO)

    return result == _C_WinApi.IDYES


def save_as_bmp(file_name, pixel_data, width, height, is_reverse_rows):
    """
    file_name       : str | Any
        If not ends with '.bmp', then will be added to file_name.
    pixel_data      : bytes | SupportsBytes
        Contains pixels. Each pixel occupies 4 bytes.
        Each byte of pixel represent single channel (in order: red, green, blue, alpha).
    width           : int | SupportsInt
        Width of bitmap in pixels. At least 1.
    height          : int | SupportsInt
        height of bitmap in pixels. At least 1.
    is_reverse_rows : bool | Any
        True - Reverses rows.

    Returns : bool
        True - when bitmap was saved successfully.

    Exceptions
        ValueError
            When value of any argument fails conversion to expected type.
        ValueError
            When number of pixels in 'file_name' is less than 'width' * 'height'.
        ValueError
            When value of 'width' or 'height' is below 1.
    """
    if not isinstance(file_name, str):
        try:
            file_name = str(file_name)
        except Exception as exception:
            raise ValueError("Value of 'file_name' is not castable to str.") from exception

    if not isinstance(pixel_data, bytes):
        try:
            pixel_data = bytes(pixel_data)
        except Exception as exception:
            raise ValueError("Value of 'pixel_data' is not castable to bytes.") from exception

    if not isinstance(width, int):
        try:
            width = int(width)
        except Exception as exception:
            raise ValueError("Value of 'width' is not castable to int.") from exception

    if not isinstance(height, int):
        try:
            height = int(height)
        except Exception as exception:
            raise ValueError("Value of 'height' is not castable to int.") from exception

    if not isinstance(is_reverse_rows, bool):
        try:
            his_reverse_rowsight = bool(is_reverse_rows)
        except Exception as exception:
            raise ValueError("Value of 'is_reverse_rows' is not castable to bool.") from exception

    if width < 1:
        raise ValueError("Value of 'width' is less than 1.")

    if height < 1:
        raise ValueError("Value of 'height' is less than 1.")

    ext = ".bmp"
    ext_len = len(ext)
    if len(file_name) >= ext_len:
        if file_name[-ext_len:] != ext:
            file_name += ext
    else:
        file_name += ext

    PIXEL_SIZE = 4 # in bytes

    number_of_pixels = len(pixel_data) // PIXEL_SIZE

    if number_of_pixels < (width * height):
        raise ValueError("Number of pixels in 'pixel_data' is less than 'width' * 'height'.")

    c_pixel_data = (_ctypes.c_uint8 * len(pixel_data)).from_buffer_copy(pixel_data)
    c_pixel_data_address = _ctypes.cast(c_pixel_data, _ctypes.c_void_p).value 

    pixel_data_size     = width * height * PIXEL_SIZE
    header_size         = _ctypes.sizeof(_C_WinApi.BITMAPFILEHEADER) + _ctypes.sizeof(_C_WinApi.BITMAPV5HEADER)
    file_size           = header_size + pixel_data_size

    c_file_data         = (_ctypes.c_uint8 * file_size)()
    c_file_data_address = _ctypes.cast(c_file_data, _ctypes.c_void_p).value 

    
    c_fh = _ctypes.cast(c_file_data_address, _C_WinApi.LPBITMAPFILEHEADER)[0]
    c_fh.bfType         = 0x4D42          # bmp file signature = {'B', 'M'}
    c_fh.bfSize         = file_size
    c_fh.bfOffBits      = header_size

    c_ih = _ctypes.cast(c_file_data_address + _ctypes.sizeof(_C_WinApi.BITMAPFILEHEADER), _C_WinApi.LPBITMAPV5HEADER)[0]
    c_ih.bV5Size        = _ctypes.sizeof(_C_WinApi.BITMAPV5HEADER)
    c_ih.bV5Width       = width
    c_ih.bV5Height      = height
    c_ih.bV5Planes      = 1
    c_ih.bV5BitCount    = 32
    c_ih.bV5Compression = _C_WinApi.BI_BITFIELDS
    c_ih.bV5SizeImage   = pixel_data_size
    c_ih.bV5RedMask     = 0xFF000000
    c_ih.bV5GreenMask   = 0x00FF0000
    c_ih.bV5BlueMask    = 0x0000FF00
    c_ih.bV5AlphaMask   = 0x000000FF
    c_ih.bV5CSType      = _C_WinApi.LCS_sRGB
    c_ih.bV5Intent      = _C_WinApi.LCS_GM_GRAPHICS

    c_file_pixel_data_p = _ctypes.cast(c_file_data_address + header_size, _ctypes.POINTER(_ctypes.c_uint8))
    ix = 0

    row_size = width * PIXEL_SIZE # in bytes

    for column_ix in range(height):
        if is_reverse_rows:
            column_ix = height - 1 - column_ix 

        column_address =  c_pixel_data_address + row_size * column_ix
 
        for pixel_ix in range(width):
            pixel = _ctypes.cast(column_address + pixel_ix * PIXEL_SIZE, _ctypes.POINTER(_ctypes.c_uint8))

            # reverse order of channels
            c_file_pixel_data_p[ix] = pixel[3]
            ix += 1
            c_file_pixel_data_p[ix] = pixel[2]
            ix += 1
            c_file_pixel_data_p[ix] = pixel[1]
            ix += 1
            c_file_pixel_data_p[ix] = pixel[0]
            ix += 1

    file_data = bytes(c_file_data)
    try:
        with open(file_name, "wb") as file:
            file.write(file_data)
    except:
        return False

    return True


def save_texture_as_bmp(file_name, tex_obj):
    """
    file_name       : str | Any
        If not ends with '.bmp', then will be added to file_name.
    tex_obj         : int | SupportsInt
        OpenGl texture name (object).

    Returns : bool
        True - when bitmap was saved successfully.

    Exceptions
        ValueError
            When value of any argument fails conversion to expected type.
    """
    if not isinstance(file_name, str):
        try:
            file_name = str(file_name)
        except Exception as exception:
            raise ValueError("Value of 'file_name' is not castable to str.") from exception

    if not isinstance(tex_obj, int):
        try:
            tex_obj = int(tex_obj)
        except Exception as exception:
            raise ValueError("Value of 'tex_obj' is not castable to int.") from exception

    is_success = False

    _C_GL.glPushAttrib(_C_GL.GL_TEXTURE_BIT)

    _C_GL.glBindTexture(_C_GL.GL_TEXTURE_2D, tex_obj)

    c_width     = _C_GL.GLint(0)
    c_height    = _C_GL.GLint(0)

    _C_GL.glGetTexLevelParameteriv(_C_GL.GL_TEXTURE_2D, 0, _C_GL.GL_TEXTURE_WIDTH, _ctypes.byref(c_width))
    _C_GL.glGetTexLevelParameteriv(_C_GL.GL_TEXTURE_2D, 0, _C_GL.GL_TEXTURE_HEIGHT, _ctypes.byref(c_height))

    width = c_width.value
    height = c_height.value

    if width > 0 and height > 0:
        PIXEL_SIZE = 4 # in bytes

        data_size = width * height * PIXEL_SIZE
        data = (_ctypes.c_uint8 * data_size)()
                   
        _C_GL.glGetTexImage(_C_GL.GL_TEXTURE_2D, 0, _C_GL.GL_RGBA, _C_GL.GL_UNSIGNED_BYTE, data);

        is_success = save_as_bmp(file_name, data, width, height, False)

    _C_GL.glPopAttrib()

    return is_success

################################################################################

def is_defined_in_gl(target):
    """
    target  : str | Any
        OpenGl extension name or OpenGL core version name.
    Returns : bool
        True, when constants and functions for target are defined in GL module.

    Note: Even if constants and functions are defined, GPU vendor might not provide them.
    """
    if not isinstance(target, str):
        try:
            target = str(target)
        except Exception as exception:
            raise ValueError("Value of 'target' is not convertible to str.") from exception

    return target in set(
        "GL_VERSION_1_0",
        "GL_VERSION_1_1",
    )

def is_defined_in_c_gl(target):
    """
    target  : str | Any
        OpenGl extension name or OpenGL core version name.
    Returns : bool
        True, when constants and functions for target are defined in C_GL module.

    Note: Even if constants and functions are defined, GPU vendor might not provide them.
    """
    if not isinstance(target, str):
        try:
            target = str(target)
        except Exception as exception:
            raise ValueError("Value of 'target' is not convertible to str.") from exception

    return target in set(
        "GL_VERSION_1_0",
        "GL_VERSION_1_1",
    )

def get_gl_error_str(gl_error_code):
    """
    gl_error_code  : int | SupportsInt
        Value returned by glGetError().
    Returns : str
    """
    if not isinstance(gl_error_code, int):
        try:
            gl_error_code = int(gl_error_code)
        except Exception as exception:
            raise ValueError("Value of 'gl_error_code' is not convertible to int.") from exception

    return _gl_support.get_gl_error_str(gl_error_code)