count = 0
attempts = 4

while count < attempts:
    password = int(input('Enter your password:'))
    if password==4455:
        print('screen is open')
        break
    count+=1
    print(count,'st complete')
else:
    print('No more attempts')

# Enter your password:55
# 1 st complete
# Enter your password:54
# 2 st complete
# Enter your password:4455
# screen is open