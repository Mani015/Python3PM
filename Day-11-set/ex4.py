# Intersection:both sets to return Common values

x1 = {11,22,33,44,55,66,77,88,99,1,2,3,4,5,6}

x2 = {11,22,33,44,55,66,'mango','mango1','lemon'}

print(x1.intersection(x2))
# {33, 66, 11, 44, 22, 55}
print(x2.intersection(x1))
# {33, 66, 11, 44, 22, 55}
