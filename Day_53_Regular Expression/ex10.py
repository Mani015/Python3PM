
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")

# r"\bain"
# r"ain\b"


b = 'Prevention is better than cure'

import re
t1 = re.findall(r'\bPre',b)
print(t1)

# x = re.findall(r"\bain", txt)

# ['Pre']

x2 = re.findall(r'\bcu',b)
# print(x2)

x3 = re.findall(r'Pre\b',b)
print(x3)

import re

txt = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:


# ['cure']



# print(x)
#
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")


y  = 'Mangoes Are Very Sweet'

y1 = re.findall(r'\b[A-Z][a-z][a-z]*',y)
print(y1)
# ['Mangoes', 'Are', 'Very', 'Sweet']
