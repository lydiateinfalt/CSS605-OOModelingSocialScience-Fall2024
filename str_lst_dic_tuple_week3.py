# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 12:28:39 2024

@author: L. Teinfalt
@course: CSS 605 Week 3 String, List, Dictionary
"""

def match(strand,seq):
    i=0
    while i < len(strand) - len(seq):
        tmp = strand[i:i+3]
        print(tmp)
        if tmp == seq:
            print('match found at', i)
        i=i+1
        
def palindrome(s):
    left = 0
    right = -1
    match = True
    while left < len(s):
        match = match and (s[left] == s[right])
        left = left + 1
        right = right -1
    return match

def histogram(s):
    d = dict()
    for ch in s:
        if ch not in d:
            d[ch] =1
        else:
            d[ch]+=1
    return d

def print_sorted_hist(h):
    for ch in sorted(h):
        print(ch,h[ch])


def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()
    
"""
•	Create an empty list
•	Use a loop to generate integers from 1 to 20, and append each such integer to the list
•	use the sum() method to compute the sum of this list.
•	print out the computed value.
"""

list=[]
counter = 0
for i in range(1,21):
    counter += 1
    print("Number", counter)
    list.append(counter)
print("Sum of numbers from list", sum(list))

"""
Express the following data consisting of keys and values
key	value
11	apple
33	banana
22	plum
46	pear
"""
fruit_dict = {11: 'apple', 33: 'banana', 22: 'plum', 46: 'pear'}

Months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
Days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mo_dy = zip(Months, Days)
month_list = []
print("Tuples: Months and their number of days")
for item in mo_dy:
    month_list.append(item)
    print(item)
print("List: Month List with their number of days", month_list)


import numpy as np
import matplotlib.pyplot as plt

#first method
random_x = np.random.random(size=100)
random_y = np.random.random(size=100)

#second  method
random_x=[]
random_y=[]
for i in range (1,101):
    random_x.append(np.random.random())
    random_y.append(np.random.random())
    
#sort values
random_x.sort()
random_y.sort()

#line chart
plt.plot(range(len(random_x)),random_x, '-b', label="X")
plt.plot(range(len(random_y)),random_y, '-r', label="Y")
plt.title("Numpy Random Generated Y vs X values")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

#Boxplots
random_a = np.random.random(size=20)
random_b = np.random.random(size=20)
random_c = np.random.random(size=20)
combined = [random_a, random_b, random_c]

#boxplot
plt.boxplot(combined, labels=['A', 'B', 'C'])
plt.title("Numpy Boxplots of Twenty Randomly Generated Values of A, B, C")
plt.ylabel("Random Values")
plt.xticks(rotation=90)
plt.show()

#Scatterplots
random_d = np.random.random(size=20)
random_e = []
for i in range (1,21):
    random_e.append(np.random.random())

#scatterplot
plt.scatter(random_d, random_e)
plt.title("Scatterplot of Twenty Randomly Generated Values of X,Y")
plt.ylabel("Random Y")
plt.xlabel("Random X")
plt.xticks(rotation=90)
plt.show()
