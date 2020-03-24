#datamodel.py

class A:
    def __init__(self):
        self.name = "Anna"

    def __len__(self):
        return len(self.name)
        
    def __add__(self, other):
        self.name + other.name

    def __repr__(self):
        return f'{self.__dict__}'   # prints out dictionary of instance variables. formal

    def __str__(self):
        return self.name   #informal

    def __getitem__ (self, key):
        return self.name[key]
