# Using global variable

x1 = 10
print('Global v:',x1)
def Outer():
    x2 = 20
    print('Enclosing  v',x2)
    print('Global v:',x1)
    def Inner():
        x3 = 30
        print('Locl v:',x3)
        print('Enclosing  v', x2)
        print('Global v:', x1)
    Inner()
    print('Enclosing  v', x2)
    print('Global v:', x1)
Outer()
print('Global v:',x1)

#Global v: 10
# Enclosing  v 20
# Global v: 10
# Locl v: 30
# Enclosing  v 20
# Global v: 10
# Enclosing  v 20
# Global v: 10
# Global v: 10

