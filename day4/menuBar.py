import tkinter as tk

# Create a window

root = tk.Tk()


def onClick():
    print("button clicked")


# creating menu
menu = tk.Menu(root)
root.config(menu=menu)


# elements of menu
file = tk.Menu(menu)
edit = tk.Menu(menu)

# adding elements to the menu
menu.add_cascade(label="File", menu=file)
menu.add_cascade(label="edit", menu=edit)

# adding elements to subMenu
file.add_cascade(label="new file")
file.add_cascade(label="Save")
file.add_cascade(label="Save as")

file.add_separator()
file.add_cascade(label="exit", command=onClick)

edit.add_cascade(label="undo")
edit.add_cascade(label="redo")

root.mainloop()
