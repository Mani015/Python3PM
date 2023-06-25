# Finally Keyword in Python
# Python provides a keyword finally, which is always executed after the try and except blocks.
# The final block always executes after the normal termination of the try block or after the try block terminates due to some exception.
x = [1,2,3,4,5]
try:
    print(x[8])
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
finally:
    print('I am Finally , i am come with/out error')

print('complete excution, this is last line')


# Index error occured and Handle
# I am Finally , i am come with/out error
# complete excution, this is last line

