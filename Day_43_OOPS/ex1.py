
class Bottle:
    Bottlename = 'Bisleri'
    BottleColor = 'White'
    def Purpose(self):
        print('To Store the Water')

B1 = Bottle()
print(B1.Bottlename,B1.BottleColor)

# How to calling a Method:
# Syn: object_Name.MethodNAme()
B1.Purpose()
# Bisleri White
# To Store the Water