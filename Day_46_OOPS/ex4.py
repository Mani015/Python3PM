# MultipleInheritance
# In multiple inheritance, one child class can inherit from multiple parent classes.
# So here is one child class and multiple parent classes.

class p1:
    def property1(self):
        print('my property belongs to my child')

class p2:
    def property2(self):
        print('this property belongs to my child')

class c1(p1,p2):
    def property3(self):
        print('this is my property')

ob1 = c1()
ob1.property3()
ob1.property1()
ob1.property2()

# this is my property
# my property belongs to my child
# this property belongs to my child

