import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',password='root',database='pen')

mydb = db.cursor()


mydb1='update stu set fname="Tony" where  marks=100'
mydb.execute(mydb1)
db.commit()