
import  mysql.connector

x1 = mysql.connector.connect(host='localhost',user='root',password='root',database='pen')
# # Cursor: cursor as an object basically communicate an entire mysql db server on you own database
x2 = x1.cursor()


# t1 = x2.execute('create table stu(sno int, fname varchar(30), lname varchar(30), age int, marks int)')

# print(t1)








x2.execute('show tables')

for i in x2:
    print(i)

# ('stu',)



