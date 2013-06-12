#!/usr/bin/env python

import sys


def bin2txt(file_name):
    b = open(file_name, 'rb').read()
    for i, t in enumerate(map(ord, b)):
        if i % 16 == 0 and i != 0:
            print('')
        print('%02x' % t),
    print('')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        bin2txt(sys.argv[1])

