

def f1(num):
    x1 = num
    return x1()
@f1
def f2():
    return 20

print(f2)
# 20

@f1
def f3():
    return 30
print(f3)
# 30


