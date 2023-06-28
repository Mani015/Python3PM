
# \w	Returns a match where the string contains any word characters
# (characters from a to Z, digits from 0-9, and the underscore _ character)

d1 = 'mee peru evvandi sir 123'
import re

w = re.findall('\w',d1)
# print(w)

# ['m', 'e', 'e', 'p', 'e', 'r', 'u', 'e', 'v', 'v', 'a', 'n', 'd', 'i', 's', 'i', 'r', '1', '2', '3']



d2 = 'My name is Devi sithara my id no 123 $ %'

w2 = re.findall('\w',d2)
print(w2)

# ['M', 'y', 'n', 'a', 'm', 'e', 'i', 's', 'D', 'e', 'v', 'i', 's', 'i', 't', 'h', 'a', 'r', 'a', 'm', 'y', 'i', 'd', 'n', 'o', '1', '2', '3']

