
# Keys Are unique:

# Unique: As mentioned above, each value has a Key; the Keys in Dictionaries should be unique.
# If we store any value with a Key that already exists,
# then the most recent value will replace the old value.

a = {1:'one',2:'two',3:'three',4:'four',5:'five'}
print(a)
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

print('keys of :',a.keys())
# keys of : dict_keys([1, 2, 3, 4, 5])

print('values of :',a.values())
# values of : dict_values(['one', 'two', 'three', 'four', 'five'])
