# Program to depict Raising Exception

try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise  # To determine whether the exception was raised or not


# An exception
# Traceback (most recent call last):
#   File "C:\Users\Test\PycharmProjects\pythonProject\Day_51_EH\raise.py", line 4, in <module>
#     raise NameError("Hi there")  # Raise Error
# NameError: Hi there
