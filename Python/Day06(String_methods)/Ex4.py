
# Check if all the characters in the text are letters:

v1 = "mangosareverysweet"
print(v1.isalpha())
# True
v2 = "jeevan kumar" # space is present in the v2
print(v2.isalpha()) # False


# Check if all the characters in the text are alphanumeric:
nameage = "prasannaage20"
print(nameage.isalnum())
# True

email = "jeevan@gmail.com"
print(email.isalnum())
# False

# Check if the string is a valid identifier:
print('jeevan'.isidentifier())
# True

print('12prasanna'.isidentifier())
# False
