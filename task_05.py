#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 5 file."""

BP = int(raw_input('What is your blood pressure? '))

if BP <= 89:
    BP_STATUS = 'Low'
elif BP >= 90 and BP <= 119:
    BP_STATUS = 'Ideal'
elif BP >= 120 and BP <= 139:
    BP_STATUS = 'Warning'
elif BP >= 140 and BP <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'EMERGENCY'

print 'Your status is currently: {0}'.format(BP_STATUS)
