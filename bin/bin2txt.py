#!/usr/bin/env python

import sys
import binascii


def bin2txt(file_name):
    a = map(binascii.b2a_hex, open(file_name, 'rb').read())
    for i, t in enumerate(a):
        if i % 16 == 0 and i != 0:
            # line feed
            print('')
        print(t),
    print('')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        bin2txt(sys.argv[1])

