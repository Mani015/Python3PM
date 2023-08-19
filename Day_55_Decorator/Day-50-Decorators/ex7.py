

def Out(new):
    def In():
        well = new()
        return 'Welcome to Python Class:' + well
    return In()

@Out
def Name1():
    return 'Narendra'

# print(Name1)
# <function Name1 at 0x000002A136A0EE50>
print(Name1)
# Welcome to Python Class:Narendra

@Out
def Name2():
    return 'Vishal'

print(Name2)
# Welcome to Python Class:Vishal
