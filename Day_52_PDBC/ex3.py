import mysql.connector


x1 = mysql.connector.connect(host='localhost',user='root',password='root')

x2 = x1.cursor()

x2.execute('create database pen')

print(x2)


# x2.execute('show databases')
# for i in x2:
#     print(i)

