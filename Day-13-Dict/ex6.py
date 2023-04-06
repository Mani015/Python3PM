# popitem()	Removes the last inserted key-value pair
cars = {'wurv':12000,'rangerover':30000,'buggati':600000,'landrover':4000,'innova':80000,'thor':60000}

print(cars)
#  {'wurv':12000,'rangerover':30000,'buggati':600000,'landrover':4000,'innova':80000,'thor':60000}

# cars.popitem('wurv')
# print(cars)
# TypeError: dict.popitem() takes no arguments (1 given)


cars.popitem()
print(cars)
# {'wurv': 12000, 'rangerover': 30000, 'buggati': 600000, 'landrover': 4000, 'innova': 80000}

cars.popitem()
print(cars)
# {'wurv': 12000, 'rangerover': 30000, 'buggati': 600000, 'landrover': 4000}

cars.popitem()
print(cars)
# {'wurv': 12000, 'rangerover': 30000, 'buggati': 600000}

