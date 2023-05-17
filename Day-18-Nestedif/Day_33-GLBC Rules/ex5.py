# Built in rule

x1=20
def fun1():
    x2 = 30
    x1 = 1000
    # print('enclosing v:',x2)
    def fun2():
        x3 = 100
        z = [x1,x2,x3]
        print('sum of z is :',sum(z))
        print('max of z is :',max(z))
        print('length is :',len(z))
    fun2()

fun1()
# print('global v:',x1)
#
# sum of z is : 1130
# max of z is : 1000
# length is : 3
