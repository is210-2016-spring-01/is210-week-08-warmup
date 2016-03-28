#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A single if statement."""

MYINPUT = raw_input('Tell me a story! ')
MAX_LENGTH = 80
LONGSTR = 'short'

# You code goes here

INPUT_STR_LEN = len(MYINPUT)

LONGSTR = 'long' if INPUT_STR_LEN > MAX_LENGTH else 'short'

OUTPUT = 'That certainly was a {0} story!'.format(LONGSTR)
print OUTPUT
