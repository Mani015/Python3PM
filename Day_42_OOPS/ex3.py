

class Dog:
    name = 'Abc'
    age = 10
    color = 'red'

d1 = Dog()
print(d1.name,d1.age,d1.color)
# creating New variable name:
# sy: objectname.New attributename = new value
d1.breed = 'German'
print(d1.breed)
print()
d2 = Dog()
d2.price = 20000
print(d2.price)

# print(d1.price)
# AttributeError: 'Dog' object has no attribute 'price'

Dog.Weight = 40
print(Dog.Weight)
# 40

print()

