# fromkeys()	Returns a dictionary with the specified keys and value
d1 = {1:'one',2:'two'}
print(d1)
# {1: 'one', 2: 'two'}

d2 = {1,2,3,4,5}
d3 = 'int'
x = d1.fromkeys(d2,d3)
print(x)
# {1: 'int', 2: 'int', 3: 'int', 4: 'int', 5: 'int'}

