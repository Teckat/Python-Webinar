import tkinter as tk

# Create a window

root = tk.Tk()

# creating frame
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

frame1.pack()
frame2.pack(side=tk.BOTTOM)

Name = tk.Label(frame1, text="frame 1", fg="red")
name2 = tk.Label(frame2, text="frame 2", fg="blue")

Name.pack()
name2.pack()

root.mainloop()
