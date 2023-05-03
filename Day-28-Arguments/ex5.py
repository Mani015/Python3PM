# Keyword arguments :

# In Python, sometimes, there is a situation where we need to pass multiple numbers of dictionary values to the function.
# Such types of arguments are called Keyword-variable-length arguments.
# We can declare a Keyword-variable-length argument with the ** (asterisk) symbol.

def Kwargs(**Dict):
    print(Dict)
    print(type(Dict))


# Kwargs()
# <class 'dict'>

Kwargs(a=1,b=2,c=3)
# {'a': 1, 'b': 2, 'c': 3}

