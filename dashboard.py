from tkinter import *
from items import Item
from employee import Employee


class Dashboard:
    def __init__(self, master):
        self.master = master
        self.master.title("PSB-Inventory-Management - Dashboard")
        self.master.geometry("1350x700+0+0")

        self.navframe = Frame(master)
        self.navframe.pack()

        self.itemButton = Button(
            self.navframe, text="Items Store", command=self.showItem)
        self.itemButton.grid(row=5, column=1)

        self.employeeButton = Button(
            self.navframe, text="Employee List", command=self.showEmployee)
        self.employeeButton.grid(row=5, column=2)

    def showItem(self):
        if hasattr(self, "employee"):
            self.employee.clearFrame()
        self.item = Item(self.master)

    def showEmployee(self):
        if hasattr(self, "item"):
            self.item.clearFrame()
        self.employee = Employee(self.master)


# master = Tk()
# obj = Dashboard(master)
# master.mainloop()
