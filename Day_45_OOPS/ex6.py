# To deleting the classvariable using by classmethod
class Python:
    course_Duration = '4 months'
    def __init__(self,Pname,Page,Pfess,Plocation):
        self.name = Pname
        self.age = Page
        self.fess = Pfess
        self.location = Plocation
    @classmethod
    def deletecvariable(cls):
        del cls.__Python__course_Duration
        print(cls.course_Duration)

S1 = Python('Thamaraselvi',20,20000,'chennai')
print(S1.course_Duration)

S1.deletecvariable()
# To deleting class variable
del S1.course_Duration
print(S1.course_Duration)


# AttributeError: _Python__Python__course_Duration


