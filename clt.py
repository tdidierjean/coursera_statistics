#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:19:09 2019

@author: thomasdidierjean
"""
#Write a function flip that simulates flipping n fair coins. 
#It should return a list representing the result of each flip as a 1 or 0
#To generate randomness, you can use the function random.random() to get
#a number between 0 or 1. Checking if it's less than 0.5 can help your 
#transform it to be 0 or 1

import random
from math import sqrt
from matplotlib import pyplot


def mean(data):
    return float(sum(data))/len(data)

def variance(data):
    mu=mean(data)
    return sum([(x-mu)**2 for x in data])/len(data)

def stddev(data):
    return sqrt(variance(data))
    

def flip(N):
    return [random.random() > 0.5 for x in range(N)]

def sample(N):
    return [mean(flip(N)) for x in range(N)]

N=1000
outcomes=sample(N)
pyplot.hist(outcomes,nbins=30)


print (mean(f))
print (stddev(f))

