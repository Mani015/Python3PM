import mysql.connector

db=mysql.connector.connect(host='localhost', user='root', password='root',database='pen')

mydb=db.cursor()
mydb.execute("select * from stu")


# print(mydb)
for i in mydb:
    print(i)

# (1, 'hari', 'naath', 20, 90)
# (2, 'bharath', 'varma', 27, 90)
