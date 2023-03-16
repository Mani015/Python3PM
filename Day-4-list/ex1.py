# index()

x1 = ['thulasi ram','sreekanth','vivek','surya',"vijay", 1 ,2 ,12.6 ,18.30 ,True ,False ,2+5j]
#          0       ,   1       ,   2   ,  3    ,   4   ,5,   6,  7  ,  8 ,    9 ,   10 ,  11
# print(x1)
# ['thulasi ram', 'sreekanth', 'vivek', 'surya', 'vijay', 1, 2, 12.6, 18.3, True, False, (2+5j)]


# sy:- variablename .index(value)

print(x1.index('thulasi ram'))
# 0

print(x1.index('surya'))
# 3

print(x1.index(12.6))
# 7

# print(x1.index(5))
# ValueError: 5 is not in list

print(x1.index(2+5j))
# 11

