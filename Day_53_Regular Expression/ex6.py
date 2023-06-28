
import re


st4 = "Keerthana BestFriend Gowthami she is 2 nd one"
# \A	Returns a match if the specified characters are at the beginning of the string
A1 = re.findall('\AKe',st4)
# print(A1)
# ['Ke']


A2 = re.findall('\AGow',st4)
# print(A2)
# []


# \Z	Returns a match if the specified characters are at the end of the string

z1 = re.findall('one\Z',st4)
print(z1)
# ['one']
