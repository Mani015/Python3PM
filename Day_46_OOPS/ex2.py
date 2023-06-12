class Animal:
    def Sleeping(self):
        print('A animal sleep')
    def Eating(self):
        print('eating every day')

class Lion(Animal):
    def hunting(self):
        print('hunting every day')
# ob1 = Animal()
# ob1.Eating()
# ob1.Sleeping()
# ob1.hunting()
# AttributeError: 'Animal' object has no attribute 'hunting'
# eating every day
# A animal sleep


ob1 = Lion()
ob1.Eating()
ob1.hunting()
ob1.Sleeping()
# eating every day
# hunting every day
# A animal sleep
