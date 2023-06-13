
# Using inheritance

class Company(object):
    def __init__(self,cname,clocation,cpincode,cnumber):
        self.name = cname
        self.location = clocation
        self.code = cpincode
        self.number  = cnumber
        print(self.name, self.location, self.code, self.number)

class Employe_1(Company):
    def __init__(self,cname,clocation,cpincode,cnumber,ename,eage,esalary,edomain,elocation):
        Company.__init__(self,cname,clocation,cpincode,cnumber)
        self.name = ename
        self.age = eage
        self.salary = esalary
        self.domain = edomain
        self.location = elocation

    def View(self):
        print(self.name, self.age, self.salary, self.domain, self.location)


class Employe_2(Company):
    def __init__(self,cname,clocation,cpincode,cnumber,ename,eage,esalary,edomain,elocation):
        self.name = ename
        self.age = eage
        self.salary = esalary
        self.domain = edomain
        self.location = elocation
    def View(self):
        print(self.name,self.age,self.salary,self.domain,self.location)


ob1 = Employe_1('ABC_Solutions','MArthahali',560093,123654,'Motu',20,50000,'PFD','Chennai')
ob1.View()

# ABC_Solutions MArthahali 560093 123654
# Motu 20 50000 PFD Chennai
