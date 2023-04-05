# SET:

# In Python, a Set is an unordered collection of data items that are unique. In other words,
# Python Set is a collection of elements (Or objects) that contains no duplicate elements.
# It is denoted by curly braces/ flower braces

s = {}
# print(type(s))
# <class 'dict'>

s1  = {1}
# print(type(s1))
# <class 'set'>

# unordered collection of data

x = {1,2,3,4,'a','b','c','d','e',12.0,36.20,"apple"}
print(x)
# {(5+6j), 1, 2, 3, 4, 36.2, 12.0, 'c', 'a', 'apple', 'b', 'e', 'd'}
print()
y = [1,2,3,4,5,6,7,8,9]
print(y)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]




#
# In Python, a Set is an unordered collection of data items that are unique. In other words, Python Set is a collection of elements (Or objects) that contains no duplicate elements.
#
# Unlike List, Python Set doesn’t maintain the order of elements, i.e., It is an unordered data set. So you cannot access elements by their index or perform insert operation using an index number.
#
# In this tutorial, we will learn Set data structure in general, different ways of creating them, and adding, updating, and removing the Set items. We will also learn the different set operations.
#
# Also See:
#
# Python Set Exercise
# Python Set Quiz
#
# Python Sets
# Python Sets
# Characteristics of a Set
#
# A set is a built-in data structure in Python with the following three characteristics.
#
# Unordered: The items in the set are unordered, unlike lists, i.e., it will not maintain the order in which the items are inserted. The items will be in a different order each time when we access the Set object. There will not be any index value assigned to each item in the set.
# Unchangeable: Set items must be immutable. We cannot change the set items, i.e., We cannot modify the items’ value. But we can add or remove items to the Set. A set itself may be modified, but the elements contained in the set must be of an immutable type.
# Unique: There cannot be two items with the same value in the set.

