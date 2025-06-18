class Person :
    def __init__(self, name, age): #class contructor 
        self.name = name #class variables
        self.age = age #class variables
    
    def greet(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')

a = Person("Alice", 30)
b = Person("Bob", 25)

# a.greet()
# print(a.age)
# b.greet()

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        if x1 < x2 and y1 > y2:
            self.x1 = x1 # class variable
            self.y1 = y1 # class variable
            self.x2 = x2 # class variable
            self.y2 = y2 # class variable
        else:
            print("Incorrect coordinates of the rectangle!")
    
    def width(self):
        return self.x2 - self.x1
    
    def height(self):
        return self.y1 - self.y2
    
    def area(self):
        return self.width() * self.height()
    
    def perimeter(self):
        return 2 * (self.width() + self.height())
    

rec = Rectangle(1, 5, 4, 2)
print(rec) #printing class instance "rec" will not show values but show the address of the object in the memory

#To solve the above issue, we can define a __str__ method in the class
class Rec:
    def __init__(self, x1, y1, x2, y2):
        if x1 < x2 and y1 > y2:
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
        else:
            print("Incorrect coordinates of the rectangle!")
    
    def width(self):
        return self.x2 - self.x1
    
    def height(self):
        return self.y1 - self.y2
    
    def area(self):
        return self.width() * self.height()
    
    def perimeter(self):
        return 2 * (self.width() + self.height())
    
    def __str__(self):
        return(str(self.x1) + ', ' + str(self.y1) + ', ' + str(self.x2) + ', '+ str(self.y2))
    
    #other methods can be defined here as well "repr", between str and rpr, str is used for user-friendly representation, while repr is used for debugging and development purposes.
    def __repr__(self):
        return(str(self.x1) + ', ' + str(self.y1) + ', ' + str(self.x2) + ', '+str(self.y2))
    
rec2 = Rec(1, 5, 4, 2)
print(rec2)  # Now this will print the coordinates of the rectangle

'''
str():
    makes the object readable
    generates output for end-user

repr():
    needs code that reproduces the object
    generates output for developer
If both methods are defined in a class, __str__ is used.
'''

#Inheritance 
#Going to use above Person class as super class
class Ten_Year_Old_Person(Person): #Now this class Inherits from Person class
    def __init__(self, name):
        Person.__init__(self, name, 10) # accesses Person's constructor

    def greet(self): # rewrites the greet method
        print("I don't talk to strangers cuz I'm only 10 years old!")

ten_years = Ten_Year_Old_Person("Chucky")
# ten_years.greet()  # This will call the overridden greet method

#Multilevel Inheritance 
class Animal():
    def __init__(self, name, food, characterstic):
        self.name = name
        self.food = food
        self.characterstic = characterstic
        print("I am a " + str(self.name) + ".")
    
    def my_characterstic(self):
        print(f'My characterstic is {self.characterstic} and I eat {self.food}.')

class Mammal(Animal): #inherits from Animal class
    def __init__(self, name, food, characterstic) : #Mammal constructor
        Animal.__init__(self, name, food, characterstic) #calls Animal's constructor

class Carnivore(Mammal):
    def __init__(self, name, food, characterstic):
        Mammal.__init__(self, name, food, characterstic) #calls Mammal's constructor

class Herbivore(Mammal):
    def __init__(self, name, food, characterstic):
        Mammal.__init__(self, name, food, characterstic)
        


elephant = Herbivore("Elephant", "grass", "Tall and Strong") # elephant is an instance of Mammal
elephant.my_characterstic()

lion = Carnivore("Lion", "meat", "King of Jungle") # lion is an instance of Carnivore
lion.my_characterstic()


class Bird(Animal):
    def __init__(self, name, food, characterstic):
        super().__init__(name, food, characterstic)
    
    def chirp(self):
        print(f"{self.name} is chirping!")
        super().my_characterstic()

sparrow = Bird("Sparrow", "seeds", "Small and Agile")
sparrow.my_characterstic()