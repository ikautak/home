#!/usr/bin/env python

import sys

if __name__ == '__main__':
    for l in iter(sys.stdin.readline, ''):
        print('%d' % int(l.rstrip(), 16))

