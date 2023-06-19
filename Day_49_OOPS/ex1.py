# ABSTRACTION:
# Abstraction is used to hide the internal functionality of the function from the users.
# The users only interact with the basic implementation of the function,
# but inner working is hidden.
# User is familiar with that "what function does" but they don't know "how it does".




class Car:
    def mileage(self):
        pass

class Tesla:
    def mileage(self):
        print("The mileage is 30kmph")

class Suzuki:
    def mileage(self):
        print("The mileage is 25kmph")

class Renault:
    def mileage(self):
        print("The mileage is 28kmph")

T = Tesla()
T.mileage()

S = Suzuki()
S.mileage()

R = Renault()
R.mileage()