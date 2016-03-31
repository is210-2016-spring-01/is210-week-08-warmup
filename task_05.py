#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A blood pressure status test."""

BLOODPRESSURE = int(raw_input('What is your blood pressure? '))
BP_STATUS = ''
BP_TEST_RESULT = 'Your status is currently: {0}!'

if BLOODPRESSURE <= 89:
    BP_STATUS = 'Low'
elif BLOODPRESSURE >= 90 and BLOODPRESSURE <= 119:
    BP_STATUS = 'Ideal'
elif BLOODPRESSURE >= 120 and BLOODPRESSURE <= 139:
    BP_STATUS = 'Warning'
elif BLOODPRESSURE >= 140 and BLOODPRESSURE <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

print BP_TEST_RESULT.format(BP_STATUS)
