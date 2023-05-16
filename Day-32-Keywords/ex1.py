#Global Keyword in Function
# In Python, global is the keyword used to access the actual global variable from outside the function.
# we use the global keyword for two purposes:

# To declare a global variable inside the function.
# Declaring a variable as global, which makes it available to function to perform the modification.

# x1 = 10
# print('global variable:',x1)
#
# def Fun():
#     x2 = 20
#     print('local variable:',x2)
# Fun()
# global variable: 10
# local variable: 20



x1 = 10
print('global variable:',x1)
# global variable: 10
def Fun():
    global x1
    x1 = 20
    print('local variable:',x1)
#     local variable: 20
Fun()
print('global variable :',x1)
# global variable : 20
