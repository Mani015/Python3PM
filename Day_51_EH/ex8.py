
# x = [1,2,3,4,5]
# try:
#     print(x[5])
# except ValueError:
#     print('value error occured and Handle')
# except IndexError:
#     print('Index error occured and Handle')
# except NameError:
#     print('Name Error occured and Handle')
# except:
#     print('Default error')
# else:
#     print('I will excute without an any error')
#
#
# print('complete excution, this is last line')

# Index error occured and Handle
# complete excution, this is last line




x = [1,2,3,4,5]
try:
    print(x[2])
except ValueError:
    print('value error occured and Handle')
except IndexError:
    print('Index error occured and Handle')
except NameError:
    print('Name Error occured and Handle')
except:
    print('Default error')
else:
    print(' I am Else,I will excute without an any error')


print('complete excution, this is last line')

# 3
#  I am Else,I will excute without an any error
# complete excution, this is last line

# Advantages of Exception Handling:
# Improved program reliability: By handling exceptions properly, you can prevent your program from crashing or producing incorrect results due to unexpected errors or input.
# Simplified error handling: Exception handling allows you to separate error handling code from the main program logic, making it easier to read and maintain your code.
# Cleaner code: With exception handling, you can avoid using complex conditional statements to check for errors, leading to cleaner and more readable code.
# Easier debugging: When an exception is raised, the Python interpreter prints a traceback that shows the exact location where the exception occurred, making it easier to debug your code.
# Disadvantages of Exception Handling:
# Performance overhead: Exception handling can be slower than using conditional statements to check for errors, as the interpreter has to perform additional work to catch and handle the exception.
# Increased code complexity: Exception handling can make your code more complex, especially if you have to handle multiple types of exceptions or implement complex error handling logic.
# Possible security risks: Improperly handled exceptions can potentially reveal sensitive information or create security vulnerabilities in your code, so it’s important to handle exceptions carefully and avoid exposing too much information about your program.
# Overall, the benefits of exception handling in Python outweigh the drawbacks, but it’s important to use it judiciously and carefully in order to maintain code quality and program reliability.