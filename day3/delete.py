import psycopg2

connection = psycopg2.connect(
    dbname='webinardb', user="postgres", password="mithukundu60@", host="localhost", port="5432")

print("connection established")

# creating cursor

cursor = connection.cursor()

# execute
delId = "2"
# query = "DELETE FROM employees where id="+delId+";"
query = "DELETE FROM employees where id=2;"

cursor.execute(query)
print("data deleted successfully")

connection.commit()
connection.close()
