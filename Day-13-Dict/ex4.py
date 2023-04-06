# setdedault()
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

cars = {'wurv':12000,'rangerover':30000,'buggati':600000,'landrover':4000,'innova':80000,'thor':60000}
print(cars)

# {'wurv': 12000, 'rangerover': 30000, 'buggati': 600000, 'landrover': 4000, 'innova': 80000, 'thor': 60000}
# sy:setdefault(key,default)
cars.setdefault('tataindica',5600000)
print(cars)
# {'wurv': 12000, 'rangerover': 30000, 'buggati': 600000, 'landrover': 4000, 'innova': 80000, 'thor': 60000, 'tataindica': 5600000}

cars.setdefault('audi')
print(cars)
# {'wurv': 12000, 'rangerover': 30000, 'buggati': 600000, 'landrover': 4000, 'innova': 80000, 'thor': 60000, 'tataindica': 5600000, 'audi': None}

cars.setdefault('benz')
print(cars)
# {'wurv': 12000, 'rangerover': 30000, 'buggati': 600000, 'landrover': 4000, 'innova': 80000, 'thor': 60000, 'tataindica': 5600000, 'audi': None, 'benz': None}


