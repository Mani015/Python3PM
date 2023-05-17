# GLobal variable using in nested function
# x1=20
# def fun1():
#     x2 = 30
#     def fun2():
#         print('global v:',x1)
#     fun2()
# fun1()
# global v: 20



x1=20
def fun1():
    x2 = 30
    x1 = 1000
    def fun2():
        print('global v:',x1)
    fun2()
    print('Enclosing v:',x1)
fun1()
print('global v:',x1)
# global v: 1000
# Enclosing v: 1000
# global v: 20
