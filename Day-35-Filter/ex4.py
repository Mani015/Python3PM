# map with filter:

print(list(filter(lambda x: x%2==0, map(lambda x: x**2,range(1,15)))))
# [4, 16, 36, 64, 100, 144, 196]

