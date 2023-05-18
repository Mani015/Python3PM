#Filter out all odd numbers using filter() and lambda function
# Here, lambda x: (x % 2 != 0) returns True or False if x is not even.
# Since filter() only keeps elements where it produces True, thus it removes all odd numbers that generated False.


# syntax:
# filter(function_name,iterable)


def even(x):
    if x%2==0:
        return x


f1 = filter(even,[1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,10])
# print(tuple(f1))
# (2, 4, 6, 8, 10, 22, 44, 10)


# using lambda

print(tuple(filter(lambda x: x%2==0,range(11))))
# (0, 2, 4, 6, 8, 10)