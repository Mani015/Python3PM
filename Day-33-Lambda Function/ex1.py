
# Lambda : A lambda function can take any number of arguments , but can have only one expression
# lambda fucntion is single line fucntion/code , we called as a anonymous

x = 10
y = 20
# print(' x is the address of :',x)
# print(' y is the address of :',y)
# x is the address of : 10
#  y is the address of : 20

# print(x+y)
# 30


# syntax:lambda arguments : expression

print((lambda x,y:x+y)(10,20))
print((lambda a,b:a*b)(2,3))
print((lambda a,b:a-b)(2,3))
print((lambda a,b:a/b)(2,3))

# 30
# 6
# -1
# 0.6666666666666666
