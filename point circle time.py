# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 18:44:06 2024

@author: petit
CSS 605 Week 4
"""

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"


class circle:
    def __init__(self, center: point, radius: float):
        self.center = center
        self.radius = radius
    
    def __str__(self):
        return f"Circle center at ({self.center.x}, {self.center.y}) with radius: {self.radius}"
    
    def area(self):
        return (3.14159*(self.radius**2))
    
    def perimeter(self):
        return (3.14159*2*self.radius)
        

print("Instantiate a point at (10,20) and print it")
p1 = point(10,20)
print(p1)   

print("Define a circle class with center defined using point class.")
print("Write code to instantiate a Circle object with a center at (10, 20) with radius of 15.")
c1 = circle(p1,15)
print(c1)
print("Area of circle",c1.area())
print("Perimeter of circle",c1.perimeter())
