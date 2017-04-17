#!/usr/bin/env python

import sys
import argparse


def split_transpose(split_lines, delimiter):
    d = []

    for l in iter(sys.stdin.readline, ''):
        d.append(l.rstrip())

        if len(d) == split_lines:
            print(delimiter.join(d))
            d = []

    if len(d) > 0:
        print(delimiter.join(d))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='split & transpose stdin')
    parser.add_argument('-l', '--lines', type=int, default=1, help='split lines')
    parser.add_argument('-d', '--delimiter', default='\t', help='delimiter char')
    args = parser.parse_args()

    if args.lines > 0:
        split_transpose(args.lines, args.delimiter)
