class A:


    # attributes / variables for data

    gender = 'Male'            #class variable - will be shared for all object  


    #STATE


    # Methods
    def __init__(self, name):
        self.name = name    # instance variable starts with 'self'


    def __repr__(self):
        return str(self.__dict__)   # {key : value}
        
    def __str__(self):
        return self.name


c = A('Anna') 
a = A('Claus')       

# check Claus solution for constructor overloading