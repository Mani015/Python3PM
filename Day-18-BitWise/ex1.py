# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal,
# but if they are actually the same object, with the same memory location:


# 1).is=Returns True if both variables are the same object
# 2).is not = Returns True if both variables are not the same object

x1 = [1,2,3,4,5,6]
x2 = [1,2,3,4,5,6,1]

# print(x1==x2)
# True

x3=x1
# print(x1 is x3)
# True
x3=x2
# print(x3 is x2)
# True


# is not
# # 2).is not = Returns True if both variables are not the same object
y1 = (1,2,3,4,5)
y2=(1,2,3,4,5,6,7)

y3=y2

# print(y2==y3)
# True

# print(y2 is not y1)


# print(y2 is not y3)
# False