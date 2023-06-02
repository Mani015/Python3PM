# To creating Different Objects:

class Mobile:
    Mobile_Brand = 'Vivo'
    Mobile_Price = 30000
    Mobile_Color = 'Blue'
    Mobile_Storage =  '128Gb'

ob1 = Mobile()
print(ob1.Mobile_Brand)
# print(ob1.Mobile_Price)
# print(ob1.Mobile_Color)
# print(ob1.Mobile_Storage)
print()
# Vivo
# 30000
# Blue
# 128Gb

ob2 = Mobile()
print(ob2.Mobile_Brand)
print(ob2.Mobile_Price)
# Updating the Attribute value:
ob2.Mobile_Brand = 'Redme'
print(ob2.Mobile_Brand)
# Vivo
# 30000
# Redme
print()
print('ob1 attribute:',ob1.Mobile_Brand)
# ob1 attribute: Vivo


