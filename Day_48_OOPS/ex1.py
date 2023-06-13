class Company(object):
    def __init__(self,cname,clocation,cpincode,cnumber):
        self.name = cname
        self.location = clocation
        self.code = cpincode
        self.number  = cnumber
    def Display(self):
        print(self.name,self.location,self.code,self.number)

class Employe_1:
    def __init__(self,ename,eage,esalary,edomain,elocation):
        self.name = ename
        self.age = eage
        self.salary = esalary
        self.domain = edomain
        self.location = elocation
    def View(self):
        print(self.name,self.age,self.salary,self.domain,self.location)


c1 = Company('ABC_Solutions','MArthahali',560093,123654)
c1.Display()
# ABC_Solutions MArthahali 560093 123654

E1 = Employe_1('Motu',20,50000,'PFD','Chennai')
E1.View()
# Motu 20 50000 PFD Chennai
