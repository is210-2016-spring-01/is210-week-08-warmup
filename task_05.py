#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task 05: create a simple branching statement to check
systolic blood pressure in common language terms"""


BP_STATUS = int(raw_input("What is your blood pressure? "))

if BP_STATUS <= 89:
    BP_STATUS = "Low"
elif BP_STATUS >= 90 and BP_STATUS <= 119:
    BP_STATUS = "Ideal"
elif BP_STATUS >= 120 and BP_STATUS <= 139:
    BP_STATUS = "Warning"
elif BP_STATUS >= 140 and BP_STATUS <= 159:
    BP_STATUS = "High"
else:
    BP_STATUS = "Emergency"

print "Your status is currently: {}!".format(BP_STATUS)
