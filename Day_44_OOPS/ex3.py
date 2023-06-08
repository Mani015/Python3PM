# Instance variable TO accessing the object


class Employee:
    def __init__(self,Empname,Empsalary,Empage):
        self.name = Empname
        # instance varaibles
        self.salary = Empsalary
        self.age = Empage

Ysrcp = Employee('jagan',1,50)

# syntax: objectname.instancevaraiblename

print(Ysrcp.name)
# jagan
print(Ysrcp.salary)
# 1
print(Ysrcp.age)
# 50