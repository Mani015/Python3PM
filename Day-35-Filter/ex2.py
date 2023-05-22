# Reduce:
from functools import reduce
def REDUCE(x,y):
    return x+y


k = [1,2,3,4,5,6,7,8,9,0,1,2,3,2,44,56,90]

r1 = reduce(REDUCE,k)
# print(r1)
# 243

# using lambda :

print(reduce(lambda x,y: x+y , range(1,11)))
# 55
