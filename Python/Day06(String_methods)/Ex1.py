s1 = "God is alive"
print(s1)
# God is alive
# upper()	Converts a string into upper case
# sy : str.upper()
print(s1.upper())
# GOD IS ALIVE

# lower()  Converts a string into lower case
s2 = 'WINDOWS IS EASY FOR BEIGNERS'
print(s2.lower())
# windows is easy for beigners

S3 = "windows is easy for beigners"
# title()	Converts the first character of each word to upper case
# print(S3.title())
# Windows Is Easy For Beigners

s4 = " PytHon iS a Beginner FrIeNdLy"
# print(s4, s4.swapcase())
#  PytHon iS a Beginner FrIeNdLy  pYThON Is A bEGINNER fRiEnDlY
print()
print()
s5 = "Jeevan Prasanna"
print(s5)
# index()	Searches the string for a specified value and returns the position of where it was found
# sy : str.index(element, start,stop)
print(s5.index('J'))
# 0
print(s5.index('e'))
# 1
# print(s5.index('e'))
#1

print(s5.index('e',2))
# 2

# print(s5.index('e',3,8))
# ValueError: substring not found

print(s5.index('z'))
# ValueError: substring not found
