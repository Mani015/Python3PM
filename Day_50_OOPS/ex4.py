
# Private Member
# We can protect variables in the class by marking them private.
# To define a private variable add two underscores as a prefix at the start of a variable name.
#
# Private members are accessible only within the class, and we can’t access them directly from the class objects


class Main_Class:
    def __init__(self,x1,x2):
        self.__private1 = x1
        self.__private2 = x2
        print('Access with in class:',self.__private1)
        print('Access with in class:', self.__private2)

Main_Class('Python','Developer')
# Access with in class: Python
# Access with in class: Developer
