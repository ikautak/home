#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random


if __name__ == '__main__':
    theme = [
            r'あ',
            r'い',
            r'う',
            r'え',
            r'お',
    ]

    while True:
        random.shuffle(theme)
        random.seed()

        for i, x in enumerate(theme):
            print('{} {}'.format(i, x))

        time.sleep(0.1)

        # move cursor
        print('\u001B[{}F'.format(len(theme) + 1))

        # clear screen
        print('\u001B[0J', end='')



