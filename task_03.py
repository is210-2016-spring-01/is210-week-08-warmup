#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A complex testcase."""

EXPENSE = 14.23
LOOKS_NICE = True
MAX_EXPENSE = 12
GET_OUT_ALIVE = False

if not (LOOKS_NICE and EXPENSE <= MAX_EXPENSE) or GET_OUT_ALIVE:
    SACRIFICE = True
else:
    SACRIFICE = False
