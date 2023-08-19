
# With out Decoration
def Out_func(Fun):
    def In_func():
        New = Fun()  #<function Out_func.<locals>.In_func at 0x000002630DD821F0>
        return New.upper()
    return In_func
def New_Feature():  # New Fucntionality
    return 'python developer'


Decoration = Out_func(New_Feature)
print(Decoration())
# PYTHON DEVELOPER

# AttributeError: 'function' object has no attribute 'upper'