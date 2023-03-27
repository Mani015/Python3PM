
z = ['mani','arjun','vinod','vishal','vivek','manoj','prasanth','dhanapal','viswa','sunil','manik']
print(z)
#['mani', 'arjun', 'vinod', 'vishal', 'vivek', 'manoj', 'prasanth', 'dhanapal', 'viswa', 'sunil', 'manik']
z.remove('manoj')
print(z)
# ['mani', 'arjun', 'vinod', 'vishal', 'vivek', 'prasanth', 'dhanapal', 'viswa', 'sunil', 'manik']

z.remove('vishal')
print(z)
# ['mani', 'arjun', 'vinod', 'vivek', 'prasanth', 'dhanapal', 'viswa', 'sunil', 'manik']

z.remove('vinod')
print(z)

# ['mani', 'arjun', 'vivek', 'prasanth', 'dhanapal', 'viswa', 'sunil', 'manik']

z.remove('mani')
print(z)
# ['arjun', 'vivek', 'prasanth', 'dhanapal', 'viswa', 'sunil', 'manik']

# z.remove('santhosh')
# print(z)

# ValueError: z.remove(x): x not in list


z.remove('vivek','sunil')
print(z)

# TypeError: list.remove() takes exactly one argument (2 given)


