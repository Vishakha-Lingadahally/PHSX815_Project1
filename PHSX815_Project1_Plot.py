#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 13:18:05 2021

@author: vishakha
"""
import matplotlib.pyplot as plt
import numpy as np

data=np.loadtxt(r'/home/vishakha/Documents/python/random_walk.csv', delimiter=',')
a=data[:,0]
b=data[:,1]
plt.plot(a,b)
plt.show()