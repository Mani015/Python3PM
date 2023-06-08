
# Static methods: A static method is a general utility method that performs a task in isolation. Inside this method,
# we don’t use instance or class variable because this static method doesn’t take any parameters like self and cls.


class A:
    @staticmethod
    def Addtiton():
        a = 10
        b = 20
        print('addition:',a + b)
    @staticmethod
    def Concatination():
        name1 = 'ABC'
        name2 = 'Python Developer'
        return name1 ,  'become a ' ,name2

Ob1 = A()
A.Addtiton()
print(A.Concatination())

# addition: 30
# ('ABC', 'become a ', 'Python Developer')

# Advantages of a Static Method
# Here, the static method has the following advantages
#
#
# Consume Less memory: Instance methods are object too, and creating them has a cost.
# Having a static method avoids that. Let’s assume you have ten employee objects and if you create gather_requirement() as a instance method then
# Python have to create a ten copies of this method (seperate for each object) which will consume more memeory.
# On the other hand static method has only one copy per class.

