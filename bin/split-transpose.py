#!/usr/bin/env python

import sys

def split_transpose(n):
    line = ''
    count = 0

    for l in iter(sys.stdin.readline, ''):
        line += l.rstrip() + '\t'
        count += 1

        if count == n:
            print(line)
            line = ''
            count = 0

    if count != 0:
        print(line)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        split_transpose(int(sys.argv[1]))

