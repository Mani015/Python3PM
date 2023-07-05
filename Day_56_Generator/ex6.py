
def Main_Fun():
    return 'Function'


# print(type(Main_Fun()))
# <class 'str'>

ob1 = Main_Fun()
# print(type(Main_Fun))
# <class 'function'>

# Create Python Generator
# In Python, similar to defining a normal function, we can define a generator function using the def keyword,
# but instead of the return statement we use the yield statement.
def Numbers():
    yield 10
    yield 20
    yield 30
    yield 40
    yield 50

# print(type(Numbers()))
# <class 'generator'>

# print(Numbers())
# <generator object Numbers at 0x000001FF9ADB77B0>


x1 = Numbers()
print(x1.__next__())
# 10
print(x1.__next__())
print(x1.__next__())
print(x1.__next__())
print(x1.__next__())
# 20
# 30
# 40
# 50
print(x1.__next__())

# StopIteration
