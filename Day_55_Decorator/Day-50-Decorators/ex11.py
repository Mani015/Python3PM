
def d1(func):
    def d2(userName, passWord):
        return "User Name and Password: ", list(func(userName, passWord))
    return d2

@d1
def d3(userName, passWord):
    return userName, passWord

print(d3("Vishal", "Vishal123"))
# ('User Name and Password: ', ['Vishal', 'Vishal123'])