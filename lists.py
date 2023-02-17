#Using python to manipulate lists


#################################################################################################################

'''
Python knows a number of compound data types, used to group together other values, the most versatile of which is a list.
Others include: tuple, dictionary, set

Lists are written as a list of comma-separated values (items) between square brackets.

Lists are MUTABLE - this means that items CAN be changed.

Lists have a bunch of methods available:
append() Adds an element at the end of the list
clear()	Removes all the elements from the list
copy() Returns a copy of the list
count()	Returns the number of elements with the specified value
extend() Add the elements of a list (or any iterable), to the end of the current list
index() Returns the index of the first element with the specified value
insert() Adds an element at the specified position
pop() Removes the element at the specified position
remove() Removes the first item with the specified value
reverse() Reverses the order of the list
sort() Sorts the list

'''

#################################################################################################################


# The Basics

# Create a list by setting a variable equal to any number of elements inside brackets (with the items separated by commas)
squares = [1, 4, 9, 16, 25]
squares # ===> prints [1, 4, 9, 16, 25]


# Indexing

'''
 +---+---+---+---+---+---+---+---+---+
 | D | i | d | C | o | d | i | n | g |
 +---+---+---+---+---+---+---+---+---+
 0   1   2   3   4   5   6   7   8   
-9  -8  -7  -6  -5  -4  -3  -2  -1
'''

squares[0]  # indexing returns the item at that index # ===> prints 1
squares[-1] # indexing from negative returns the item working from the end of the list # ===> prints 25


# Create a list copy
squares[:]


# Concatenate (glue together) multiple lists
squares + [36, 49, 64, 81, 100] # prints ===> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Alter an item in a list
cubes = [1, 8, 27, 65, 125]  # let's say you want to change '65' to '64'...
cubes[3] = 64  # replaces the the element in at index 3 with '64'
cubes # prints ===> [1, 8, 27, 64, 125]


# The append() method
cubes.append(216)  # you can add an item to the end of a list (i.e. the cube of 6 (216)) by appending that value onto 'cubes'
cubes.append(7 ** 3)  # you can also append a value using operators (i.e. the cube of 7)
cubes # prints  ===> [1, 8, 27, 64, 125, 216, 343]


# The len() method
letters = ['a', 'b', 'c', 'd']
len(letters) # ===> prints 4

#################################################################################################################


# Nesting Lists

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

x # prints ===> [['a', 'b', 'c'], [1, 2, 3]]

x[0] # prints ===> ['a', 'b', 'c']

x[0][1] # prints ===> 'b'

#################################################################################################################


# List comprehension

# define 'y' as an empty list
y = []

# loop over all integers from 0 to the tenth integer, one at a time
# for each integer, add the cubed integer value to 'y'
for x in range(10):
    y.append(x**2)

y # ===> prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# alternatively, you can simply define 'y' as the for loop function above:

y = [x**2 for x in range(10)] # ===> prints the same as above

#################################################################################################################


# Built-in list() method
x = list(('bobby', 'at', 'didcoding','dot', 'com')) # creates a new list out of the items argument
x # ===> prints ['bobby', 'at', 'didcoding', 'dot', 'com']
