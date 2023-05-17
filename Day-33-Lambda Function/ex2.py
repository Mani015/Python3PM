# User input method



x = int(input('Enter 1st number :'))
y = int(input('Enter 2nd number:'))

print((lambda x,y : x+y)(x,y))

print((lambda x,y : x-y)(x,y))
print((lambda x,y : x*y)(x,y))
print((lambda x,y : x/y)(x,y))
print((lambda x,y : x//y)(x,y))
# Enter 1st number :20
# Enter 2nd number:15
# 35
# 5
# 300
# 1.3333333333333333
# 1

