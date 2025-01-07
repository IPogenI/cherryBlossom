'''OpenGL extension OES.rgb8_rgba8

This module customises the behaviour of the 
OpenGL.raw.GLES2.OES.rgb8_rgba8 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension enables RGB8 and RGBA8 renderbuffer
	storage formats

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/rgb8_rgba8.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.OES.rgb8_rgba8 import *
from OpenGL.raw.GLES2.OES.rgb8_rgba8 import _EXTENSION_NAME

def glInitRgb8Rgba8OES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION