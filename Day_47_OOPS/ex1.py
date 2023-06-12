# Multiple level Inheritance:
# Multilevel inheritance
# In multilevel inheritance, a class inherits from a child class or derived class.
# Suppose three classes A, B, C. A is the superclass, B is the child class of A, C is the child class of B.
# In other words, we can say a chain of classes is called multilevel inheritance.

class Grand_Parent(object):
    def Method1(self):
        print('this is grandfather property')
class Father(Grand_Parent):
    def Method2(self):
        print('This is father property')
class Child(Father):
    def Method3(self):
        print('This is Child class')

ob1 = Child()
ob1.Method1()
#this is grandfather property
ob1.Method2()
#This is father property
ob1.Method3()
# This is Child class
