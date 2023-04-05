
# remove()
s1 = {1,2,3,4,5,6,7}
print(s1)
#{1, 2, 3, 4, 5, 6, 7}

s1.remove(2)
# print(s1)
# {1, 3, 4, 5, 6, 7}


s1.remove(1,3)
print(s1)
# TypeError: set.remove() takes exactly one argument (2 given)