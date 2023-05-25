
# Interpreter capacity:
#  import sys
# # sys:The sys modules provieds accesss to the system specific parameter and function
import sys

s1 = sys.getrecursionlimit()
print('Capacity of interpreter:',s1)
# Capacity of interpreter: 1000



i=1

def Recursive():
    global i
    print('function__!',i)
    i = i+1
    Recursive()
Recursive()