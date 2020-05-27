import tkinter as tk
import parser
i = 0

# create a window

root = tk.Tk()
root.title("calculator")
# ========================== functions =============================================


def insertValue(num):
    global i
    display.insert(i, num)
    i += 1


def clear():
    display.delete(0, tk.END)


def calculate():
    string = display.get()
    print(string, type(string))

    try:
        result = eval(parser.expr(string).compile())
        print(result)
        clear()
        display.insert(0, result)
    except Exception:
        clear()
        display.insert(0, "Error")


# ======================= GUI =====================================================
display = tk.Entry(root)
display.grid(row=0, columnspan=4, sticky=tk.W+tk.E)

tk.Button(root, text="1", width=5,
          command=lambda: insertValue(1)).grid(row=1, column=0)
tk.Button(root, text="2", width=5,
          command=lambda: insertValue(2)).grid(row=1, column=1)
tk.Button(root, text="3", width=5,
          command=lambda: insertValue(3)).grid(row=1, column=2)

tk.Button(root, text="4", width=5,
          command=lambda: insertValue(4)).grid(row=2, column=0)
tk.Button(root, text="5", width=5,
          command=lambda: insertValue(5)).grid(row=2, column=1)
tk.Button(root, text="6", width=5,
          command=lambda: insertValue(6)).grid(row=2, column=2)

tk.Button(root, text="7", width=5,
          command=lambda: insertValue(7)).grid(row=3, column=0)
tk.Button(root, text="8", width=5,
          command=lambda: insertValue(8)).grid(row=3, column=1)
tk.Button(root, text="9", width=5,
          command=lambda: insertValue(9)).grid(row=3, column=2)

tk.Button(root, text="0", width=5,
          command=lambda: insertValue(0)).grid(row=4, column=1)

tk.Button(root, text="+", width=5,
          command=lambda: insertValue("+")).grid(row=1, column=3)
tk.Button(root, text="-", width=5,
          command=lambda: insertValue("-")).grid(row=2, column=3)
tk.Button(root, text="*", width=5,
          command=lambda: insertValue("*")).grid(row=3, column=3)
tk.Button(root, text="/", width=5,
          command=lambda: insertValue("/")).grid(row=4, column=3)


tk.Button(root, text="AC", width=5, command=clear).grid(row=4, column=0)
tk.Button(root, text="=", width=5, command=calculate).grid(row=4, column=2)
root.mainloop()
