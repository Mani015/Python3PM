
x = [1,2,3,4,5,6,7,8,9,10]

# for i in x:
#     print(i*i)

# Function with map()
# The map() function in Python takes in a function and a list as an argument.
# The function is called with a lambda function and a list and a new list is returned which contains all the lambda modified items returned by that function for each item.


# Sy:
# map(function_Name,iterable/sequence of values)


def Square(i):
    return i**2

m1 = map(Square,x)
# print(m1)
# <map object at 0x0000022C1E28ADC0>
# print(list(m1))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# print(tuple(m1))
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print(set(m1))
# {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}


