# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 22:16:31 2021

@author: SLSCOTT
"""


import pandas as pd

def logistic(r, x, k):
    dx = r*x*(1.0 - (x/k))
    return (dx)

# set up 
num_steps = 250
r = 0.03
k = 100
x = 1
xpop = []

# move thru time
for t in range(num_steps):
    dx = logistic(r, x, k)
    x = x + dx
    print('t=%d, dx=%g, x=%g'%(t, dx, x))
    
    xpop.append(x)

df = pd.DataFrame({
        "pop" : xpop
        })
    
df.plot()