
def Fun():
    name = 'abhiram'
    print('my good name is ' + name)
# Fun()
# my good name is abhiram


name = 'hari'
print('my friend is ',name,'he is good boy')
# USING FORMATE STRING
print(f'my friend is {name} he is good')
# my friend is  hari he is good boy
# my friend is hari he is good


# If we try to access the local variable from the outside of the function, we will get the error as NameError.

def New_function():
    fr1 = 'banana'
    fr2 = 'apple'
    # print('local variable_1:',fr1)
    # print('local variable_2:',fr2)
#     local variable_1: banana
# local variable_2: apple
New_function()
print('locav v:',fr1)

# NameError: name 'fr1' is not defined
