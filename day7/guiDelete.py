# this is a GUI developed for deleting data from postgress database
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

# deleteing data from database

# ========================= function ==============================================


def deleteData():
    deleteId = entryId.get()

    if(deleteId):
        query = "DELETE FROM employees where id="+deleteId+";"
        cursor.execute(query)
        connection.commit()
        tk.messagebox.showinfo(
            "Teckat", "Your Data has been deleted Successfully")
        entryId.delete(0, tk.END)
        entryId.focus()
    else:

        tk.messagebox.showinfo(
            "Teckat", "Invalid Data")
        entryId.delete(0, tk.END)
        entryId.focus()


# =========================== GUI =================================================

entryDeleteLabel = tk.Label(root, text='Delete Data', font=fontSizeHeading)
entryDeleteLabel.grid(row=0, column=1)

entryIdLabel = tk.Label(root, text='Enter Id : ', font=fontSizeData)
entryIdLabel.grid(row=1, column=0)

entryId = tk.Entry(root)
entryId.grid(row=1, column=1)

deleteButton = tk.Button(root, text="delete Data : ",
                         font=fontSizeData, command=deleteData)
deleteButton.grid(row=2, column=1)
root.mainloop()
