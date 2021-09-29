from tkinter import *
from tkinter import messagebox
from dashboard import Dashboard
from AdminModel import AdminModel

class Login:
    def authLogin(self):
        if self.usernameText.get() == "" or self.passwordText.get() == "":
            messagebox.showerror(
                "Error", "Username and Password field are required", parent=self.frame)
        else:
            if AdminModel().auth(self.usernameText.get(), self.passwordText.get()):
                Dashboard(self.master)
                self.frame.destroy()
            else:
                messagebox.showerror(
                    "Error", "Invalid username and password", parent=self.frame)

    def __init__(self, master):
        self.master = master
        self.master.title("PSB-Inventory-Management - Login")
        self.master.geometry("1350x700+0+0")

        self.frame = Frame(master)
        self.frame.pack()

        self.username = Label(self.frame, text="Username")
        self.username.grid(row=0, column=0)

        self.password = Label(self.frame, text="Password")
        self.password.grid(row=1, column=0)

        self.usernameText = Entry(self.frame)
        self.usernameText.grid(row=0, column=1)

        self.passwordText = Entry(self.frame)
        self.passwordText.grid(row=1, column=1)

        self.loginButton = Button(
            self.frame, text="Login", command=self.authLogin)
        self.loginButton.grid(row=2, column=1, padx=10, pady=10)


master = Tk()
obj = Login(master)
master.mainloop()

""" root = tk.Tk()

root.title("PSB-Inventory-Management")

title = tk.Label(root, text="Login", font=("Helvetica", 16))
title.pack()

usernameLabel = tk.Label(root, text="Username")
usernameText = tk.Entry(root, width=20)
usernameLabel.pack()
usernameText.pack()

passwordLabel = tk.Label(root, text="Password")
passwordText = tk.Entry(root, width=20)
passwordLabel.pack()
passwordText.pack()


def addItem():
    if usernameText.get() == "" or passwordText.get() == "":
    res = tk.messagebox.showerror(
        "Error", "Username and Password field are required")
    res.pack()

    print(usernameText.get())


canvas = tk.Canvas(root, width=700, height=700)
canvas.pack()

submitBtn = tk.Button(root, text="Submit", command=addItem)
submitBtn.pack()

root.mainloop() """

# import modules
"""  
from tkinter import *
import os
 

 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter your username and passward to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 

 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Login to gain Access", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    
 
    main_screen.mainloop()
 
 
main_account_screen() """
