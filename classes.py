# Python classes


#################################################################################################################

'''

'Classes' provide a means of bundling data and functionality together.
Creating a new 'class' creates a new type of object, allowing new instances of that type to be made.

Python classes provide all the standard features of Object Oriented Programming:
- the class inheritance mechanism allows multiple base classes
- a derived class can override any methods of its base class or classes
- a method can call the method of a base class with the same name.

The simplest form of class definition looks like this:

class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>

Class definitions, like function definitions ('def' statements), must be executed (aka "called") before they have any effect.

'''

#################################################################################################################


# The Basics


# Define a new class

class MyClass:
    """A simple example class"""
    i = 12345
    
    def f(self):
        return 'hello world'


# Call the contents of the class

MyClass.i         # return the int ===> prints 12345

MyClass.f         # returns a function object ===> prints '<function MyClass.f at 0x000001FD999D8900>'

MyClass.__doc__   # magic method/dunder method that return the text literal ===> prints 'A simple example class'



# Instantiate the class by assigning it to a variable

x = MyClass() #instantiates the class

# Once, instantiated, you can call the classes contents by invoking that variable

x.i               # return the int ===> prints 12345

x.f()             # calls the class method ===> prints 'hello world'

'''

Notice in the class definition above that 'self' is passed as the first arg
We pass the methods instance object in as the first arg, so, 'x.f()' is the equivalent of 'MyClass.f(x)'

Note: 'self' has no special meaning to Python - it's just convention to use it

'''

#################################################################################################################


# Class with special initial state - we user __init__

# This allows us to pass args to the class for greater flexibility

class MyClass:
    """A simple example class"""
    def __init__(self, my_int:int):
        self.i = my_int
    
    def f(self):
        new = self.i ** 3
        return new

x = MyClass(4) # instantiates the class with an arugment of 4

x.i # returns the int ===> prints 4

x.f() # calls the class method ===> prints 64, which is 4 ** 3

#################################################################################################################


# Instance objects

# We can add and delete attributes to our class object as follows:


# Add a data attribute and assign a value
x.counter = 1

while x.counter < 10:
    x.counter = x.counter * 2
    # first loop x.counter == 2
    # second loop x.counter == 4
    # third loop x.counter == 8
    # fourth loop x.counter == 16
    # fifth loop does not start as x.counter > 10

print(x.counter) # ===> prints 16


# Delete the data attribute with 'del' keyword
del x.counter

print(x.counter) # ===> prints 'AttributeError: 'MyClass' object has no attribute 'counter''

#################################################################################################################


# Class variables vs Instance variables

# Create a new class called 'Dog'
# there is a class variable 'kind' that is universally available
# there are instance variables that are only available to the instance

class Dog:
    kind = 'canine'               # class variable shared by all instances (the value remains the same for all instances)
    def __init__(self, name):
        self.name = name          # instance variable unique to each instance (the value will depend on the instance)
        self.tricks = []
    def add_trick(self, trick):
        self.tricks.append(trick)


# Assign the class to multiple instances, 'd' and 'e'

d = Dog('Fido')
e = Dog('Buddy')

# The class variable will remain the same:

d.kind  # ===> prints 'canine'
e.kind  # ===> prints 'canine'

# The instance variables will depend on the instance arguments:

d.name  # ===> prints 'Fido'
e.name  # ===> prints 'Buddy'


d.add_trick('roll over')
e.add_trick('play dead')
e.add_trick('go fetch')

d.tricks  # ===> prints ['roll over']
e.tricks  # ===> prints ['play dead', 'go fetch']

#################################################################################################################


# Inheritance

'''

A class can inherit attributes from other classes ('base classes').
When this happens, the class is called a 'derived class'

class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>

Execution of a derived class definition proceeds the same as for a base class.
When the class object is constructed, the base class is remembered.

This is used for resolving attribute references: If a requested attribute is not found in the class, the search proceeds to look in the base class. 
This rule is applied recursively if the base class itself is derived from some other class.

Derived classes may extend OR override methods of their base classes.

'''

# Create a new class called 'Mapping' that will act as a base class:

class Mapping:
    '''
    Private variable example.
    checkout __update - this is called name mangling  
    Is done without regard to syntactical position
    '''
    def __init__(self, iterable):
        self.items_list = []
        self.iterable = iterable
    
    def update(self):
        for item in self.iterable:
            self.items_list.append(item)    


# Next, create a new class called 'MappingSubClass' that accepts the 'Mapping' base class as an argument (and therefore becomes a derived class):

class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


# Instantiate a new 'MappingSubClass' instance called 'm':

m = MappingSubclass([1,2,3,4])

m.items_list  # ===> prints an empty list, '[]'

# Call the update method on 'm', supplying relevant arguments:

m.update(["one","two","three"], ["these", "are", "values"])

m.items_list  # ===> prints [('one', 'these'), ('two', 'are'), ('three', 'values')]

# The above happens because 'MappingSubClass' is utilizing the 'update()' function defined in the 'Mapping' base class

#################################################################################################################
