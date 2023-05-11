x1 = 10
print('global v:',x1)

def Same():
    x1 = 20
    print('local v:',x1)
    print('global v:',globals()['x1']+x1)

Same()
print('global v:',x1)
# global v: 10
# local v: 20
# global v: 30
# global v: 10
