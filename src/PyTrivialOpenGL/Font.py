import ctypes as _ctypes
import enum as _enum
from copy import deepcopy as _deepcopy

from PyTrivialOpenGL.C_GL.VERSION_1_1.Types import GLuint

from ._Private  import C_WGL    as _C_WGL
from ._Private  import C_WinApi as _C_WinApi
from .          import C_GL     as _C_GL

from .Utility import get_gl_error_str as _get_gl_error_str
from .Size import Size
from .Point import Point
from .Log import log_debug as _log_debug

from .Window import to_window as _to_window

class FontSizeUnitId(_enum.Enum):
    PIXELS = _enum.auto()
    POINTS = _enum.auto()

class FontStyleId(_enum.Enum):
    NORMAL  = _enum.auto()
    BOLD    = _enum.auto()

# Ranges are from unicode space.
# Font might not have all glyphs from this ranges.
class UnicodeCharSetId(_enum.Enum):
    CUSTOM          = _enum.auto()

    # Unicode Plane 0 - BMP - Basic Multilingual Plane 
    RANGE_0000_FFFF = _enum.auto()
    ENGLISH         = _enum.auto()

class UnicodeCodePoint:
    # "WHITE SQUARE" 
    # Represents missing glyph.
    WHITE_SQUARE               = 0x25A1

    # "REPLACEMENT CHARACTER"
    # Represent out of range character.
    REPLACEMENT_CHARACTER      = 0xFFFD

class CodePointRange:
    """
    from_   : int
    to      : int
    """
    def __init__(self, from_, to = None):
        """
        from_ : int | SupportsInt
        to : int | SupportsInt | None
            When type is None, then 'to' have same value as 'from_'.
        """
        if not isinstance(from_, int):
            try:
                from_ = int(from_)
            except Exception as exception:
                raise ValueError("Value of 'from_' is not convertible to int.") from exception

        if to is None:
            to = from_
        elif not isinstance(to, int):
            try:
                to = int(to)
            except Exception as exception:
                raise ValueError("Value of 'to' is not convertible to int.") from exception

        self.from_  = from_
        self.to     = to

def _get_code_point_ranges(char_set_id):
    """
    char_set_id : UnicodeCharSetId
    Returns     : List[CodePointRange]
    """
    if char_set_id == UnicodeCharSetId.CUSTOM:
        return []

    if char_set_id == UnicodeCharSetId.RANGE_0000_FFFF:
        return [CodePointRange(0x0000, 0xFFFF)]

    if char_set_id == UnicodeCharSetId.ENGLISH:
        return [
            CodePointRange(0x0020, 0x007E),
            CodePointRange(UnicodeCodePoint.WHITE_SQUARE),
            CodePointRange(UnicodeCodePoint.REPLACEMENT_CHARACTER),
        ]

    return []


class _FontInfo:
    def __init__(self, name, size, size_unit_id, style_id, charset_id, code_point_ranges = None, distance_between_glyphs = 0, distance_between_lines = 0):
        """
        name                    : str | Any
        size                    : int | SupportsInt
        size_unit_id            : FontSizeUnitId
        style_id                : FontStyleId
        charset_id              : UnicodeCharSetId
        code_point_ranges       : List[CodePointRange | Tuple[int | SupportsInt, int | SupportsInt] | int | SupportsInt] | None
            Must be an list, when 'charset_id' is 'UnicodeCharSetId.CUSTOM'.
            Must be None, when 'charset_id' is other than 'UnicodeCharSetId.CUSTOM'.
        distance_between_glyphs : int | SupportsInt
        distance_between_lines  : int | SupportsInt
        """
        if not isinstance(name, str):
            try:
                name = str(name)
            except Exception as exception:
                raise ValueError("Value of 'name' is not convertible to str.") from exception

        if not isinstance(size, int):
            try:
                size = int(size)
            except Exception as exception:
                raise ValueError("Value of 'size' is not convertible to int.") from exception

        if not isinstance(size_unit_id, FontSizeUnitId):
            raise ValueError("Type of 'size_unit_id' is unexpected.")

        if not isinstance(style_id, FontStyleId):
            raise ValueError("Type of 'style_id' is unexpected.")

        if not isinstance(charset_id, UnicodeCharSetId):
            raise ValueError("Type of 'charset_id' is unexpected.")

        if isinstance(code_point_ranges, list):
            proper_code_point_rangess = []

            index = 0
            for code_point_range in code_point_ranges:
                if isinstance(code_point_range, CodePointRange):
                    proper_code_point_rangess.append(_deepcopy(code_point_range))
                elif isinstance(code_point_range, tuple):
                    pass
                elif isinstance(code_point_range, int):
                    proper_code_point_rangess.append(CodePointRange(code_point_range))
                else:
                    try:
                        code_point_range = int(code_point_range)
                    except Exception as exception:
                        raise ValueError("At %d item of 'code_point_ranges'. Value is not convertible to int.") from exception

                    proper_code_point_rangess.append(CodePointRange(code_point_range))
                index += 1

        elif code_point_ranges is not None:
            raise ValueError("Type of 'code_point_ranges' is unexpected.")

        if charset_id == UnicodeCharSetId.CUSTOM and not isinstance(code_point_ranges, list):
            raise ValueError("When 'charset_id' is 'UnicodeCharSetId.CUSTOM', then code_point_ranges must contain list of code point ranges.")

        if charset_id != UnicodeCharSetId.CUSTOM and code_point_ranges is not None:
            raise ValueError("When 'charset_id' is not 'UnicodeCharSetId.CUSTOM', then code_point_ranges must by None.")

        if charset_id != UnicodeCharSetId.CUSTOM:
            code_point_ranges = _get_code_point_ranges(charset_id)

        self.name                    = name              
        self.size                    = size                   
        self.size_unit_id            = size_unit_id           
        self.style_id                = style_id               
        self.charset_id              = charset_id             
        self.code_point_ranges       = code_point_ranges      
        self.distance_between_glyphs = distance_between_glyphs
        self.distance_between_lines  = distance_between_lines 


class _GlyphData:
    """
    """
    def __init__(self):
        self.width      = 0
        self.tex_obj    = 0

        self.x1         = 0
        self.y1         = 0
        self.x2         = 0
        self.y2         = 0


class _FontData:
    """
    info                    : _FontInfo
    font_height             : int
    font_ascent             : int
    font_descent            : int
    font_internal_leading   : int
    glyphs                  : Dict[int, _GlyphData]
    tex_objs                : List[int]
    """
    def __init__(self):
        self.info                   = _FontInfo("", 0, FontSizeUnitId.PIXELS, FontStyleId.NORMAL, UnicodeCharSetId.ENGLISH)

        self.font_height            = 0         # in pixels    
        self.font_ascent            = 0         # in pixels   
        self.font_descent           = 0         # in pixels   
        self.font_internal_leading  = 0         # in pixels   

        self.glyphs                 = {}        # indexed by character code from unicode space

        # Array of OpenGL Texture Object Identifiers (Texture Names).
        # Pixel Format: RGBA (8 bits per channel).
        # Orientation: First pixel refers to left-bottom corner of image.
        self.tex_objs               = []


class _FrameBuffer:
    _GL_FRAMEBUFFER_EXT             = 0x8D40
    _GL_FRAMEBUFFER_BINDING         = 0x8CA6
    _GL_COLOR_ATTACHMENT0_EXT       = 0x8CE0
    _GL_FRAMEBUFFER_COMPLETE_EXT    = 0x8CD5

    """
    _glGenFramebuffersEXT           : Callable
    _glDeleteFramebuffersEXT        : Callable
    _glBindFramebufferEXT           : Callable
    _glFramebufferTexture2DEXT      : Callable
    _glCheckFramebufferStatusEXT    : Callable
    _width                          : int
    _height                         : int
    _fbo                            : int
    _prev_fbo                       : int
    _err_msg                        : str
    """

    def __init__(self):
        self._clear()

    def create(self, width, height):
        self._clear()

        if self.is_ok():
            # void (APIENTRY *m_glGenFramebuffersEXT)(GLsizei n, GLuint *framebuffers);
            self._glGenFramebuffersEXT = _ctypes.WINFUNCTYPE(None, _C_GL.GLsizei, _ctypes.POINTER(_C_GL.GLuint))(
                _C_WGL.wglGetProcAddress(b"glGenFramebuffersEXT")
            )
            if not self._glGenFramebuffersEXT: self._err_msg = "Can not load 'glGenFramebuffersEXT'."
            
        if self.is_ok():
            # void (APIENTRY *m_glDeleteFramebuffersEXT)(GLsizei n, const GLuint *framebuffers);
            self._glDeleteFramebuffersEXT = _ctypes.WINFUNCTYPE(None, _C_GL.GLsizei, _ctypes.POINTER(_C_GL.GLuint))(
                _C_WGL.wglGetProcAddress(b"glDeleteFramebuffersEXT")
            )
            if not self._glDeleteFramebuffersEXT: self._err_msg = "Can not load 'glDeleteFramebuffersEXT'."

        if self.is_ok():
            # void (APIENTRY *m_glBindFramebufferEXT)(GLenum target, GLuint framebuffer);
            self._glBindFramebufferEXT = _ctypes.WINFUNCTYPE(None, _C_GL.GLenum, _C_GL.GLuint)(
                _C_WGL.wglGetProcAddress(b"glBindFramebufferEXT")
            )
            if not self._glBindFramebufferEXT: self._err_msg = "Can not load 'glBindFramebufferEXT'."

        if self.is_ok():
            # void (APIENTRY *m_glFramebufferTexture2DEXT)(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level);
            self._glFramebufferTexture2DEXT = _ctypes.WINFUNCTYPE(None, _C_GL.GLenum, _C_GL.GLenum, _C_GL.GLenum, _C_GL.GLuint, _C_GL.GLint)(
                _C_WGL.wglGetProcAddress(b"glFramebufferTexture2DEXT")
            )
            if not self._glFramebufferTexture2DEXT: self._err_msg = "Can not load 'glFramebufferTexture2DEXT'."

        if self.is_ok():
            # GLenum (APIENTRY* m_glCheckFramebufferStatusEXT)(GLenum target);
            self._glCheckFramebufferStatusEXT = _ctypes.WINFUNCTYPE(_C_GL.GLenum, _C_GL.GLenum)(
                _C_WGL.wglGetProcAddress(b"glCheckFramebufferStatusEXT")
            )
            if not self._glCheckFramebufferStatusEXT: self._err_msg = "Can not load 'glCheckFramebufferStatusEXT'."

        if self.is_ok():
            self._width     = width
            self._height    = height

        if self.is_ok():
            c_max_viewport_size = (_C_GL.GLint * 2)()
            _C_GL.glGetIntegerv(_C_GL.GL_MAX_VIEWPORT_DIMS, c_max_viewport_size)

            if _C_GL.glGetError() != 0:
                self._err_msg = "Can not get maximal view port dimensions. OpenGL Error: %s." % _get_gl_error_str(_C_GL.glGetError())
                
        if self.is_ok():
            c_max_texture_size = _C_GL.GLint(0)
            _C_GL.glGetIntegerv(_C_GL.GL_MAX_TEXTURE_SIZE, _ctypes.byref(c_max_texture_size))

            if _C_GL.glGetError() != 0:
                self._err_msg = "Can not get maximal texture size. OpenGL Error: %s." % _get_gl_error_str(_C_GL.glGetError())

        if self.is_ok():
            if width > c_max_viewport_size[0] or width > c_max_texture_size.value or height > c_max_viewport_size[1] or height > c_max_texture_size.value:
                 self._err_msg = "Value of width or/and height are to big. (max_viewport_width=%d, max_viewport_height=%d, max_texture_width=%d, max_texture_height=%d)" % (
                    c_max_viewport_size[0],  c_max_viewport_size[1], c_max_texture_size.value, c_max_texture_size.value
                 )
                
        if self.is_ok():
            c_fbo = _C_GL.GLuint(0)
            self._glGenFramebuffersEXT(1, _ctypes.byref(c_fbo))

            if _C_GL.glGetError() != 0:
                self._err_msg = "Can not generate frame buffer. OpenGL Error: %s." % _get_gl_error_str(_C_GL.glGetError())
            else:
                self._fbo = c_fbo.value
                
        if self.is_ok():
            c_prev_fbo = _C_GL.GLint(0)
            _C_GL.glGetIntegerv(self._GL_FRAMEBUFFER_BINDING, _ctypes.byref(c_prev_fbo))

            if _C_GL.glGetError() != 0:
                self._err_msg = "Can not get current framebuffer. OpenGL Error: %s." % _get_gl_error_str(_C_GL.glGetError())
            else:
                self._prev_fbo = c_prev_fbo.value

        if self.is_ok():
            self._glBindFramebufferEXT(self._GL_FRAMEBUFFER_EXT, self._fbo)

            if _C_GL.glGetError() != 0:
                self._err_msg = "Can not bind framebuffer. OpenGL Error: %s." % _get_gl_error_str(_C_GL.glGetError())
        
        _C_GL.glPushAttrib(_C_GL.GL_ENABLE_BIT)
        _C_GL.glPushAttrib(_C_GL.GL_TEXTURE_BIT)

    def destroy(self):
        if self.is_ok():
            self._glFramebufferTexture2DEXT(self._GL_FRAMEBUFFER_EXT, self._GL_COLOR_ATTACHMENT0_EXT, _C_GL.GL_TEXTURE_2D, 0, 0)

            if _C_GL.glGetError() != 0:
                self._err_msg = "Can not detach texture from framebuffer. OpenGL Error: %s." % _get_gl_error_str(_C_GL.glGetError())

        _C_GL.glPopAttrib()
        _C_GL.glPopAttrib()
        
        if self.is_ok():
            self._glBindFramebufferEXT(self._GL_FRAMEBUFFER_EXT, self._prev_fbo)

            if _C_GL.glGetError() != 0:
                self._err_msg = "Can not rebind previous framebuffer. OpenGL Error: %s." % _get_gl_error_str(_C_GL.glGetError())

        if self.is_ok():
            c_fbo = _C_GL.GLuint(self._fbo)
            self._glDeleteFramebuffersEXT(1, _ctypes.byref(c_fbo))

            if _C_GL.glGetError() != 0:
                self._err_msg = "Can not delete framebuffer. OpenGL Error: %s." % _get_gl_error_str(_C_GL.glGetError())
        

    def is_ok(self):
        """
        Returns : bool
        """
        return self._err_msg == ""

    def get_err_msg(self):
        """
        Returns : str
        """
        return self._err_msg

    def gen_and_bind_tex(self):
        """
        Returns : int
        """
        tex_obj = _C_GL.GLuint(0)

        if self.is_ok():
            _C_GL.glGenTextures(1, _ctypes.byref(tex_obj))
            _C_GL.glBindTexture(_C_GL.GL_TEXTURE_2D, tex_obj)
            _C_GL.glDisable(_C_GL.GL_TEXTURE_2D)

            _C_GL.glTexParameteri(_C_GL.GL_TEXTURE_2D, _C_GL.GL_TEXTURE_MIN_FILTER, _C_GL.GL_NEAREST)
            _C_GL.glTexParameteri(_C_GL.GL_TEXTURE_2D, _C_GL.GL_TEXTURE_MAG_FILTER, _C_GL.GL_NEAREST)
            _C_GL.glTexImage2D(_C_GL.GL_TEXTURE_2D, 0, _C_GL.GL_RGBA, self._width, self._height, 0, _C_GL.GL_RGBA, _C_GL.GL_UNSIGNED_BYTE, None)

            self._glFramebufferTexture2DEXT(self._GL_FRAMEBUFFER_EXT, self._GL_COLOR_ATTACHMENT0_EXT, _C_GL.GL_TEXTURE_2D, tex_obj, 0)
                    
            if self._glCheckFramebufferStatusEXT(self._GL_FRAMEBUFFER_EXT) != self._GL_FRAMEBUFFER_COMPLETE_EXT:
                self._err_msg = "Frame buffer is not complete."

                self._glFramebufferTexture2DEXT(self._GL_FRAMEBUFFER_EXT, self._GL_COLOR_ATTACHMENT0_EXT, _C_GL.GL_TEXTURE_2D, 0, 0);
                _C_GL.glDeleteTextures(1, _ctypes.byref(tex_obj))
                tex_obj.value = 0

        return tex_obj.value
    

    def _clear(self):
        self._glGenFramebuffersEXT          = None
        self._glDeleteFramebuffersEXT       = None
        self._glBindFramebufferEXT          = None
        self._glFramebufferTexture2DEXT     = None
        self._glCheckFramebufferStatusEXT   = None

        self._width         = 0
        self._height        = 0

        self._fbo           = 0
        self._prev_fbo      = 0

        self._err_msg       = ""


class _DisplayListSet:
    """
    code_point_range    : CodePointRange
    first               : int
    range_              : int
    base                : int
    """
    def __init__(self, from_, to = None):
        self.code_point_range = CodePointRange(from_, to)
    
        self.first        = 0
        self.range_       = 0
        self.base         = 0


class _FontDataGenerator:
    """
    _data                   : _FontData
    _device_context_handle  : int
    _display_list_sets      : List[_DisplayListSet]
    _err_msg                : str
    """
    def __init__(self):
        self._data                  = _FontData()
        self._device_context_handle = 0
        self._display_list_sets     = []

        self._err_msg   = ""

    def generate(self, font_info):
        """
        font_info   : _FontInfo
        Returns     : _FontData
        """
        self._err_msg           = ""
        self._data.info         = font_info

        window_handle = _to_window()._window_handle

        self._device_context_handle = _C_WinApi.GetDC(window_handle)

        old_text_align = _C_WinApi.SetTextAlign(self._device_context_handle, _C_WinApi.TA_LEFT | _C_WinApi.TA_TOP | _C_WinApi.TA_NOUPDATECP)

        if old_text_align == _C_WinApi.GDI_ERROR:
            self._err_msg = "Can set window device context text align."
        else:
            old_map_mode = _C_WinApi.SetMapMode(self._device_context_handle, _C_WinApi.MM_TEXT)
            if old_map_mode == 0:
                self._err_msg =  "Can set window device context map mode."
            else:
                requested_font_height = self._to_pixels(font_info.size, font_info.size_unit_id)

                font_handle = _C_WinApi.CreateFontW(
                        requested_font_height,                    
                        0, 0, 0,                            
                        _C_WinApi.FW_BOLD if font_info.style_id == FontStyleId.BOLD else _C_WinApi.FW_NORMAL,
                        _C_WinApi.FALSE, _C_WinApi.FALSE, _C_WinApi.FALSE,
                        _C_WinApi.ANSI_CHARSET, # For W version of this function, should create a font bitmap with all having glyphs for unicode range from 0000 to FFFF.
                        _C_WinApi.OUT_TT_PRECIS,
                        _C_WinApi.CLIP_DEFAULT_PRECIS,
                        _C_WinApi.ANTIALIASED_QUALITY,
                        _C_WinApi.FF_DONTCARE | _C_WinApi.DEFAULT_PITCH,
                        font_info.name
                ) 

                if not font_handle:
                    self._err_msg = "Can not create font source."
                else:
                    old_font_handle = _C_WinApi.SelectObject(self._device_context_handle, font_handle); 

                    # --- Gets Font Metrics --- #
                    metric = _C_WinApi.TEXTMETRICW()
                    _C_WinApi.GetTextMetricsW(self._device_context_handle, _ctypes.byref(metric))
                    self._data.font_height              = metric.tmHeight
                    self._data.font_ascent              = metric.tmAscent
                    self._data.font_descent             = metric.tmDescent
                    self._data.font_internal_leading    = metric.tmInternalLeading

                    # debug section
                    #print(m_data.font_height)
                    #print(m_data.font_ascent)
                    #print(m_data.font_descent)
                    #print(m_data.font_internal_leading)

                    # Note: Requested font size (requested_font_height) might be different from created font size (m_data.font_height).

                    def get_code_point_ranges_of_current_win_font(device_context_handle):
                        """
                        device_context_handle   : int
                        Returns                 : List[CodePointRange]
                        """
                        code_point_ranges = []

                        buffer_size = _C_WinApi.GetFontUnicodeRanges(device_context_handle, _C_WinApi.NULL)
                        buffer = (_ctypes.uint8 * buffer_size)()

                        glyphset = _ctypes.cast(buffer, _C_WinApi.LPGLYPHSET)
  
                        _C_WinApi.GetFontUnicodeRanges(device_context_handle, glyphset);
                        # debug
                        #print(glyphset[0].cbThis);
                        #print(glyphset[0].flAccel);
                        #print(glyphset[0].cGlyphsSupported);
                        #print(glyphset[0].cRanges);

                        for ix in range(glyphset[0].cRanges):
                            from_   = glyphset[0].ranges[ix].wcLow
                            to      = from_ + glyphset[0].ranges[ix].cGlyphs - 1

                            code_point_ranges.append(CodePointRange(from_, to))
            
                        return code_point_ranges

                    # debug
                    #for range_ in get_code_point_ranges_of_current_win_font(self.device_context_handle)):
                    #    _log_debug("[%04X..%04X]" % (range_.from_, range_.to))

                    # --- Generates Display Lists and Intermediary Font Bitmaps --- #

                    ranges = []
                    for range_ in self._data.info.code_point_ranges:
                        if range_.from_ > 0xFFFF or range_.to > 0xFFFF:
                                self._err_msg = "Unicode code point is out of supported range. Supported unicode code point range is from 0000 to (including) FFFF. "
                                break

                        def push_range_widhout_code_point(code_point, range_, ranges):
                            """
                            code_point  : int
                            range_      : CodePointRange
                            ranges      : List[CodePointRange]
                            """
                            def is_in(code, range_):
                                """
                                code : int
                                range_ : CodePointRange
                                """
                                return range_.from_ <= code and code <= range_.to
             
                            if is_in(code_point, range_):
                                if range_.from_ != code_point:
                                    ranges.append(CodePointRange(range_.from_, code_point - 1))
                                
                                if range_.to != code_point:
                                    ranges.append(CodePointRange(code_point + 1, range_.to));
                                
                            else:
                                ranges.append(range_)
    
                        # Function wglUseFontBitmapsW have problem with generating font bitmap when FFFF code point is present in range.
                        # Workaround: Remove this code point from range, since it's a non-character code point. 
                        push_range_widhout_code_point(0xFFFF, range_, ranges);
                    

                    if self.is_ok():
                        _C_GL.glPushAttrib(_C_GL.GL_ALL_ATTRIB_BITS)

                        for range_ in ranges:
                            # _log_debug("[%04X..%04X]" % (range_.from_, range_.to)) # debug
                   
                            display_list_set = _DisplayListSet(range_.from_, range_.to)

                            display_list_set.first  = display_list_set.code_point_range.from_
                            display_list_set.range_  = display_list_set.code_point_range.to - display_list_set.code_point_range.from_ + 1
                            display_list_set.base   = _C_GL.glGenLists(display_list_set.range_)

                            if display_list_set.base == 0:
                                self._err_msg = "Can not generate display list for unicode range [%04X..%04X]." % (display_list_set.code_point_range.from_, display_list_set.code_point_range.to)
                                break

                            is_success = _C_WGL.wglUseFontBitmapsW(self._device_context_handle, display_list_set.first, display_list_set.range_, display_list_set.base)

                            # Workaround for strange behavior. For POPUP window first call of wglUseFontBitmapsA fail with GetError() = 0.
                            # Second call, right after first, seams to succeed.
                            if not is_success:
                               is_success = _C_WGL.wglUseFontBitmapsW(self._device_context_handle, display_list_set.first, display_list_set.range_, display_list_set.base)

                            if not is_success:
                                self._err_msg =  "Can not create intermediary font bitmap for unicode range [%04X..%04X]." % (display_list_set.code_point_range.from_, display_list_set.code_point_range.to)
                                break

                            self._display_list_sets.append(display_list_set)

                        # --- Generate Font Textures --- #

                        if self.is_ok():
                            self._generate_font_textures(1024, 1024)
      
                        # --- Destroys Display Lists and Clears Ranges --- #

                        for display_list_set in self._display_list_sets:
                            _C_GL.glDeleteLists(display_list_set.base, display_list_set.range_)

                        self._display_list_sets.clear()

                        _C_GL.glPopAttrib()
                    
                    _C_WinApi.SelectObject(self._device_context_handle, old_font_handle)
                    _C_WinApi.DeleteObject(font_handle)
                
                _C_WinApi.SetMapMode(self._device_context_handle, old_map_mode)
            
            _C_WinApi.SetTextAlign(self._device_context_handle, old_text_align);
        

        _C_WinApi.ReleaseDC(window_handle, self._device_context_handle);
        self._device_context_handle = _C_WinApi.NULL;

        data = self._data
        self._data = _FontData()

        return data if self.is_ok() else _FontData()

    def is_ok(self):
        return self._err_msg == ""

    def get_err_msg(self):
        return self._err_msg


    def _points_to_pixel(self, points):
        return points * 4 // 3

    def _get_char_size(self, c):
        """
        c : str
            Single character.
        """
        c_c     = _ctypes.c_wchar(c)
        c_size  = _C_WinApi.SIZE()

        if _C_WinApi.GetTextExtentPoint32W(self._device_context_handle, _ctypes.byref(c_c), 1, _ctypes.byref(c_size)):
            return Size(c_size.cx, c_size.cy)

        return Size(0, 0)

    def _to_pixels(self, size, size_unit_id):
        """
        size        : int
        size_unit   : FontSizeUnitId
        """
        if size_unit_id == FontSizeUnitId.PIXELS:
            return size
        if size_unit_id == FontSizeUnitId.POINTS:
            return self._points_to_pixel(size)
        return 0

    def _render_glyph_to_texture(self, list_base, x, y, c):
        """
        list_base : int
        x : int
        y : int
        c : str
            Single character.
        """
        _C_GL.glPushAttrib(_C_GL.GL_ENABLE_BIT)
        _C_GL.glPushAttrib(_C_GL.GL_COLOR_BUFFER_BIT)
        _C_GL.glPushAttrib(_C_GL.GL_LIST_BIT)

        _C_GL.glEnable(_C_GL.GL_BLEND)
        _C_GL.glBlendFunc(_C_GL.GL_SRC_ALPHA, _C_GL.GL_ONE_MINUS_SRC_ALPHA)
                
        _C_GL.glColor4ub(255, 255, 255, 255)
        _C_GL.glRasterPos2i(x, y)

        _C_GL.glListBase(list_base)
        c_c = _ctypes.c_wchar(c)
        _C_GL.glCallLists(1, _C_GL.GL_UNSIGNED_SHORT, _ctypes.byref(c_c))

        _C_GL.glPopAttrib()
        _C_GL.glPopAttrib()
        _C_GL.glPopAttrib()

    def _generate_font_textures(self, width, height):
        """
        width : int
        height : int
        """

        frame_buffer = _FrameBuffer()
        frame_buffer.create(width, height)

        if frame_buffer.is_ok():
            tex_obj = frame_buffer.gen_and_bind_tex()

        if frame_buffer.is_ok():
            self._data.tex_objs.append(tex_obj)

            _C_GL.glPushAttrib(_C_GL.GL_VIEWPORT_BIT)
            _C_GL.glViewport(0, 0, width, height)

            _C_GL.glPushAttrib(_C_GL.GL_MATRIX_MODE)
            _C_GL.glMatrixMode(_C_GL.GL_PROJECTION)
            _C_GL.glPushMatrix()
            _C_GL.glLoadIdentity()
            _C_GL.glOrtho(0, width, 0, height, 1, -1)
            _C_GL.glMatrixMode(_C_GL.GL_MODELVIEW)
            _C_GL.glPushMatrix()
            _C_GL.glLoadIdentity()

            _C_GL.glPushAttrib(_C_GL.GL_COLOR_BUFFER_BIT)
            _C_GL.glClearColor(0.0, 0.0, 0.0, 0.0)

            _C_GL.glClear(_C_GL.GL_COLOR_BUFFER_BIT)

            y = height - self._data.font_height
            pos = Point(0, y)
 
            for display_list_set in self._display_list_sets:
                if not frame_buffer.is_ok():
                    break

                for code in range(display_list_set.code_point_range.from_, display_list_set.code_point_range.to + 1):
                    size = self._get_char_size(chr(code))

                    if (pos.x + size.width) >= width:
                        pos.x = 0

                        if (pos.y - self._data.font_height) <= 0:
                            # run out of space in texture, generate next texture
                            tex_obj = frame_buffer.gen_and_bind_tex()

                            if not frame_buffer.is_ok():
                                break

                            _C_GL.glClear(_C_GL.GL_COLOR_BUFFER_BIT)

                            self._data.tex_objs.append(tex_obj)

                            # printf("T%d [%04X]\n", (int)m_data.tex_objs.size() - 1, code); // debug

                            pos = Point(0, y)
                        else:
                            pos.y -= self._data.font_height
                   
                    
                    def to_tex_space(pos, size):
                        return pos / size


                    glyph_data = _GlyphData()

                    glyph_data.width = size.width
                    glyph_data.tex_obj = tex_obj

                    glyph_data.x1 = to_tex_space(pos.x, width);
                    glyph_data.y1 = to_tex_space(pos.y - self._data.font_descent, height);
                    glyph_data.x2 = to_tex_space(pos.x + size.width, width);
                    glyph_data.y2 = to_tex_space(pos.y - self._data.font_descent + self._data.font_height, height);

                    self._data.glyphs[code] = glyph_data
              
                    self._render_glyph_to_texture(
                        display_list_set.base, 
                        pos.x, pos.y, 
                        chr(code - display_list_set.first) # corrects character code to match glyph index in display list
                    )
                    
                    # Used as workaround for overlapping glyphs when they are drawn.
                    ADDITIONAL_SAFE_SPACE = 1

                    pos.x += size.width + ADDITIONAL_SAFE_SPACE

            _C_GL.glMatrixMode(_C_GL.GL_PROJECTION)
            _C_GL.glPopMatrix()
            _C_GL.glMatrixMode(_C_GL.GL_MODELVIEW)
            _C_GL.glPopMatrix()
                    
            _C_GL.glPopAttrib()
            _C_GL.glPopAttrib()
            _C_GL.glPopAttrib()
            
            frame_buffer.destroy()

        if not frame_buffer.is_ok():
            self._err_msg = frame_buffer.get_err_msg()




