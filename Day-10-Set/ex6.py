

z1 ={22,33,44,55,66,77,88,99,11,10,12,13,45,[1,2,3,4,5,6]}
print(z1)


z1.update({'python','java','html'})
# print(z1)
# {33, 66, 99, 10, 11, 44, 77, 12, 13, 45, 22, 55, 88}
# {33, 66, 99, 'python', 10, 11, 44, 77, 12, 13, 45, 22, 55, 88, 'html', 'java'}

z1.update({'hari'})
# print(z1)
# {'java', 33, 66, 99, 'python', 10, 11, 44, 77, 12, 13, 45, 'html', 'hari', 22, 55, 88}

x = [1,2,3,4,5,6]

# z1.add(x)
# print(z1)
# TypeError: unhashable type: 'list'

