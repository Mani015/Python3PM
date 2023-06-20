
# Name Mangling to access private members
# We can directly access private and protected variables from outside of a class through name mangling.
# The name mangling is created on an identifier by adding two leading underscores and one trailing underscore,
# like this _classname__dataMember,
# where classname is the current class, and data member is the private variable name.

class Main:
    def __init__(self,x1,y1,z1,x2,y2,z2):
        self.x1 = x1
        self.__y1 = y1
        self.__z1_ = z1
        self.___x2 = x2
        self.____y2__ = y2
        self.__z2__ = z2
    def __private_(self):
        print('i am private ')

print(dir(Main(1,2,3,4,5,6)))

# ['_Main___x2', '_Main__y1', '_Main__z1_', '____y2__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '__z2__', 'x1']

ob1 = Main(1,2,3,4,5,6)
# To accessing public members
print(ob1.x1)
print(ob1.__z2__)
print(ob1.____y2__)
# 1
# 6
# 5

print()
# To accessing the Private members outside of the class
# sy: objname._classname__private_Member_
print(ob1._Main___x2)
# 4
print(ob1._Main__y1)
# 2
print(ob1._Main__z1_)
# 3



