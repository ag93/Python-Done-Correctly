# -*- coding: utf-8 -*-
x = [1,2,3,4]
y = [7,8,3,2]
z = ['a','b','c','d']

for a,b,c in zip(x,y,z):
    print(a,b,c)
    
#Zip funtiion does not create a list but instead creates a zip object. To verify:
    
print(zip(x,y,z))

#Output: <zip object at 0x000001BDA0F31E08>

#To convert it into a list:
x = list(zip(x,y,z))
print(x)

#We can also use zip to create a dictionary
names = ['Jill','Jack','Jeb','Jessica']
grades = [99,56,24,87]

d = dict(zip(names,grades))
print(d)

