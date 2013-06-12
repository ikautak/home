#!/usr/bin/env python

import sys
import struct


def txt2bin(file_name):
    d = [int(x, 16) for x in open(file_name, 'r').read().rstrip().split()]

    o = file(file_name + '.bin', 'wb')
    for c in d:
        o.write(struct.pack('B', c))
    o.close()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        map(txt2bin, sys.argv[1:])

