

def Numbers():
    yield 10
    yield 20
    yield 30
    yield 40
    yield 50

# x1 = Numbers()
#
# for i in x1:
#     print(i)
# 10
# 20
# 30
# 40
# 50


def Fun():
    i = 0
    k = 0
    while i<=10:
        k1 = k**2
        yield k1
        i+=1
        k+=1

ob1 = Fun()
for i in ob1:
    print(i)

# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
