# Set is doesn't allows duplicate values/set items are unique
s1 = {1,2,3,4,5,6,True,2,3}
# print(s1)
# {1, 2, 3, 4, 5, 6}


s2 = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}
# print(s2)
# {0}

# list allows a duplicate values
s3 = [1,2,3,4,5,6,7,8,9,1,2,3,'hari','suri','hari']

print('list is :',s3)
# list is : [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 'hari', 'suri', 'hari']
# Type conversion:

s4 = set(s3)
print('set is :',s4)
# set is : {'hari', 1, 2, 3, 4, 5, 6, 7, 8, 9, 'suri'}



