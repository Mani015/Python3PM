# Transfer statements
# In Python, transfer statements are used to alter the program’s way of execution in a certain manner.
# For this purpose, we use three types of transfer statements.


# break:	Terminate the current loop. Use the break statement to come out of the loop instantly.

# The break statement is used inside the loop to exit out of the loop. In Python,
# when a break statement is encountered inside a loop, the loop is immediately terminated,
# and the program control transfer to the next statement following the loop.
x = [1,2,3,4,5,6,7,8,9,10]


for i in x:
    if i==7:
        break
    print(i)
# 1
# 2
# 3
# 4
# 5
# 6