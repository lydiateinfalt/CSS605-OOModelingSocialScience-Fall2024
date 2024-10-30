# -*- coding: utf-8 -*-
"""
Population Dynamics.py

Model of logistic population growth

We contrast conventional "top-down" methods
with Object-Oriented methods in this lab

steve scott
22 Aug 2021
GMU CSS 605 / Econ 899

"""
import matplotlib.pyplot as plt

#
# now use an OO implementation
#
class Population():
    """ models a population using logistic growth """
    def __init__(self, x, r, K):
        self.x = x
        self.r = r
        self.K = K

    def __str__(self):
        msg = '%g, %g, %g'%(self.x, self.r, self.K)
        return msg

    def logistic(self):
        dx = (self.x * self.r) * (1.0 - (self.x / self.K))
        return dx

    def mkdata(self, timespan):
        val = []
        val.append(self.x)
        for i in timespan:
            x = val[i]
            dx = self.logistic()
            newval = x + dx
            if (i < max(timespan)):
                val.append(newval)
            self.x = newval
        return val

#
# create some Population objects and popsize histories
#
xvals = range(0, 20)
x0 = 90
K = 100

r = 0.54
p1 = Population( x0, r, K)
p1_hist = p1.mkdata( xvals )

r = 1.04
p2 = Population( x0, r, K)
p2_hist = p2.mkdata( xvals )

r = 1.54
p3 = Population( x0, r, K)
p3_hist = p3.mkdata( xvals )

r = 2.54
p4 = Population( x0, r, K)
p4_hist = p4.mkdata( xvals )

#
# plot results
#
plt.plot( xvals, p1_hist, 'r-', label = 'r=0.54' )
plt.plot( xvals, p2_hist, 'g-', label = 'r=1.04' )
plt.plot( xvals, p3_hist, 'b-', label = 'r=1.54' )
plt.plot( xvals, p4_hist, 'c-', label = 'r=2.54' )

plt.title('Population Growth')
plt.xlabel('time')
plt.ylabel('pop size')
plt.axis( xmin=0,
          xmax=1.50*max(xvals),
          ymin=0.75*x0,
          ymax=1.50*K)
plt.legend()
plt.grid()
plt.show()