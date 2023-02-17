# Using Python to manipulate sets


#################################################################################################################

'''
Python knows a number of compound data types used to group together other values.
They are: tuple, dictionary, set, list

A 'set' is an unordered collection with no duplicate elements.

Like a dictionary, a set is defined by a curly brackets.

Sets are MUTABLE - this means that items CAN be changed.

Set has a whole bunch of built-in methods available:

add() Adds an element to the set
clear() Removes all the elements from the set
copy() Returns a copy of the set
difference() Returns a set containing the difference between two or more sets
difference_update() Removes the items in this set that are also included in another, specified set
discard() Remove the specified item
intersection() Returns a set, that is the intersection of two or more sets
intersection_update() Removes the items in this set that are not present in other, specified set(s)
isdisjoint() Returns whether two sets have a intersection or not
issubset() Returns whether another set contains this set or not
issuperset() Returns whether this set contains another set or not
pop() Removes an element from the set
remove() Removes the specified element
symmetric_difference() Returns a set with the symmetric differences of two sets
symmetric_difference_update() Inserts the symmetric differences from this set and another
union() Return a set containing the union of sets
update() Update the set with another set, or any other iterable

'''

#################################################################################################################


# Create a set by defining a variable as values inside curly brackets separated by commas
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

basket # duplicates are not allowed in sets, so they will have been removed ===> prints {'apple', 'orange', 'pear', 'banana'}

#################################################################################################################


# Fast membership testing

'orange' in basket # ===> prints 'True'
'crabgrass' in basket # ===> prints 'False'

#################################################################################################################


# Using set() operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')

a       # unique letters in a ===> prints {'a', 'r', 'd', 'c', 'b'}
a - b   # letters in a but not in b ===> prints {'r', 'b', 'd'} 
a | b   # letters in a or b or both ===> prints {'a', 'z', 'r', 'd', 'c', 'm', 'b', 'l'}
a & b   # letters in both a and b ===> prints {'a', 'c'}
a ^ b   # letters in a or b but not both ===> prints {'d', 'b', 'z', 'r', 'm', 'l'}

# IMPORTANT - the above sets will not always print in the same order !!!

#################################################################################################################


# Set comprehension

# creates a set out of any characters the satisfy the conditional of the for loop 
a = {x for x in 'abracadabra' if x not in 'abc'}
a # ===> prints {'r', 'd'}

#################################################################################################################


# Built-in set() function

x = set(('bobby','bobby', 'at', 'didcoding', 'dot', 'com')) # creates a set out of a tuple (or any other elements you pass in) 
x # ===> prints {'at', 'bobby', 'didcoding', 'dot', 'com'}

#################################################################################################################
