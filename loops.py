# Python control flows - Loops


####################################################################################################################

'''

Python’s 'for' statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.

The built-in 'range()' function comes in handy if you do need to iterate over a sequence of numbers.
It generates arithmetic progressions:

range(start, stop, step)

'start' : the value of the start parameter (or 0 if the parameter was not supplied)
'stop' : the value of the stop parameter
'step' : the value of the step parameter (or 1 if the parameter was not supplied)

'''


####################################################################################################################


# Looping over a list

# Create a sample list of string elements

words = ['cat', 'window', 'defenestrate']

# In the 'for' loop below, the 'w' below is a placeholder variable for the element being iterated over during the loop
# You can use any name for that placeholder and call that name in the ensuing loop body

for w in words:
    print(w, len(w))

# the above prints:
# cat 3
# window 6
# defenestrate 12

####################################################################################################################


# Loop over a dictionary using items()

# Create a sample dictionary

users = {
    'Quinn': 'active',
    'Éléonore': 'inactive',
    'John': 'active'
    }

# In the for loop below, 'user' is referring to the key and 'status' is referring to the value
# Again, these are simply placeholder variables that can be named anything
# 'users.copy().items()' is referring to the items in a copy of the 'users' dictionary
# If the value in the iterated key-value pair is 'inactive', the 'del' function will delete the matching key (and consequently, it's value), in 'users'

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

users # ===> prints {'Quinn': 'active', 'John': 'active'}

####################################################################################################################


# Strategy:  Create a new collection

# Create an empty dictionary

active_users = {}

# Iterate over the items in the 'users' dictionary above, using 'user' and 'status' as variable placeholder for the keys and values
# If the iterated item's value is 'active', add the 'user' as a new key in 'active_users' and assign it's value to that user's 'status'

for user, status in users.items():
    if status == 'active':
        active_users[user] = status

# active_users  ===> prints {'Quinn': 'active', 'John': 'active'}

####################################################################################################################


# The built-in 'range()' function

# Syntax:
# range(start, stop, step)

# Arguments:
# 'start' : the value of the start parameter (or 0 if the parameter was not supplied)
# 'stop' : the value of the stop parameter
# 'step' : the value of the step parameter (or 1 if the parameter was not supplied)

# With just one argument provided below, 'start' is assumed to be '0' and 'step' is assumed to be '1'
# so, this for loop will iterate over (and print) all numbers starting at 0, one at a time, until it hits the 'stop' value ('5')

for i in range(5):
    print(i)

# the above code prints: 
# 0
# 1
# 2
# 3
# 4

####################################################################################################################


# Create lists with list() and range()

# start at 5, stop at 10th integer, one integer at a time
list(range(5, 10))  # ===> prints  [5, 6, 7, 8, 9]

# start at 0, stop at 10th integer, three integers at a time
list(range(0, 10, 3))  # ===> prints [0, 3, 6, 9]

# start at -10, stop at -100 integer, go backwards 30 integers at a time
list(range(-10, -100, -30))  # ===> prints [-10, -40, -70]

####################################################################################################################


# Use for loops with range()

# Define a new list
a = ['Mary', 'had', 'a', 'little', 'lamb']

# Loop over each item in the range of the length of 'a' and print each items index and the value of that index
for i in range(len(a)):
    print(i, a[i])

# The above function prints ===>
# 0 Mary
# 1 had
# 2 a
# 3 little
# 4 lamb

####################################################################################################################


# The built-in sum() function

# The function below sums the first 4 integers starting at 0, one at a time ( 0 + 1 + 2 + 3 )

sum(range(4))   # prints ===> 6

####################################################################################################################
