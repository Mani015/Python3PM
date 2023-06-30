

sd = 'Devi is 21 and Gowthami is 20 \
     Bhargavi is 22 and Keerthana is 24'


import re

age = re.findall('\d{2}',sd)

# print('student ages:',age)
# student ages: ['21', '20', '22', '24']

names = re.findall(r'[A-z][a-z]*',sd)
print('names:',names)






import re

fruits = 'Banana is 10 and Mango is 20' \
         'Orange is 20 and Apple is 12 '


n = re.findall('\d{2}',fruits)
print(n)

name = re.findall('[A-Z][a-z]*',fruits)
print(name)
# ['10', '20', '20', '12']
# ['Banana', 'Mango', 'Orange', 'Apple']

dict = {}

var = 0

for i in name:
     dict[i] = n[var]
     var+=1
print(dict)

# {'Banana': '10', 'Mango': '20', 'Orange': '20', 'Apple': '12'}
