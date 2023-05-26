
def Fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1

    else:
        return (Fibonacci(num-1) + Fibonacci(num-2))
num = int(input('Enter one number:'))

print('Fibinacci Start:')

for i in range(0,num):
    print(Fibonacci(i),end= ' ')
# Enter one number:10
# Fibinacci Start:
# 0 1 1 2 3 5 8 13 21 34

