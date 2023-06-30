import re

# find iter value index

st3 = 'I will fight for the right'

# import re
#
# for i in re.finditer('i',st3):
#     t1 = i.span()
#     print(t1)
# (3, 4)
# (8, 9)
# (22, 23)


# range of matching

s4 = "Running, cooking, eating, dancing,singing"

x1 = re.findall('[c-s]ing',s4)
for i in x1:
    print(i)
# ning
# king
# cing
# sing



# x2 = re.findall('[^R-s]ing',s4)
# for i in x2:
#     print(i)

# ting
# cing

