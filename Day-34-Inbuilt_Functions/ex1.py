# if else using lambda function:

# Max = lambda a, b: a if (a > b) else b

# print(Max(1, 2)



a = 10
if a%2==0:
    print('even number')
else:
    print('odd number')



print((lambda a:('even number') if a%2==0 else 'odd number')(10))


