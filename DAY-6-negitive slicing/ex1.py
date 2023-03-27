# Negitive slicing:

x = [1,2,3,4,5,6,7,8,9,0,11,22,33,44,55,66]
# sy: variable name[ending value: starting value]

# without staring negitve value
print(x[-10:])
# [7, 8, 9, 0, 11, 22, 33, 44, 55, 66]

print(x[-5:])
# [22, 33, 44, 55, 66]

print(x[-12:])
# [5, 6, 7, 8, 9, 0, 11, 22, 33, 44, 55, 66]
print(x[-15:])
# [2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 22, 33, 44, 55, 66]


print(x[-18:])
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 22, 33, 44, 55, 66]

# print(x[-18])
# IndexError: list index out of range

print(x[-1])
# 66
