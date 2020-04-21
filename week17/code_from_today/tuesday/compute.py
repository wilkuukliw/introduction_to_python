# compute.py

from time import sleep

def compute():
    val = []
    for i in range(10):
        sleep(.5)
        val.append(i)
    return val

class Compute:
    #def __call__(self):
    #    val = []
    #    for i in range(10):
    #        sleep(.5)
    #        val.append(i)
    #    return val

    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        temp = self.start
        self.start += 1
        if self.start > 10:
            raise StopIteration()
        sleep(.5)
        return temp


# generator function 
def compute2():
    for i in range(10):
        yield i      # instead of return


def cc():
    yield 1


# generator expression
g = (i for i in range(10))
