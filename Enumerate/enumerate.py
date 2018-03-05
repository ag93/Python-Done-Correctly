# -*- coding: utf-8 -*-
"""
In an attempt to attach an index value, or some other unique value to list items, something like this comes to mind:
"""

temp = ['left','right','up','down']
for i in range(len(temp)):
    print(i, temp[i])

#Though this does the job, it is highly inefficient. Instead we can use this:
    
for i,j in enumerate(temp):
    print(i,j)
    
#The enumerate function returns a tuple containing the count, and then the actual value from the iterable. That iterable can be a dicttionary:
    
new_dict = dict(enumerate(temp))
print(new_dict)