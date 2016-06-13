#!/usr/bin/env python
""" ./grayscale.py [image file]
"""

import sys
import Image

def grayscale(f):
    Image.open(f).convert('LA').save(f + '_grayscale.png')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        grayscale(sys.argv[1])

