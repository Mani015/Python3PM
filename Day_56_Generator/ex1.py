
# In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated over.
#
# Generators are useful when we want to produce a large sequence of values,
# but we don't want to store all of them in memory at once.


x = [1,2,3,4,5,6,7,8,9,10]
# print(x)
# [1,2,3,4,5,6,7,8,9,10]
import sys

print(sys.getsizeof(x))
# 152

# for i in range(1,11):
#     print(x)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sys.getsizeof(range(1,11)))
# 48
