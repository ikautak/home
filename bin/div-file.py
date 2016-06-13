#!/usr/bin/env python
""" ./div-file.py [file]
"""

import sys
import os.path


def bin_div(f, size=4*1024*1024):
    l = os.path.getsize(f)
    div_num = (l + size - 1) / size
    last = (size * div_num) - l

    b = open(f, 'rb')
    for i in range(div_num):
        read_size = last if i == div_num-1 else size
        data = b.read(read_size)
        out = open(f + '.frac' + str(i), 'wb')
        out.write(data)
        out.close()
    b.close()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        bin_div(sys.argv[1])

