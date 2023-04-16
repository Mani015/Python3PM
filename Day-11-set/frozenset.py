# Frozen set:
# Python frozenset() Method creates an immutable Set object from an iterable.
# It is a built-in Python function.
# As it is a set object therefore we cannot have duplicate values in the frozenset.

x= {1,2,3,4,5,6,7,8}
print(type(x))
# <class 'set'>

y = frozenset(x)
print(type(y))
# <class 'frozenset'>


z = y.copy()
print(type(z))
# <class 'frozenset'>



