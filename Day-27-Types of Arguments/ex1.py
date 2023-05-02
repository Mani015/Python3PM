# Python Function Arguments
# The argument is a value, a variable, or an object that we pass to a function or method call. In Python, there are four types of arguments allowed.

# Positional arguments
# keyword arguments
# Default arguments
# Variable-length arguments


# Positional Arguments

# Positional arguments are arguments that are pass to function in proper positional order.
# That is, the 1st positional argument needs to be 1st when the function is called.
# The 2nd positional argument needs to be 2nd when the function is called, etc.



def Fun(x):
    print(' fucntion')
    print(' x  value is:',x)

# Fun()
# TypeError: Fun() missing 1 required positional argument: 'x'
Fun(10)
#  fucntion
#  x  value is: 10
