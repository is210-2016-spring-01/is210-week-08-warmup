#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 8 warmup task 5 that prompts for blood presure and performs
   an analysis of the number."""

BP_LOOKUP = ((89, 'Low'), (119, 'Ideal'), (139, 'Warning'), (159, 'High'),
             (999, 'Emergency'))

MY_BP = int(raw_input('Please enter your blood presure: '))

for bp in BP_LOOKUP:

    if MY_BP <= bp[0]:
        BP_STATUS = bp[1]
        break

else:
    BP_STATUS = bp[1]

print 'Your status is currently: {0}'.format(BP_STATUS)
