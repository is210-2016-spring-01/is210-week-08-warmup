#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week-08 warmup tasks"""

import sys
try:
    x = int(raw_input("What is your blood pressure?"))
except ValueError:
    print "Invalid input"
    sys.exit(0)

if x > 0 and x <= 89:
    print "Your status is currently: Low!"
elif x >= 90 and x <= 119:
    print "Your status is currently: Ideal!"
elif x >= 120 and x <= 139:
    print "Your status is currently: Warning!"
elif x >= 140 and x <= 159:
    print "Your status is currently: High!"
else:
    print "Your status is currently: Emergency!"
