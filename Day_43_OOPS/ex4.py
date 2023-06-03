class Mobile:
    def __init__(self,BrandName,BrandPrice,BrandColor,BrandRAM):
        self.Brand = BrandName
        self.Price = BrandPrice
        self.color = BrandColor
        self.RAM = BrandRAM
        # print(self.Brand)
        # print(self.Price)
        # print(self.color)
        # print(self.RAM)

M1 = Mobile('Dell',50000,'Balck','2gb')

# TO calling Attributes using Current Object Name:
print(M1.Brand)
print(M1.Price)
print(M1.color)
print(M1.RAM)

# Dell
# 50000
# Balck
# 2gb

M2 = Mobile('Hp',60000,'Grey','6gb')
print(M2.Brand)
print(M2.Price)
print(M2.color)
print(M2.RAM)
# Hp
# 60000
# Grey
# 6gb
