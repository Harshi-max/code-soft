import tkinter as tk

# Function to update the expression in the text entry widget
def click(event):
    current_text = entry.get()
    new_text = event.widget.cget("text")
    
    if new_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif new_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, new_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the expression
entry = tk.Entry(root, width=20, font=("Arial", 24), bd=10, borderwidth=4, relief="ridge")
entry.grid(row=0, column=0, columnspan=4)

# Button labels in a list
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and place buttons in a grid
row_val = 1
col_val = 0

for button in buttons:
    btn = tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18))
    btn.grid(row=row_val, column=col_val)
    btn.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the Tkinter event loop
root.mainloop()
