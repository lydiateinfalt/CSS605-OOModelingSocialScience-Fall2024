# -*- coding: utf-8 -*-
"""
L. Teinfalt
CSS 605 - Week 2
Fall 2024

"""
print("Fibonacci Sequence")
def fib(n):
    
    if (n == 1 or n == 2):
        return 1
    else:
        return (fib(n-1)+ fib(n-2))
    
for i in range(1,11):
    print ("i=", i, ",fib(i)=", fib(i))  

