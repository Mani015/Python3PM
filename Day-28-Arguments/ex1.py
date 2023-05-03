# Default Arguments
# Default arguments take the default value during the function call if we do not pass them.
# We can assign a default value to an argument in function definition using the = assignment operator.

def Default(a=10,b=20):
    print('a is :',a)
    print('b is :',b)

Default()
# a is : 10
# b is : 20

# suppose if we are passing the aguments when function is called.
Default('python')
# a is : python
# b is : 20



Default('python', 'java')
# a is : python
# b is : java

