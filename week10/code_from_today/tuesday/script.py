<<<<<<< HEAD
class A:


    # attributes / variables for data

    gender = 'Male'            #class variable - will be shared for all object  


    #STATE


    # Methods
    def __init__(self, name):
        self.name = name    # instance variable starts with 'self'


    def __repr__(self):
        return str(self.__dict__)   # {key : value}
        
=======
# script.py



class A:

    # attributes / variables for data

    gender = 'Male'

    # Methods
    def __init__(self, *args): # age = 33 # default values
        
        if len(args) == 1:
            self.name = args[0]  # instance variable (starts with 'self')
        if len(args)  == 2:
            self.age = args[1]
            self.name = args[0]  # instance variable (starts with 'self')

    def __repr__(self):
        return str(self.__dict__)  # {key : value}

>>>>>>> 72c0f91791ba777caafebaac0253aaa14cf2194e
    def __str__(self):
        return self.name


<<<<<<< HEAD
c = A('Anna') 
a = A('Claus')       

# check Claus solution for constructor overloading
=======
c = A('Claus', 66, 33, 44,  666)
a = A('Anna')








>>>>>>> 72c0f91791ba777caafebaac0253aaa14cf2194e
