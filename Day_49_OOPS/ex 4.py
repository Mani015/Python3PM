# Concrete classes contain only concrete (normal)methods whereas abstract classes may contain both concrete methods and abstract methods. The concrete class provides an implementation of abstract methods,
# the abstract base class can also provide an implementation by invoking the methods via super().

from abc import ABC ,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def motor(self):
        pass
    @abstractmethod
    def tyre(self):
        pass
    def concreate(self):
        print('this is EV car')
class Tesla(vehicle):
    def motor(self):
        print("the car name is volvo")
    def tyre(self):
        print('Car is 4 wheels vehicle')
class TATA(vehicle):
    def motor(self):
        print("the tata motor massy Ferguson")
    def tyre(self):
        print('Car is 4 wheels vehicle')
    def concreate(self):
        print('seat is 4*2')
        super().concreate()

# ob1 = Tesla()
# ob1.motor()
# ob1.tyre()
# ob1.concreate()

# the car name is volvo
# Car is 4 wheels vehicle
# this is EV car

ob2 = TATA()
ob2.tyre()
ob2.motor()
ob2.concreate()
# Car is 4 wheels vehicle
# the tata motor massy Ferguson
# this is EV car



# Car is 4 wheels vehicle
# the tata motor massy Ferguson
# seat is 4*2
# this is EV car
