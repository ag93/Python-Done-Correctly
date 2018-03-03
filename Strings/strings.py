# -*- coding: utf-8 -*-
import os
"""
Conventional way of sring concatination

names = ['Marc', 'Nico', 'Rafael', 'Elon']

for name in names:
    statement = 'Hey there ' + name
    print(statement)
"""


#New/Better way of concatination

names = ['Marc', 'Nico', 'Rafael', 'Elon']

for name in names:
    statement = ' '.join(['Hey there', name])
    print(statement)
    
#This method provides better scaling!
    
    
"""

Conventional way of joining  file path string

/starting/file/path + '/' + filename
"""

#New/Better way of concatination
location_of_files = 'C:\\Users\\Aniket Gade\\Desktop\\Doing Python the Right Way!'
file_name = 'test.txt'

with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())
    
    
""" We want to fill in the blanks with variables for a string like:
    ____ bought ____ apples today!
"""

who = 'Ryuk'
how_many = 15

#So we want the sentence to be Ryuk bought 15 apples today!.

print('{} bought {} apples today!'.format(who, how_many))