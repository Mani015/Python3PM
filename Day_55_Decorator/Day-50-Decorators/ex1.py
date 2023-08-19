
# 1).assigning function to a variable

def Who():
    print('Basic Fucntion ')

New = Who

print(f'{New}')
# <function Who at 0x000002069A8AED30>
print(f"{Who}")
# <function Who at 0x000001803CDDDD30>

New()
# Basic Fucntion
Who()
# Basic Fucntion
