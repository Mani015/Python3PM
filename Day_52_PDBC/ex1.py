import mysql.connector

x1 = mysql.connector.connect(host='localhost',user='root',password='root')

print(x1)

if x1:
    print('connected to mysql successfully')
else:
    print('connected to mysql unsuccessfully')



# <mysql.connector.connection_cext.CMySQLConnection object at 0x000002361C37B160>
# connected to mysql successfully
