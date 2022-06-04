import mysql.connector

databaseName="egdb"

config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': databaseName,
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
query="Select id,name from employees"
cursor=cnx.cursor()
cursor.execute("USE "+databaseName)
cursor.execute(query)
for (id,name) in cursor:
	print("Your Id is {}, Name is {} ".format(id, name))
cnx.commit()
cursor.close()
cnx.close()