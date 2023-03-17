
x1 = [11,22,33,44,55,66,77,88,99,12,34,56,78,90,13,14,15,16,17,'bhavani','bhargavi','vinod']
# TO using step over value
# sy:variablename[start : end : stepover]
# print(x1[0:10:2])
# start =0  : end = 10: step= 2
# # Start =0 ----->11
# # Start = 0 + 2 = 2----->33
# # Start = 2 + 2 = 4 ---->55
# # Start = 4 + 2 = 6-->77
# # Start = 6 + 2 = 8 -->99


# [11, 33, 55, 77, 99]
print(x1[0:10])
# [11, 22, 33, 44, 55, 66, 77, 88, 99, 12]

print(x1[2:12])
# [33, 44, 55, 66, 77, 88, 99, 12, 34, 56]

print(x1[3:])
# [44, 55, 66, 77, 88, 99, 12, 34, 56, 78, 90, 13, 14, 15, 16, 17, 'bhavani', 'bhargavi', 'vinod']
print(x1[9:20])
# [12, 34, 56, 78, 90, 13, 14, 15, 16, 17, 'bhavani']
