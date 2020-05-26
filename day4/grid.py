import tkinter as tk

# Create a window

root = tk.Tk()

name1 = tk.Label(root, text="Aman")
name2 = tk.Label(root, text="Rahul")
name3 = tk.Label(root, text="Manoj")

name1.grid(row=0, column=0)
name2.grid(row=1, column=1)
name3.grid(row=3, column=3)

root.mainloop()
