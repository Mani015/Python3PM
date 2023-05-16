# Nonlocal Variable in Function
# In Python, nonlocal is the keyword used to declare a variable that acts as a global variable
# for a nested function (i.e., function within another function).
#
# We can use a nonlocal keyword when we want to declare a variable in the local scope but act as a global scope.
x1 = 10
print('global variable:',x1)
# global variable: 10
def Fun():
    x1 = 20
    print('Enclosing variable:',x1)
    def InnerFunction():
        nonlocal x1
        y1 = 20
        z1 = 30
        x1 = y1+z1
        print('local variable :',x1)
    InnerFunction()
    print('Enlcosing variable:',x1)
    print('global variable',globals()['x1'])
Fun()
print('global variable :',x1)

# global variable: 10
# Enclosing variable: 20
# local variable : 50
# Enlcosing variable: 50
# global variable 10
# global variable : 10