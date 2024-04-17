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

# Rewriting the above code to more easier OOP

class Dog:
    pass

    def __init__(self, eat, sleep, bark, bite):
        self.eat= eat
        self.sleep= sleep
        self.bark= bark
        self.bite=bite

dog1=Dog()
  