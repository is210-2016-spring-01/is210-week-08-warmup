#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""BloodPressure"""


BloodPress = raw_input("What is your blood pressure?")
BloodPress = int(BloodPress)

if BloodPress <= 89:
    BP_STATUS = 'Low'

elif BloodPress >= 90 and BP <= 119:
    BP_STATUS = 'Ideal'

elif BloodPress >= 120 and BP <= 139:
    BP_STATUS = 'Warning'

elif BloodPress >= 140 and BP <= 159:
    BP_STATUS = 'High'

else:
    BP_STATUS = 'Emergency'

OUTPUT = 'Your status is currently: {}'.format(BP_STATUS)
print OUTPUT
