class property1:
    pass

class property2:
    def land1(self):
        print("this is property2")

class child(property1,property2):
   pass

ob1 = child()
ob1.land1()
ob1.land1()
ob1.land1()

# this is property3
# this is property3
# this is property3


# this is property1
# this is property1
# this is property1