
# What is self in Python?
# In object-oriented programming, whenever we define methods for a class,
# we use self as the first parameter in each case.

# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.

class Bottle:
    Bottlename = 'Bisleri'
    BottleColor = 'White'
    def Purpose(self):
        print('To Store the Water')

B1 = Bottle()
print(B1.Bottlename,B1.BottleColor)
# Bisleri White

# To calling method using class name:
# Syntax:className.MethodNAme()

# Bottle.Purpose()
# TypeError: Purpose() missing 1 required positional argument: 'self'


Bottle.Purpose(B1)

# Bisleri White
# To Store the Water
