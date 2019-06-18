#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def f(p0, p1, p2):
    return ((1-p1) * p0) / ((1-p1) * p0 + p2 * (1-p0)) 

print(f(0.1, 0.9, 0.8))