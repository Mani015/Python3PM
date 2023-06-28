
# The findall() Function
# The findall() function returns a list containing all matches.

st1 = 'Believe you can and youre halfway there  do anything'

import re

f1 = re.findall('can',st1)
# print(f1)
# ['can']


f2 = re.findall('a',st1)

# print(f2,'are', len(f2))
# ['a', 'a', 'a', 'a', 'a'] are 5


# Example
# Return an empty list if no match was found:

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)