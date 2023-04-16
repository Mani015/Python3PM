# isdisjoint

# x1 = {1,2,3,4,5,6,7,8,9,10}
#
# x2 = {11,22,33,44,55,66,'mango','mango1','lemon'}

# print(x1.isdisjoint(x2))

# True



x1 = {1,2,3,4,5,6,7,8,9,10,11}

x2 = {22,33,44,55,66,'mango','mango1','lemon'}
print(x1.isdisjoint(x2))

# False

print(x2.isdisjoint(x1))
# True

