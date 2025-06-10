import tkinter as tk
import math

def on_button_click(button):
    if button == "C":
        display.delete(0, tk.END)
    elif button == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            error()
    elif button == "√":
        try:
            value = float(display.get())
            result = math.sqrt(value)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            error()
    elif button == "%":
        try:
            value = float(display.get())
            result = value / 100
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            error()
    else:
        display.insert(tk.END, button)

def error():
    display.delete(0, tk.END)
    display.insert(tk.END, "Помилка")
    root.after(2, lambda: display.delete(0, tk.END))


def set_theme(theme):
    if theme == "light":
        root.config (bg ="lightgray")
        display.config (bg = "lightgray", fg = "black")
    elif theme == "dark":
        root.config(bg = "black")
        display.config(bg= "gray", fg= "black")
    elif theme == "skyblue":
        root.config(bg = "skyblue")
        display.config(bg = "skyblue", fg = "white")
    elif theme == "deep pink":
        root.config(bg = "deep pink")
        display.config(bg = "deep pink", fg = "white")
    elif theme == "aqua":
        root.config(bg="aquamarine")
        display.config(bg="aquamarine", fg="black")
    for button in buttons:
        button.config(bg = "lightgray" if theme == "light" else "darkgray" if theme == "dark" else "lightblue" if theme == "skyblue" else "darkgray" if theme == "pink" else "white" if theme == "aqua" else "white", fg = "black")

root = tk.Tk()
root.title("Калькулятор")
root.geometry("385x450")

display = tk.Entry(root, font = ("Arial", 24), justify = "right")
display.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

buttons = []
button_texts = [

'7', '8', '9', '/',
'4', '5', '6', '*',
'1', '2', '3', '-',
'C', '0', '=', '+',
'.', '%', '√',

]

row_val = 1
col_val = 0

for text in button_texts:
    button = tk.Button(root, text = text, font = ("Arial", 18), width = 5, height = 2,
    command = lambda text = text: on_button_click(text))
    button.grid(row = row_val, column = col_val)
    buttons.append(button)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff = 0)
theme_menu.add_command(label = "Світла тема", command = lambda: set_theme("light"))
theme_menu.add_command(label = "Темна тема", command = lambda: set_theme("dark"))
theme_menu.add_command(label = "Небесно синя тема", command = lambda: set_theme("skyblue"))
theme_menu.add_command(label = "Розова тема", command = lambda: set_theme("deep pink"))
theme_menu.add_command(label = "Аквамаринова тема", command = lambda: set_theme("aqua"))
menubar.add_cascade(label = "Змінити тему", menu=theme_menu)

root.config(menu = menubar)
set_theme("light")
root.mainloop()