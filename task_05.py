#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05 Module"""

BP_INPUT = int(raw_input('What is your blood pressure? '))
BP_STATUS = ''
BP_RESULT = 'Your blood pressure status is currently: {0}.'

if BP_INPUT <= 89:
    BP_STATUS = 'Low'
elif BP_INPUT >= 90 and BP_INPUT <= 119:
    BP_STATUS = 'Ideal'
elif BP_INPUT >= 120 and BP_INPUT <= 139:
    BP_STATUS = 'Warning'
elif BP_INPUT >= 140 and BP_INPUT <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

print BP_RESULT.format(BP_STATUS)
