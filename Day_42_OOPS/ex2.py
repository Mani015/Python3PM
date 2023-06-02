
class Mobile:
    name = 'lava'
    price = 20000
    color = 'black'

ob1 = Mobile()
print(ob1.price,ob1.color,ob1.name)
#20000 black lava
ob1.price = 30000
print(ob1.price)

ob2 = Mobile()
print(ob2.price,ob2.color,ob2.name)
# 20000 black lava
ob2.price = 25000
print(ob2.price)

# Updating Attribute value using by class name:
# classname.AttributeName = NewValue

# Mobile.price = 99999
#
# print(ob1.price)
