#!/usr/bin/env python

import sys

if __name__ == '__main__':
    for l in iter(sys.stdin.readline, ''):
        print('0x%x' % int(l.rstrip(), 10))

