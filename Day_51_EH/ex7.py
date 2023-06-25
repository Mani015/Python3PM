
# try:
#     print(x)
# except ValueError:
#     print('value error occured and Handle')
# except IndexError:
#     print('Index error occured and Handle')
# except:
#     print('Default error')
#
# except NameError:
#     print('Name Error occured and Handle')
#
# print('complete excution, this is last line')


# SyntaxError: default 'except:' must be last


try:
    print(x)
except ValueError:
    print('value error occured and Handle')
except IndexError:
    print('Index error occured and Handle')
except NameError:
    print('Name Error occured and Handle')
except:
    print('Default error')
print('complete excution, this is last line')

# Name Error occured and Handle
# complete excution, this is last line