
# Decorator using for loop
def d1(n):
    def d2(func):
        global i
        for i in range(n):
            func()
    return d2

@d1(5)
def d3():
    print('Loops: ', i)

# Loops:  0
# Loops:  1
# Loops:  2
# Loops:  3
# Loops:  4
# Loops:  5