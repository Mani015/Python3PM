
# 2). Passing Function as an Argument in Python


def Squre(num):
    return num**2

def Cube(num):
    return num**3

def New_Behaviour(func):
    print(func(2))

# New_Behaviour()
# TypeError: New_Behaviour() missing 1 required positional argument: 'func'
New_Behaviour(Squre)  # 4
New_Behaviour(Cube) # 8
