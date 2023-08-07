import ctypes as _ctypes
import enum as _enum
from copy import deepcopy as _deepcopy

from ._Private  import C_WGL as _C_WGL
from .          import C_GL as _C_GL

from .Utility import get_gl_error_str as _get_gl_error_str

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

        elif not isinstance(code_point_ranges, None):
            raise ValueError("Type of 'code_point_ranges' is unexpected.")

        if charset_id == UnicodeCharSetId.CUSTOM and not isinstance(code_point_ranges, list):
            raise ValueError("When 'charset_id' is 'UnicodeCharSetId.CUSTOM', then code_point_ranges must contain list of code point ranges.")

        if charset_id != UnicodeCharSetId.CUSTOM and not isinstance(code_point_ranges, None):
            raise ValueError("When 'charset_id' is not 'UnicodeCharSetId.CUSTOM', then code_point_ranges must by None.")

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

