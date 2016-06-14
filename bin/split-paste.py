#!/usr/bin/env python

import sys

def split_paste(n):
    d = [[] for _ in range(n)]

    for i, l in enumerate(iter(sys.stdin.readline, '')):
        d[i % n].append(l.rstrip())

    for l in d:
        print('\t'.join(l))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        split_paste(int(sys.argv[1]))

