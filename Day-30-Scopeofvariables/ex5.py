
# how to get global variable to the inside of class

x1 = 10
print('global v:',x1)

def Same():
    x1 = 20
    print('local v:',x1)
    print('global v:',globals()['x1'])

Same()
print('global v:',x1)

# global v: 10
# local v: 20
# global v: 10
# global v: 10
