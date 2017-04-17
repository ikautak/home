#!/usr/bin/env python

import sys
import argparse


def split_paste(split_lines, delimiter):
    d = [[] for _ in range(split_lines)]

    for i, l in enumerate(iter(sys.stdin.readline, '')):
        d[i % split_lines].append(l.rstrip())

    for l in d:
        print(delimiter.join(l))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='split & paste stdin')
    parser.add_argument('-l', '--lines', type=int, default=1, help='split lines')
    parser.add_argument('-d', '--delimiter', default='\t', help='delimiter char')
    args = parser.parse_args()

    if args.lines > 0:
        split_paste(args.lines, args.delimiter)