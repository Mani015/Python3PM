
# 4).Nested Functions in Python

# def Outer_fun(num1):
#     def Inner_fun(num2):
#         return 'sum of num1 + num2',num2 + num1
#     print(Inner_fun(5))
# Outer_fun(5)
# ('sum of num1 + num2', 10)


def Outer_fun(num1):
    def Inner_fun(num2):
        return 'sum of num1 + num2',num2 + num1
    return Inner_fun(5)
print(Outer_fun(5))

# ('sum of num1 + num2', 10)
