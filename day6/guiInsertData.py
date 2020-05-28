# this is a GUI developed for inserting data in postgress database
import tkinter as tk
import tkinter.font as font
import psycopg2
import tkinter.messagebox

root = tk.Tk()
root.geometry('1000x700')
root.title('Teckat')

# postgress database connection
connection = psycopg2.connect(
    dbname='webinardb', user="postgres", password="mithukundu60@", host="localhost", port="5432")

print("connection established")

# creating cursor

cursor = connection.cursor()

# font heading
fontSizeHeading = font.Font(size=20)
fontSizeData = font.Font(size=15)
# name address department_no salary
# ==================================== function ================================


def addData():
    name = entryAddName.get()
    address = entryAddAddress.get()
    department = entryAddDepartment.get()
    salary = entryAddSalary.get()

    print(type(name), type(address), type(department), type(salary))
    if(name and address and department and salary):
        query = "INSERT INTO employees(name,address,department_number,salary) values('" + \
            name+"','"+address+"','"+department+"','"+salary+"');"
        cursor.execute(query)
        connection.commit()
        print("data entered successfully")
        tk.messagebox.showinfo("Teckat", "data entered successfully")

        entryAddName.delete(0, tk.END)
        entryAddAddress.delete(0, tk.END)
        entryAddDepartment.delete(0, tk.END)
        entryAddSalary.delete(0, tk.END)
        entryAddName.focus()
    else:
        tk.messagebox.showinfo("Teckat", "Invalid Data")


    # ==================================== GUI =======================================
    # Adding main label
addDataLabel = tk.Label(root, text="Add Data", font=fontSizeHeading)
addDataLabel.grid(row=0, column=1, pady=5)

# adding data labels
entryAddNameLabel = tk.Label(root, text="Name : ", font=fontSizeData)
entryAddNameLabel.grid(row=1, column=0, pady=5)
entryAddAddressLabel = tk.Label(root, text="Address : ", font=fontSizeData)
entryAddAddressLabel.grid(row=2, column=0, pady=5)
entryAddDepartmentLabel = tk.Label(
    root, text="Department no. : ", font=fontSizeData)
entryAddDepartmentLabel.grid(row=3, column=0, pady=5)
entryAddSalaryLabel = tk.Label(root, text="Salary : ", font=fontSizeData)
entryAddSalaryLabel.grid(row=4, column=0, pady=5)

# Adding entry form

entryAddName = tk.Entry(root, width=50)
entryAddName.grid(row=1, column=1, ipady=7)
entryAddAddress = tk.Entry(root, width=50)
entryAddAddress.grid(row=2, column=1, ipady=7)
entryAddDepartment = tk.Entry(root, width=50)
entryAddDepartment.grid(row=3, column=1, ipady=7)
entryAddSalary = tk.Entry(root, width=50)
entryAddSalary.grid(row=4, column=1, ipady=7)

# subit data button
submitDataButton = tk.Button(
    root, text="Submit Data", font=fontSizeData, command=addData)
submitDataButton.grid(row=5, column=1, pady=5, ipady=5)


root.mainloop()
