# Python Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:

#' & ' 	AND	(Sets each bit to 1 if both bits are 1)	x & y


a=10
b=20
print(a&b)
#0


print(True & True)
#  1 & 1 =1
print(False & True)
#  0 & 1 =0
print(True & False)
#  1 & 0 = 0
print(False & False)
#  0 & 0 = 0

# True
# False
# False
# False

# a=10 --> 0 1 0 1 0
# b=20 --> 1 0 1 0 0
#          -----------  we are applying & condition
#          0 0  0  0  0


print(25&94)
# 24
print(37&77)
# 5
print(64&102)
# 64