#!/usr/bin/env python
""" ./cat-file.py [file] [num]
concatenate files
"""

import sys


def bin_cat(f, num):
    out = open(f + '.out', 'wb')

    for i in range(num):
        frac = open(f + '.frac' + str(i), 'rb')
        out.write(frac.read())
        frac.close()
    out.close()


if __name__ == '__main__':
    if len(sys.argv) > 2:
        bin_cat(sys.argv[1], int(sys.argv[2]))

