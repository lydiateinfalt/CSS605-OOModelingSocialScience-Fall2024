# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:18:26 2024

@author: petit
CSS 605 Week 5 Microeconomics Lab
"""

import matplotlib.pyplot as plt

def gendata(n, slope, intercept):
# fit linear data
    data_set = [x*slope + intercept for x in range(n)]
    return data_set

def surplus(demand, supply):
    value = 0
    ptr = 0
    while (demand[ptr] >= supply[ptr]) and (ptr < len(demand)):
        diff = demand[ptr] - supply[ptr]
        value = value + diff
        ptr = ptr + 1
    return value

n = 50

#
# create supply curve
#
supply = gendata(n,10.0, 0.0)
supply.sort()

#
# create demand curve
#
demand = gendata(n, -10.0, 500.0)
demand.sort()
demand.reverse()

# make the x values
xvals = [x for x in range(n)]
# make a plot
plt.plot(xvals, supply, "r-", label="supply")
plt.plot(xvals, demand, "b-", label="demand")
plt.title('supply-demand model (supply slope =10.0)')
plt.xlabel('Q (quantity)')
plt.ylabel('P (price)')
plt.legend()
plt.ylim(0, 1000)
plt.grid()
plt.show()
# print results
market_surplus = surplus(demand, supply)
print('market surplus = %8.2f' % (market_surplus))