import tkinter as tk

# Create a window

root = tk.Tk()


def onClick():
    print("Button clicked")


# create a button
click = tk.Button(root, text="Click to display", command=onClick)

click.pack()

root.mainloop()
