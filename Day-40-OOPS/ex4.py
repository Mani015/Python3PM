# To creating an object

# print(type([]))
# <class 'list'>
x1 = [1,2,3,4,5,6,7]
x2 = x1
x3 = x2
x4 = x3
x5 = x4
# print(x5)
# print(x2)
# [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7]


class Employee_Details:
    emp_Name = 'Kaarthik'
    emp_Salary = 60000
    emp_Age = 21
    emp_Mobilenumber = 9874561230
    emp_Location = 'pune'

# TO creating object name
# sy: objectname = Classname()
E1 = Employee_Details()
# E2 = Employee_Details()

# calling attributes with objectname
# Sy: objectName.Attribute
print(E1.emp_Name)
# Kaarthik
print(E1.emp_Salary)
print(E1.emp_Age)
print(E1.emp_Mobilenumber)
print(E1.emp_Location)
# 60000
# 21
# 9874561230
# pune
