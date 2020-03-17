# inheritance.py


class A:
    def __init__(self, name):
        self.name = name

class B:
    def __init__(self, age):
        self.age = age


class C(A, B):
    def __init__(self, name, age):
        # super().__init__(name)

        A.__init__(self, name)
        B.__init__(self, age)
    
