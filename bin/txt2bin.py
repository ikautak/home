#!/usr/bin/env python

import sys
import binascii


def txt2bin(file_name):
    d = map(binascii.a2b_hex, open(file_name, 'r').read().rstrip().split())

    o = open(file_name + '.bin', 'wb')
    o.write(''.join(d))
    o.close()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        map(txt2bin, sys.argv[1:])

