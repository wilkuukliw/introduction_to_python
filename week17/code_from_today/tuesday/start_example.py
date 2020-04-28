# start_example.py


#@profile
def sum_of_list():
    return sum([i*i for i in range(1, 1000000)])

#@profile
def sum_of_generator():
    return sum((i*i for i in range(1, 1000000)))


sum_of_list()
sum_of_generator()
