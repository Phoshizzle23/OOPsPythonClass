# OOP's - Python

############################
#### Intro to OOP's ####
############################

# into functions
"""def hello():
    print("Hello")

hello()

print(type(hello))

# Methods
string = "Hello"
print(string.upper())

# Create own class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

d = Dog("Matt", 35)
print(d.get_name())
print(d.get_age())
d.set_age(63)
print(d.get_age())
d2 = Dog("Tim", 12)
print(d2.get_name())
print(d2.get_age())
d.bark()
print(d.add_one(5))
print(type(d))
print(type(d2))"""

############################
## Student Marks Project ##
############################
"""
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        if len(self.students) == 0:
            return 0
        total_grade = sum(student.get_grade() for student in self.students)
        return total_grade / len(self.students)



s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print(course.students[0].name)
print(course.get_average_grade())
"""

############################
#### Inheritance ####
############################
"""
# Parent Class
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old!!!")

    def speak(self):
        print("Im a Pet!!!")

# Child Classes
class Cat(Pet):
    def speak(self):
        print("Meow")


class Dog(Pet):
    def speak(self):
        print("Bark")


class Fish(Pet):
    pass


class Rabbit(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) # -> from parent class
        self.color = color

    def show(self):
        print(f"I am {self.name} | {self.age} years old and I am {self.color}!!!\n")

    def speak(self):
        print("To infinity and beyond!!!\n")

# Pet class
p = Pet("Tim", 19)
p.show()
p.speak()

# Cat class
c = Cat("Bill", 34)
c.show()
c.speak()

# Dog class
d = Dog("Jill", 25)
d.show()
d.speak()

# Fish class
f = Fish("Bubbles", 10)
f.show()
f.speak()

# Rabbit class
r = Rabbit("Jacko", 5, "white")
r.show()
r.speak()
"""
##################
# Class Attributes
##################

"""
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

p1 = Person("Tim")
print(Person.number_of_people)
p2 = Person("Jill")
print(Person.number_of_people)

"""
###################
## Class Methods ##
###################

"""
class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()


    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p11 = Person("Tim")

p22 = Person("Jill")

print(Person.number_of_people_())
"""

####################
## Static Methods ##
####################

"""
class Math:
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("Run")


print(Math.add5(5))

print(Math.add10(5))

print(Math.pr())

"""