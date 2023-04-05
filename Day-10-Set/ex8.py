# Type conversion
a = 10
print(type(a))
# <class 'int'>

b = str(a)
print(type(b))
# <class 'str'>

c =complex(b)
print(c)
print(type(c))
# (10+0j)
# <class 'complex'>

d = int(c)
print(d)
print(type(d))
# TypeError: can't convert complex to int

