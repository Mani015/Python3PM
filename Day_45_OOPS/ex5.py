# Class method: Used to access or modify the class state.
# In method implementation, if we use only class variables,
# then such type of methods we should declare as a class method.
# The class method has a cls parameter which refers to the class.

class Python:
    course_Duration = '4 months'
    def __init__(self,Pname,Page,Pfess,Plocation):
        self.name = Pname
        self.age = Page
        self.fess = Pfess
        self.location = Plocation

    def Updateclassvariable(cls,New_Name):
        cls.course_Duration = New_Name
        print(cls.course_Duration)

S1 = Python('Thamaraselvi',20,20000,'chennai')
print(S1.course_Duration)
# 4 months
S1.Updateclassvariable('3 Months only')
# 4 months
# 3 Months only
