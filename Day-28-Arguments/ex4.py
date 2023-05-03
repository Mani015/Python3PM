


def Variable_Length(*py):
    x = py
    return list(x)

# print(Variable_Length(1,2,3,4,5,6,7,8,9,10,11,12,13))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


# sum of 1st 10 numbers using variable lenght arguments


def Sum_VLA(*num):
    x = list(num)
    return sum(x)
print(Sum_VLA(1,2,3,4,5,6,7,8,9,10))
# 55


def addition(*numbers):
    total = 0
    for no in numbers:
        total = total + no
    print("Sum is:", total)


# 0 arguments
addition()

# 5 arguments
addition(10, 5, 2, 5, 4)

