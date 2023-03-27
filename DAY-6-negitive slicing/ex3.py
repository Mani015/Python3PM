# Negitive slicing using ending and starting


x = [1,2,3,4,5,6,7,8,9,0,11,22,33,44,55,66]
# Sy: variable name[endingvalue : starting value]


print(x[-5:-1])
# [22, 33, 44, 55]

print(x[-6:-2])

# [11, 22, 33, 44]


print(x[-10:-1])
# [7, 8, 9, 0, 11, 22, 33, 44, 55]


print(x[-15:-10])
# [2, 3, 4, 5, 6]

print(x[-16:-4])

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 22]

print(x[:])
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 22, 33, 44, 55, 66]




