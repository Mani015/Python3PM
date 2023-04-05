

x1 = {'vivo':10000,'redmi':20000,'samsung':25000,'apple':500000,'realme':30000,'one+':40000,'vivo':26000}

print(x1.get('vivo'))
# 26000

print(x1.get('redmi'))
# 20000
print(x1.get('samsung'))
# 25000
print(x1.get('apple'))
# 50000
print(x1.get('realme'))
# 30000
print(x1.get('one+'))
# 40000


print(x1.get('lava'))
# None