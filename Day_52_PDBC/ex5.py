# import mysql.connector
#
# x1 = mysql.connector.connect(host='localhost',user='root',password='root',database='pen')
#
# x2 = x1.cursor()
#
#
# t1 = "insert into stu(sno,fname,lname,age,marks) values (%s,%s,%s,%s)"
#
# d1 = [(1,'rangith','kumar',20,97),(2,'bharath','varma',27,98)]
# x2.executemany(t1,d1)
#
# x1.commit()



import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',password='root',database='pen')


mydb=db.cursor()

data="Insert into stu(sno, fname, lname, age,marks) values (%s, %s,%s,%s,%s)"
cat=[(1,'hari','naath',20,90),(2,'bharath','varma',27,90)]

mydb.executemany(data,cat)
db.commit()

