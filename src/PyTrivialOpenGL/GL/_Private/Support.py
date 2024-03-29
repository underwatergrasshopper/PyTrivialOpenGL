"""
Inner support for GL module.
"""

from ... import C_GL as _C_GL
import ctypes as _ctypes

### Cache ###

class _Cache:
    def __init__(self):
        self.clear()

    def clear(self):
        self.c_vertex_array_pointer         = None
        self.c_normal_array_pointer         = None
        self.c_color_array_pointer          = None
        self.c_index_array_pointer          = None
        self.c_edge_flag_array_pointer      = None
        self.c_tex_coord_array_pointer      = None
        self.c_interleaved_array_pointer    = None

        self.c_array                        = None

        self.c_select_buffer                = None
        self.c_feedback_buffer              = None

_cache = _Cache()

def to_cache():
    return _cache

### List <-> C Array ###

def list_part_to_c_array(l_type, l, exact_len, c_type):
    num_of_elements_to_take = min(exact_len, len(l))

    return (c_type * exact_len)(*(l_type(l[ix]) for ix in range(num_of_elements_to_take)))

def list_to_c_array(l_type, l, min_len, c_type):
    return (c_type * max(min_len, len(l)))(*(l_type(e) for e in l))

def list_part_to_c_array_no_conv(l, exact_len, c_type):
    num_of_elements_to_take = min(exact_len, len(l))

    return (c_type * exact_len)(*(l[ix] for ix in range(num_of_elements_to_take)))

def list_to_c_array_no_conv(l, min_len, c_type):
    return (c_type * max(min_len, len(l)))(*(e for e in l))

def make_c_array(c_type, length):
    return (c_type * length)()

def c_array_to_list(py_type, c_array):
    return [py_type(element) for element in c_array]

### Maps ###

def gl_type_id_to_c_type(type_):
    return _gl_type_id_to_c_type_map.get(type_, None)

_gl_type_id_to_c_type_map = {
    _C_GL.GL_BYTE             : _C_GL.GLbyte,
    _C_GL.GL_UNSIGNED_BYTE    : _C_GL.GLubyte,
    _C_GL.GL_SHORT            : _C_GL.GLshort,
    _C_GL.GL_UNSIGNED_SHORT   : _C_GL.GLushort,
    _C_GL.GL_INT              : _C_GL.GLint,
    _C_GL.GL_UNSIGNED_INT     : _C_GL.GLuint,
    _C_GL.GL_FLOAT            : _C_GL.GLfloat,
    _C_GL.GL_DOUBLE           : _C_GL.GLdouble,
    _C_GL.GL_2_BYTES          : _C_GL.GLbyte,
    _C_GL.GL_3_BYTES          : _C_GL.GLbyte,
    _C_GL.GL_4_BYTES          : _C_GL.GLbyte,
}

def gl_type_id_to_py_type(type_):
    return _gl_type_id_to_py_type_map.get(type_, None)

_gl_type_id_to_py_type_map = {
    _C_GL.GL_BYTE             : int,
    _C_GL.GL_UNSIGNED_BYTE    : int,
    _C_GL.GL_SHORT            : int,
    _C_GL.GL_UNSIGNED_SHORT   : int,
    _C_GL.GL_INT              : int,
    _C_GL.GL_UNSIGNED_INT     : int,
    _C_GL.GL_FLOAT            : float,
    _C_GL.GL_DOUBLE           : float,
    _C_GL.GL_2_BYTES          : int, 
    _C_GL.GL_3_BYTES          : int,  
    _C_GL.GL_4_BYTES          : int,  
}

def get_read_pixels_format_count(format_):
    return _read_pixels_format_count.get(format_, None)

def get_read_pixels_type_size(type_):
    return _read_pixels_type_size.get(type_, None)

def get_gl_error_str(gl_error_code):
    gl_error_str = _gl_error_code_to_str.get(gl_error_code, None)
    if gl_error_str is None:
        return "(%d)" % gl_error_code
    return gl_error_str

def get_map_stride(target):
    return _map_strides.get(target, None)

def get_map_1d_stride(target):
    return _map_1d_strides.get(target, None)

def get_map_2d_stride(target):
    return _map_2d_strides.get(target, None)

_map_1d_strides = {
    _C_GL.GL_MAP1_COLOR_4             : 4, 
    _C_GL.GL_MAP1_INDEX               : 1, 
    _C_GL.GL_MAP1_NORMAL              : 3, 
    _C_GL.GL_MAP1_TEXTURE_COORD_1     : 1, 
    _C_GL.GL_MAP1_TEXTURE_COORD_2     : 2, 
    _C_GL.GL_MAP1_TEXTURE_COORD_3     : 3, 
    _C_GL.GL_MAP1_TEXTURE_COORD_4     : 4, 
    _C_GL.GL_MAP1_VERTEX_3            : 3, 
    _C_GL.GL_MAP1_VERTEX_4            : 4, 
}

_map_2d_strides = {
    _C_GL.GL_MAP2_COLOR_4             : 4,
    _C_GL.GL_MAP2_INDEX               : 1, 
    _C_GL.GL_MAP2_NORMAL              : 3, 
    _C_GL.GL_MAP2_TEXTURE_COORD_1     : 1, 
    _C_GL.GL_MAP2_TEXTURE_COORD_2     : 2, 
    _C_GL.GL_MAP2_TEXTURE_COORD_3     : 3, 
    _C_GL.GL_MAP2_TEXTURE_COORD_4     : 4, 
    _C_GL.GL_MAP2_VERTEX_3            : 3,
    _C_GL.GL_MAP2_VERTEX_4            : 4,
}

_map_strides = _map_1d_strides | _map_2d_strides

def is_map_1d_target(target):
    return target in [
        _C_GL.GL_MAP1_COLOR_4, 
        _C_GL.GL_MAP1_INDEX, 
        _C_GL.GL_MAP1_NORMAL, 
        _C_GL.GL_MAP1_TEXTURE_COORD_1, 
        _C_GL.GL_MAP1_TEXTURE_COORD_2, 
        _C_GL.GL_MAP1_TEXTURE_COORD_3, 
        _C_GL.GL_MAP1_TEXTURE_COORD_4, 
        _C_GL.GL_MAP1_VERTEX_3, 
        _C_GL.GL_MAP1_VERTEX_4, 
    ]

def get_fog_params_length(pname):
    return _fog_params_lengths.get(pname, None)

_fog_params_lengths = {
    # Note: Commented items are from OpenGL above version 1.1.

    _C_GL.GL_FOG_MODE         : 1,
    _C_GL.GL_FOG_DENSITY      : 1,
    _C_GL.GL_FOG_START        : 1,
    _C_GL.GL_FOG_END          : 1,
    _C_GL.GL_FOG_INDEX        : 1,
    _C_GL.GL_FOG_COLOR        : 4,
    # _C_GL.GL_FOG_COORD_SRC    : 1,
}

def get_pixel_map_size_id(map_id):
    return _pixel_map_size_ids.get(map_id, None)

_pixel_map_size_ids = {
    _C_GL.GL_PIXEL_MAP_I_TO_I : _C_GL.GL_PIXEL_MAP_I_TO_I_SIZE,
    _C_GL.GL_PIXEL_MAP_S_TO_S : _C_GL.GL_PIXEL_MAP_S_TO_S_SIZE,
    _C_GL.GL_PIXEL_MAP_I_TO_R : _C_GL.GL_PIXEL_MAP_I_TO_R_SIZE,
    _C_GL.GL_PIXEL_MAP_I_TO_G : _C_GL.GL_PIXEL_MAP_I_TO_G_SIZE,
    _C_GL.GL_PIXEL_MAP_I_TO_B : _C_GL.GL_PIXEL_MAP_I_TO_B_SIZE,
    _C_GL.GL_PIXEL_MAP_I_TO_A : _C_GL.GL_PIXEL_MAP_I_TO_A_SIZE,
    _C_GL.GL_PIXEL_MAP_R_TO_R : _C_GL.GL_PIXEL_MAP_R_TO_R_SIZE,
    _C_GL.GL_PIXEL_MAP_G_TO_G : _C_GL.GL_PIXEL_MAP_G_TO_G_SIZE,
    _C_GL.GL_PIXEL_MAP_B_TO_B : _C_GL.GL_PIXEL_MAP_B_TO_B_SIZE,
    _C_GL.GL_PIXEL_MAP_A_TO_A : _C_GL.GL_PIXEL_MAP_A_TO_A_SIZE,
}

def get_tex_gen_params_length(pname):
    return _tex_gen_params_lengths.get(pname, None)

_tex_gen_params_lengths = {
    _C_GL.GL_TEXTURE_GEN_MODE : 1,
    _C_GL.GL_OBJECT_PLANE     : 4,
    _C_GL.GL_EYE_PLANE        : 4,
}

def get_tex_env_params_length(pname):
    return _tex_env_params_lengths.get(pname, None)

_tex_env_params_lengths = {
    _C_GL.GL_TEXTURE_ENV_MODE     : 1,
    _C_GL.GL_TEXTURE_ENV_COLOR    : 4,   
    # _C_GL.GL_COMBINE_RGB          : 1,
    # _C_GL.GL_COMBINE_ALPHA        : 1,
    # _C_GL.GL_SRC0_RGB             : 1,
    # _C_GL.GL_SRC1_RGB             : 1,
    # _C_GL.GL_SRC2_RGB             : 1,
    # _C_GL.GL_SRC0_ALPHA           : 1,
    # _C_GL.GL_SRC1_ALPHA           : 1,
    # _C_GL.GL_SRC2_ALPHA           : 1,
    # _C_GL.GL_OPERAND0_RGB         : 1,
    # _C_GL.GL_OPERAND1_RGB         : 1,
    # _C_GL.GL_OPERAND2_RGB         : 1,
    # _C_GL.GL_OPERAND0_ALPHA       : 1,
    # _C_GL.GL_OPERAND1_ALPHA       : 1,
    # _C_GL.GL_OPERAND2_ALPHA       : 1,
    # _C_GL.GL_RGB_SCALE            : 1,
    _C_GL.GL_ALPHA_SCALE          : 1,
    # _C_GL.GL_COORD_REPLACE_OES    : 1,   # bool only, glGetTexEnv{...} only
}

def get_call_lists_py_type(type_):
    return _call_lists_py_types.get(type_, None)

_call_lists_py_types = {
    _C_GL.GL_BYTE             : int,
    _C_GL.GL_UNSIGNED_BYTE    : int,
    _C_GL.GL_SHORT            : int,
    _C_GL.GL_UNSIGNED_SHORT   : int,
    _C_GL.GL_INT              : int,
    _C_GL.GL_UNSIGNED_INT     : int,
    _C_GL.GL_FLOAT            : float,
    _C_GL.GL_2_BYTES          : int,
    _C_GL.GL_3_BYTES          : int,
    _C_GL.GL_4_BYTES          : int,
}

def get_call_lists_c_type(type_):
    return _call_lists_c_types.get(type_, None)

_call_lists_c_types = {
    _C_GL.GL_BYTE             : _C_GL.GLbyte,
    _C_GL.GL_UNSIGNED_BYTE    : _C_GL.GLubyte,
    _C_GL.GL_SHORT            : _C_GL.GLshort,
    _C_GL.GL_UNSIGNED_SHORT   : _C_GL.GLushort,
    _C_GL.GL_INT              : _C_GL.GLint,
    _C_GL.GL_UNSIGNED_INT     : _C_GL.GLuint,
    _C_GL.GL_FLOAT            : _C_GL.GLfloat,
    _C_GL.GL_2_BYTES          : _C_GL.GLubyte,
    _C_GL.GL_3_BYTES          : _C_GL.GLubyte,
    _C_GL.GL_4_BYTES          : _C_GL.GLubyte,
}

def get_acceptable_tex_target_ids():
    return _acceptable_tex_target_ids

_acceptable_tex_target_ids = set([
    # Note: Commented items are from OpenGL above version 1.1.

    _C_GL.GL_TEXTURE_1D, 
    _C_GL.GL_TEXTURE_2D, 
    # _C_GL.GL_TEXTURE_3D, 
    # _C_GL.GL_TEXTURE_1D_ARRAY, 
    # _C_GL.GL_TEXTURE_2D_ARRAY, 
    # _C_GL.GL_TEXTURE_RECTANGLE, 
    _C_GL.GL_PROXY_TEXTURE_1D, 
    _C_GL.GL_PROXY_TEXTURE_2D, 
    # _C_GL.GL_PROXY_TEXTURE_3D, 
    # _C_GL.GL_TEXTURE_CUBE_MAP_POSITIVE_X, 
    # _C_GL.GL_TEXTURE_CUBE_MAP_NEGATIVE_X, 
    # _C_GL.GL_TEXTURE_CUBE_MAP_POSITIVE_Y, 
    # _C_GL.GL_TEXTURE_CUBE_MAP_NEGATIVE_Y, 
    # _C_GL.GL_TEXTURE_CUBE_MAP_POSITIVE_Z, 
    # _C_GL.GL_TEXTURE_CUBE_MAP_NEGATIVE_Z, 
    # _C_GL.GL_TEXTURE_CUBE_MAP_ARRAY,
    # _C_GL.GL_PROXY_TEXTURE_CUBE_MAP,
])

def get_tex_level_parameter_number(pname):
    return _tex_level_parameter_numbers.get(pname, None)

_tex_level_parameter_numbers = {
    # Note: Commented items are from OpenGL above version 1.1.

    _C_GL.GL_TEXTURE_WIDTH                  : 1,
    _C_GL.GL_TEXTURE_HEIGHT                 : 1,
    # _C_GL.GL_TEXTURE_DEPTH                  : 1,
    # _C_GL.GL_TEXTURE_INTERNAL_FORMAT        : 1,
    _C_GL.GL_TEXTURE_BORDER                 : 1,
    # _C_GL.GL_TEXTURE_RED_TYPE               : 1, 
    # _C_GL.GL_TEXTURE_GREEN_TYPE             : 1, 
    # _C_GL.GL_TEXTURE_BLUE_TYPE              : 1, 
    # _C_GL.GL_TEXTURE_ALPHA_TYPE             : 1, 
    # _C_GL.GL_TEXTURE_DEPTH_TYPE             : 1,
    _C_GL.GL_TEXTURE_RED_SIZE               : 1,
    _C_GL.GL_TEXTURE_GREEN_SIZE             : 1,
    _C_GL.GL_TEXTURE_BLUE_SIZE              : 1,
    _C_GL.GL_TEXTURE_ALPHA_SIZE             : 1,
    _C_GL.GL_TEXTURE_LUMINANCE_SIZE         : 1,
    _C_GL.GL_TEXTURE_INTENSITY_SIZE         : 1,
    # _C_GL.GL_TEXTURE_DEPTH_SIZE             : 1,
    # _C_GL.GL_TEXTURE_COMPRESSED             : 1,
    # _C_GL.GL_TEXTURE_COMPRESSED_IMAGE_SIZE  : 1,
    # _C_GL.GL_TEXTURE_BUFFER_OFFSET          : 1,
    # _C_GL.GL_TEXTURE_BUFFER_SIZE            : 1,
}

def get_tex_format_element_number(format_):
    return _texture_format_element_numbers.get(format_, None)


_texture_format_element_numbers = {
    # Note: Commented items are from OpenGL above version 1.1.

    _C_GL.GL_COLOR_INDEX      : 1,
    _C_GL.GL_STENCIL_INDEX    : 1,
    _C_GL.GL_DEPTH_COMPONENT  : 1,
    # _C_GL.GL_DEPTH_STENCIL    : 2,
    _C_GL.GL_RED              : 1,
    _C_GL.GL_GREEN            : 1,
    _C_GL.GL_BLUE             : 1,
    _C_GL.GL_ALPHA            : 1,
    # _C_GL.GL_RG               : 2,
    _C_GL.GL_RGB              : 3,
    _C_GL.GL_RGBA             : 4,
    # _C_GL.GL_BGR              : 3,
    # _C_GL.GL_BGRA             : 4,
    # _C_GL.GL_RED_INTEGER      : 1,
    # _C_GL.GL_GREEN_INTEGER    : 1,
    # _C_GL.GL_BLUE_INTEGER     : 1,
    # _C_GL.GL_RG_INTEGER       : 2,
    # _C_GL.GL_RGB_INTEGER      : 3,
    # _C_GL.GL_RGBA_INTEGER     : 4,
    # _C_GL.GL_BGR_INTEGER      : 3,
    # _C_GL.GL_BGRA_INTEGER     : 4,
    _C_GL.GL_LUMINANCE        : 1,
    _C_GL.GL_LUMINANCE_ALPHA  : 2,
}

def get_tex_type_mul_div_size(type_):
    return _texture_type_mul_div_sizes.get(type_, None)

_texture_type_mul_div_sizes = {
    # Note: Commented items are from OpenGL above version 1.1.

    _C_GL.GL_UNSIGNED_BYTE                   : (1, 1), 
    _C_GL.GL_BYTE                            : (1, 1),
    _C_GL.GL_UNSIGNED_SHORT                  : (2, 1),
    _C_GL.GL_SHORT                           : (2, 1),
    _C_GL.GL_UNSIGNED_INT                    : (4, 1),
    _C_GL.GL_INT                             : (4, 1),
    # _C_GL.GL_HALF_FLOAT                      : (2, 1),
    _C_GL.GL_FLOAT                           : (4, 1),
    # _C_GL.GL_UNSIGNED_BYTE_3_3_2             : (1, 3),        # GL_RGB, GL_BGR
    # _C_GL.GL_UNSIGNED_BYTE_2_3_3_REV         : (1, 3),        # GL_RGB, GL_BGR
    # _C_GL.GL_UNSIGNED_SHORT_5_6_5            : (2, 3),        # GL_RGB, GL_BGR
    # _C_GL.GL_UNSIGNED_SHORT_5_6_5_REV        : (2, 3),        # GL_RGB, GL_BGR
    # _C_GL.GL_UNSIGNED_SHORT_4_4_4_4          : (2, 4),        # GL_RGBA, GL_ABGR
    # _C_GL.GL_UNSIGNED_SHORT_4_4_4_4_REV      : (2, 4),        # GL_RGBA, GL_ABGR
    # _C_GL.GL_UNSIGNED_SHORT_5_5_5_1          : (2, 4),        # GL_RGBA, GL_ABGR
    # _C_GL.GL_UNSIGNED_SHORT_1_5_5_5_REV      : (2, 4),        # GL_RGBA, GL_ABGR
    # _C_GL.GL_UNSIGNED_INT_8_8_8_8            : (4, 4),        # GL_RGBA, GL_ABGR
    # _C_GL.GL_UNSIGNED_INT_8_8_8_8_REV        : (4, 4),        # GL_RGBA, GL_ABGR
    # _C_GL.GL_UNSIGNED_INT_10_10_10_2         : (4, 4),        # GL_RGBA, GL_ABGR
    # _C_GL.GL_UNSIGNED_INT_2_10_10_10_REV     : (4, 4),        # GL_RGBA, GL_ABGR
    # _C_GL.GL_UNSIGNED_INT_24_8               : (4, 2),        # GL_DEPTH_STENCIL (?)
    # _C_GL.GL_UNSIGNED_INT_10F_11F_11F_REV    : (4, 3),        # GL_RGB, GL_BGR
    # _C_GL.GL_UNSIGNED_INT_5_9_9_9_REV        : (4, 4),        # GL_RGBA, GL_ABGR
    # _C_GL.GL_FLOAT_32_UNSIGNED_INT_24_8_REV  : (4, 3),        # (?)
}

def get_tex_parameter_length(pname):
    return _tex_parameter_lengths.get(pname, None)


_tex_parameter_lengths = {
    # Note: Commented items are from OpenGL above version 1.1.

    # _C_GL.GL_DEPTH_STENCIL_TEXTURE_MODE : 1,
    # _C_GL.GL_TEXTURE_BASE_LEVEL : 1,
    _C_GL.GL_TEXTURE_BORDER_COLOR : 4,
    # _C_GL.GL_TEXTURE_COMPARE_FUNC : 1,
    # _C_GL.GL_TEXTURE_COMPARE_MODE : 1,
    # _C_GL.GL_TEXTURE_LOD_BIAS : 1,
    _C_GL.GL_TEXTURE_MIN_FILTER : 1,
    _C_GL.GL_TEXTURE_MAG_FILTER : 1,
    # _C_GL.GL_TEXTURE_MIN_LOD : 1,
    # _C_GL.GL_TEXTURE_MAX_LOD : 1,
    # _C_GL.GL_TEXTURE_MAX_LEVEL : 1,
    # _C_GL.GL_TEXTURE_SWIZZLE_R : 1,
    # _C_GL.GL_TEXTURE_SWIZZLE_G : 1,
    # _C_GL.GL_TEXTURE_SWIZZLE_B : 1,
    # _C_GL.GL_TEXTURE_SWIZZLE_A : 1,
    # _C_GL.GL_TEXTURE_SWIZZLE_RGBA : 4,
    _C_GL.GL_TEXTURE_WRAP_S : 1,
    _C_GL.GL_TEXTURE_WRAP_T : 1,
    # _C_GL.GL_TEXTURE_WRAP_R : 1,
    _C_GL.GL_TEXTURE_PRIORITY : 1,
    # _C_GL.GL_DEPTH_TEXTURE_MODE : 1,
    # _C_GL.GL_GENERATE_MIPMAP : 1,
    _C_GL.GL_TEXTURE_RESIDENT : 1,
}

def get_num_of_get_values(pname):
    """
    ReturnType : int
    """
    num = _num_of_get_values.get(pname, None)

    if isinstance(num, tuple):
        c_num = _C_GL.GLint()
        _C_GL.glGetIntegerv(num[0], _ctypes.byref(c_num))
        return int(c_num.value)

    return num

_num_of_get_values = {
    # Note: Commented items are from OpenGL above version 1.1.

    _C_GL.GL_ACCUM_ALPHA_BITS : 1,
    _C_GL.GL_ACCUM_BLUE_BITS : 1,
    _C_GL.GL_ACCUM_CLEAR_VALUE : 4,
    _C_GL.GL_ACCUM_GREEN_BITS : 1,
    _C_GL.GL_ACCUM_RED_BITS : 1,
    # _C_GL.GL_ACTIVE_TEXTURE : 1,
    # _C_GL.GL_ALIASED_LINE_WIDTH_RANGE : 2,
    # _C_GL.GL_ALIASED_POINT_SIZE_RANGE : 2,
    _C_GL.GL_ALPHA_BIAS : 1,
    _C_GL.GL_ALPHA_BITS : 1,
    _C_GL.GL_ALPHA_SCALE : 1,
    _C_GL.GL_ALPHA_TEST : 1,
    _C_GL.GL_ALPHA_TEST_FUNC : 1,
    _C_GL.GL_ALPHA_TEST_REF : 1,
    # _C_GL.GL_ARRAY_BUFFER_BINDING : 1,
    _C_GL.GL_ATTRIB_STACK_DEPTH : 1,
    _C_GL.GL_AUTO_NORMAL : 1,
    _C_GL.GL_AUX_BUFFERS : 1,
    _C_GL.GL_BLEND : 1,
    # _C_GL.GL_BLEND_COLOR : 4,
    # _C_GL.GL_BLEND_DST_ALPHA : 1,
    # _C_GL.GL_BLEND_DST_RGB : 1,
    # _C_GL.GL_BLEND_EQUATION_ALPHA : 1,
    # _C_GL.GL_BLEND_EQUATION_RGB : 1,
    # _C_GL.GL_BLEND_SRC_ALPHA : 1,
    # _C_GL.GL_BLEND_SRC_RGB : 1,
    _C_GL.GL_BLUE_BIAS : 1,
    _C_GL.GL_BLUE_BITS : 1,
    _C_GL.GL_BLUE_SCALE : 1,
    # _C_GL.GL_CLIENT_ACTIVE_TEXTURE : 1,
    _C_GL.GL_CLIENT_ATTRIB_STACK_DEPTH : 1,
    _C_GL.GL_CLIP_PLANE0 : 1,
    _C_GL.GL_CLIP_PLANE1 : 1,
    _C_GL.GL_CLIP_PLANE2 : 1,
    _C_GL.GL_CLIP_PLANE3 : 1,
    _C_GL.GL_CLIP_PLANE4 : 1,
    _C_GL.GL_CLIP_PLANE5 : 1,
    _C_GL.GL_COLOR_ARRAY : 1,
    # _C_GL.GL_COLOR_ARRAY_BUFFER_BINDING : 1,
    _C_GL.GL_COLOR_ARRAY_SIZE : 1,
    _C_GL.GL_COLOR_ARRAY_STRIDE : 1,
    _C_GL.GL_COLOR_ARRAY_TYPE : 1,
    _C_GL.GL_COLOR_CLEAR_VALUE : 4,
    _C_GL.GL_COLOR_LOGIC_OP : 1,
    _C_GL.GL_COLOR_MATERIAL : 1,
    _C_GL.GL_COLOR_MATERIAL_FACE : 1,
    _C_GL.GL_COLOR_MATERIAL_PARAMETER : 1,
    # _C_GL.GL_COLOR_MATRIX : 16,
    # _C_GL.GL_COLOR_MATRIX_STACK_DEPTH : 1,
    # _C_GL.GL_COLOR_SUM : 1,
    # _C_GL.GL_COLOR_TABLE : 1,
    _C_GL.GL_COLOR_WRITEMASK : 4,
    # _C_GL.GL_COMPRESSED_TEXTURE_FORMATS : tuple(_C_GL.GL_NUM_COMPRESSED_TEXTURE_FORMATS),
    # _C_GL.GL_CONTEXT_FLAGS : 1,
    # _C_GL.GL_CONVOLUTION_1D : 1,
    # _C_GL.GL_CONVOLUTION_2D : 1,
    _C_GL.GL_CULL_FACE : 1,
    _C_GL.GL_CULL_FACE_MODE : 1,
    _C_GL.GL_CURRENT_COLOR : 4,
    # _C_GL.GL_CURRENT_FOG_COORD : 1,
    _C_GL.GL_CURRENT_INDEX : 1,
    _C_GL.GL_CURRENT_NORMAL : 3,
    # _C_GL.GL_CURRENT_PROGRAM : 1,
    _C_GL.GL_CURRENT_RASTER_COLOR : 4,
    _C_GL.GL_CURRENT_RASTER_DISTANCE : 1,
    _C_GL.GL_CURRENT_RASTER_INDEX : 1,
    _C_GL.GL_CURRENT_RASTER_POSITION : 4,
    _C_GL.GL_CURRENT_RASTER_POSITION_VALID : 1,
    # _C_GL.GL_CURRENT_RASTER_SECONDARY_COLOR : 4,
    _C_GL.GL_CURRENT_RASTER_TEXTURE_COORDS : 4,
    # _C_GL.GL_CURRENT_SECONDARY_COLOR : 4,
    _C_GL.GL_CURRENT_TEXTURE_COORDS : 4,
    # _C_GL.GL_DEBUG_GROUP_STACK_DEPTH : 1,
    _C_GL.GL_DEPTH_BIAS : 1,
    _C_GL.GL_DEPTH_BITS : 1,
    _C_GL.GL_DEPTH_CLEAR_VALUE : 1,
    _C_GL.GL_DEPTH_FUNC : 1,
    _C_GL.GL_DEPTH_RANGE : 2,
    _C_GL.GL_DEPTH_SCALE : 1,
    _C_GL.GL_DEPTH_TEST : 1,
    _C_GL.GL_DEPTH_WRITEMASK : 1,
    # _C_GL.GL_DISPATCH_INDIRECT_BUFFER_BINDING : 1,
    _C_GL.GL_DITHER : 1,
    _C_GL.GL_DOUBLEBUFFER : 1,
    _C_GL.GL_DRAW_BUFFER : 1,
    # _C_GL.GL_DRAW_BUFFER0 : 1,
    # _C_GL.GL_DRAW_BUFFER1 : 1,
    # _C_GL.GL_DRAW_BUFFER10 : 1,
    # _C_GL.GL_DRAW_BUFFER11 : 1,
    # _C_GL.GL_DRAW_BUFFER12 : 1,
    # _C_GL.GL_DRAW_BUFFER13 : 1,
    # _C_GL.GL_DRAW_BUFFER14 : 1,
    # _C_GL.GL_DRAW_BUFFER15 : 1,
    # _C_GL.GL_DRAW_BUFFER2 : 1,
    # _C_GL.GL_DRAW_BUFFER3 : 1,
    # _C_GL.GL_DRAW_BUFFER4 : 1,
    # _C_GL.GL_DRAW_BUFFER5 : 1,
    # _C_GL.GL_DRAW_BUFFER6 : 1,
    # _C_GL.GL_DRAW_BUFFER7 : 1,
    # _C_GL.GL_DRAW_BUFFER8 : 1,
    # _C_GL.GL_DRAW_BUFFER9 : 1,
    # _C_GL.GL_DRAW_FRAMEBUFFER_BINDING : 1,
    _C_GL.GL_EDGE_FLAG : 1,
    _C_GL.GL_EDGE_FLAG_ARRAY : 1,
    # _C_GL.GL_EDGE_FLAG_ARRAY_BUFFER_BINDING : 1,
    _C_GL.GL_EDGE_FLAG_ARRAY_STRIDE : 1,
    # _C_GL.GL_ELEMENT_ARRAY_BUFFER_BINDING : 1,
    _C_GL.GL_FEEDBACK_BUFFER_SIZE : 1,
    _C_GL.GL_FEEDBACK_BUFFER_TYPE : 1,
    _C_GL.GL_FOG : 1,
    _C_GL.GL_FOG_COLOR : 4,
    # _C_GL.GL_FOG_COORD_ARRAY : 1,
    # _C_GL.GL_FOG_COORD_ARRAY_BUFFER_BINDING : 1,
    # _C_GL.GL_FOG_COORD_ARRAY_STRIDE : 1,
    # _C_GL.GL_FOG_COORD_ARRAY_TYPE : 1,
    # _C_GL.GL_FOG_COORD_SRC : 1,
    _C_GL.GL_FOG_DENSITY : 1,
    _C_GL.GL_FOG_END : 1,
    _C_GL.GL_FOG_HINT : 1,
    _C_GL.GL_FOG_INDEX : 1,
    _C_GL.GL_FOG_MODE : 1,
    _C_GL.GL_FOG_START : 1,
    # _C_GL.GL_FRAGMENT_SHADER_DERIVATIVE_HINT : 1,
    _C_GL.GL_FRONT_FACE : 1,
    # _C_GL.GL_GENERATE_MIPMAP_HINT : 1,
    _C_GL.GL_GREEN_BIAS : 1,
    _C_GL.GL_GREEN_BITS : 1,
    _C_GL.GL_GREEN_SCALE : 1,
    # _C_GL.GL_HISTOGRAM : 1,
    # _C_GL.GL_IMPLEMENTATION_COLOR_READ_FORMAT : 1,
    # _C_GL.GL_IMPLEMENTATION_COLOR_READ_TYPE : 1,
    _C_GL.GL_INDEX_ARRAY : 1,
    # _C_GL.GL_INDEX_ARRAY_BUFFER_BINDING : 1,
    _C_GL.GL_INDEX_ARRAY_STRIDE : 1,
    _C_GL.GL_INDEX_ARRAY_TYPE : 1,
    _C_GL.GL_INDEX_BITS : 1,
    _C_GL.GL_INDEX_CLEAR_VALUE : 1,
    _C_GL.GL_INDEX_LOGIC_OP : 1,
    _C_GL.GL_INDEX_MODE : 1,
    _C_GL.GL_INDEX_OFFSET : 1,
    _C_GL.GL_INDEX_SHIFT : 1,
    _C_GL.GL_INDEX_WRITEMASK : 1,
    # _C_GL.GL_LAYER_PROVOKING_VERTEX : 1,
    _C_GL.GL_LIGHTING : 1,
    _C_GL.GL_LIGHT_MODEL_AMBIENT : 4,
    # _C_GL.GL_LIGHT_MODEL_COLOR_CONTROL : 1,
    _C_GL.GL_LIGHT_MODEL_LOCAL_VIEWER : 1,
    _C_GL.GL_LIGHT_MODEL_TWO_SIDE : 1,
    _C_GL.GL_LIGHT0 : 1,
    _C_GL.GL_LIGHT1 : 1,
    _C_GL.GL_LIGHT2 : 1,
    _C_GL.GL_LIGHT3 : 1,
    _C_GL.GL_LIGHT4 : 1,
    _C_GL.GL_LIGHT5 : 1,
    _C_GL.GL_LIGHT6 : 1,
    _C_GL.GL_LIGHT7 : 1,
    _C_GL.GL_LINE_SMOOTH : 1,
    _C_GL.GL_LINE_SMOOTH_HINT : 1,
    _C_GL.GL_LINE_STIPPLE : 1,
    _C_GL.GL_LINE_STIPPLE_PATTERN : 1,
    _C_GL.GL_LINE_STIPPLE_REPEAT : 1,
    _C_GL.GL_LINE_WIDTH : 1,
    _C_GL.GL_LINE_WIDTH_GRANULARITY : 1,
    _C_GL.GL_LINE_WIDTH_RANGE : 2,
    _C_GL.GL_LIST_BASE : 1,
    _C_GL.GL_LIST_INDEX : 1,
    _C_GL.GL_LIST_MODE : 1,
    _C_GL.GL_LOGIC_OP_MODE : 1,
    # _C_GL.GL_MAJOR_VERSION : 1,
    _C_GL.GL_MAP1_COLOR_4 : 1,
    _C_GL.GL_MAP1_GRID_DOMAIN : 2,
    _C_GL.GL_MAP1_GRID_SEGMENTS : 1,
    _C_GL.GL_MAP1_INDEX : 1,
    _C_GL.GL_MAP1_NORMAL : 1,
    _C_GL.GL_MAP1_TEXTURE_COORD_1 : 1,
    _C_GL.GL_MAP1_TEXTURE_COORD_2 : 1,
    _C_GL.GL_MAP1_TEXTURE_COORD_3 : 1,
    _C_GL.GL_MAP1_TEXTURE_COORD_4 : 1,
    _C_GL.GL_MAP1_VERTEX_3 : 1,
    _C_GL.GL_MAP1_VERTEX_4 : 1,
    _C_GL.GL_MAP2_COLOR_4 : 1,
    _C_GL.GL_MAP2_GRID_DOMAIN : 4,
    _C_GL.GL_MAP2_GRID_SEGMENTS : 2,
    _C_GL.GL_MAP2_INDEX : 1,
    _C_GL.GL_MAP2_NORMAL : 1,
    _C_GL.GL_MAP2_TEXTURE_COORD_1 : 1,
    _C_GL.GL_MAP2_TEXTURE_COORD_2 : 1,
    _C_GL.GL_MAP2_TEXTURE_COORD_3 : 1,
    _C_GL.GL_MAP2_TEXTURE_COORD_4 : 1,
    _C_GL.GL_MAP2_VERTEX_3 : 1,
    _C_GL.GL_MAP2_VERTEX_4 : 1,
    _C_GL.GL_MAP_COLOR : 1,
    _C_GL.GL_MAP_STENCIL : 1,
    _C_GL.GL_MATRIX_MODE : 1,
    # _C_GL.GL_MAX_3D_TEXTURE_SIZE : 1,
    # _C_GL.GL_MAX_ARRAY_TEXTURE_LAYERS : 1,
    _C_GL.GL_MAX_ATTRIB_STACK_DEPTH : 1,
    _C_GL.GL_MAX_CLIENT_ATTRIB_STACK_DEPTH : 1,
    # _C_GL.GL_MAX_CLIP_DISTANCES : 1,
    _C_GL.GL_MAX_CLIP_PLANES : 1,
    # _C_GL.GL_MAX_COLOR_MATRIX_STACK_DEPTH : 1,
    # _C_GL.GL_MAX_COLOR_TEXTURE_SAMPLES : 1,
    # _C_GL.GL_MAX_COMBINED_ATOMIC_COUNTERS : 1,
    # _C_GL.GL_MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS : 1,
    # _C_GL.GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS : 1,
    # _C_GL.GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS : 1,
    # _C_GL.GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS : 1,
    # _C_GL.GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS : 1,
    # _C_GL.GL_MAX_COMBINED_UNIFORM_BLOCKS : 1,
    # _C_GL.GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS : 1,
    # _C_GL.GL_MAX_COMPUTE_ATOMIC_COUNTERS : 1,
    # _C_GL.GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS : 1,
    # _C_GL.GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS : 1,
    # _C_GL.GL_MAX_COMPUTE_TEXTURE_IMAGE_UNITS : 1,
    # _C_GL.GL_MAX_COMPUTE_UNIFORM_BLOCKS : 1,
    # _C_GL.GL_MAX_COMPUTE_UNIFORM_COMPONENTS : 1,
    # _C_GL.GL_MAX_COMPUTE_WORK_GROUP_COUNT : 1,
    # _C_GL.GL_MAX_COMPUTE_WORK_GROUP_INVOCATIONS : 1,
    # _C_GL.GL_MAX_COMPUTE_WORK_GROUP_SIZE : 1,
    # _C_GL.GL_MAX_CUBE_MAP_TEXTURE_SIZE : 1,
    # _C_GL.GL_MAX_DEBUG_GROUP_STACK_DEPTH : 1,
    # _C_GL.GL_MAX_DEPTH_TEXTURE_SAMPLES : 1,
    # _C_GL.GL_MAX_DRAW_BUFFERS : 1,
    # _C_GL.GL_MAX_DUAL_SOURCE_DRAW_BUFFERS : 1,
    # _C_GL.GL_MAX_ELEMENTS_INDICES : 1,
    # _C_GL.GL_MAX_ELEMENTS_VERTICES : 1,
    # _C_GL.GL_MAX_ELEMENT_INDEX : 1,
    _C_GL.GL_MAX_EVAL_ORDER : 1,
    # _C_GL.GL_MAX_FRAGMENT_ATOMIC_COUNTERS : 1,
    # _C_GL.GL_MAX_FRAGMENT_INPUT_COMPONENTS : 1,
    # _C_GL.GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS : 1,
    # _C_GL.GL_MAX_FRAGMENT_UNIFORM_BLOCKS : 1,
    # _C_GL.GL_MAX_FRAGMENT_UNIFORM_COMPONENTS : 1,
    # _C_GL.GL_MAX_FRAGMENT_UNIFORM_VECTORS : 1,
    # _C_GL.GL_MAX_FRAMEBUFFER_HEIGHT : 1,
    # _C_GL.GL_MAX_FRAMEBUFFER_LAYERS : 1,
    # _C_GL.GL_MAX_FRAMEBUFFER_SAMPLES : 1,
    # _C_GL.GL_MAX_FRAMEBUFFER_WIDTH : 1,
    # _C_GL.GL_MAX_GEOMETRY_ATOMIC_COUNTERS : 1,
    # _C_GL.GL_MAX_GEOMETRY_INPUT_COMPONENTS : 1,
    # _C_GL.GL_MAX_GEOMETRY_OUTPUT_COMPONENTS : 1,
    # _C_GL.GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS : 1,
    # _C_GL.GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS : 1,
    # _C_GL.GL_MAX_GEOMETRY_UNIFORM_BLOCKS : 1,
    # _C_GL.GL_MAX_GEOMETRY_UNIFORM_COMPONENTS : 1,
    # _C_GL.GL_MAX_INTEGER_SAMPLES : 1,
    # _C_GL.GL_MAX_LABEL_LENGTH : 1,
    _C_GL.GL_MAX_LIGHTS : 1,
    _C_GL.GL_MAX_LIST_NESTING : 1,
    _C_GL.GL_MAX_MODELVIEW_STACK_DEPTH : 1,
    _C_GL.GL_MAX_NAME_STACK_DEPTH : 1,
    _C_GL.GL_MAX_PIXEL_MAP_TABLE : 1,
    # _C_GL.GL_MAX_PROGRAM_TEXEL_OFFSET : 1,
    _C_GL.GL_MAX_PROJECTION_STACK_DEPTH : 1,
    # _C_GL.GL_MAX_RECTANGLE_TEXTURE_SIZE : 1,
    # _C_GL.GL_MAX_RENDERBUFFER_SIZE : 1,
    # _C_GL.GL_MAX_SAMPLE_MASK_WORDS : 1,
    # _C_GL.GL_MAX_SERVER_WAIT_TIMEOUT : 1,
    # _C_GL.GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS : 1,
    # _C_GL.GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS : 1,
    # _C_GL.GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS : 1,
    # _C_GL.GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS : 1,
    # _C_GL.GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS : 1,
    # _C_GL.GL_MAX_TEXTURE_BUFFER_SIZE : 1,
    # _C_GL.GL_MAX_TEXTURE_COORDS : 1,
    # _C_GL.GL_MAX_TEXTURE_IMAGE_UNITS : 1,
    # _C_GL.GL_MAX_TEXTURE_LOD_BIAS : 1,
    _C_GL.GL_MAX_TEXTURE_SIZE : 1,
    _C_GL.GL_MAX_TEXTURE_STACK_DEPTH : 1,
    # _C_GL.GL_MAX_TEXTURE_UNITS : 1,
    # _C_GL.GL_MAX_UNIFORM_BLOCK_SIZE : 1,
    # _C_GL.GL_MAX_UNIFORM_BUFFER_BINDINGS : 1,
    # _C_GL.GL_MAX_UNIFORM_LOCATIONS : 1,
    # _C_GL.GL_MAX_VARYING_COMPONENTS : 1,
    # _C_GL.GL_MAX_VARYING_FLOATS : 1,
    # _C_GL.GL_MAX_VARYING_VECTORS : 1,
    # _C_GL.GL_MAX_VERTEX_ATOMIC_COUNTERS : 1,
    # _C_GL.GL_MAX_VERTEX_ATTRIBS : 1,
    # _C_GL.GL_MAX_VERTEX_ATTRIB_BINDINGS : 1,
    # _C_GL.GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET : 1,
    # _C_GL.GL_MAX_VERTEX_OUTPUT_COMPONENTS : 1,
    # _C_GL.GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS : 1,
    # _C_GL.GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS : 1,
    # _C_GL.GL_MAX_VERTEX_UNIFORM_BLOCKS : 1,
    # _C_GL.GL_MAX_VERTEX_UNIFORM_COMPONENTS : 1,
    # _C_GL.GL_MAX_VERTEX_UNIFORM_VECTORS : 1,
    # _C_GL.GL_MAX_VIEWPORTS : 1,
    _C_GL.GL_MAX_VIEWPORT_DIMS : 2,
    # _C_GL.GL_MINMAX : 1,
    # _C_GL.GL_MINOR_VERSION : 1,
    # _C_GL.GL_MIN_MAP_BUFFER_ALIGNMENT : 1,
    # _C_GL.GL_MIN_PROGRAM_TEXEL_OFFSET : 1,
    _C_GL.GL_MODELVIEW_MATRIX : 16,
    _C_GL.GL_MODELVIEW_STACK_DEPTH : 1,
    _C_GL.GL_NAME_STACK_DEPTH : 1,
    _C_GL.GL_NORMALIZE : 1,
    _C_GL.GL_NORMAL_ARRAY : 1,
    # _C_GL.GL_NORMAL_ARRAY_BUFFER_BINDING : 1,
    _C_GL.GL_NORMAL_ARRAY_STRIDE : 1,
    _C_GL.GL_NORMAL_ARRAY_TYPE : 1,
    # _C_GL.GL_NUM_COMPRESSED_TEXTURE_FORMATS : 1,
    # _C_GL.GL_NUM_EXTENSIONS : 1,
    # _C_GL.GL_NUM_PROGRAM_BINARY_FORMATS : 1,
    # _C_GL.GL_NUM_SHADER_BINARY_FORMATS : 1,
    _C_GL.GL_PACK_ALIGNMENT : 1,
    # _C_GL.GL_PACK_IMAGE_HEIGHT : 1,
    _C_GL.GL_PACK_LSB_FIRST : 1,
    _C_GL.GL_PACK_ROW_LENGTH : 1,
    # _C_GL.GL_PACK_SKIP_IMAGES : 1,
    _C_GL.GL_PACK_SKIP_PIXELS : 1,
    _C_GL.GL_PACK_SKIP_ROWS : 1,
    _C_GL.GL_PACK_SWAP_BYTES : 1,
    _C_GL.GL_PERSPECTIVE_CORRECTION_HINT : 1,
    _C_GL.GL_PIXEL_MAP_A_TO_A_SIZE : 1,
    _C_GL.GL_PIXEL_MAP_B_TO_B_SIZE : 1,
    _C_GL.GL_PIXEL_MAP_G_TO_G_SIZE : 1,
    _C_GL.GL_PIXEL_MAP_I_TO_A_SIZE : 1,
    _C_GL.GL_PIXEL_MAP_I_TO_B_SIZE : 1,
    _C_GL.GL_PIXEL_MAP_I_TO_G_SIZE : 1,
    _C_GL.GL_PIXEL_MAP_I_TO_I_SIZE : 1,
    _C_GL.GL_PIXEL_MAP_I_TO_R_SIZE : 1,
    _C_GL.GL_PIXEL_MAP_R_TO_R_SIZE : 1,
    _C_GL.GL_PIXEL_MAP_S_TO_S_SIZE : 1,
    # _C_GL.GL_PIXEL_PACK_BUFFER_BINDING : 1,
    # _C_GL.GL_PIXEL_UNPACK_BUFFER_BINDING : 1,
    # _C_GL.GL_POINT_DISTANCE_ATTENUATION : 3,
    # _C_GL.GL_POINT_FADE_THRESHOLD_SIZE : 1,
    _C_GL.GL_POINT_SIZE : 1,
    _C_GL.GL_POINT_SIZE_GRANULARITY : 1,
    # _C_GL.GL_POINT_SIZE_MAX : 1,
    # _C_GL.GL_POINT_SIZE_MIN : 1,
    _C_GL.GL_POINT_SIZE_RANGE : 2,
    _C_GL.GL_POINT_SMOOTH : 1,
    _C_GL.GL_POINT_SMOOTH_HINT : 1,
    # _C_GL.GL_POINT_SPRITE : 1,
    _C_GL.GL_POLYGON_MODE : 2,
    _C_GL.GL_POLYGON_OFFSET_FACTOR : 1,
    _C_GL.GL_POLYGON_OFFSET_FILL : 1,
    _C_GL.GL_POLYGON_OFFSET_LINE : 1,
    _C_GL.GL_POLYGON_OFFSET_POINT : 1,
    _C_GL.GL_POLYGON_OFFSET_UNITS : 1,
    _C_GL.GL_POLYGON_SMOOTH : 1,
    _C_GL.GL_POLYGON_SMOOTH_HINT : 1,
    _C_GL.GL_POLYGON_STIPPLE : 1,
    # _C_GL.GL_POST_COLOR_MATRIX_ALPHA_BIAS : 1,
    # _C_GL.GL_POST_COLOR_MATRIX_ALPHA_SCALE : 1,
    # _C_GL.GL_POST_COLOR_MATRIX_BLUE_BIAS : 1,
    # _C_GL.GL_POST_COLOR_MATRIX_BLUE_SCALE : 1,
    # _C_GL.GL_POST_COLOR_MATRIX_COLOR_TABLE : 1,
    # _C_GL.GL_POST_COLOR_MATRIX_GREEN_BIAS : 1,
    # _C_GL.GL_POST_COLOR_MATRIX_GREEN_SCALE : 1,
    # _C_GL.GL_POST_COLOR_MATRIX_RED_BIAS : 1,
    # _C_GL.GL_POST_COLOR_MATRIX_RED_SCALE : 1,
    # _C_GL.GL_POST_CONVOLUTION_ALPHA_BIAS : 1,
    # _C_GL.GL_POST_CONVOLUTION_ALPHA_SCALE : 1,
    # _C_GL.GL_POST_CONVOLUTION_BLUE_BIAS : 1,
    # _C_GL.GL_POST_CONVOLUTION_BLUE_SCALE : 1,
    # _C_GL.GL_POST_CONVOLUTION_COLOR_TABLE : 1,
    # _C_GL.GL_POST_CONVOLUTION_GREEN_BIAS : 1,
    # _C_GL.GL_POST_CONVOLUTION_GREEN_SCALE : 1,
    # _C_GL.GL_POST_CONVOLUTION_RED_BIAS : 1,
    # _C_GL.GL_POST_CONVOLUTION_RED_SCALE : 1,
    # _C_GL.GL_PRIMITIVE_RESTART_INDEX : 1,
    # _C_GL.GL_PROGRAM_BINARY_FORMATS : tuple(_C_GL.GL_NUM_PROGRAM_BINARY_FORMATS),
    # _C_GL.GL_PROGRAM_PIPELINE_BINDING : 1,
    # _C_GL.GL_PROGRAM_POINT_SIZE : 1,
    _C_GL.GL_PROJECTION_MATRIX : 16,
    _C_GL.GL_PROJECTION_STACK_DEPTH : 1,
    # _C_GL.GL_PROVOKING_VERTEX : 1,
    _C_GL.GL_READ_BUFFER : 1,
    # _C_GL.GL_READ_FRAMEBUFFER_BINDING : 1,
    _C_GL.GL_RED_BIAS : 1,
    _C_GL.GL_RED_BITS : 1,
    _C_GL.GL_RED_SCALE : 1,
    # _C_GL.GL_RENDERBUFFER_BINDING : 1,
    _C_GL.GL_RENDER_MODE : 1,
    # _C_GL.GL_RESCALE_NORMAL : 1,
    _C_GL.GL_RGBA_MODE : 1,
    # _C_GL.GL_SAMPLER_BINDING : 1,
    # _C_GL.GL_SAMPLES : 1,
    # _C_GL.GL_SAMPLE_BUFFERS : 1,
    # _C_GL.GL_SAMPLE_COVERAGE_INVERT : 1,
    # _C_GL.GL_SAMPLE_COVERAGE_VALUE : 1,
    # _C_GL.GL_SAMPLE_MASK_VALUE : 1,
    _C_GL.GL_SCISSOR_BOX : 4,
    _C_GL.GL_SCISSOR_TEST : 1,
    # _C_GL.GL_SECONDARY_COLOR_ARRAY : 1,
    # _C_GL.GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING : 1,
    # _C_GL.GL_SECONDARY_COLOR_ARRAY_SIZE : 1,
    # _C_GL.GL_SECONDARY_COLOR_ARRAY_STRIDE : 1,
    # _C_GL.GL_SECONDARY_COLOR_ARRAY_TYPE : 1,
    _C_GL.GL_SELECTION_BUFFER_SIZE : 1,
    # _C_GL.GL_SEPARABLE_2D : 1,
    # _C_GL.GL_SHADER_COMPILER : 1,
    # _C_GL.GL_SHADER_STORAGE_BUFFER_BINDING : 1,           # glGetIntegeri_v
    # _C_GL.GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT : 1,
    # _C_GL.GL_SHADER_STORAGE_BUFFER_SIZE : 1,              # glGetIntegeri_v
    # _C_GL.GL_SHADER_STORAGE_BUFFER_START : 1,             # glGetIntegeri_v
    _C_GL.GL_SHADE_MODEL : 1,
    # _C_GL.GL_SMOOTH_LINE_WIDTH_GRANULARITY : 1,
    # _C_GL.GL_SMOOTH_LINE_WIDTH_RANGE : 2,
    # _C_GL.GL_SMOOTH_POINT_SIZE_GRANULARITY : 1,
    # _C_GL.GL_SMOOTH_POINT_SIZE_RANGE : 2,
    # _C_GL.GL_STENCIL_BACK_FAIL : 1,
    # _C_GL.GL_STENCIL_BACK_FUNC : 1,
    # _C_GL.GL_STENCIL_BACK_PASS_DEPTH_FAIL : 1,
    # _C_GL.GL_STENCIL_BACK_PASS_DEPTH_PASS : 1,
    # _C_GL.GL_STENCIL_BACK_REF : 1,
    # _C_GL.GL_STENCIL_BACK_VALUE_MASK : 1,
    # _C_GL.GL_STENCIL_BACK_WRITEMASK : 1,
    _C_GL.GL_STENCIL_BITS : 1,
    _C_GL.GL_STENCIL_CLEAR_VALUE : 1,
    _C_GL.GL_STENCIL_FAIL : 1,
    _C_GL.GL_STENCIL_FUNC : 1,
    _C_GL.GL_STENCIL_PASS_DEPTH_FAIL : 1,
    _C_GL.GL_STENCIL_PASS_DEPTH_PASS : 1,
    _C_GL.GL_STENCIL_REF : 1,
    _C_GL.GL_STENCIL_TEST : 1,
    _C_GL.GL_STENCIL_VALUE_MASK : 1,
    _C_GL.GL_STENCIL_WRITEMASK : 1,
    _C_GL.GL_STEREO : 1,
    _C_GL.GL_SUBPIXEL_BITS : 1,
    _C_GL.GL_TEXTURE_1D : 1,
    _C_GL.GL_TEXTURE_2D : 1,
    # _C_GL.GL_TEXTURE_3D : 1,
    _C_GL.GL_TEXTURE_BINDING_1D : 1,
    # _C_GL.GL_TEXTURE_BINDING_1D_ARRAY : 1,
    _C_GL.GL_TEXTURE_BINDING_2D : 1,
    # _C_GL.GL_TEXTURE_BINDING_2D_ARRAY : 1,
    # _C_GL.GL_TEXTURE_BINDING_2D_MULTISAMPLE : 1,
    # _C_GL.GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY : 1,
    # _C_GL.GL_TEXTURE_BINDING_3D : 1,
    # _C_GL.GL_TEXTURE_BINDING_BUFFER : 1,
    # _C_GL.GL_TEXTURE_BINDING_CUBE_MAP : 1,
    # _C_GL.GL_TEXTURE_BINDING_RECTANGLE : 1,
    # _C_GL.GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT : 1,
    # _C_GL.GL_TEXTURE_COMPRESSION_HINT : 1,
    _C_GL.GL_TEXTURE_COORD_ARRAY : 1,
    # _C_GL.GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING : 1,
    _C_GL.GL_TEXTURE_COORD_ARRAY_SIZE : 1,
    _C_GL.GL_TEXTURE_COORD_ARRAY_STRIDE : 1,
    _C_GL.GL_TEXTURE_COORD_ARRAY_TYPE : 1,
    # _C_GL.GL_TEXTURE_CUBE_MAP : 1,
    _C_GL.GL_TEXTURE_GEN_Q : 1,
    _C_GL.GL_TEXTURE_GEN_R : 1,
    _C_GL.GL_TEXTURE_GEN_S : 1,
    _C_GL.GL_TEXTURE_GEN_T : 1,
    _C_GL.GL_TEXTURE_MATRIX : 16,
    _C_GL.GL_TEXTURE_STACK_DEPTH : 1,
    # _C_GL.GL_TIMESTAMP : 1,
    # _C_GL.GL_TRANSFORM_FEEDBACK_BUFFER_BINDING : 1,       # glGetIntegeri_v
    # _C_GL.GL_TRANSFORM_FEEDBACK_BUFFER_SIZE : 1,          # glGetIntegeri_v
    # _C_GL.GL_TRANSFORM_FEEDBACK_BUFFER_START : 1,         # glGetIntegeri_v
    # _C_GL.GL_TRANSPOSE_COLOR_MATRIX : 16,
    # _C_GL.GL_TRANSPOSE_MODELVIEW_MATRIX : 16,
    # _C_GL.GL_TRANSPOSE_PROJECTION_MATRIX : 16,
    # _C_GL.GL_TRANSPOSE_TEXTURE_MATRIX : 16,
    # _C_GL.GL_UNIFORM_BUFFER_BINDING : 1,                  # glGetIntegeri_v
    # _C_GL.GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT : 1,
    # _C_GL.GL_UNIFORM_BUFFER_SIZE : 1,                     # glGetIntegeri_v
    # _C_GL.GL_UNIFORM_BUFFER_START : 1,                    # glGetIntegeri_v
    _C_GL.GL_UNPACK_ALIGNMENT : 1,
    # _C_GL.GL_UNPACK_IMAGE_HEIGHT : 1,
    _C_GL.GL_UNPACK_LSB_FIRST : 1,
    _C_GL.GL_UNPACK_ROW_LENGTH : 1,
    # _C_GL.GL_UNPACK_SKIP_IMAGES : 1,
    _C_GL.GL_UNPACK_SKIP_PIXELS : 1,
    _C_GL.GL_UNPACK_SKIP_ROWS : 1,
    _C_GL.GL_UNPACK_SWAP_BYTES : 1,
    _C_GL.GL_VERTEX_ARRAY : 1,
    # _C_GL.GL_VERTEX_ARRAY_BINDING : 1,
    # _C_GL.GL_VERTEX_ARRAY_BUFFER_BINDING : 1,
    _C_GL.GL_VERTEX_ARRAY_SIZE : 1,
    _C_GL.GL_VERTEX_ARRAY_STRIDE : 1,
    _C_GL.GL_VERTEX_ARRAY_TYPE : 1,
    # _C_GL.GL_VERTEX_BINDING_BUFFER : 1,
    # _C_GL.GL_VERTEX_BINDING_DIVISOR : 1,
    # _C_GL.GL_VERTEX_BINDING_OFFSET : 1,
    # _C_GL.GL_VERTEX_BINDING_STRIDE : 1,
    # _C_GL.GL_VERTEX_PROGRAM_POINT_SIZE : 1,
    # _C_GL.GL_VERTEX_PROGRAM_TWO_SIDE : 1,
    _C_GL.GL_VIEWPORT : 4,                                # glGetIntegeri_v
    # _C_GL.GL_VIEWPORT_BOUNDS_RANGE : 2,
    # _C_GL.GL_VIEWPORT_INDEX_PROVOKING_VERTEX : 1,
    # _C_GL.GL_VIEWPORT_SUBPIXEL_BITS : 1,
    _C_GL.GL_ZOOM_X : 1,
    _C_GL.GL_ZOOM_Y : 1,
}

_read_pixels_format_count = {
    # Note: Commented items are from OpenGL above version 1.1.

    _C_GL.GL_COLOR_INDEX          : 1,
    _C_GL.GL_STENCIL_INDEX        : 1,
    _C_GL.GL_DEPTH_COMPONENT      : 1,
    _C_GL.GL_RGB                  : 3,
    # _C_GL.GL_BGR                  : 3,
    _C_GL.GL_RGBA                 : 4,
    # _C_GL.GL_BGRA                 : 4,
    _C_GL.GL_RED                  : 1,
    _C_GL.GL_GREEN                : 1,
    _C_GL.GL_BLUE                 : 1,
    _C_GL.GL_ALPHA                : 1,
    _C_GL.GL_LUMINANCE            : 1,
    _C_GL.GL_LUMINANCE_ALPHA      : 1,
}

_read_pixels_type_size = {
    # Note: Commented items are from OpenGL above version 1.1.

    _C_GL.GL_UNSIGNED_BYTE                : 1,
    _C_GL.GL_BYTE                         : 1,
    _C_GL.GL_BITMAP                       : 1 / 8,
    _C_GL.GL_UNSIGNED_SHORT               : 2,
    _C_GL.GL_SHORT                        : 2,
    _C_GL.GL_UNSIGNED_INT                 : 4,
    _C_GL.GL_INT                          : 4,
    _C_GL.GL_FLOAT                        : 4,
    # _C_GL.GL_UNSIGNED_BYTE_3_3_2          : 1,
    # _C_GL.GL_UNSIGNED_BYTE_2_3_3_REV      : 1,
    # _C_GL.GL_UNSIGNED_SHORT_5_6_5         : 2,
    # _C_GL.GL_UNSIGNED_SHORT_5_6_5_REV     : 2,
    # _C_GL.GL_UNSIGNED_SHORT_4_4_4_4       : 2,
    # _C_GL.GL_UNSIGNED_SHORT_4_4_4_4_REV   : 2,    
    # _C_GL.GL_UNSIGNED_SHORT_5_5_5_1       : 2,
    # _C_GL.GL_UNSIGNED_SHORT_1_5_5_5_REV   : 2,    
    # _C_GL.GL_UNSIGNED_INT_8_8_8_8         : 4,
    # _C_GL.GL_UNSIGNED_INT_8_8_8_8_REV     : 4,
    # _C_GL.GL_UNSIGNED_INT_10_10_10_2      : 4,
    # _C_GL.GL_UNSIGNED_INT_2_10_10_10_REV  : 4,    
}

_gl_error_code_to_str = {
    # Note: Commented items are from OpenGL above version 1.1.

    _C_GL.GL_NO_ERROR                       : "GL_NO_ERROR",
    _C_GL.GL_INVALID_ENUM                   : "GL_INVALID_ENUM",
    _C_GL.GL_INVALID_VALUE                  : "GL_INVALID_VALUE",
    _C_GL.GL_INVALID_OPERATION              : "GL_INVALID_OPERATION",
    # _C_GL.GL_INVALID_FRAMEBUFFER_OPERATION  : "GL_INVALID_FRAMEBUFFER_OPERATION",
    _C_GL.GL_OUT_OF_MEMORY                  : "GL_OUT_OF_MEMORY",
    _C_GL.GL_STACK_UNDERFLOW                : "GL_STACK_UNDERFLOW",
    _C_GL.GL_STACK_OVERFLOW                 : "GL_STACK_OVERFLOW",
    # _C_GL.GL_TABLE_TOO_LARGE                : "GL_TABLE_TOO_LARGE",
}