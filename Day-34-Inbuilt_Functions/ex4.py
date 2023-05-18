
# print(map(lambda i : i%2==0,[11,3,4,2,5,66,77,88,56,45,34,23,12]))
# <map object at 0x000002023B03ADC0>


print(list(map(lambda i : i%2==0,[11,3,4,2,5,66,77,88,56,45,34,23,12])))

print(set(map(lambda i : i%2==0,[11,3,4,2,5,66,77,88,56,45,34,23,12])))

x = [1,2,3,4,5,4,3,2,3,4,5,6,7,8,7,5,6,7,8,10]
print(set(x))

# [False, False, True, True, False, True, False, True, True, False, True, False, True]
# {False, True}
# {1, 2, 3, 4, 5, 6, 7, 8, 10}

