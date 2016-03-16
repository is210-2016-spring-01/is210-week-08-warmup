#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A  module to record patients' blood pressure"""

BLOOD_PRESSURE = int(raw_input('What is patient blood pressure?'))
BP_STATUS = ''
BLOOD_PRESSURE_RESULT = 'Your pressure is currently: {0}.'

if BLOOD_PRESSURE <= 89:
    BP_STATUS = 'Low'
elif BLOOD_PRESSURE >= 90 and BLOOD_PRESSURE <= 119:
    BP_STATUS = 'Ideal'
elif BLOOD_PRESSURE >= 120 and BLOOD_PRESSURE <= 139:
    BP_STATUS = 'Warning'
elif BLOOD_PRESSURE >= 140 and BLOOD_PRESSURE <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

print BLOOD_PRESSURE_RESULT.format(BP_STATUS)

