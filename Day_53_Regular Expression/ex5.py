st3 = "My name is Harry my age is 23"

import re

# D: it returns only string except integers
D1 = re.findall('\D',st3)
# print(D1)
#
# ['M', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'H', 'a', 'r', 'r', 'y', ' ', 'm', 'y', ' ', 'a', 'g', 'e', ' ', 'i', 's', ' ']


# s it returns spaces
s1 = re.findall('\s',st3)
# print(s1)
# [' ', ' ', ' ', ' ', ' ', ' ', ' ']


# S :

S1 = re.findall('\S',st3)
print(S1)

# ['M', 'y', 'n', 'a', 'm', 'e', 'i', 's', 'H', 'a', 'r', 'r', 'y', 'm', 'y', 'a', 'g', 'e', 'i', 's', '2', '3']
