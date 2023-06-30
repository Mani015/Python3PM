#Passing Function as an Argument in Python
# Similar to assigning functions to variables, we can also pass functions as arguments to other functions.
# The functions which accept the arguments are called higher-order functions.
def Fun1(x):
    return 'square of :',x**2

def Fun2(y):
    return 'cube of:',y**3


def Calling_Fun(mainfunction):
    print(mainfunction(24))

Calling_Fun(Fun1)
# ('square of :', 576)

Calling_Fun(Fun2)

# ('cube of:', 13824)
