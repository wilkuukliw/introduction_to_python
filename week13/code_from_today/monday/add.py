# add.py

"""
Write a decorator that writes to a log file the time stamp of each time this function is called.

Change the log decorator to also printing the values of the argument together with the timestamp.

Print the result of the decorated function to the log file also.

Create a new function and call it printer(text) that takes a text as parameter and either returns or prints the text 2 times. Decorate it with your logfunction. Does it work?
"""

from datetime import datetime   # import built in module 

def log(func):
    def wrapper(*args):
        # log to a text file - week 9 
        f = open('log.txt', 'a+')   #open = create    a+ means append / w means write 
        f.write(f'{datetime.now()}, {args} = {func(*args)} \n')
        #return the decorated function
        return func(*args)
    return wrapper


@log
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

@log
def printer(text):
    return text * 2
