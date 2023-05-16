x1 = 10
print('global variable:',x1)
# global variable: 10
def Fun():

    x1 = 20
    print('Enclosing variable:',x1)
    def InnerFunction():
        global x1
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
# Enlcosing variable: 20
# global variable 50
# global variable : 50

