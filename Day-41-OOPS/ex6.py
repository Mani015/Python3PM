

class Employee_Details:
    emp_Name = 'Kaarthik'
    emp_Salary = 60000
    emp_Age = 21
    emp_Mobilenumber = 9874561230
    emp_Location = 'pune'

E3 = Employee_Details()
# print('Before deleting attribute value:',E3.emp_Salary)
# Before deleting attribute value: 60000


# To deleting the AttributeName:
# syn: del objectname.attributeName

del E3.emp_Salary
print(E3.emp_Salary)
# AttributeError: emp_Salary

