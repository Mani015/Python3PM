#When we have nested functions, the inner function can access the variables of the outer function.
# The variables of the outer function are called as non-local variables inside the inner function,
# and they are said to be under the enclosed scope.


def Outer_Info():
    name2 = 'python'
    print('Enclosing  scope:', name2)
    def Inner_Info():
        name3 = 'jango'
        print('local scope:', name3)
        print('enclosing variable:',name2)

    Inner_Info()
    print('enclosing variable:',name2)
Outer_Info()


# Enclosing  scope: python
# local scope: jango
# enclosing variable: python
# enclosing variable: python
