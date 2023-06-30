

def Outer(name):
    def Inner():
        v1 = name()

        return 'Happy birthday ' + v1
    return Inner

@Outer
def Decorate():
    return 'Devi'

print(Decorate())
# Happy birthday Devi

@Outer
def K1():
    return 'Kerthana reddy'

print(K1())

# Happy birthday Kerthana reddy
