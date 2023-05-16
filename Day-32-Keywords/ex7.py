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
        def belofunction():
            global x1
            x1 = 100
            print('local varaible:',x1)
        belofunction()
        print('1st enclosing variable :',x1)
    InnerFunction()
    print('Enlcosing variable:',x1)
    print('global variable',globals()['x1'])
Fun()
print('global variable :',x1)

# global variable: 10
# Enclosing variable: 20
# local variable : 50
# local varaible: 100
# 1st enclosing variable : 50
# Enlcosing variable: 50
# global variable 100
# global variable : 100