
# Access Modifiers in Python
# Encapsulation can be achieved by declaring the data members and methods of a class either as private or protected. But In Python, we don’t have direct access modifiers like public, private, and protected. We can achieve this by using single underscore and double underscores.
#
# Access modifiers limit access to the variables and methods of a class. Python provides three types of access modifiers private, public, and protected.
#
# Public Member: Accessible anywhere from otside oclass.
# Private Member: Accessible within the class
# Protected Member: Accessible within the class and its sub-classes

# Public Member: Accessible anywhere from otside oclass.
# Public data members are accessible within and outside of a class.
# All member variables of the class are by default public.
class Person(object):
    def __init__(self,Pname,Page):
        self.name = Pname
        self.age = Page
        print('name is :',Pname)
        print('age is :',Page)
    def Publicmethod(self):
        print(f'my name is{self.name}, age is :{self.age} ')

class Robo(Person):
    def Publicmethod1(self):
        print(f'my name is{self.name}, age is :{self.age} ')


ob1 = Person('Hari',22)
ob1.Publicmethod()
# name is : Hari
# age is : 22
# my name isHari, age is :22
