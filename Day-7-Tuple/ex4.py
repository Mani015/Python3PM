
t2 = (1,2,3,4,5,6,7,8,9,1,2,3,4,5,11,22,33,44,4,6,'mango','cherry',1+2j,)

# objectname.index(value, start, stop)
print(t2.index(1))
# 0

print(t2.index(1,2,10))
# 9

print(t2.index(2))
# 1

print(t2.index(2,2,20))
# 10

print(t2.index(3))
# 2

print(t2.index(3,3,20))
# 11

print(t2.index(4))
# 3

print(t2.index(4,4,20))
# 12

print(t2.index(5))
# 4

print(t2.index(5,5,20))
# 13
