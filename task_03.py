#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A complex testcase."""

EXPENSE = 14.23
LOOKS_NICE = True
MAX_EXPENSE = 12
GET_OUT_ALIVE = False

SACRIFICE = (True if LOOKS_NICE is True and EXPENSE <= MAX_EXPENSE else
             GET_OUT_ALIVE is False)
