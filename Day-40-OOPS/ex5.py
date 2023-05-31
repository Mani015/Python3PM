# Updating a Attribute Name:

class Employee_Details:
    emp_Name = 'Kaarthik'
    emp_Salary = 60000
    emp_Age = 21
    emp_Mobilenumber = 9874561230
    emp_Location = 'pune'

# calling class

E2 = Employee_Details()
print('Before Updating attribute value:',E2.emp_Name)
# Before Updating attribute value: Kaarthik

# update the attribute value
# sy objectname.attributename = New_Value

E2.emp_Name = 'Deepika'
print('After Updating attribute value:',E2.emp_Name)
# After Updating attribute value: Deepika

E2.emp_Location = 'Delhi'
print(E2.emp_Location)
# Delhi
