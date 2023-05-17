# Enclosing Rule:
# Enclosing is special scope that only exist for nested function if the local scope is an inner or nested fucntion then the enclosing
# scope of the outer or enclsing fucntion
# this scope contains naems that u defiend ina enclosing function


x1=20
def fun1():
    x2 = 30
    x1 = 1000
    print('enclosing v:',x2)
    def fun2():
        x3 = 100
    fun2()

fun1()
print('global v:',x1)
# NameError: name 'x3' is not defined


# enclosing v: 30
# global v: 20
