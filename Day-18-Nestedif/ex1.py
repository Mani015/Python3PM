# Nested_if

# the nesting of an if statement insdie another if statement with or/out an else statement in some cases we need nesting of if statement to make the entire program
# flow of code in a semantic order and make it easily readble



a = 10
if a>50:
    print('1---->it  is true')
    a=int(input('Enter one number:'))
    if a<11:
        print('2----->this is true')
    else:
        print('this is false')

else:
    print('IT is false')