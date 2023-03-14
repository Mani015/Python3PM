# list is a mutable datatype:
# Mutable: The elements of the list can be modified. We can add or remove items to the list after it has been created.


list1 = [1,2,3,4,5,6]
print(list1)
# [1, 2, 3, 4, 5, 6]

# adding the data

# append method:append method it has taken a value /data it adding the end of the current list
# sy: variablename . add(value/data)

list1.append(7)
print(list1)
# [1, 2, 3, 4, 5, 6, 7]

list1.append(8)
print(list1)
# [1, 2, 3, 4, 5, 6, 7, 8]

list1.append(9)
print(list1)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


list1.append(10,'ab','c','d')
print(list1)
# TypeError: list.append() takes exactly one argument (4 given)