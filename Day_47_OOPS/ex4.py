# ython super() function
# When a class inherits all properties and behavior from the parent class is called inheritance.
# In such a case, the inherited class is a subclass and the latter class is the parent class.
#
# In child class, we can refer to parent class by using the super() function.
# The super function returns a temporary object of the parent class that allows
# us to call a parent class method inside a child class method.

# Syntax: super().method_Name
class Grand_Father(object):
    def Method1(self):
        print('This is Grand_parent 1 ')
    def Method2(self):
        print('This is Grand_Fther 2 ')
class Father(Grand_Father):
    def Method2(self):
        print('This is Father 1')
    def Method_2_1(self):
          super().Method2()

class Grand_Child(Father):
    def Method3(self):
        print('This is Child 1')

ob1 = Grand_Child()
ob1.Method1()
ob1.Method2()
ob1.Method3()
ob1.Method_2_1()
# <bound method Grand_Father.Method2 of <__main__.Grand_Child object at 0x0000018E8F50C760>>

# This is Grand_parent 1
# This is Father 1
# This is Child 1
# This is Grand_Fther 2