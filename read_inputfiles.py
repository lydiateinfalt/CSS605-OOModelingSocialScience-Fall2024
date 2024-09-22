# -*- coding: utf-8 -*-
"""
L. Teinfalt
CSS 605 - Week 2
Fall 2024
#Reading and parsing input csv file

"""
import os


filepath = r'C:\Users\petit\.spyder-py3'
dir = r'CSS 605'
filename = r'airport.csv'

fullpath = os.path.join(filepath,dir,filename)
file = open(fullpath,'r')

#read files
headings = file.readline()
print('DEBUG: headings=%s'%(headings))
data = file.readlines()

maxflight=1
maxname = ''
for line in data:
    line = line.strip()
    #print('DEBUG: line=%s'%(line))
    
    #parsing fields from the line
    name, total = line.split(',')
    
    total=int(total)
    
    #print data
    print('Airport Name= %s, Total Flights=%d'%(name,total))
        
    if total > maxflight:
        maxflight= total
        maxname = name
    

print('------------------------------------------------')
print('In 2018, the airport with the highest number of flights is = %s with a total of flights= %d'%(maxname,maxflight))

    
    

 
