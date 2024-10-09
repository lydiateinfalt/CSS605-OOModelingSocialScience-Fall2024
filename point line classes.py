# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:43:22 2024
CSS 605: Week 4

@author: petit
"""

class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return ('%d. %d' % (self.x, self.y))
    
class Line():
    def __init__(self, P1, P2):
        self.p1 = P1
        self.p2 = P2
    
    def __str__(self):
        return ('%s, %s' % (self.p1, self.p2))
    