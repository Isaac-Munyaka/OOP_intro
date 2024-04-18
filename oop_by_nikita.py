class Student:
    pass


    def exam(self):# method under the student class
        print("Student is eligible to sit for exam")

    def admission(self):
        print("Welcome to Our School")



obj= Student() #instance/object
obj2 =Student()


# class Finance:
    # pass

# obj2= Finance()
print(obj)
print(obj2)

obj.exam()
obj2.exam()
obj.admission()
obj2.admission() 


class Dog:
    pass
    
    # methods
    def eat(self):
        print("The dog ate today")
    
    def sleep(self):
        print("The dog slept today, after eating")

    def bark(self):
        print("Has barked 5 times today")

    def bite(self):
        print("It has not bitten nor chased any kid today")

simba = Dog()   #simba is the object, so I am creating an instance of the object
fluffy = Dog()
nala = Dog()
pappi= Dog()
tommy = Dog()


fluffy.bark()
tommy.eat()
nala.bite()
simba.sleep()


class Admission:
    def __init__(self, name, email, id, address, gender):
        self.name = name
        self.email = email
        self.id= id
        self.address = address
        self.gender= gender
    
    def onboard(self):
        print(f"Congratulations {self.name} of id {self.id}, for being admitted to Flatiron School")


class Finance(Admission):
    def __init__(self, name, email, id, fee, amount,balance):
        super().__init__(name, email, id,) #Inheriting methods from the super class
        self.fee = fee
        self.amount = amount
        self.balance = balance


    def balance(self, amount):
        print(f"{self.name}: your balnce is Ksh{self.amount}")



class Cat:

    def __init__(self, meow="meow"): #another way of defining the attributes
        self.meow = meow


    
    
fifi = Cat()
fifi.meow

class Dog:

    def __init__(self, bark = "woof"):
         self.bark = bark

garry= (Dog)
garry.bark