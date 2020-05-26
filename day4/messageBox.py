import tkinter as tk
import tkinter.messagebox

# Create a window

root = tk.Tk()


def onClick():
    tk.messagebox.showinfo("Teckat", "Welcome to Teckat")


def answer():
    result = tk.messagebox.askquestion("question", "Do you like this course")
    print(result)

    if (result == "yes"):
        tk.messagebox.showinfo("Teckat", "Thank you for liking the course")
    else:
        tk.messagebox.showinfo(
            "Teckat", "Sorry, we will try to make it better")


# create a button
click = tk.Button(root, text="Click to display", command=onClick)
question = tk.Button(root, text="answer question", command=answer)
click.pack()
question.pack()
root.mainloop()
