# In Python, a decorator is a design pattern that allows you to modify the functionality of a
# function by wrapping it in another function.
#
# The outer function is called the decorator,
# which takes the original function as an argument and returns a modified version of it.

def Main_Fun(name):
    def New_Func():
        v1 = name()
        return 'welcome to our special guest:' + v1
    return New_Func()


# print(Main_Fun())
# TypeError: Main_Fun() missing 1 required positional argument: 'name'



def Advance_fun():
    return 'Python'

ob1 = Main_Fun(Advance_fun)
print(ob1)

# welcome to our special guest:Python


def Devi_Fun():
    return 'Devi sithara'

ob2 = Main_Fun(Devi_Fun)
print(ob2)

# welcome to our special guest:Devi sithara


