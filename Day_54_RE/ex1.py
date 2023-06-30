

st1 = 'Always find reason to smile'

import re

if re.findall('pain',st1):
    print('yes is there!')
else:
    print('there is no here')
# yes is there!

print()

st2 = "every one looks so much better when they smile"

x1 = re.findall('o',st2)
for i in x1:
    print(i)

# o
# o
# o
# o

