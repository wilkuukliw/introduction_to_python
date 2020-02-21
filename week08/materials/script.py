# script.py

def deco(func):
    def wrapper(*args):
        print('Hello', end='')
        print(func(*args), end='')
        print(' the great', )
    return wrapper


@deco
def greet(name):
    return name * 2


