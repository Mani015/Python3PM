
# With out decoration
def Task1(func):
    def Task2(st1,st2):
        print('New Defination')
        return func(st1, "are " + st2)
    return Task2
def Addtional(st1,st2):
    print('New Decoration')
    return st1,st2

ob1 = Task1(Addtional)
print(ob1('Mangos','very sweet'))

# New Defination
# New Decoration
# ('Mangos', 'are very sweet')


