

def Outer():
    print('I am outer function')
    def Inner():
        print('I am inner fucntion')
    Inner()

print('start')
# Outer()
print('end')
# start
# end