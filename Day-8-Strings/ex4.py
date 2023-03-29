z = 'hello,energy,mental,power,pepper'
print(z)
# hello,energy,mental,power,pepper
print()
# print(z.replace('e','0'))
# h0llo,0n0rgy,m0ntal,pow0r,p0pp0r


# sy: objectname.replace(oldname,newname,count)
print(z.replace('e','0',1))
# h0llo,energy,mental,power,pepper

print(z.replace('e','0',2))
# h0llo,0nergy,mental,power,pepper

print(z.replace('e','0',3))
# h0llo,0n0rgy,mental,power,pepper

print(z.replace('e','0',4))
# h0llo,0n0rgy,m0ntal,power,pepper

print(z.replace('e','0',5))
# h0llo,0n0rgy,m0ntal,pow0r,pepper

