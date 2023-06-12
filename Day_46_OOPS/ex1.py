# Inheritance:
# The process of inheriting the properties of the parent class into a child class is called inheritance.
# The existing class is called a base class or parent class and the new class is called a subclass or child class or derived class.

# In Object-oriented programming, inheritance is an important aspect.
# The main purpose of inheritance is the reusability of code because we can use the existing class to create a new class instead of creating it from scratch.


# Single inheritance
# Multiple Inheritance
# Multilevel inheritance
# Hierarchical Inheritance
# Hybrid Inheritance


# In single inheritance, a child class inherits from a single-parent class.
# Here is one child class and one parent class.
class Animal:
    def Sleeping(self):
        print('A animal sleep')
    def Eating(self):
        print('eating every day')

class Lion:
    def hunting(self):
        print('hunting every day')
ob1 = Animal()
ob1.Eating()
ob1.Sleeping()

# eating every day
# A animal sleep

ob2 = Lion()
ob2.hunting()
# hunting every day





