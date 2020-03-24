# decorator.py


# Functions in python are first class function
# functions can take other functions as parameters
# functions can return other functions


def my_first_class_function(x):   # my_first_class_function(greet)()
    return x

#def greet():
#    print('Hello')



# Inner functions

def foo():

    # define a function
    def inner():
        return 'inner msg'

    # executig                   if you want to use function that has inner inside you need to assign outer >> x = foo() and then >> x()
    #x = inner()
    #print(x)

    return inner


# simple decorator

def my_decorator(func):

    def wrapper(*args):    # *args so we can provide any or various parameters to decorators if we have several of them taking different ones
        print('Something before execution of func')
        func(*args) # print('Hello')
        print('Something happens after')
    
    return wrapper
"""
@my_decorator
def greet():
    print('Hello')
"""

# greet = my_decorator(greet)



"""
@my_decorator
def greet(name):
    print(f'Hello {name}')

@my_decorator
def greet_me_2():
    print('Hello')

"""


# decorator returning values

def my_dec(func):
    def wrapper(*args):
        x = 'From before \n'
        x += func(*args) + '\n'
        x += 'After func'
        return x
    return wrapper



@my_dec
def greet(name):
    return f'Hello {name}'



















    
