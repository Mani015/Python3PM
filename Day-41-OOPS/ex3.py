# To calling a Attributes using class name

class Lap_Top:
    lapBrand = 'HP'
    lapPrice = 50000
    lapColor = 'Black'

Lap_Top()
# Syntax: class_Name.Attribute1

print(Lap_Top.lapBrand)
# HP
print(Lap_Top.lapPrice)
# 50000
print(Lap_Top.lapColor)
# Black

# print(Lap_Top.Processor)
# AttributeError: type object 'Lap_Top' has no attribute 'Processor'

x = 10
# print(y)
# NameError: name 'y' is not defined



