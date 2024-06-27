x1 = "Good morning"
# print(x1)
# Good morning
# The find() method finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.

# find(value,start,stop)
print(x1.find('o'))
# 1
print(x1.find('o',3))
# 6

print(x1.find('Z'))
# -1


# capitalize()	Converts the first character to upper case

print('prasanna'.capitalize())
# Prasanna


# The casefold() method returns a string where all the characters are lower case.
#
# This method is similar to the lower() method, but the casefold() method is stronger,
# more aggressive, meaning that it will convert more characters into lower case,
# and will find more matches when comparing two strings and both are converted using the casefold() method.


x3 = "Success Some Times Require When Are Correct"
print(x3.casefold())
# success some times require when are correct
