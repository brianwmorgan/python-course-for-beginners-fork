# Python control flows - If statement


#################################################################################################################

'''

Python uses the usual flow control statements known from other languages, with some twists.
Perhaps the most well-known statement type is the if statement.

Think of an if statement as a way to check to see if conditions are met!

If a condition is met, do something... else do something different!

'elif' stands for 'else if'

Both 'elif' and 'else' are optional!

'''

#################################################################################################################


# The Basics

# the code below defines a function 'number_play' that accepts an argument, 'x'
# the syntax for an if statement uses the 'if" keyword and  immediately defines the condition ('x < 0')
# if the condition is met, the ensuing code is executed
# if not, it moves on to the next condition (if there is one)
# if an 'else' statement is provided, the ensuing code will execute if no 'if' conditions are met

def number_play(x):
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

number_play(-1)      # ===> prints 'Negative changes to zero'
number_play(0)       # ===> prints 'Zero'
number_play(1)       # ===> prints 'Single'
number_play(2)       # ===> prints 'More'

#################################################################################################################
