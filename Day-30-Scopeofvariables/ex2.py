# Scope of Global Variable:

# def Main_Fun():
#     Local1 = 'Gowthami'
#     print('local variable:',Local1)
# Main_Fun()
# print('local variable:',Local1)
# NameError: name 'Local1' is not defined


# Socpe: we can use amywhere
x1 = 'Keerthana'
print('global variable:',x1)
def Main_Fun():
    Local1 = 'Gowthami'
    print('local variable:',Local1)
    print('global variable:', x1)
Main_Fun()
print('global variable:',x1)