
# The count() method returns the number of times a specified value appears in the string.

v1 =  "Love is feeling that you feel , when you feel that you are feeling"
# sy : str.count(value,start,stop)

print(v1.count('o'))
# 4
print(v1.count('feel'))
# 4
# from indexing between  12 to 25  , how many feel  's presented
print(v1.count('feel',12,30))
# 1

# Check if all the characters in a string are decimals (0-9):
num = '12345'
print(num.isdecimal())
# True

info = "jeevan123"
print(info.isdecimal())
# False


# Check if all the characters in the text are digits:
x = "12.0"
print(x.isdigit())
# False

print('2233'.isdigit())
# True

