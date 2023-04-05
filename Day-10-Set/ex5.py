# add(): add method takes exactly one argument

z1 ={22,33,44,55,66,77,88,99,11,10,12,13,45}
print(z1)
# {33, 66, 99, 10, 11, 44, 77, 12, 13, 45, 22, 55, 88}

z1.add(100)
print(z1)
# {33, 66, 99, 100, 10, 11, 44, 77, 12, 13, 45, 22, 55, 88}

z1.add('python','java')
print(z1)
# TypeError: set.add() takes exactly one argument (2 given)



