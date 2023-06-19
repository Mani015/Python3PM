



from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass

class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph")


class Renault(Car):
    def mileage(self):
        print("The mileage is 28kmph")


T = Tesla()
T.mileage()

S = Suzuki()
S.mileage()

R = Renault()
R.mileage()