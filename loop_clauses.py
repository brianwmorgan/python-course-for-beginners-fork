# Python control flows - Loop clauses

#################################################################################################################


'''

Python has a few statements and clauses that we can use in loops. 
These are: 'break', 'continue', 'else', 'pass'.

Loop statements may have an 'else' clause: It is executed when the loop terminates through exhaustion of the iterable (with for loops)...
...OR when the condition becomes false (with while loops), ...
...but NOT when the loop is terminated by a break statement. 

'''

#################################################################################################################


# The 'break' statement

for n in range(2, 10):      # this is the equivalent of 'for n in [2,3,4,5,6,7,8,9]:'
    for x in range(2, n):   # the first loop is for x in range(2, 2):
        if n % x == 0: 
            print(n, 'equals', x, '*', n//x)
            break
    # The 'else' code runs when no 'break' clause occurs
    else:
        print(n, 'is a prime number')

# The above code prints:

# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3

#################################################################################################################


# The 'continue' statement

for num in range(2, 10):      # This is the equivalent of 'for n in [2,3,4,5,6,7,8,9]:'
    if num % 2 == 0:
        print("Found an even number", num)
        continue # Will continue with the next loop (the ensuing loop has the code below executed on it rather than the code above)
    print("Found an odd number", num)

# The above code will print:

# Found an even number 2
# Found an odd number 3
# Found an even number 4
# Found an odd number 5
# Found an even number 6
# Found an odd number 7
# Found an even number 8
# Found an odd number 9

#################################################################################################################


#  The 'pass' statement

class MyPassClass:
    pass

# 'pass' means that it does nothing

def my_pass_def(*args):
    pass #Needs looking at

my_pass_def() # ===> prints/does nothing

#################################################################################################################
