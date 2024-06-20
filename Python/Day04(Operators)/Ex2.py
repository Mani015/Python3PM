# Identity operator : is, is not
# To check Having both objects has a  same id's

l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]
# sy : object1 is object2
# Returns False : when they don't have same Id's
print(l1 is l2)
# print('L1 id :',id(l1))
# print("L2 id: ", id(l2))
# L1 id : 1907010976576
# L2 id:  1907010976384

# Returns True: they have same id's
l3 = l2

print('L3 id :',id(l3))
print("L2 id: ", id(l2))
# L3 id : 1810643565120
# L2 id:  1810643565120

print(l2 is l3)

# -------------------------------------------------------------------
# is not : Returns True: they don't have same id's
print(l1 is not l2)

# is not : # Returns False : when they  have same Id's
print(l2 is not l3)
# False
