#!/bin/sh

# ./nkf-utf8.sh *.c
# ./nkf-utf8.sh *.h

for file in ${1:-*.*}
do
    if [ -e $file ]
    then
        nkf -w -Lu --overwrite $1
        echo $file
    fi
done

