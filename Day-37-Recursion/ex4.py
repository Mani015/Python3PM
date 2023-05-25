

# direct calling

def f1():
    print('Function_1')
def f2():
    print('Function_2')
def f3():
    print('Function_3')


# f3()
# f2()
# f1()

# Function_3
# Function_2
# Function_1




#Indirect calling

def fun1():
    print('function_1')
    fun2()
def fun2():
    print('function_2')
    fun3()
def fun3():
    print('function_3')


fun1()

# function_1
# function_2
# function_3


















