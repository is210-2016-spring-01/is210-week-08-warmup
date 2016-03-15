#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Hyper tension?"""


BP = raw_input("What is your blood pressure?")
BP = int(BP)

if BP <= 89:
    BP_STATUS = 'Low'

elif BP >= 90 and BP <= 119:
    BP_STATUS = 'Ideal'

elif BP >= 120 and BP <= 139:
    BP_STATUS = 'Warning'

elif BP >= 140 and BP <= 159:
    BP_STATUS = 'High'

else:
    BP_STATUS = 'Emergency'

OUTPUT = 'Your status is currently: {}'.format(BP_STATUS)
print OUTPUT
