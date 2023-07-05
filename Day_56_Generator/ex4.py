

# using while loop


x = map(lambda i : i**2,range(1,11))



while True:
    try:
        value = next(x)
        print(value)
    except StopIteration:
        print('iteration completed ,No values')
        break


# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
# iteration completed ,No values
