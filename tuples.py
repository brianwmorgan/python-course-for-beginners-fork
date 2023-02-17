#Using python to manipulate tuples

'''
Python knows a number of compound data types, 
used to group together other values.
They are:
tuple
dictionary
set
list

Tuples are written as a list of comma-separated 
values (items) between parentheses.


Tuples are immutable - this means that items can not be changed. However,
a tuple can contain mutable objects.

Tuple has 2 methods available.
count()	Returns the number of elements with the specified value
index() Returns the index of the first element with the specified value
'''

#The basics - tuple packing
t = 12345, 54321, 'hello!'
t[0] # ===> prints 12345
t # ===> prints (12345, 54321, 'hello!')

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u # ===> prints ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Tuples are immutable:
t[0] = 88888 # ===> prints 'TypeError: 'tuple' object does not support item assignment'

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v[0][1] = 36
v # ===> prints ([1, 36, 3], [3, 2, 1])

#Indexing
'''
 +---+---+---+---+---+---+---+---+---+
 | D | i | d | C | o | d | i | n | g |
 +---+---+---+---+---+---+---+---+---+
 0   1   2   3   4   5   6   7   8   
-9  -8  -7  -6  -5  -4  -3  -2  -1
'''

t = 12345, 54321, 'hello!'
t[0]  # indexing returns the item ===> prints '12345'
t[-1] # ===> prints 'hello!'

#trailing comma creates a tuple with a length of one
empty = ()
singleton = 'hello',
len(empty) # ===> prints 0
len(singleton) # ===> prints 1
singleton # ===> prints ('hello",)

#Unpacking a tuple (takes each item from a tuple and assigns it to a new variable)
x, y, z = t
x # ===> prints 12345
y # ===> prints 54321
z # ===> prints 'hello!'

#built-in function tuple()
x = tuple(['bobby', 'at', 'didcoding','dot', 'com']) # creates a tuple object out the input (in this case, a list)
x # ===> prints ('bobby', 'at', 'didcoding', 'dot', 'com'), which is now immutable
x[1] = 'barf' # ===> prints 'TypeError'

#Tuple comprehension...Just use list comprehension with the tuple function
tuple([x**2 for x in range(10)]) # ===> prints (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
