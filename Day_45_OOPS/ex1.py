# classvariables:
# Class Variables: A class variable is a variable that is declared inside of class,
# but outside of any instance method or __init__() method.

# In Python, Class variables are declared when a class is being constructed.
# They are not defined inside any methods of a class because of this only one copy of the static variable will be created and shared between all objects of the class.





# To access the class variable by using  instance method
class Book:
    c_variable1 = 10
    c_variable2 = 20
    def __init__(self,Bname):
        self.name = Bname
    def ClassVariable(self):
        print(self.c_variable1)
        print(self.c_variable2)

b1 = Book('Classmate')
b1.ClassVariable()
# 10
# 20


