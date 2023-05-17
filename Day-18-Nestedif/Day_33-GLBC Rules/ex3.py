# Local rule
# local is the code bloackof body of any python fucntion/ lambda expression, This python scope contains the name that u defined inside the function
# These names will only be visible code of fromthe code of function,it's created at fucntioncall not at function defination

x1=20
def fun1():
    x2 = 30
    x1 = 1000
    def fun2():
        x3 = 100
        print('local scope:',x3)
        print('enclosing v:',x1)
    fun2()
    print('Enclosing v:',x1)
fun1()
print('global v:',x1)

# local scope: 100
# enclosing v: 1000
# Enclosing v: 1000
# global v: 20
