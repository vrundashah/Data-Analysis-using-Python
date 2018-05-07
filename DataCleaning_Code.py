# -*- coding: utf-8 -*-
"""
Created on Sun May 06 18:22:48 2018

@author: Vrunda B Shah
"""

rem_missing1 = rem_missing['Inspection Type']
# Dropping of columns
rem_missing = rem_missing.drop(['DBA Name', 'AKA Name', 'Inspection Date', 'Month', 'Date'], axis = 1)

print (rem_missing.head())
rem_missing.to_csv('file_clean.csv', index = False)

np.savetxt('a.txt', rem_missing1, fmt='%5s', delimiter = ',', newline = '\n')

fhand = open('b.txt')
count = 0
d = dict()
for line in fhand:
	line = line.rstrip()  # strip off additional line space
	line1 = line.split(",")
	for temp in line1:
		print (temp)
		if temp not in d:
			d[temp] = 1
		else:
			d[temp] = d[temp] + 1
print(d)
	
lst = list(d.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, d[key]) 

import pandas as pd

dict1 = d
df = pd.DataFrame(data=dict1, index=[0])

df = (df.T)
print (df)
df.to_csv('dict1.csv')
