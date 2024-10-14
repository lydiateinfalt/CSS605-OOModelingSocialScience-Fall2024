# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:57:36 2024

@author: petit
CSS 605 Week 5: Pandas
"""

import pandas as pd
td = pd.read_csv("town_data.csv")
print(td.index)
print(td.values)
print(td.columns)


print(td.loc[td['Population2010']>5000])
print(td.nlargest(5,'MedianAge'))
print(td.nsmallest(5,'MedianHomePrice'))
print(td.sort_values('MedianHomePrice', ascending=False))
