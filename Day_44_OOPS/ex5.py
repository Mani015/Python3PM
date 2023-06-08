class Emp(object):
    def __init__(self,ename,esalary,elocation,ephone):
        self.name = ename
        self.salary = esalary
        self.location = elocation
        self.phone = ephone

    def deletesalary(self):
        del self.salary

    def Appearence(self):
        print(self.name,self.salary,self.location,self.phone)
    # def Incremetsalary(self,new_salary):
    #     self.salary+= new_salary
    # def namechange(self,New_Name):
    #     self.name = New_Name



E1 = Emp('Martin',20000,'chennai',9874561230)
# E1.Appearence()
# del E1.location
# print(E1.location)
# Martin 20000 chennai 9874561230
# E1.namechange('Peterpark')
# print(E1.name)
# peterpark
# E1.deletesalary()
# print(E1.salary)
# AttributeError: 'Emp' object has no attribute 'salary'

