# pop()	Removes the element with the specified key
cars = {'wurv':12000,'rangerover':30000,'buggati':600000,'landrover':4000,'innova':80000,'thor':60000}

print(cars)
# {'wurv': 12000, 'rangerover': 30000, 'buggati': 600000, 'landrover': 4000, 'innova': 80000, 'thor': 60000}
# cars.pop()
# print(cars)
# TypeError: pop expected at least 1 argument, got 0

# Sy:pop(key)
cars.pop('landrover')
print(cars)
# {'wurv': 12000, 'rangerover': 30000, 'buggati': 600000, 'innova': 80000, 'thor': 60000}

cars.pop('wurv')
print(cars)
# {'rangerover': 30000, 'buggati': 600000, 'innova': 80000, 'thor': 60000}

cars.pop('buggati')
print(cars)
# {'rangerover': 30000, 'innova': 80000, 'thor': 60000}

cars.pop('mahindra')
print(cars)
# KeyError: 'mahindra'