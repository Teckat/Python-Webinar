import tkinter as tk

# Create a window

root = tk.Tk()

name1 = tk.Label(root, text="Aman")
name2 = tk.Label(root, text="Rahul")
name3 = tk.Label(root, text="Manoj")

# place-> change position accordingly, we can change relative to the screen size, change height and width, relative height and width

name1.place(relx=.3, rely=.7)
name2.place(relx=.4, rely=.8)
name3.place(x=0, y=50)

root.mainloop()
