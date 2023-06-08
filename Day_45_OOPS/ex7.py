# To make a method as class method, add @classmethod decorator before the method definition, and add cls as the first parameter to the method.
#
# The @classmethod decorator is a built-in function decorator. In Python, we use the @classmethod decorator to declare a method as a class method. The @classmethod decorator is an expression that gets evaluated after our function is defined.
#
# Let’s see how to create a factory method using the class method. In this example, we will create a Student class object using the class method.
#
# from datetime import date
#
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):
        # calculate age an set it as a age
        # return new object
        return cls(name, date.today().year - birth_year)

    def show(self):
        print(self.name + "'s age is: " + str(self.age))

jessa = Student('Jessa', 20)
jessa.show()

# create new object using the factory method
joy = Student.calculate_age("Joy", 1995)
joy.show()

