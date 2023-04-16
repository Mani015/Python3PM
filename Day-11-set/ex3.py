# UNION: Two adding the both sets
x1 = {11,22,33,44,55,66,77,88,99,1,2,3,4,5,6}

x2 = {11,22,33,44,55,66,77,88,99,'mango','mango1','lemon'}

print(x1.union(x2))

print(x2.union(x1))

# {1, 2, 66, 3, 4, 5, 6, 11, 77, 'lemon', 22, 'mango', 88, 33, 99, 44, 'mango1', 55}
# {1, 66, 2, 3, 4, 5, 6, 11, 77, 'lemon', 22, 'mango', 88, 33, 99, 44, 'mango1', 55}
