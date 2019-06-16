#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sqrt

data1=[49., 66, 24, 98, 37, 64, 98, 27, 56, 93, 68, 78, 22, 25, 11]

def mean(data):
    return sum(data)/len(data)

def median(data):
    sData = sorted(data)
    return sData[int(len(data) / 2)]

def mode(data):
    modeCount = 0
    modeValue = None
    for i in range(len(data)):
        currCount = data.count(data[i])
        if (currCount > modeCount):
            modeValue = data[i]
            modeCount = currCount
    
    return modeValue

def variance(data):
    meanVal = mean(data)
    
    # brackets transform the iterator into a list
    return mean([(x - meanVal)**2 for x in data])
    
def stddev(data):
    return sqrt(variance(data))
    
print(mean(data1))
print(median(data1))
print(mode(data1))
print(variance(data1))