# Taking both variable names is same[global and local]


x1 = 10
print('global v:',x1)

def Same():
    x1 = 20
    print('local v:',x1)
    print('global v:', x1)

Same()
print('global v:',x1)
# global v: 10
# local v: 20
# global v: 20
# global v: 10

