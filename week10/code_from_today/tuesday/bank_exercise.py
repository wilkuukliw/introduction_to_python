#bank_exercise.py

class Bank:

    def __init__(self):
        self.accounts = []   # list - posibility to create many accounts   // to print b.accounts[0].account

class Account:
        
    def __init__(self,number,customer):    
        self.number = number
        self.customer = customer 

class Customer:

    def __init__(self,name):
        self.name = name
