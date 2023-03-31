# Nested list

# A list contained with in a another list

x = [1,2,3,4,5,6]
# print('this is normal ist:',x)

# this is normal ist: [1, 2, 3, 4, 5, 6]


y = [11,22,33,44,[22,33,44,55],10,20,30,[2,3,4,5,6],21,22,23]
#     0, 1,2,  3, ----4-------, 5, 6, 7,-----8-----,9 ,10, 11

print('Nested list:',y)
# Nested list: [11, 22, 33, 44, [22, 33, 44, 55], 10, 20, 30, [2, 3, 4, 5, 6], 21, 22, 23]


print(y[0])
# 11
print(y[1])
# 22
print(y[2])
# 33
print(y[3])
# 44
print(y[4])
# 22,33,44,55

print(y[5])
# 10
print(y[6])
# 20
print(y[7])
30
print(y[8])
2,3,4,5,6
print(y[9])
21
print(y[10])
# 22
print(y[11])
23
