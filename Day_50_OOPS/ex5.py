class Main_Class:
    def __init__(self,x1,x2):
        self.__private1 = x1
        self.__private2 = x2
        print('Access with in class:',self.__private1)
        print('Access with in class:', self.__private2)
    def __Privatemethod(self):
        print('I am Prive mathod ')

ob1 = Main_Class
# ob1.__privatemethod()
# AttributeError: type object 'Main_Class' has no attribute '__privatemethod'


print(ob1.__private1)
# AttributeError: type object 'Main_Class' has no attribute '__private1'

