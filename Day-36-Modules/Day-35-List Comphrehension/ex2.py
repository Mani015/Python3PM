
# Using If condtion
# syntax: [expression for value in iterable if condtion]


x1 = [1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,66]

print([k for k in x1 if k%2==0])
# [2, 4, 6, 8, 10, 22, 44, 66]



# if else
# syntax: [expression if condtion else condtion for value in iterable ]

print([i if i%2==0 else i+1 for i in range(1,11)])
# [2, 2, 4, 4, 6, 6, 8, 8, 10, 10]
