# -*- coding: utf-8 -*-
"""
L. Teinfalt
CSS 605 - Week 2
Fall 2024
9/19/2024

Factorial
"""
print('Factorials: Recursive Method')
def factorial(n):
    
    if not isinstance(n,int):
        print("Factorial is valid for integers")
        return None
    elif n < 0:
        print('Factorials not defined for negatives')
        return None
    elif n == 0 | n== 1:
        return 1
    else:
        f = n*(factorial(n-1))
        return f

for i in range(1,11):
    print ("factorial of", i, "is", factorial(i))    

print("-----------------------------------")
print('Factorials: Non-Recursive Method')
def fact(n):
    if not isinstance(n,int):
        print("Factorial is valid for integers")
        return None
    elif n < 0:
        print('Factorials not defined for negatives')
        return None
    fact=1
    for k in range(2, n+1):
        fact = fact*k
    return fact

for j in range(1,11):
    print ("factorial of", j, "is", fact(j))    