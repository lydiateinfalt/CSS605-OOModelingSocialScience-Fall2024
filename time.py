# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:13:48 2024

@author: petit
CSS 605: Week 4
"""

class time:
    """ Represents time of day attributes: day, hour, minute, second
    """
    def __init__(self, day, hour, minute, second):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __str__(self):
        return f"({self.day}: {self.hour}: {self.minute}: {self.second})"
    
    def add_time ( t1, t2):
        sum = time()
        sum.day = t1.day + t2.day
        sum.hour = t1.hour + t2.hour
        sum.minute = t1.minute + t2.minute
        sum.second = t1.second + t2.second
        return sum

               
    def increment( time, seconds ):
        time.second += seconds 
        if time.second >= 60:
            time.second -= 60
            time.minute +=1
        if time.minute >=60:
            time.minute -= 60
            time.hour +=1
        if time.hour >= 24:
            time.hour -= 24
            time.day +=1
        return time
            
         