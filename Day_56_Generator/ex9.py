# using yield keyword

# def Table(x):
#     print(x, 'Table start:')
#     for i in range(1,11):
#         yield f'{x} x {i} = {x*i}'
#
#
# ob1 = Table(x = int(input('Enter one number:')))
#
# for k in ob1:
#     print(k)


# 9 Table start:
# 9 x 1 = 9
# 9 x 2 = 18
# 9 x 3 = 27
# 9 x 4 = 36
# 9 x 5 = 45
# 9 x 6 = 54
# 9 x 7 = 63
# 9 x 8 = 72
# 9 x 9 = 81
# 9 x 10 = 90



# using return keyword


def Table(x):
    print(x, 'Table start:')
    for i in range(1,11):
        return f'{x} x {i} = {x*i}'


ob1 = Table(x = int(input('Enter one number:')))

for k in ob1:
    print(k,end='')

# Enter one number:8
# 8 Table start:
# 8 x 1 = 8




# Memory Efficient
# A normal function to return a sequence will create the entire sequence in memory before returning the result. This is an overkill, if the number of items in the sequence is very large.
#
# Generator implementation of such sequences is memory friendly and is preferred since it only produces one item at a time.