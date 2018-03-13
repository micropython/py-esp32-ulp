import sys

from .assemble import Assembler
from .link import make_binary


def src_to_binary(lines):
    assembler = Assembler()
    assembler.assemble(lines)
    assembler.dump()
    text, data, bss_len = assembler.fetch()
    return make_binary(text, data, bss_len)


def main(fn):
    with open(fn) as f:
        lines = f.readlines()

    binary = src_to_binary(lines)

    if fn.endswith('.s') or fn.endswith('.S'):
        fn = fn[:-2]
    with open(fn + '.ulp', 'wb') as f:
        f.write(binary)


main(sys.argv[1])

