
s1 = {1,2,3,4,5,6,7,8,'a','aa','b','d','10'}

s2 = {'apple','mango','orange','melon',11,22,33,44,5}

print(s1.difference(s2))
# {1, 2, 3, 4, 'd', 6, 7, 8, '10', 'a', 'aa', 'b'}
print()
print(s2.difference(s1))
# {33, 11, 'mango', 'melon', 44, 'orange', 22, 'apple'}
