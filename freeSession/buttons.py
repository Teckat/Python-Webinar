# creating frames and adding buttons to it


import tkinter as tk
root = tk.Tk()


buttonTop = tk.Button(root, text="click here", fg="#ff00ff")
buttonTop.pack()

label = tk.Label(root, text="Hello")
label.pack()

buttonBottom = tk.Button(root, text="click here", fg="#ff00ff")
buttonBottom.pack()

root.mainloop()
