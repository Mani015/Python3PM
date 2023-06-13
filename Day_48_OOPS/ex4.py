# Method Overloading
# single class, multiple methods with the same name

class Addition:
    def m1(self):
        print('I am First method')

    def m1(self):
        print('I am second method')

ob1 = Addition()
ob1.m1()
ob1.m1()