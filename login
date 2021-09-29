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
