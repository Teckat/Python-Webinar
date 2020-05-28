import psycopg2

connection = psycopg2.connect(
    dbname='webinardb', user="postgres", password="mithukundu60@", host="localhost", port="5432")

print("connection established")

# creating cursor

cursor = connection.cursor()

# input

name = input('Enter Name')
address = input('Enter Address')
department_no = input('enter department number')
salary = input('enter salary')


query = "INSERT INTO employees(name, address,department_number, salary) values('" + \
    name+"','"+address+"','"+department_no+"','"+salary+"');"
cursor.execute(query)
# query = "INSERT INTO employees(name, address,department_number, salary) values(%s,%s,%s,%s);"
# cursor.execute(query, (name, address, department_no, salary))

print("Data inserted successfully")

connection.commit()
connection.close()
