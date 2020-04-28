# school_of_students.py

#create:

#A list of dictionaries of students (ie: students = [{‘id’: 1,’name’: ‘Claus’, ‘major’: ‘Math’}]), cretated in a normal function that returns the resul.

#A Generator that “returns” a generator object. So the student is yield instead of returned.


import random
import time

# Timer decorator
def timer(func):
    def wrapper(*args):
        start = time.time()
        val = func(*args)
        end = (time.time()) - start
        print(f'Time elepsed: {end}')
        return val
    return wrapper

# the exercise:

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

@timer
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    # return result

@timer
def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person













