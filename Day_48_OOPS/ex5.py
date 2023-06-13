# The process of calling the same method with different parameters is known as method overloading.
# Python does not support method overloading.
# Python considers only the latest defined method even if you overload the method.
# Python will raise a TypeError if you overload the method.

class Addtion:
    def Method1(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

        print(self.a + self.b + self.c)
    def Method1(self,x,y):
        self.x = x
        self.y = y
        print(self.x + self.y)
    def Method1(self):
        super().Method1
        print('I am Basic method')

ob1 = Addtion()
# ob1.Method1(10,20,30)
# TypeError: Method1() takes 3 positional arguments but 4 were given
ob1.Method1()
# TypeError: Method1() takes 1 positional argument but 2 were given

