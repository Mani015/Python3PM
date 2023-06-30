# @ Symbol With Decorator
# Instead of assigning the function call to a variable,
# Python provides a much more elegant way to achieve this functionality using the @ symbol. For example,

def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()
