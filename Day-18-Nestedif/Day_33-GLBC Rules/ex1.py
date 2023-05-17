# GLobal Variable rules
# Global scope is the top-most scope in python program,script,or module.
# This python scope contains all of the names that you define at the top level of a program or a module names in this python
# scope are visible from everywhere in your code.

x1 = 20
# print('global variable:',x1)
def Innerfunction():
    print('global variable:',x1)
Innerfunction()
# global variable: 20


