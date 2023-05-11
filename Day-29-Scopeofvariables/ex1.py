# a=10
# a=20
# print(a)


# SCOPE OF VARIABLES:
# When we define a function with variables, then those variables’ scope is limited to that function. In Python,
# the scope of a variable is an area where a variable is declared. It is called the variable’s local scope.

# 1).Local Scope
# 2).Global Scope
# 3).Enclosing Scop
# 4).Built-in-Scope


# Local Variable in function
# A local variable is a variable declared inside the function that is not accessible from outside of the function.
# The scope of the local variable is limited to that function only where it is declared.



def LocalVariable():
    x = 10
    print('local variable:',x)
LocalVariable()
# local variable: 10
