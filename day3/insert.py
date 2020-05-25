import psycopg2

connection = psycopg2.connect(
    dbname='webinardb', user="postgres", password="mithukundu60@", host="localhost", port="5432")

print("connection established")

# creating cursor

cursor = connection.cursor()

# execute

cursor.execute(
    ''' INSERT INTO employees(name, address,department_number, salary) values('Anita', 'jsr','04','20000.13')''')

print("Data inserted successfully")

connection.commit()
connection.close()
