class Grand_Parent(object):
    def Method1(self):
        print('this is grandfather property 1')
    def Method2(self):
        print('This is grandfather property 2')
class Father(Grand_Parent):
    def Method2(self):
        print('This is father property')
class Child(Father):
    def Method3(self):
        print('This is Child class')


ob1 = Child()
ob1.Method1()
ob1.Method2()
ob1.Method2()
ob1.Method3()

# this is grandfather property 1
# This is father property
# This is father property
# This is Child class

