
st2 = 'My name is Teja bhargavi my number is 234565678'

import re

# match integers:  d

d1 = re.findall('\d',st2)
# print(d1)
# ['2', '3', '4', '5', '6', '5', '6', '7', '8']

d2 = re.findall('\d{1}',st2)
# print(d2)
# ['2', '3', '4', '5', '6', '5', '6', '7', '8']

d3 = re.findall('\d{1,2}',st2)
# print(d3)
# ['23', '45', '65', '67', '8']


d4 = re.findall('\d{4}',st2)
print(d4)
# ['2345', '6567']
