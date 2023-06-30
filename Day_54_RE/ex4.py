

x1 = "cat,mat,rat,bat,hat,fat,jat,sat"
import re

# r1 = re.findall('[a-m]at',x1)
# for i in r1:
#     print(i)

# cat
# mat
# bat
# hat
# fat
# jat



r1 = re.findall('[^a-m]at',x1)
for i in r1:
    print(i)
# rat
# sat
