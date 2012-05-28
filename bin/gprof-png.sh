#!/bin/sh

gprof $1 | python gprof2dot.py -n 0 -e 0 | dot -T png -o $1_result.png

