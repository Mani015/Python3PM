# GLobal Variable:
# A Global Variuable is a variable ,Which is defined out side of the function

x1 = 10
print('GLobal variable:',x1)
# GLobal variable: 10
def Main_Function():
    x2 = 20
    print('Local Varaible:',x2)
#     Local Varaible: 20
Main_Function()
# GLobal variable: 10
# Local Varaible: 20
