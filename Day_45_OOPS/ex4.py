


class Python:
    course_Duration = '4 months'
    def __init__(self,Pname,Page,Pfess,Plocation):
        self.name = Pname
        self.age = Page
        self.fess = Pfess
        self.location = Plocation


S1 = Python('Deepika',22,25000,'Banglore')
S2 = Python('Devisri',22,23000,'Chennai')
S3 = Python('Keerthana',23,25000,'Pune')
S4 = Python('Gowthami',20,20000,'hyderbad')
S5 = Python('Tejabharagvi',23,25000,'Kadapa')

for i in [S1,S2,S3,S4,S5]:
    print(i.name)
    print(i.age)
    print(i.fess)
    print(i.location)
    print(i.course_Duration)
    print()

# Deepika
# 22
# 25000
# Banglore
# 4 months
#
# Devisri
# 22
# 23000
# Chennai
# 4 months
#
# Keerthana
# 23
# 25000
# Pune
# 4 months
#
# Gowthami
# 20
# 20000
# hyderbad
# 4 months
#
# Tejabharagvi
# 23
# 25000
# Kadapa
# 4 months
