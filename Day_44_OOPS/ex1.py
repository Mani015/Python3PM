l1 = [-1,-10,12,13,-24,36]

# for i in l1:
#     if i>0:
#         print(i)
#     else:
#         print(0)
# print(len(l1))
# 6



for k in range(len(l1)):
    if l1[k]<0:
        l1[k]=0
print(l1)
# [0, 0, 12, 13, 0, 36]


