#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 5 docstring."""

QUESTION = int(raw_input('What is your blood pressure? '))

if QUESTION <= 89:
    BP_STATUS = 'Low'
elif QUESTION <= 119:
    BP_STATUS = 'Ideal'
elif QUESTION <= 139:
    BP_STATUS = 'Warning'
elif QUESTION <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

OUTPUT = 'Your status is currently: {0}!'.format(BP_STATUS)
print OUTPUT
