
#  Init :
#
# #
# # The __init__ function is called every time an object is created from a class.
# # The __init__ method lets the class initialize the object's attributes and serves no other purpose.
# # It is only used within classes.

# To understand the meaning of classes we have to understand the built-in __init__() function.
#
# All classes have a function called __init__(), which is always executed when the class is being initiated

# Syntax:
# class className:
#     def __init__(self,para1,para2,.......Para n):
#         object.attributename1 = para1
#         object.attributename2 = para2
#         object.attributename_n = para N


class Mobile:
    def __init__(self,BrandName,BrandPrice,BrandColor,BrandRAM):
        self.Brand = BrandName
        self.Price = BrandPrice
        self.color = BrandColor
        self.RAM = BrandRAM
        print(self.Brand)
        print(self.Price)
        print(self.color)
        print(self.RAM)

M1 = Mobile('Dell',50000,'Balck','2gb')


# Dell
# 50000
# Balck
# 2gb











