'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_EXT_texture_storage'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_EXT_texture_storage',error_checker=_errors._error_checker)
GL_ALPHA16F_EXT=_C('GL_ALPHA16F_EXT',0x881C)
GL_ALPHA32F_EXT=_C('GL_ALPHA32F_EXT',0x8816)
GL_ALPHA8_EXT=_C('GL_ALPHA8_EXT',0x803C)
GL_BGRA8_EXT=_C('GL_BGRA8_EXT',0x93A1)
GL_LUMINANCE16F_EXT=_C('GL_LUMINANCE16F_EXT',0x881E)
GL_LUMINANCE32F_EXT=_C('GL_LUMINANCE32F_EXT',0x8818)
GL_LUMINANCE8_ALPHA8_EXT=_C('GL_LUMINANCE8_ALPHA8_EXT',0x8045)
GL_LUMINANCE8_EXT=_C('GL_LUMINANCE8_EXT',0x8040)
GL_LUMINANCE_ALPHA16F_EXT=_C('GL_LUMINANCE_ALPHA16F_EXT',0x881F)
GL_LUMINANCE_ALPHA32F_EXT=_C('GL_LUMINANCE_ALPHA32F_EXT',0x8819)
GL_R16F_EXT=_C('GL_R16F_EXT',0x822D)
GL_R32F_EXT=_C('GL_R32F_EXT',0x822E)
GL_R8_EXT=_C('GL_R8_EXT',0x8229)
GL_RG16F_EXT=_C('GL_RG16F_EXT',0x822F)
GL_RG32F_EXT=_C('GL_RG32F_EXT',0x8230)
GL_RG8_EXT=_C('GL_RG8_EXT',0x822B)
GL_RGB10_A2_EXT=_C('GL_RGB10_A2_EXT',0x8059)
GL_RGB10_EXT=_C('GL_RGB10_EXT',0x8052)
GL_RGB16F_EXT=_C('GL_RGB16F_EXT',0x881B)
GL_RGB32F_EXT=_C('GL_RGB32F_EXT',0x8815)
GL_RGBA16F_EXT=_C('GL_RGBA16F_EXT',0x881A)
GL_RGBA32F_EXT=_C('GL_RGBA32F_EXT',0x8814)
GL_TEXTURE_IMMUTABLE_FORMAT_EXT=_C('GL_TEXTURE_IMMUTABLE_FORMAT_EXT',0x912F)
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei)
def glTexStorage1DEXT(target,levels,internalformat,width):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glTexStorage2DEXT(target,levels,internalformat,width,height):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei)
def glTexStorage3DEXT(target,levels,internalformat,width,height,depth):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei)
def glTextureStorage1DEXT(texture,target,levels,internalformat,width):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glTextureStorage2DEXT(texture,target,levels,internalformat,width,height):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei)
def glTextureStorage3DEXT(texture,target,levels,internalformat,width,height,depth):pass
