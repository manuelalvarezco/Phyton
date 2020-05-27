#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 14:30:03 2020

@author: luismanuelalvarez
"""


def contains(sequence,item):
    for element in sequence:
        if item == element:
            return True
        
    return False

print(contains([100,200,300,400],200))
print(contains([100,200,300,400],300))
print(contains([100,200,300,400],350))
