
# Python Instance Variables: Learn to create and access instance variables. Modify values of instance variables.
# Understand how dynamically we can add or delete instance variables from the object

# Instance variables: If the value of a variable varies from object to object,
# then such variables are called instance variables.
# Class Variables: A class variable is a variable that is declared inside of class,
# but outside of any instance method or __init__() method.

class Employee:
    def __init__(self,Empname,Empsalary,Empage):
        self.name = Empname
        # instance varaibles
        self.salary = Empsalary
        self.age = Empage
    def View(self):
        print(self.name,self.salary,self.age)


# To accessing the two ways
E1 = Employee('Devi',80000,20)
# E1.View()

# Employee.View()
# TypeError: View() missing 1 required positional argument: 'self'
Employee.View(E1)
# Devi 80000 20



