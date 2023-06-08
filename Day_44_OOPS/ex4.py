
# Instance methods: Used to access or modify the object state. If we use instance variables inside a method,
# such methods are called instance methods. It must have a self parameter to refer to the current object.

class Emp(object):
    def __init__(self,ename,esalary,elocation,ephone):
        self.name = ename
        self.salary = esalary
        self.location = elocation
        self.phone = ephone

    def Appearence(self):
        print(self.name,self.salary,self.location,self.phone)
    def Incremetsalary(self,new_salary):
        self.salary+= new_salary


E1 = Emp('Martin',20000,'chennai',9874561230)
E1.Appearence()
# Martin 20000 chennai 9874561230
E1.Incremetsalary(10000)
print(E1.salary)
# 30000
