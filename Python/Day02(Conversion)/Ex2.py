# Explicit Type Conversion
# We can convert data in one type to another explicitly using int(), float(), complex() etc; This is called typecasting

a = 12
print(type(a))
# <class 'int'>
# A integer is convert into float by using   'float()'
b = float(a)
print(type(b))
print(b)
# <class 'float'>
# 12.0

print()
# integer to complex :
a1 = 13
b1 = complex(a1)
print(type(b1))
print(b1)
# <class 'complex'>
# (13+0j)


# complex to int
x1 = 2 + 5j
x2 = int(x1)
print(x2)
# TypeError: can't convert complex to int

