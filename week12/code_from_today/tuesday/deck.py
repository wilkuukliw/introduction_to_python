#deck.py

class Deck:
    def __init__(self):                 #   >> d = Deck()
        self.cards = ['A', 'K', 4, 7]   # list of cards that are included in deck

    def __getitem__(self,key):
        return self.cards[key]              # >> d[1] 

    def __len__(self):
        return len(self.cards)              # >> len(c)

    def __add__(self,other):                #  >> c = Deck()
        return self.cards + other.cards     #  >> d + c 
 
    def __repr__(self):                     # >> d    or top level representation repr(d)
        return f'{self.__dict__}'           # >> {'cards': ['A', 'K', 4, 7]}      

    def __str__ (self):                     # informal representation
        return str(self.cards)              # >> str(d)    >> "['A', 'K', 4, 7]"

    def __setitem__ (self, key, val):
        self.cards[key] = val

    def __delitem__ (self, key):
        del(self.cards[key])             # we do not use return but del instead 
