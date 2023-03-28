
# What is a Tuple
# Tuples are ordered collections of heterogeneous data that are unchangeable.
# Heterogeneous means tuple can store variables of all types.
# It is denoted by paranthesis  '( )'


# Tuple is immutable datatype: phonenumber , Adharcardnumber,Pan card number , vechile number,
# 6987542103




# Ordered: Tuples are part of sequence data types, which means they hold the order of the data insertion. It maintains the index value for each item.
# Unchangeable: Tuples are unchangeable, which means that we cannot add or delete items to the tuple after creation.
# Heterogeneous: Tuples are a sequence of data of different data types (like integer, float, list, string, etc;) and can be accessed through indexing and slicing.
# Contains Duplicates: Tuples can contain duplicates, which means they can have items with the same value

t1 = ()
# print(type(t1))
# <class 'tuple'>

# ordered collections:
# Ordered: Tuples are part of sequence data types,
# which means they hold the order of the data insertion. It maintains the index value for each item.
t2 = (1,2,3,4,5,6,7,8)
# print(t2)
# (1, 2, 3, 4, 5, 6, 7, 8)


# heterogeneous data takes more than one data type:[string, int, bool, complex, float]
# Tuples are a sequence of data of different data types (like integer, float, list, string, etc;)
# and can be accessed through indexing and slicing.
x1 = (1,2,3,'apple','banana','mango',"orange",True,False,2+6j,12.30)
print(x1)
# (1, 2, 3, 'apple', 'banana', 'mango', 'orange', True, False, (2+6j), 12.3)
x2 = (1,2,3,4,5,[1,2,3,4,5])
print(x2)

# (1, 2, 3, 4, 5, [1, 2, 3, 4, 5])


