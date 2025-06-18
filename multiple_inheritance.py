#Multiple Inheritance
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f'Hi, I am {self.name}.')

class Student(Person): # Student inherits from Person class
    def __init__(self, name, roll_number):
        self.name = name # Attribute inherited from the Person class
        self.roll_number = roll_number # Student's attribute
        Person.__init__(self, name) # Person's constructor or super.__init__(name)
    
    def report(self): #student method
        print("My roll numnber is " + str(self.roll_number) + ".")

class Teacher(Person): # Teacher inherits from Person class
    def __init__(self, name, course):
        self.name = name # Attribute inherited from the Person class
        self.course = course # Teacher's attribute
        Person.__init__(self, name) # Person's constructor
    
    def introduce(self):
        print("I teach " + self.course + ".")

class Teaching_Assitant(Student, Teacher): #inherits from both Student and Teacher class
    def __init__(self, name, roll_number, course, grade):
        self.name = name # Attribute inherited from the Person class
        self.roll_number = roll_number # Attribute inherited from the Student class
        self.course = course # Attribute inherited from the Teacher class
        self.grade = grade # Teaching_Assitant's attribute
    
    def details(self): #Teaching_Assitant method
        if self.grade == 'A*' or self.grade == "A" or self.grade == "A-":
            Person.greet(self) # can access Person's greet method
            Student.report(self) # can access Student's report method
            Teacher.introduce(self) # can access Teacher's introduce method
            print("I got an "+ str(self.grade) + " in " + self.course + ".")
        else : 
            print(self.name + ", you can not apply for TAship.")

ta = Teaching_Assitant("Alice", 101, "Python Programming", "A*")
ta.details()

ta2 = Teaching_Assitant('Ahmed', 107, 'Algorithms' ,'B')
ta2.details()