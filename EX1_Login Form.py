from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Login Form")
window.geometry("500x360")

header = Label(window, text="Login Form", font=("Arial", 15, 'bold'))
header.pack()

username_text = Label(window, text="Enter Username: ")
username_text.place(x=0,y=300)

password_text = Label(window, text="Enter Password: ")
password_text.place(x=0,y=450)

username = Entry(window)
username.place(x=335, y=300)

password = Entry(window, show="*")
password.place(x=335, y=450)

def login():
    user = username.get()
    pwd = password.get()
    
    if user == "" or pwd == "":
        messagebox.showwarning("Warning", "Fill in the blanks!")
    else:
        messagebox.showinfo("Login Success", f"Welcome, {user}!")
        
        
login_btn = Button(window, text="Login", command=login, fg="white", bg="blue")
login_btn.place(x=430, y=700)         

window.mainloop()
