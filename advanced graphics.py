# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 12:40:33 2024

@author: petit
CSS 605 Week 5: Advanced graphics (Line charts, historgrams)
"""

import numpy as np
import matplotlib.pyplot as plt

""" Problem 1.1 """
xvals = [x for x in range(50)]

D1 = np.random.random(50) * 100
D2 = np.random.random(50) * 200
D3 = np.random.random(50) * 400

D1.sort()
D2.sort()
D3.sort()

plt.plot(xvals , D1, linestyle ='solid', color='red', label = "type a")
plt.plot(xvals , D2, linestyle ='dashed', color=(0.0, 0.0, 1.0), label = "type b")
plt.plot(xvals , D3, linestyle = 'dashdot', color='g', label = "type c")
plt.title("Experiment Results")
plt.xlabel("time")
plt.ylabel("observed effect")
plt.legend()
plt.show()

""" Problem 1.2 """
d1 = np.random.normal(loc=10, scale=1, size=100)
d2 = np.random.normal(loc=20, scale=3, size=100)

d1.sort()
d2.sort()

plt.subplot (1,2,1) # rows, cols, panel number
plt.hist(x=d1, bins=20, color='blue', alpha = 0.4, label='type a', edgecolor='black')
plt.title("type a")
plt.ylim(0,13)
plt.xlim(5,15)
plt.grid()

plt.subplot (1,2,2)
plt.hist(x=d2, bins=20, color='blue', alpha = 0.4, label='type b', edgecolor='black')
plt.title("type b")
plt.grid()
plt.ylim(0,13)
plt.xlim(5,30)
plt.show()