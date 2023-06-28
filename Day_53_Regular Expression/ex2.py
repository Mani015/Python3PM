

import re

m1 = re.match('A RegEx, or Regular Expression','A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.pravallika')
# print(m1)

# <re.Match object; span=(0, 30), match='A RegEx, or Regular Expression'>



# The search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.
#
# If there is more than one match, only the first occurrence of the match will be returned:

st1 = 'Believe you can and youre halfway there'
s1 = re.search('and',st1)
print(s1)
# <re.Match object; span=(16, 19), match='and'>



import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# The first white-space character is located in position: 3
