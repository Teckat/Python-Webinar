import psycopg2

connection = psycopg2.connect(
    dbname='webinardb', user="postgres", password="mithukundu60@", host="localhost", port="5432")

print("connection established")

# creating cursor

cursor = connection.cursor()

# cursor execution

cursor.execute(
    '''create table employees(ID serial,name text,address text, department_number int, salary float); ''')
print("table created")

# commit the connection

connection.commit()
connection.close()
