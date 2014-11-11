# -*- coding: utf-8 -*-

import sys

import gxf
import pygments

@gxf.register()
class Disassemble(gxf.DataCommand):
    '''
    Disassemble a specified section of memory.
    '''

    def setup(self, parser):
        parser.add_argument("what", type=gxf.LocationType())
        parser.add_argument("until", type=gxf.LocationType(), nargs='?')
        parser.add_argument("-v", "--verbose", action="store_true")

        parser.add_argument("-f", "--function", action="store_true")
        parser.add_argument("-c", "--count", type=int, default=10)
        parser.add_argument("-b", "--before", type=int, default=0)
        parser.add_argument("-r", "--real", action="store_true")
        parser.add_argument("-x", "--hexdump", action="store_true")

    def run(self, args):

        if args.function:
            disassembly = gxf.disassembly.disassemble(
                args.what, None, args.hexdump)
        elif args.until is not None:
            disassembly = gxf.disassembly.disassemble(
                args.what, args.until, args.hexdump)
        else:
            disassembly = gxf.disassembly.disassemble_lines(
                args.what, args.count + args.before, -args.before,
                hexdump=args.hexdump, ignfct=args.real)

        if args.verbose and disassembly.msg:
            print(disassembly.msg)
        elif not args.function:
            print("   ...")

        disassembly.output()

        if not args.function:
            print("   ...")
