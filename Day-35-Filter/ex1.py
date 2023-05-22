
# FIlter:

def Vowels(k):
    if k not in 'aeiou':
        return k

# sen = input('Enter one sentence:')
# f1 = filter(Vowels,sen)
# print(list(f1))

# Enter one sentence:banglore is a beatiful city
# ['b', 'n', 'g', 'l', 'r', ' ', 's', ' ', ' ', 'b', 't', 'f', 'l', ' ', 'c', 't', 'y']


# Using FIlter:
print(tuple(filter(lambda x: x not in 'aeiou','love your enemies and do good to them')))
# ('l', 'v', ' ', 'y', 'r', ' ', 'n', 'm', 's', ' ', 'n', 'd', ' ', 'd', ' ', 'g', 'd', ' ', 't', ' ', 't', 'h', 'm')
