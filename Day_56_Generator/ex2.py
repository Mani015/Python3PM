

x = [1,2,3,4,5,6,7,8,9,10]

y = map(lambda i:i**2,x)

# print(y)
# <map object at 0x000001E3850CB160>
# print(list(y))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# next method access next values
# print(next(y))
# # 1
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# StopIteration



for i in range(1,11):
    print(next(y))

# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100