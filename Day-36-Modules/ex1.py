# from module1 import Addition,Subtraction,Multiplication,Division

# * this indicate all
from module1 import *
x = int(input('Enter 1st number:'))

y = int(input('Enter 2nd number:'))


num = int(input('Enter 1 is addition:, enter 2 is subtraction:..?,Enter 3 is multiplication:,Enter 4 is division:' ))

if num==1:
    print(Addition(x,y))

elif num == 2:
    print(Subtraction(x,y))

elif num==3:
    print(Multiplication(x,y))


elif num==4:
    print(Division(x,y))


else:
    print('You have enterd wrong input')

# Enter 1st number:12
# Enter 2nd number:13
# Enter 1 is addition:, enter 2 is subtraction:..?,Enter 3 is multiplication:,Enter 4 is division:3
# 156
