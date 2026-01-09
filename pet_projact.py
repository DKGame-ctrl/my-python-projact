import tkinter as tk
import math


def press(value):
    entry.insert(tk.END, value)


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        expr = entry.get()
        # evaluate the expression safely enough for this simple calculator
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        clear()
        entry.insert(0, "Error")


def sqrt():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        clear()
        entry.insert(0, "Error")


root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(0, 0)

entry = tk.Entry(root, font=("Arial", 20), justify=tk.RIGHT)
entry.pack(fill="x", padx=10, pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'C', '+',
    '√', '='
]

row_val = 0
col_val = 0

for b in buttons:
    if b == '=':
        cmd = calculate
    elif b == 'C':
        cmd = clear
    elif b == '√':
        cmd = sqrt
    else:
        cmd = lambda x=b: press(x)

    bth = tk.Button(
        frame,
        text=b,
        width=5,
        height=2,
        font=("Arial", 16),
        command=cmd,
    )
    bth.grid(row=row_val, column=col_val, padx=5, pady=2)

    col_val += 1
    if col_val == 4:
        col_val = 0
        row_val += 1

root.mainloop()