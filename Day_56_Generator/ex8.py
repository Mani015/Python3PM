
import sys

def Fun():
    i = 0
    k = 0
    while i<=10:
        k1 = k**2
        i += 1
        k += 1
        return k1

ob1 = Fun()
for i in ob1:
    print(i)

# TypeError: 'int' object is not iterable
