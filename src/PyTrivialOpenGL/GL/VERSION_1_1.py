import ctypes as _ctypes

from .._C_GL.VERSION_1_1.Constants import *
from .._C_GL import VERSION_1_1 as _C_GL_1_1

### Command Execution ###

#GLenum glGetError(void);

def glGetError():
    """
    Returns (int).
    """
    return int(_C_GL_1_1.glGetError())

### Vertex Specification ###

# Begin and End

def glBegin(mode):
    """
    mode : int
    """
    _C_GL_1_1.glBegin(int(mode))

def glEnd():
    _C_GL_1_1.glEnd()

# Polygon Edges

#void glEdgeFlag(GLboolean flag);
#void glEdgeFlagv(const GLboolean *flag);

# Vertex Specification

#void glVertex2d(GLdouble x,GLdouble y);
#void glVertex2dv(const GLdouble *v);

def glVertex2f(x, y):
    """
    x : float
    y : float
    """
    _C_GL_1_1.glVertex2f(float(x), float(y))

#void glVertex2f(GLfloat x,GLfloat y);

#void glVertex2fv(const GLfloat *v);
#void glVertex2i(GLint x,GLint y);
#void glVertex2iv(const GLint *v);
#void glVertex2s(GLshort x,GLshort y);
#void glVertex2sv(const GLshort *v);
#void glVertex3d(GLdouble x,GLdouble y,GLdouble z);
#void glVertex3dv(const GLdouble *v);
#void glVertex3f(GLfloat x,GLfloat y,GLfloat z);
#void glVertex3fv(const GLfloat *v);
#void glVertex3i(GLint x,GLint y,GLint z);
#void glVertex3iv(const GLint *v);
#void glVertex3s(GLshort x,GLshort y,GLshort z);
#void glVertex3sv(const GLshort *v);
#void glVertex4d(GLdouble x,GLdouble y,GLdouble z,GLdouble w);
#void glVertex4dv(const GLdouble *v);
#void glVertex4f(GLfloat x,GLfloat y,GLfloat z,GLfloat w);
#void glVertex4fv(const GLfloat *v);
#void glVertex4i(GLint x,GLint y,GLint z,GLint w);
#void glVertex4iv(const GLint *v);
#void glVertex4s(GLshort x,GLshort y,GLshort z,GLshort w);
#void glVertex4sv(const GLshort *v);

#void glTexCoord1d(GLdouble s);
#void glTexCoord1dv(const GLdouble *v);
#void glTexCoord1f(GLfloat s);
#void glTexCoord1fv(const GLfloat *v);
#void glTexCoord1i(GLint s);
#void glTexCoord1iv(const GLint *v);
#void glTexCoord1s(GLshort s);
#void glTexCoord1sv(const GLshort *v);
#void glTexCoord2d(GLdouble s,GLdouble t);
#void glTexCoord2dv(const GLdouble *v);
#void glTexCoord2f(GLfloat s,GLfloat t);
#void glTexCoord2fv(const GLfloat *v);
#void glTexCoord2i(GLint s,GLint t);
#void glTexCoord2iv(const GLint *v);
#void glTexCoord2s(GLshort s,GLshort t);
#void glTexCoord2sv(const GLshort *v);
#void glTexCoord3d(GLdouble s,GLdouble t,GLdouble r);
#void glTexCoord3dv(const GLdouble *v);
#void glTexCoord3f(GLfloat s,GLfloat t,GLfloat r);
#void glTexCoord3fv(const GLfloat *v);
#void glTexCoord3i(GLint s,GLint t,GLint r);
#void glTexCoord3iv(const GLint *v);
#void glTexCoord3s(GLshort s,GLshort t,GLshort r);
#void glTexCoord3sv(const GLshort *v);
#void glTexCoord4d(GLdouble s,GLdouble t,GLdouble r,GLdouble q);
#void glTexCoord4dv(const GLdouble *v);
#void glTexCoord4f(GLfloat s,GLfloat t,GLfloat r,GLfloat q);
#void glTexCoord4fv(const GLfloat *v);
#void glTexCoord4i(GLint s,GLint t,GLint r,GLint q);
#void glTexCoord4iv(const GLint *v);
#void glTexCoord4s(GLshort s,GLshort t,GLshort r,GLshort q);
#void glTexCoord4sv(const GLshort *v);

#void glNormal3b (GLbyte nx,GLbyte ny,GLbyte nz);
#void glNormal3bv(const GLbyte *v);
#void glNormal3d(GLdouble nx,GLdouble ny,GLdouble nz);
#void glNormal3dv(const GLdouble *v);
#void glNormal3f(GLfloat nx,GLfloat ny,GLfloat nz);
#void glNormal3fv(const GLfloat *v);
#void glNormal3i(GLint nx,GLint ny,GLint nz);
#void glNormal3iv(const GLint *v);
#void glNormal3s(GLshort nx,GLshort ny,GLshort nz);
#void glNormal3sv(const GLshort *v);

#void glColor3b(GLbyte red,GLbyte green,GLbyte blue);
#void glColor3bv(const GLbyte *v);
#void glColor3d(GLdouble red,GLdouble green,GLdouble blue);
#void glColor3dv(const GLdouble *v);

#void glColor3f(GLfloat red,GLfloat green,GLfloat blue);

def glColor3f(red, green, blue):
    """
    red     : float
    green   : float
    blue    : float
    """
    _C_GL_1_1.glColor3f(float(red), float(green), float(blue))


#void glColor3fv(const GLfloat *v);
#void glColor3i(GLint red,GLint green,GLint blue);
#void glColor3iv(const GLint *v);
#void glColor3s(GLshort red,GLshort green,GLshort blue);
#void glColor3sv(const GLshort *v);
#void glColor3ub(GLubyte red,GLubyte green,GLubyte blue);
#void glColor3ubv(const GLubyte *v);
#void glColor3ui(GLuint red,GLuint green,GLuint blue);
#void glColor3uiv(const GLuint *v);
#void glColor3us(GLushort red,GLushort green,GLushort blue);
#void glColor3usv(const GLushort *v);
#void glColor4b(GLbyte red,GLbyte green,GLbyte blue,GLbyte alpha);
#void glColor4bv(const GLbyte *v);
#void glColor4d(GLdouble red,GLdouble green,GLdouble blue,GLdouble alpha);
#void glColor4dv(const GLdouble *v);
#void glColor4f(GLfloat red,GLfloat green,GLfloat blue,GLfloat alpha);
#void glColor4fv(const GLfloat *v);
#void glColor4i(GLint red,GLint green,GLint blue,GLint alpha);
#void glColor4iv(const GLint *v);
#void glColor4s(GLshort red,GLshort green,GLshort blue,GLshort alpha);
#void glColor4sv(const GLshort *v);
#void glColor4ub(GLubyte red,GLubyte green,GLubyte blue,GLubyte alpha);
#void glColor4ubv(const GLubyte *v);
#void glColor4ui(GLuint red,GLuint green,GLuint blue,GLuint alpha);
#void glColor4uiv(const GLuint *v);
#void glColor4us(GLushort red,GLushort green,GLushort blue,GLushort alpha);
#void glColor4usv(const GLushort *v);

#void glIndexd(GLdouble c);
#void glIndexdv(const GLdouble *c);
#void glIndexf(GLfloat c);
#void glIndexfv(const GLfloat *c);
#void glIndexi(GLint c);
#void glIndexiv(const GLint *c);
#void glIndexs(GLshort c);
#void glIndexsv(const GLshort *c);
#void glIndexub(GLubyte c);
#void glIndexubv(const GLubyte *c);

### Vertex Arrays ###

#void glVertexPointer(GLint size,GLenum type,GLsizei stride,const GLvoid *pointer);
#void glNormalPointer(GLenum type,GLsizei stride,const GLvoid *pointer);
#void glColorPointer(GLint size,GLenum type,GLsizei stride,const GLvoid *pointer);
#void glIndexPointer(GLenum type,GLsizei stride,const GLvoid *pointer);
#void glEdgeFlagPointer(GLsizei stride,const GLvoid *pointer);
#void glTexCoordPointer(GLint size,GLenum type,GLsizei stride,const GLvoid *pointer);
#void glEnableClientState(GLenum array);
#void glDisableClientState(GLenum array);
#void glArrayElement(GLint i);

# Drawing Commands
#void glDrawArrays(GLenum mode,GLint first,GLsizei count);
#void glDrawElements(GLenum mode,GLsizei count,GLenum type,const GLvoid *indices);
#void glInterleavedArrays(GLenum format,GLsizei stride,const GLvoid *pointer);

### Rectangles, Matrices, Texture Coordinates ###

# Rectangles

#void glRectd(GLdouble x1,GLdouble y1,GLdouble x2,GLdouble y2);
#void glRectdv(const GLdouble *v1,const GLdouble *v2);
#void glRectf(GLfloat x1,GLfloat y1,GLfloat x2,GLfloat y2);
#void glRectfv(const GLfloat *v1,const GLfloat *v2);
#void glRecti(GLint x1,GLint y1,GLint x2,GLint y2);
#void glRectiv(const GLint *v1,const GLint *v2);
#void glRects(GLshort x1,GLshort y1,GLshort x2,GLshort y2);
#void glRectsv(const GLshort *v1,const GLshort *v2);

# Matrices

def glMatrixMode(mode):
    """
    mode : int
    """
    _C_GL_1_1.glMatrixMode(int(mode))

#void glLoadMatrixd(const GLdouble *m);
#void glLoadMatrixf(const GLfloat *m);
#void glMultMatrixd(const GLdouble *m);
#void glMultMatrixf(const GLfloat *m);

def glLoadIdentity():
    _C_GL_1_1.glLoadIdentity()

#void glRotated(GLdouble angle,GLdouble x,GLdouble y,GLdouble z);

def glRotatef(angle, x, y, z):
    """
    angle   : float
    x       : float
    y       : float
    z       : float
    """
    _C_GL_1_1.glRotatef(float(angle), float(x), float(y), float(z))


#void glTranslated(GLdouble x,GLdouble y,GLdouble z);

def glTranslatef(x, y, z):
    """
    x       : float
    y       : float
    z       : float
    """
    _C_GL_1_1.glTranslatef(float(x), float(y), float(z))


#void glScaled(GLdouble x,GLdouble y,GLdouble z);

def glScalef(x, y, z):
    """
    x       : float
    y       : float
    z       : float
    """
    _C_GL_1_1.glScalef(float(x), float(y), float(z))

#void glFrustum(GLdouble left,GLdouble right,GLdouble bottom,GLdouble top,GLdouble zNear,GLdouble zFar);

def glOrtho(left, right, bottom, top, zNear, zFar):
    """
    left    : float
    right   : float
    bottom  : float
    top     : float
    zNear   : float
    zFar    : float
    """
    _C_GL_1_1.glOrtho(float(left), float(right), float(bottom), float(top), float(zNear), float(zFar))

def glPushMatrix():
    _C_GL_1_1.glPushMatrix()

def glPopMatrix():
    _C_GL_1_1.glPopMatrix()

# Generating Texture Coordinates

#void glTexGend(GLenum coord,GLenum pname,GLdouble param);
#void glTexGendv(GLenum coord,GLenum pname,const GLdouble *params);
#void glTexGenf(GLenum coord,GLenum pname,GLfloat param);
#void glTexGenfv(GLenum coord,GLenum pname,const GLfloat *params);
#void glTexGeni(GLenum coord,GLenum pname,GLint param);
#void glTexGeniv(GLenum coord,GLenum pname,const GLint *params);

### Viewport and Clipping ###

# Controlling the Viewport

#void glDepthRange (GLclampd zNear,GLclampd zFar);

def glViewport(x, y, width, height):
    """
    x       : int
    y       : int
    width   : int
    height  : int
    """
    _C_GL_1_1.glViewport(int(x), int(y), int(width), int(height))

# Clipping

#void glClipPlane(GLenum plane,const GLdouble *equation);
#void glGetClipPlane(GLenum plane,GLdouble *equation);

### Lighting and Color ###

# Lighting/ Lighting Parameter Specification

#void glMaterialf(GLenum face,GLenum pname,GLfloat param);
#void glMaterialfv(GLenum face,GLenum pname,const GLfloat *params);
#void glMateriali(GLenum face,GLenum pname,GLint param);
#void glMaterialiv(GLenum face,GLenum pname,const GLint *params);

#void glLightf(GLenum light,GLenum pname,GLfloat param);
#void glLightfv(GLenum light,GLenum pname,const GLfloat *params);
#void glLighti(GLenum light,GLenum pname,GLint param);
#void glLightiv(GLenum light,GLenum pname,const GLint *params);

#void glLightModelf(GLenum pname,GLfloat param);
#void glLightModelfv(GLenum pname,const GLfloat *params);
#void glLightModeli(GLenum pname,GLint param);
#void glLightModeliv(GLenum pname,const GLint *params);

# ColorMaterial 

#void glColorMaterial(GLenum face,GLenum mode);

# Flatshading

#void glShadeModel(GLenum mode);

# Queries

#void glGetLightfv(GLenum light,GLenum pname,GLfloat *params);
#void glGetLightiv(GLenum light,GLenum pname,GLint *params);
#void glGetMaterialfv(GLenum face,GLenum pname,GLfloat *params);
#void glGetMaterialiv(GLenum face,GLenum pname,GLint *params);

### Rendering Control and Queries ###

# Current Raster Position

#void glRasterPos2d(GLdouble x,GLdouble y);
#void glRasterPos2dv(const GLdouble *v);
#void glRasterPos2f(GLfloat x,GLfloat y);
#void glRasterPos2fv(const GLfloat *v);
#void glRasterPos2i(GLint x,GLint y);
#void glRasterPos2iv(const GLint *v);
#void glRasterPos2s(GLshort x,GLshort y);
#void glRasterPos2sv(const GLshort *v);
#void glRasterPos3d(GLdouble x,GLdouble y,GLdouble z);
#void glRasterPos3dv(const GLdouble *v);
#void glRasterPos3f(GLfloat x,GLfloat y,GLfloat z);
#void glRasterPos3fv(const GLfloat *v);
#void glRasterPos3i(GLint x,GLint y,GLint z);
#void glRasterPos3iv(const GLint *v);
#void glRasterPos3s(GLshort x,GLshort y,GLshort z);
#void glRasterPos3sv(const GLshort *v);
#void glRasterPos4d(GLdouble x,GLdouble y,GLdouble z,GLdouble w);
#void glRasterPos4dv(const GLdouble *v);
#void glRasterPos4f(GLfloat x,GLfloat y,GLfloat z,GLfloat w);
#void glRasterPos4fv(const GLfloat *v);
#void glRasterPos4i(GLint x,GLint y,GLint z,GLint w);
#void glRasterPos4iv(const GLint *v);
#void glRasterPos4s(GLshort x,GLshort y,GLshort z,GLshort w);
#void glRasterPos4sv(const GLshort *v);

### Rasterization ###

# Points

#void glPointSize(GLfloat size);

# Line Segments

#void glLineWidth(GLfloat width);

# Other Line Segments Features

#void glLineStipple(GLint factor,GLushort pattern);

# Stipple Query

#void glGetPolygonStipple(GLubyte *mask);

# Polygons

#void glFrontFace(GLenum mode);
#void glCullFace(GLenum mode);

# Stippling

#void glPolygonStipple(const GLubyte *mask);

# Polygon Rasterization & Depth Offset

#void glPolygonMode(GLenum face,GLenum mode);
#void glPolygonOffset(GLfloat factor,GLfloat units);

# Pixel Rectangles

#void glPixelStoref(GLenum pname,GLfloat param);
#void glPixelStorei(GLenum pname,GLint param);

# Pixel Transfer Modes

#void glPixelTransferf(GLenum pname,GLfloat param);
#void glPixelTransferi(GLenum pname,GLint param);

#void glPixelMapfv(GLenum map,GLsizei mapsize,const GLfloat *values);
#void glPixelMapuiv(GLenum map,GLsizei mapsize,const GLuint *values);
#void glPixelMapusv(GLenum map,GLsizei mapsize,const GLushort *values);

# Enumerated Queries

#void glGetPixelMapfv(GLenum map,GLfloat *values);
#void glGetPixelMapuiv(GLenum map,GLuint *values);
#void glGetPixelMapusv(GLenum map,GLushort *values);

# Rasterization of Pixel Rectangles

#void glDrawPixels(GLsizei width,GLsizei height,GLenum format,GLenum type,const GLvoid *pixels);
#void glPixelZoom(GLfloat xfactor,GLfloat yfactor);

# Bitmaps

#void glBitmap(GLsizei width,GLsizei height,GLfloat xorig,GLfloat yorig,GLfloat xmove,GLfloat ymove,const GLubyte *bitmap);

### Texturing ###

# Texture Image Specification

#void glTexImage1D(GLenum target,GLint level,GLint internalformat,GLsizei width,GLint border,GLenum format,GLenum type,const GLvoid *pixels);
#void glTexImage2D(GLenum target,GLint level,GLint internalformat,GLsizei width,GLsizei height,GLint border,GLenum format,GLenum type,const GLvoid *pixels);

# Alt. Texture Image Specification Commands 

#void glCopyTexImage1D(GLenum target,GLint level,GLenum internalFormat,GLint x,GLint y,GLsizei width,GLint border);
#void glCopyTexImage2D(GLenum target,GLint level,GLenum internalFormat,GLint x,GLint y,GLsizei width,GLsizei height,GLint border);
#void glTexSubImage1D(GLenum target,GLint level,GLint xoffset,GLsizei width,GLenum format,GLenum type,const GLvoid *pixels);
#void glTexSubImage2D(GLenum target,GLint level,GLint xoffset,GLint yoffset,GLsizei width,GLsizei height,GLenum format,GLenum type,const GLvoid *pixels);
#void glCopyTexSubImage1D(GLenum target,GLint level,GLint xoffset,GLint x,GLint y,GLsizei width);
#void glCopyTexSubImage2D(GLenum target,GLint level,GLint xoffset,GLint yoffset,GLint x,GLint y,GLsizei width,GLsizei height);

# Texture Parameters

#void glTexParameterf(GLenum target,GLenum pname,GLfloat param);
#void glTexParameterfv(GLenum target,GLenum pname,const GLfloat *params);
#void glTexParameteri(GLenum target,GLenum pname,GLint param);
#void glTexParameteriv(GLenum target,GLenum pname,const GLint *params);

# Texture Objects

#void glBindTexture(GLenum target,GLuint texture);
#void glDeleteTextures(GLsizei n,const GLuint *textures);
#void glGenTextures(GLsizei n,GLuint *textures);
#GLboolean glAreTexturesResident(GLsizei n,const GLuint *textures,GLboolean *residences);
#void glPrioritizeTextures(GLsizei n,const GLuint *textures,const GLclampf *priorities);

# Texture Environments & Texture Functions 

#void glTexEnvf(GLenum target,GLenum pname,GLfloat param);
#void glTexEnvfv(GLenum target,GLenum pname,const GLfloat *params);
#void glTexEnvi(GLenum target,GLenum pname,GLint param);
#void glTexEnviv(GLenum target,GLenum pname,const GLint *params);

# Enumerated Queries

#void glGetTexEnvfv(GLenum target,GLenum pname,GLfloat *params);
#void glGetTexEnviv(GLenum target,GLenum pname,GLint *params);
#void glGetTexGendv(GLenum coord,GLenum pname,GLdouble *params);
#void glGetTexGenfv(GLenum coord,GLenum pname,GLfloat *params);
#void glGetTexGeniv(GLenum coord,GLenum pname,GLint *params);

#void glGetTexParameterfv(GLenum target,GLenum pname,GLfloat *params);
#void glGetTexParameteriv(GLenum target,GLenum pname,GLint *params);
#void glGetTexLevelParameterfv(GLenum target,GLint level,GLenum pname,GLfloat *params);
#void glGetTexLevelParameteriv(GLenum target,GLint level,GLenum pname,GLint *params);

# Texture Queries

#void glGetTexImage(GLenum target,GLint level,GLenum format,GLenum type,GLvoid *pixels);
#GLboolean glIsTexture(GLuint texture);

### Color Sum, Fog, and Hints  ###

# Fog

#void glFogf(GLenum pname,GLfloat param);
#void glFogfv(GLenum pname,const GLfloat *params);
#void glFogi(GLenum pname,GLint param);
#void glFogiv(GLenum pname,const GLint *params);

# Hints

#void glHint(GLenum target,GLenum mode);

### Drawing, Reading, and Copying Pixels ###

# Reading Pixels

#void glReadPixels(GLint x,GLint y,GLsizei width,GLsizei height,GLenum format,GLenum type,GLvoid *pixels);
#void glReadBuffer(GLenum mode);

# Copying Pixels

#void glCopyPixels(GLint x,GLint y,GLsizei width,GLsizei height,GLenum type);

### Per-Fragment Operations ###

# Scissor Test

#void glScissor(GLint x,GLint y,GLsizei width,GLsizei height);

# Alpha Test

#void glAlphaFunc(GLenum func,GLclampf ref);

# Stencil Test

#void glStencilFunc(GLenum func,GLint ref,GLuint mask);
#void glStencilOp(GLenum fail,GLenum zfail,GLenum zpass);

# Depth Buffer Test

#void glDepthFunc(GLenum func);

# Blending

#void glBlendFunc(GLenum sfactor,GLenum dfactor);

# Logical Operation 

#void glLogicOp(GLenum opcode);

### Whole Framebuffer Operations ###

# Selecting a Buffer for Writing

#void glDrawBuffer(GLenum mode);

# Fine Control of Buffer Updates

#void glIndexMask(GLuint mask);
#void glColorMask(GLboolean red,GLboolean green,GLboolean blue,GLboolean alpha);
#void glDepthMask(GLboolean flag);
#void glStencilMask(GLuint mask);

# Clearing the Buffers

def glClear(mask):
    """
    mask : int
    """
    _C_GL_1_1.glClear(int(mask))

def glClearColor(red, green, blue, alpha):
    """
    red     : float
    green   : float
    blue    : float
    alpha   : float
    """
    _C_GL_1_1.glClearColor(float(red), float(green), float(blue), float(alpha))

#void glClearIndex(GLfloat c);
#void glClearDepth(GLclampd depth);
#void glClearStencil(GLint s);
#void glClearAccum(GLfloat red,GLfloat green,GLfloat blue,GLfloat alpha);

# Accumulation Buffer

#void glAccum(GLenum op,GLfloat value);

### Special Functions ###

# Evaluators

#void glMap1d(GLenum target,GLdouble u1,GLdouble u2,GLint stride,GLint order,const GLdouble *points);
#void glMap1f(GLenum target,GLfloat u1,GLfloat u2,GLint stride,GLint order,const GLfloat *points);
#void glMap2d(GLenum target,GLdouble u1,GLdouble u2,GLint ustride,GLint uorder,GLdouble v1,GLdouble v2,GLint vstride,GLint vorder,const GLdouble *points);
#void glMap2f(GLenum target,GLfloat u1,GLfloat u2,GLint ustride,GLint uorder,GLfloat v1,GLfloat v2,GLint vstride,GLint vorder,const GLfloat *points);

#void glEvalCoord1d(GLdouble u);
#void glEvalCoord1dv(const GLdouble *u);
#void glEvalCoord1f(GLfloat u);
#void glEvalCoord1fv(const GLfloat *u);
#void glEvalCoord2d(GLdouble u,GLdouble v);
#void glEvalCoord2dv(const GLdouble *u);
#void glEvalCoord2f(GLfloat u,GLfloat v);
#void glEvalCoord2fv(const GLfloat *u);

#void glMapGrid1d(GLint un,GLdouble u1,GLdouble u2);
#void glMapGrid1f(GLint un,GLfloat u1,GLfloat u2);
#void glMapGrid2d(GLint un,GLdouble u1,GLdouble u2,GLint vn,GLdouble v1,GLdouble v2);
#void glMapGrid2f(GLint un,GLfloat u1,GLfloat u2,GLint vn,GLfloat v1,GLfloat v2);

#void glEvalMesh1(GLenum mode,GLint i1,GLint i2);
#void glEvalMesh2(GLenum mode,GLint i1,GLint i2,GLint j1,GLint j2);

#void glEvalPoint1(GLint i);
#void glEvalPoint2(GLint i,GLint j);

# Enumerated Query

#void glGetMapdv(GLenum target,GLenum query,GLdouble *v);
#void glGetMapfv(GLenum target,GLenum query,GLfloat *v);
#void glGetMapiv(GLenum target,GLenum query,GLint *v);

# Selection

#void glInitNames(void);
#void glPopName(void);
#void glPushName(GLuint name);
#void glLoadName(GLuint name);
#GLint glRenderMode(GLenum mode);
#void glSelectBuffer(GLsizei size,GLuint *buffer);

# Feedback

#void glFeedbackBuffer(GLsizei size,GLenum type,GLfloat *buffer);
#void glPassThrough(GLfloat token);

# Display Lists

#void glNewList(GLuint list,GLenum mode);
#void glEndList(void);
#void glCallList(GLuint list);
#void glCallLists(GLsizei n,GLenum type,const GLvoid *lists);
#void glListBase(GLuint base);
#GLuint glGenLists(GLsizei range);
#GLboolean glIsList(GLuint list);
#void glDeleteLists(GLuint list,GLsizei range);

### Synchronization ###

# Flush and Finish 

def glFlush():
    _C_GL_1_1.glFlush()

#void glFinish(void);

### State and State Requests ###

#void glDisable(GLenum cap);
#void glEnable(GLenum cap);

# Simple Queries

#void glGetBooleanv(GLenum pname,GLboolean *params);

def glGetIntegerv(pname, n):
    """
    pname   : int
    n       : int
        Number of integers to get.
    Returns (List[int]).
    """
    params = (_C_GL_1_1.GLint * n)()
    _C_GL_1_1.glGetIntegerv(int(pname), _ctypes.byref(params))
    return [int(param) for param in params]


#void glGetFloatv(GLenum pname,GLfloat *params);
#void glGetDoublev(GLenum pname,GLdouble *params);
#GLboolean glIsEnabled(GLenum cap);

# Pointer and String Queries [

#void glGetPointerv(GLenum pname,GLvoid **params);

def glGetString(name):
    """
    name   : int
    Returns (str).
    """
    return _ctypes.cast(_C_GL_1_1.glGetString(int(name)), _ctypes.c_char_p).value.decode()

# Saving and Restoring State

def glPushAttrib(mask):
    """
    mask : int
    """
    _C_GL_1_1.glPushAttrib(int(mask))

def glPopAttrib():
    _C_GL_1_1.glPopAttrib()

#void glPushClientAttrib(GLbitfield mask);
#void glPopClientAttrib(void);
