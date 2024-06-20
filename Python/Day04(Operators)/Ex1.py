# Membership Operator works on Iterables [list,tuple,set,dict]
# Membership Operators it contains two here : in, not in

# in : To check the Specified Item is exist in the Given object
Friends = ['Anitha','Prasanna','Jeevan','Vandana']
# Returns True : when the Specified item is present in the given object or variableName
# sy : value in variablename
print('Anitha' in Friends)
# True

# Returns False : when the Specified item is not  present in the given object or variableName

print('Santhosh' in Friends)
# False
# ------------------------------------------------------------------------

# not in :
# True : when the Specified item is not  present in the given object or variableName
print('Samantha' not in Friends)
# True
# False: when the Specified item is present in the given object or variableName
print('Prasanna' not in Friends)
# False
