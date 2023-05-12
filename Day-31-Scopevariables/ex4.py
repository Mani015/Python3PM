
# Built-In Function:
# Built-in Scope
# The variables and names that are defined in the python built-in modules are said to be under the built-in scope.
# The names which are under built-in scope can be used directly in the program just by importing the respective module.
# For example, range( ), print( ), input( ), global, nonlocal, globals( ), len(),max(),Min() ,sum() and many more

x1 = 10
def Outer():
    x2 = 20
    def Inner():
        x3 = 30
        z = [x1,x2,x3]
        # z = [10,20,30]
        print(sum(z))
        print(max(z))


    Inner()
Outer()
# 60
