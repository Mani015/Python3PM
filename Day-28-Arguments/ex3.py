# Variable-length Arguments
# In Python, sometimes, there is a situation where we need to pass multiple numbers of arguments to the function.
# Such types of arguments are called variable-length arguments.
# We can declare a variable-length argument with the * (asterisk) symbol.

#  Using Normal parameters
# def f1(a,b):
#     print(a, b)
# f1(1,2)


def VLA(*python):
    print(python)

# VLA(1,2,3,4,5,6,7,8,9)
# (1, 2, 3, 4, 5, 6, 7, 8, 9)


