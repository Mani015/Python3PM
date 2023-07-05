import sys
x = [1,2,3,4,5,6,7,8,9,10]

y = map(lambda i:i**2,x)

# print(sys.getsizeof(y))
# 48


print(y.__next__())
print(y.__next__())
print(y.__next__())
print(y.__next__())
print(y.__next__())

# 1
# 4
# 9
# 16
# 25