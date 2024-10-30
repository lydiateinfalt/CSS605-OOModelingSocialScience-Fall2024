# -*- coding: utf-8 -*-
"""
DOI_Model.py

models diffusion of innovation in a population
using "classical" differential equations

Created on Tue Nov  5 22:22:30 2019

@author: SLSCOTT
sscotta@gmu.edu
CSS 605 / Econ 895
Fall 2019
"""
import pandas as pd

"""
doi()

Given:
    potential : size of potential pop
    adopter: size of adopter pop
    disposer: size of disposer pop
    
    alpha : adoption rate
    beta: disposal rate

Returns:
   p_dot, a_dot, d_dot: values of the partial
       derivatives at the point x, y, z
"""
def doi(potential, adopter, disposer, beta=0.05, gamma=0.20):
    p_dot = -1.0 * beta * potential * adopter
    a_dot = (1.0 * beta * potential * adopter) + (-1.0 * gamma * adopter)
    d_dot = 1.0 * gamma * adopter
    return p_dot, a_dot, d_dot

# set up diff eq parameters
dt = 0.01
num_steps = 1000
beta = 0.01
gamma = 0.30

# set up lists to hold intermediate values
p_s = [0] * (num_steps + 1)
a_s = [0] * (num_steps + 1)
d_s = [0] * (num_steps + 1)

# Set initial values for bin sizes
p_s[0] = 99
a_s[0] = 1
d_s[0] = 0

# Step through "time", calculating the 
# partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps):
    p_dot, a_dot, d_dot = doi(p_s[i], a_s[i], d_s[i], beta, gamma)
    
    p_s[i + 1] = p_s[i] + (p_dot * dt)
    a_s[i + 1] = a_s[i] + (a_dot * dt)
    d_s[i + 1] = d_s[i] + (d_dot * dt)

'''
for i in range(num_steps):
    print('%g, %g, %g' % (p_s[i], a_s[i], d_s[i]))
'''

# create data frame, print results
df = pd.DataFrame({
        "potential" : p_s,
        "adapter" : a_s,
        "disposer" : d_s})
df.plot()
