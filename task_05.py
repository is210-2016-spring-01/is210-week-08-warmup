#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Determing blood pressure status"""

BP_STATUS = raw_input('What is your blood pressure? ')
BP_STATUS = int(BP_STATUS)

if BP_STATUS <= 89:
    BP_STATUS = 'Low'
elif BP_STATUS > 89 and BP_STATUS <= 119:
    BP_STATUS = 'Ideal'
elif BP_STATUS > 119 and BP_STATUS <= 139:
    BP_STATUS = 'Warning'
elif BP_STATUS > 139 and BP_STATUS <= 159:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'
print 'Your status is currently: {}'.format(BP_STATUS)
