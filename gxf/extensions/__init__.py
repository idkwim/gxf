# -*- coding: utf-8 -*-

import gxf


@gxf.register(prefix=True)
class Gx(gxf.Command):
    '''
    This is the important gx main command, it does nothing.

    This is used as a prefix command for all the extensions
    included with the gfx framework.
    '''

    def run(self, args):
        pass

# Extensions loaded when import gx:

with gxf.register.prefix("gx"):
    import gxf.extensions.reload
    import gxf.extensions.meta
    import gxf.extensions.testi

    import gxf.extensions.telescope
    import gxf.extensions.addr
    import gxf.extensions.vmaps
    import gxf.extensions.disassemble
    import gxf.extensions.heading
    import gxf.extensions.pae
    import gxf.extensions.context
    import gxf.extensions.registers
