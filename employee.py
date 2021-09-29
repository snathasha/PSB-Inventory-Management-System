from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from EmployeeModel import EmployeeModel


class Employee:
    def __init__(self, master):
        self.master = master
        self.master.title("PSB-Inventory-Management - Employee")
        self.master.geometry("1350x700+0+0")
        self.frame = Frame(master)
        self.frame.pack()

        # main Form-----------------------------------------------------
        self.nameLabel = Label(self.frame, text="Name")
        self.nameLabel.grid(row=0, column=0)

        self.empLabel = Label(self.frame, text="Employee_no")
        self.empLabel.grid(row=1, column=0)

        self.dateLabel = Label(self.frame, text="Registered at")
        self.dateLabel.grid(row=2, column=0)

        self.name = Entry(self.frame)
        self.name.grid(row=0, column=1)

        self.emp_no = Entry(self.frame)
        self.emp_no.grid(row=1, column=1)

        self.date = Entry(self.frame)
        self.date.grid(row=2, column=1)

        # Item Form-----------------------------------------------------
        self.frameItem = Frame(master)

        self.nameLabel = Label(self.frameItem, text="Employee")
        self.nameLabel.grid(row=0, column=4)

        self.empLabel = Label(self.frameItem, text="Item")
        self.empLabel.grid(row=1, column=4)

        self.dateLabel = Label(self.frameItem, text="Qty")
        self.dateLabel.grid(row=2, column=4)

        self.dateLabel = Label(self.frameItem, text="Registered at")
        self.dateLabel.grid(row=3, column=4)

        self.employee = Entry(self.frameItem)
        self.employee.grid(row=0, column=5)

        self.itemvalues = EmployeeModel().getItem()

        self.item_id = Combobox(
            self.frameItem, values=self.itemvalues)
        self.item_id.grid(row=1, column=5)

        self.qty = Entry(self.frameItem)
        self.qty.grid(row=2, column=5)

        self.datei = Entry(self.frameItem)
        self.datei.grid(row=3, column=5)

        # action Form-----------------------------------------------------
        self.loginButton = Button(
            self.frame, text="Add Employee", command=self.addEmployee)
        self.loginButton.grid(row=3, column=1)

        self.showButton = Button(
            self.frame, text="Offer Items", command=self.fromItem)
        self.showButton.grid(row=3, column=2)

        self.assignButton = Button(
            self.frame, text="Received Items", command=self.showItem)
        self.assignButton.grid(row=3, column=4)

        self.clearButton = Button(
            self.frame, text="All Clear", command=self.clearData)
        self.clearButton.grid(row=3, column=5)

        # Sort---------------------------
        self.col = Combobox(self.frame, values=(
            'name', 'employee_no', 'registered_at'))
        self.col.grid(row=6, column=1)

        self.order = Combobox(self.frame, values=('asc', 'desc'))
        self.order.grid(row=6, column=2)

        self.searchButton = Button(
            self.frame, text="Sort", command=self.sortItem)
        self.searchButton.grid(row=6, column=3)

        # Search---------------------------
        self.search = Entry(self.frame)
        self.search.grid(row=6, column=4)

        self.searchButton = Button(
            self.frame, text="Search", command=self.searchItem)
        self.searchButton.grid(row=6, column=5)

        # Table-----------------------------------------------------
        self.frameTable = Frame(master)
        self.frameTable.pack()
        # columns
        columns = ('#1', '#2', '#3', '#4')

        self.tree = Treeview(self.frameTable, columns=columns, show='headings')

        # define headings
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Name')
        self.tree.heading('#3', text='Employee No')
        self.tree.heading('#4', text='Date')

        self.tree.pack()
        self.getEmployee()

    def addEmployee(self):
        if self.name.get() == "":
            messagebox.showerror("Error", "Please enter name")
        elif self.emp_no.get() == "":
            messagebox.showerror("Error", "Please enter employee no")
        elif self.date.get() == "":
            messagebox.showerror("Error", "Please enter registerd date")
        else:
            try:

                EmployeeModel().create(self.name.get(), self.emp_no.get(), self.date.get())
                self.clearData()
                self.getEmployee()
                messagebox.showinfo("Success", "Employee added")
            except Exception as e:
                messagebox.showerror("Error", e)

    def getEmployee(self):
        try:
            lst = EmployeeModel().get()
            for i in lst:
                self.tree.insert('', 'end', values=i)

        except Exception as e:
            messagebox.showerror("ErrorF", e)

    def showItem(self):
        if self.tree.selection():
            if hasattr(self, 'frameshow'):
                self.frameshow.destroy()
            self.frameshow = Frame(self.master)
            x = self.tree.selection()[0]
            item = self.tree.item(x)['values']
            self.frameshow.pack()

            columns = ('#1', '#2', '#3')
            self.treeshow = Treeview(
                self.frameshow, columns=columns, show='headings')
            self.treeshow.heading('#1', text='Item')
            self.treeshow.heading('#2', text='Qty')
            self.treeshow.heading('#3', text='Date')
            self.treeshow.pack()

            self.nameLabel1 = Label(self.frameshow, text="Name :" + item[1])
            self.nameLabel1.pack()
            try:
                lst = EmployeeModel().show(item[0])
                for i in lst:
                    items = [i[5], i[12], i[13]]
                    self.treeshow.insert('', 'end', values=items)

            except Exception as e:
                messagebox.showerror("Error", e)
        else:
            messagebox.showerror(
                "Error", "Please select the row you want to show")

    def fromItem(self):
        if self.tree.selection():
            if hasattr(self, 'frameshow'):
                self.frameshow.destroy()

            if hasattr(self, 'itemvalues'):
                self.itemvalues = EmployeeModel().getItem()

            x = self.tree.selection()[0]
            item = self.tree.item(x)['values']

            self.employee_id = item[0]
            self.qty.delete(0, END)
            self.datei.delete(0, END)

            self.employee.insert(0, item[1])
            self.frameItem.pack()

            self.assignButton = Button(
                self.frameItem, text="Apply to Employee", command=self.assignItem)
            self.assignButton.grid(row=5, column=5)
        else:
            messagebox.showerror(
                "Error", "Please select the row you want to assign")

    def assignItem(self):
        if self.item_id.get().partition(' ')[0] == "":
            messagebox.showerror("Error", "Please select item")
        elif self.qty.get() == "":
            messagebox.showerror("Error", "Please enter qty")
        elif self.datei.get() == "":
            messagebox.showerror("Error", "Please enter assigned_at")
        else:
            try:
                EmployeeModel().updateItem(self.employee_id, self.item_id.get().partition(' ')[0],
                                           self.qty.get(), self.datei.get())
                self.frameItem.destroy()
                messagebox.showinfo("Success", "Item assign")
            except Exception as e:
                messagebox.showerror("Error", e)

    def sortItem(self):
        order = self.order.get()
        col = self.col.get()
        fetchdata = self.tree.get_children()
        for f in fetchdata:
            self.tree.delete(f)
        try:
            lst = EmployeeModel().sort(order, col)
            print(lst)
            if len(lst) == 0:
                messagebox.showerror("Error", "No item found")
            else:
                for i in lst:
                    self.tree.insert('', 'end', values=i)

        except Exception as e:
            messagebox.showerror("Error", e)

    def searchItem(self):
        query = self.search.get()
        fetchdata = self.tree.get_children()
        for f in fetchdata:
            self.tree.delete(f)
        try:
            lst = EmployeeModel().search(query)
            if len(lst) == 0:
                messagebox.showerror("Error", "No item found")
            else:
                for i in lst:
                    self.tree.insert('', 'end', values=i)

        except Exception as e:
            messagebox.showerror("Error", e)

    def clearData(self):
        self.name.delete(0, END)
        self.emp_no.delete(0, END)
        self.date.delete(0, END)
        if hasattr(self, 'itemvalues'):
            self.itemvalues = EmployeeModel().getItem()

        if hasattr(self, 'frameshow'):
            self.frameshow.destroy()
        self.getEmployee()

    def clearFrame(self):
        self.frame.destroy()
        self.frameItem.destroy()
        self.frameTable.destroy()
        if hasattr(self, 'frameshow'):
            self.frameshow.destroy()


# master = Tk()
# obj = Employee(master)
# master.mainloop()
