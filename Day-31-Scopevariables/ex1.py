# Enclosing Variable
# Enclosing scope is a special scope that only existed for nested functions if the local scope is an inner or nested function then the enclosing scope is the
# scope of the outer or enclosing function is called Enclosing
# this scope contains the names that u defined in the enclosing fucntion


def Outer_Info():
    name2 = 'python'
    print('Enclosing  scope:',name2)
    def Inner_Info():
        name3 = 'jango'
        print('local scope:',name3)

    Inner_Info()
Outer_Info()

# Enclosing  scope: python
# local scope: jango
