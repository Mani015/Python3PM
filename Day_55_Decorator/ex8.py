def my_decor(func):
    def my_wrap(str1, str2):
        print("Decorator Function")
        return func(str1, str2)
    return my_wrap
def my_function(str1, str2):
    print("Main Function")
    print(str1 + " are " +  str2)
my_function = my_decor(my_function)
my_function("Mangoes", "Sweet")

# Decorator Function
# Main Function
# Mangoes are Sweet
