# compute.py

from time import sleep

def compute():
    val = []
    for i in range(10):
        sleep(.5)
        val.append(i)

    return val


    # to call it in terminal - > compute()


class Compute:
  #  def __call__(self):
   #     val = []
    #    for i in range(10):
     #       sleep(.5)
      #      val.append(i)
       # return val

        # here i need to create object first  >>comp = Compute()   >>comp()

# to make list iterable: need to implement these two 

        def __iter__(self):
            self.start = 0
            return self

        def __next__(self):
            temp = self.start
            self.start += 1
            if self.start > 10:
                raise StopIteration
            sleep(.5)
            return temp


# generator function ! without return statement

def compute2():
    for i in range(10):
        sleep(.5)
        yield i   # instead of returning
        

# >> g = compute2()   -- generator
# >> next(g)        executes immediately, without waiting .5sec


def cc():
    yield 1   # just to raise this error StopIteration


# generator expression ! that is easier to read

g = (i for i in range(10))