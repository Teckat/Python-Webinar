import psycopg2

connection = psycopg2.connect(
    dbname='webinardb', user="postgres", password="mithukundu60@", host="localhost", port="5432")

print("connection established")

# creating cursor

cursor = connection.cursor()

# execute
query = "select * from employees where salary>20000;"
cursor.execute(query)

print("query executed")

row = cursor.fetchall()
print(row)
print(row[0][1])
connection.commit()
connection.close()
