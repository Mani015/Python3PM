import mysql.connector

x1 = mysql.connector.connect(host='localhost',user='root',password='root')

# print(x1)


x2 = x1.cursor()

x2.execute('show databases')

# print(x2)
for i in x2:
    print(i)

# ('dell',)
# ('information_schema',)
# ('mango',)
# ('mysql',)
# ('performance_schema',)
# ('sys',)

