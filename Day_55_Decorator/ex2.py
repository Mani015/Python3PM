

# Nested Function:

# Function Returning Another Function in Python
# Python also allows us to define a function that returns another function.

def Main_Fun(x):
    def Next_Fun(y):
        return x + y
    return Next_Fun

ob1 = Main_Fun(10)
ob2 = ob1(12)
print(ob2)
# 22



# def m1(x):
#     return x
#
# ob1 = m1(19)
# x = ob1
# print(x+2+4)





# Nested Functions in Python
# The Python language lets us create a function within another function.
# These enclosed functions are called nested functions

def math():
    def square(num):
        return num**2
    print(square(2))
math()





# Non-local Variable and Closure in Python
# A nested function is one that is defined inside another function. The variables of the enclosing scope can be accessed by nested functions. These variables are called non-local variables.
#
# By default, non-local variables are read-only. To modify them, we need to use a keyword called nonlocal.
#
# Closure Functions are nested functions that can access non-local variables.
#
# Example of non-local variable and closure function in Python
#
# def math(num):
#     def square():
#         return num**2
#     print(square())
# math(2)

#