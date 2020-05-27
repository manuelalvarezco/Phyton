#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 17:43:51 2020

@author: luismanuelalvarez
"""


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,15,100)
y = np.sin(x)

plt.plot(x,y)

plt.grid()

plt.xlabel("x")
plt.ylabel("f(x) = sin x")