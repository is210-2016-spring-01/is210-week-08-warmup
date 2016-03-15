#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Blood pressure interpreter."""

BPRESS = int(raw_input('What\'s your blood pressure? '))

if BPRESS < 90:
    BP_STATUS = 'Low'
elif BPRESS < 120:
    BP_STATUS = 'Ideal'
elif BPRESS < 140:
    BP_STATUS = 'Warning'
elif BPRESS < 160:
    BP_STATUS = 'High'
else:
    BP_STATUS = 'Emergency'

print 'Your status is currently: {0}!.'.format(BP_STATUS)
