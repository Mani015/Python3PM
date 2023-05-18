


def func(n):
    return n+1

m2 = map(func,[1,2,3,4,5,6,7,8,9,0,11])
# print(list(m2))
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 12]





# using lambda

x2 = map(lambda x:x**2,range(11))
print(list(x2))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

