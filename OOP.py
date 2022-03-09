class iamBird:

    #instance attr
    def __init__(self):
        print("iamBird class constructor is executing! ")
      
    
    def canSwim(self):
        print(" I am a Bird...")

    def canSwim(self):
        print(" I can swim")


class iamParrot:
    #class attribute
    species = "Bird"

    #instance attr
    def __init__(self,name,age):
        print("iamParrot class constructor is executing! ")
        self.name = name
        self.age = age
    def canSing(self, thisSong):
        return "{} can sing {}...".format(self.name,thisSong)

# iamParrot class inheriting 
class iamPenguin(iamBird):

    #instance attr
    def __init__(self):
        #call super function
        super().__init__()
        print("Penguin is ready! ")
      
    
    def whoisThis(self):
        print(" I am a Penguin...")

    def canRun(self):
        print(" I can run faster")
    #since we inherited iamBird class we will omit ff
    #def canSwim(self):
    #   print(" I can swim")


#lets instantiate the parrot class
par1 = iamParrot("IamParrot1",10)
par2 = iamParrot("IamParrot2",17)

    #accessing instance attributes
print("{} is {} years of age".format(par1.name,par1.age))
    
print("{} is {} years of age".format(par2.name,par2.age))
print(par1.canSing("KKKKKK"))
print(par2.canSing("papapa"))

    #Accessing the child class attri(inheritance)
pg1 =iamPenguin()
pg1.whoisThis()
pg1.canSwim()
pg1.canRun()
