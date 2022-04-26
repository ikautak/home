#!/bin/bash

filename=tmp$$

cat > $filename
if [ $# -eq 0 ]
then
  gnuplot -p <<EOF
set nokey
plot '$filename' with line
EOF
else
  gnuplot <<EOF
set nokey
set terminal png
set output '$1'
plot '$filename' with line
EOF
fi

rm $filename

