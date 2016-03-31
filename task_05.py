#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""blood pressure is scary."""

BP = raw_input('What is your blood pressure? ')
BP = int(BP)

if BP <= 89:
    BP_STATUS = 'Low'
elif 90 <= BP <= 119:
    BP_STATUS = 'Ideal'
elif 120 <= BP <= 139:
    BP_STATUS = 'Warning'
elif 140 <= BP <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

MYVAR = 'Your status is currently: {0}!'.format(BP_STATUS)
print MYVAR
