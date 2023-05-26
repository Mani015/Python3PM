
def Recursion(i):
    if i==1:
        return 1
    else:
        return i + Recursion(i-1)
i = int(input('Enter a one number:'))

print(Recursion(i))
# Enter a one number:10
# 55

