from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("400x400")
window.title("Food Order Form")

heading = Label(window, text="What would you like sir?", font=("Arial", 15))
heading.pack(pady=10)

# Variables to track selections (0 = not selected, 1 = selected)
pizza_var = IntVar()
burger_var = IntVar()
pasta_var = IntVar() 

# Use Checkbuttons so multiple items can be selected/unselected
Checkbutton(window, text="Pizza", variable=pizza_var).place(x=50, y=150, anchor='w')
Checkbutton(window, text="Burger", variable=burger_var).place(x=50, y=200, anchor='w')
Checkbutton(window, text="Pasta", variable=pasta_var).place(x=50, y=255, anchor='w')

def submit():
    orders = []
    if pizza_var.get():
        orders.append("Pizza")
    if burger_var.get():
        orders.append("Burger")
    if pasta_var.get():
        orders.append("Pasta")

    if not orders:
        messagebox.showwarning("Warning", "You didn't select any orders!")
    else:    
        messagebox.showinfo("Delivery Message", "You ordered: " + ", ".join(orders))

Button(window, text="Submit", bg="green", fg="white",
       activebackground="darkgreen", command=submit).place(x=150, y=320)

window.mainloop()
