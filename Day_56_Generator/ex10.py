import sys

def Devi(x):
    l1 = []
    for i in range(1,11):
        l1.append(f'{x} x {i} = {x*i}')
    return l1

y1 = Devi(5)
print('size taken return:',sys.getsizeof(y1))
for i in y1:
    print(i)

# size taken return: 184
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
