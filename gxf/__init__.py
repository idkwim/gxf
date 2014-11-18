# -*- coding: utf-8 -*-

__author__ = 'Wannes `wapiflapi` Rombouts'
__email__ = 'wapiflapi@yahoo.fr'
__version__ = '0.1.0'

try:
    import gdb
except ImportError:
    GDB = False
else:
    GDB = True

if GDB:
    from gxf.formatting import *
    from gxf.basics import *
    from gxf.commands import *
    from gxf.disassembly import *
    from gxf.errors import *
    from gxf.cpu import *
    from gxf.memory import *
