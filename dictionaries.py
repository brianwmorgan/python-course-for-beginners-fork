#Using python to manipulate dictionary

#################################################################################################################


'''

Python knows a number of compound data types used to group together other values.
One of the most used is a dictionary.
Others include: tuple, list, set

Dictionaries are used to store data values in key:value pairs.
Dictionaries are defined as curly brackets around comma-separated key-values, where the key is a string and the value is any data type.

some_dict = {
    'a_key': 'a_value',
    'a_key_2': 'a_value_2',
    'a_key_3': ['a_list', 'as', 'a value'],
    'a_key_4': {'a_dict': 'as a value'}
}

Dictionaries are MUTABLE - this means that item values CAN be changed

Dictionaries have a bunch of methods available:

clear() Removes all the elements from the dictionary
copy() Returns a copy of the dictionary
fromkeys() Returns a dictionary with the specified keys and value
get() Returns the value of the specified key
items() Returns a list containing a tuple for each key value pair
keys() Returns a list containing the dictionary's keys
pop() Removes the element with the specified key
popitem() Removes the last inserted key-value pair
setdefault() Returns the value of the specified key. If the key does not exist: 
insert the key, with the specified value
update() Updates the dictionary with the specified key-value pairs
values() Returns a list of all the values in the dictionary

'''

#################################################################################################################


# The Basics

# Define a new dictionary

some_dict = {
    'a_key': 'a_value',
    'a_key_2': 'a_value_2',
    'a_key_3': ['a_list', 'as', 'a value'],
    'a_key_4': {'a_dict': 'as a value'}
}

some_dict # ===> prints {'a_key': 'a_value', 'a_key_2': 'a_value_2', 'a_key_3': ['a_list', 'as', 'a value'], 'a_key_4': {'a_dict': 'as a value'}}


# Reference a dictionary item by key name, NOT by index

some_dict[0]           # this will return an error as you need to reference the key by name ===> prints 'KeyError: 0'
some_dict['a_key']     # ===> prints 'a_value'
some_dict['a_key_4']   # ===> prints {'a_dict': 'as a value'}


# Create a copy of a dictionary with the copy() method

dict_copy = some_dict.copy()
dict_copy # ===> prints {'a_key': 'a_value', 'a_key_2': 'a_value_2', 'a_key_3': ['a_list', 'as', 'a value'], 'a_key_4': {'a_dict': 'as a value'}}


# Alter a dictionary by accessing a key and reassigning it's value

some_dict['a_key'] = 'new_value'  
some_dict['a_key'] # ===> prints 'new value'


# Determine dictionary length

len(some_dict) # ===> prints 4


# Show all keys and values with keys() and values() methods

some_dict.keys() # ===> prints dict_keys(['a_key', 'a_key_2', 'a_key_3', 'a_key_4'])
some_dict.values() # ===> prints dict_values(['new_value', 'a_value_2', ['a_list', 'as', 'a value'], {'a_dict': 'as a value'}])

#################################################################################################################


# Dictionary comprehension

# this defines a new dictionary where each key is the integer being looped over and each value is the integrer squared

new_thing = {x: x**2 for x in (2, 4, 6)}
new_thing # prints ===> {2: 4, 4: 16, 6: 36}

#################################################################################################################


# Built-in dict() function

x = dict(a=1, b=2, c=3, d=4) # creates a dictionary out of a series of defined variables
x # ===> prints {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#################################################################################################################
