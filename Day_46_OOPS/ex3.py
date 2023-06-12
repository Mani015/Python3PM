
class Parent:
    def Property1(self):
        print('my property belongs to my child')

class Child(Parent):
    def Property2(self):
        print('This is child property')

ob1 = Child()
ob1.Property2()
ob1.Property1()
# This is child property
# my property belongs to my child