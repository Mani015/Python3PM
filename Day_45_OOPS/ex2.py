# TO accessing the class variables using object
class Bike(object):
    Bike_name = 'Royal Enfield'
    Bike_Price = 200000
    def Method1(self):
        print('Class variable are declared inside of class to accessing the object ')


R1 = Bike()
# objectname.classvariable

print(R1.Bike_name,R1.Bike_Price)
R1.Method1()
# Royal Enfield 200000
# Class variable are declared inside of class to accessing the object
