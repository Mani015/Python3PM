
# Hierarchical Inheritance
# In Hierarchical inheritance, more than one child class is derived from a single parent class.
# In other words, we can say one parent class and multiple child classes.
class father:
    def land(self):
        print('p1 land property only')
class child1(father):
    def house(self):
        print('c1 property only')

class child2(father):
    def own(self):
        print('c2 property only')

ob1=child1()
ob1.house()
ob1.land()
# c1 property only
# p1 land property only

ob2 = child2()
ob2.land()
ob2.own()
# p1 land property only
# c2 property only
