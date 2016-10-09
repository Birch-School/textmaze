#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Python dictionarys

Dictionaries save information as a key:value pair.  You can find things
by asking for it by name.  In a list, you have to know the position of
an item.

Values can be pretty much any valid Python structure, like a string,
list, tuple, or even anyother dictionary.
 
'''

#create empty dictionary
shoes = {}

#this one has some key/value pairs
drawer = {'tea spoons': 10, 'soup spoons': 12, 'forks': 8, 'knives': 7}      

# print everything as entered (items may be out of order!)
print (drawer) 

# 2 different ways to find out how many forks?
# The get method is probably more Python-y
print (drawer['forks'])
print (drawer.get('forks'))

# show all the keys
print (drawer.keys())

# show all the values
print (drawer.values())

# now lets turn the values into a simple list
mylist = list(drawer.values())
print (mylist)



