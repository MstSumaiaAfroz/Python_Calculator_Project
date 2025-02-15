import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
expression = ""

def press_button(value):
    global expression
    expression += str(value)
    input_text.set(expression)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except Exception as e:
        input_text.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    input_text.set("")

input_text = tk.StringVar()

display = tk.Entry(root, textvariable=input_text, font=("Arial", 20), justify="right", bd=8, relief="sunken")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]
row, col = 1, 0
for button in buttons:
    if button == "C":
        action = clear
    elif button == "=":
        action = calculate
    else:
        action = lambda x=button: press_button(x)

    tk.Button(
        root, text=button, font=("Arial", 18), command=action, width=5, height=2
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:  
        col = 0
        row += 1
root.mainloop()