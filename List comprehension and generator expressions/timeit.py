# -*- coding: utf-8 -*-

import timeit

#print(timeit.timeit('1+3', number = 50000000))  #Just an example on how to use timeit


#For List Generator (Time = 0.03318725482074569)
print(timeit.timeit('''input_list = range(100)
def div_by_two(num):
    if (num/2).is_integer():
        return True
    else:
        return False

# generator:
xyz = (i for i in input_list if div_by_two(i))
''', number=50000))
    
    
#For List Comprehension (Time = 1.118188210717335) 
print(timeit.timeit('''input_list = range(100)
def div_by_two(num):
    if (num/2).is_integer():
        return True
    else:
        return False

# comprehension:
xyz = [i for i in input_list if div_by_two(i)]''', number=50000))
    
    
"""This proves that list comprehension takes more time as it has to write it in memory"""