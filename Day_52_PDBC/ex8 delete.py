import mysql.connector

db=mysql.connector.connect(host='localhost', user='root', password='root',database='pen')

mydb=db.cursor()

my='delete from stu where age=27'
mydb.execute(my)

db.commit()