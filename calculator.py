import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.config(bg="#2B2B2B")

expression = ""

# Dark mode colors
bg_color = "#2B2B2B"
display_bg = "#1E1E1E"
display_fg = "#FFFFFF"
button_bg = "#3C3C3C"
button_fg = "#FFFFFF"

display = tk.Entry(root, font=("Arial", 20), justify="right", bg=display_bg, fg=display_fg, bd=0)
display.pack(fill="both", padx=5, pady=5)

def click(char):
    global expression
    if char == "=":
        try:
            result = eval(expression)
            expression = str(result)
            display.delete(0, tk.END)
            display.insert(0, expression)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
            expression = ""
    elif char == "C":
        expression = ""
        display.delete(0, tk.END)
    else:
        expression += str(char)
        display.delete(0, tk.END)
        display.insert(0, expression)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

for row in buttons:
    frame = tk.Frame(root, bg=bg_color)
    frame.pack(fill="both", expand=True)
    for btn_text in row:
        tk.Button(
            frame, 
            text=btn_text, 
            font=("Arial", 16), 
            command=lambda x=btn_text: click(x),
            bg=button_bg,
            fg=button_fg,
            activebackground="#4A4A4A",
            activeforeground=button_fg,
            bd=0
        ).pack(side="left", fill="both", expand=True, padx=2, pady=2)

root.mainloop()
