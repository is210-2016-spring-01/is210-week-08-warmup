#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A single if statement."""

MYINPUT = raw_input('Tell me a story! ')
MAX_LENGTH = 80
LONGSTR = 'short'

LENGTH = len(MYINPUT)

if LENGTH > MAX_LENGTH:
    LONGSTR = 'long'

OUTPUT = 'That certainly was a {0} story!'.format(LONGSTR)
print OUTPUT
