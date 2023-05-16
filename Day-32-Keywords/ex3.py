

x1 = 10
print('global variable:',x1)
# global variable: 10
def Fun():
    global x1
    x1 = 20
    print('Enclosing variable:',x1)
    def InnerFunction():
        x1 = 30
        print('local variable :',x1)
    InnerFunction()
    print('Enlcosing variable:',x1)
    print('global variable',globals()['x1'])
Fun()
print('global variable :',x1)
# global variable :20


# global variable: 10
# Enclosing variable: 20
# local variable : 30
# Enlcosing variable: 20
# global variable 20
# global variable : 20