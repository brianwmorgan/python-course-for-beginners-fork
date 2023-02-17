# Modules


#################################################################################################################

'''

In Python we are able to write a long program and save as a 'module'.
This is known as "creating a script".

We are able to import modules across modules and into the Python interpreter.
This negates the need to keep repeating ourselves.

Pythons standard library can be found here https://docs.python.org/3/library/

'''

#################################################################################################################

# The statement below goes at the top of your file to import the 'demo_func' function from the 'functions.py' file
# (see 'function.py' file to see how the function works)

from functions import demo_func

# Local file functions:

def func_1(arg:int):
    x = [y for y in range(2, 10, 2)]
    x.append(arg)
    print(x)

def func_2(number:int, power:int):
    print(pow(number,power))

# Since you've imported 'demo_func', you can use it in this file:

my_int = demo_func(28)
my_int # ===> prints the result (which is 32)

func_2(my_int, 16) # ===> prints 1208925819614629174706176 (the result of the nested function calls)

#################################################################################################################
