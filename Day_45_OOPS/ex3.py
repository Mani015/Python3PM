# To deleteting the class variable by using instance method
# del self.classvariable
class Bike(object):
    Bike_name = 'Royal Enfield'
    Bike_Price = 200000

    def Deletingclassvariable(self):
        del self.Bike_Price

ob1 = Bike()
print(ob1.Bike_name)
# Royal Enfield

print(ob1.Bike_Price)
# 2000000

ob1.Deletingclassvariable()
print(ob1.Bike_Price)
# AttributeError: Bike_Price
