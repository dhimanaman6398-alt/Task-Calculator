import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]


for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(
            root,
            text=text,
            font=("Arial", 18),
            command=calculate,
            bg="lightgreen"
        )
    else:
        btn = tk.Button(
            root,
            text=text,
            font=("Arial", 18),
            command=lambda t=text: click(t)
        )

    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")


clear_btn = tk.Button(
    root,
    text="C",
    font=("Arial", 18),
    command=clear,
    bg="tomato"
)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()