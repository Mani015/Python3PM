#the Keys in Dictionaries should be unique.

x = {1:'one',2:'two',3:'three',4:'four',5:'five',1:'number_one',2:'number_two'}
print(x)
# {1: 'number_one', 2: 'number_two', 3: 'three', 4: 'four', 5: 'five'}

y = {'one':1,'two':2,'three':3,'four':4,'two':22}
print(y)
# {'one': 1, 'two': 22, 'three': 3, 'four': 4}


# Values are duplicate:

z = {'mango':'fruit','banana':'fruit','orange':'fruit','cheery':'fruit'}

print(z)
# {'mango': 'fruit', 'banana': 'fruit', 'orange': 'fruit', 'cheery': 'fruit'}


