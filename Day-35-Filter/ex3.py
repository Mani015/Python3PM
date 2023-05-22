# filter with map


x1 = list(filter(lambda x: x%2==1, range(1,21)))
print(x1)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print(list(map(lambda x: x**2 ,x1)))
# [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]



print()
print(list(map(lambda x: x**2, filter(lambda x: x%2==1 ,range(1,21)))))
# [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]

