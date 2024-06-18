# Type conversion or Casting
# Number Type Conversion
# Python allows the conversion of data from one type to another in two ways.
#
# Implicit type conversion
# Explicit type conversion
#
# Implicit Type Conversion
# In the case of two compatible data types, Python performs the type conversion implicitly.
#  Compatible data types are in general two numeric data types like int and float.
# It will convert the smaller data type to larger one to prevent any data loss. For eg.; int data will be converted to float.
#
# But, if we try to perform some operations between a string and int types then it will throw Type error.

a = 10
print(type(a))
# <class 'int'>
b = 12.30
print(type(b))
# <class 'float'>

c = a + b
print(type(c))
# <class 'float'>


x = 3.45 # --->  FLoat
y = 2+5j # ---> Complex
z = x + y
print(z)
print(type(z))
# (5.45+5j)
# <class 'complex'>

