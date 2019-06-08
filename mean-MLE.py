#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def mean(oldmean,n,x):
    return oldmean + (x - oldmean) / (n + 1)    

def likelihood(dist,data):
    lh = 1
    for x in data:
        lh = lh * dist[x]
    return lh

print(likelihood({'A':0.2,'B':0.2,'C':0.2,'D':0.2,'E':0.2},'ABCEDDECAB'))