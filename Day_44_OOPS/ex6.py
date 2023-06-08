class Emp(object):
    def __init__(self,ename,esalary,elocation,ephone):
        self.name = ename
        self.salary = esalary
        self.location = elocation
        self.phone = ephone

    def deletesalary(self):
        del self.salary

    def Appearence(self):
        print(self.name,self.location,self.phone)


E1 = Emp('python',25000,'grk',987456123)
E1.deletesalary()

E1.Appearence()
# python grk 987456123
