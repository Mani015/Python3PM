import multipledispatch as multipledispatch
class Addtion:
    @multipledispatch.dispatch(int,int,int)
    def Method1(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

        print(self.a + self.b + self.c)

    @multipledispatch.dispatch(int, int)
    def Method1(self,x,y):
        self.x = x
        self.y = y
        print(self.x + self.y)
    @multipledispatch.dispatch()
    def Method1(self):
        print('I am Basic method')

ob1 = Addtion()
ob1.Method1(10,20)
# 30
ob1.Method1(1,2,3)
# 6
ob1.Method1()
# I am Basic method

