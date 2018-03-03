# -*- coding: utf-8 -*-

comprehension = [i for i in range(5000)] #Creates a list and stores it in memory

generator = (i for i in range(5000)) #Creates a list but  does not store in memory

#Generator Expression with a function
input_list = [5,6,2,1,6,7,10,12]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i)) #This is a generator expression
print(list(xyz))

xyz = [i for i in input_list if div_by_five(i)] #This is a list comprenhension
print(xyz)

""" Embeded List Comprehensions   """
[[print(i,ii) for ii in range(3)] for i in range(5)] # Prints a list of matrix of 5x5


""" Embeded Generator Expression """
xyz = ((print(i,ii) for ii in range(3)) for i in range(5)) #Generates a matrix of 5x5 to iterate over
for i in xyz:
    for ii in i:
        print(ii)