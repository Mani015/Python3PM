
# Protected Member
# Protected members are accessible within the class and also available to its sub-classes.
# To define a protected member, prefix the member name with a single underscore _.
#
# Protected data members are used when you implement inheritance and want to allow data members access to only child classes.


class Parent:
    def __init__(self,Pname,Psalary):
        self._name = Pname
        self._salary = Psalary
        # print(self._name,self._salary)
    def _protectedmethod(self):
        print('I am protected method')
class Child(Parent):
    def _protectedmethod(self):
       print(self._name,self._salary)


# x1 = Parent('Devi',50000)
# x1._protectedmethod()
# Devi 50000
# I am protected method

x2 = Child('devi',50000)
x2. _protectedmethod()
# devi 50000
# devi 50000