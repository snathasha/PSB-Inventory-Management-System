from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from ItemModel import ItemModel


class Item:
    def __init__(self, master):
        self.master = master
        self.master.title("PSB-Inventory-Management - Items")
        self.master.geometry("1350x700+0+0")

        # Form---------------------------
        self.frame = Frame(master)
        self.frame.pack()

        self.nameLabel = Label(self.frame, text="Name")
        self.nameLabel.grid(row=0, column=0)

        self.cateLabel = Label(self.frame, text="Category")
        self.cateLabel.grid(row=1, column=0)

        self.qtyLabel = Label(self.frame, text="Qty")
        self.qtyLabel.grid(row=2, column=0)

        self.priceLabel = Label(self.frame, text="Price")
        self.priceLabel.grid(row=3, column=0)

        self.dateLabel = Label(self.frame, text="Date")
        self.dateLabel.grid(row=4, column=0)

        self.name = Entry(self.frame)
        self.name.grid(row=0, column=1)

        self.cate = Combobox(self.frame, values=('Stationary', 'Electric'))
        self.cate.grid(row=1, column=1)

        self.qty = Entry(self.frame)
        self.qty.grid(row=2, column=1)

        self.price = Entry(self.frame)
        self.price.grid(row=3, column=1)

        self.date = Entry(self.frame)
        self.date.grid(row=4, column=1)

        # Action---------------------------
        self.loginButton = Button(
            self.frame, text="Add Item", command=self.addItem)
        self.loginButton.grid(row=5, column=1)

        self.updateButton = Button(
            self.frame, text="Edit Item", command=self.editItem)
        self.updateButton.grid(row=5, column=2)

        self.updateButton = Button(
            self.frame, text="Update Item", command=self.updateItem)
        self.updateButton.grid(row=5, column=3)

        self.deleteButton = Button(
            self.frame, text="Delete Item", command=self.deleteItem)
        self.deleteButton.grid(row=5, column=4)

        self.clearButton = Button(
            self.frame, text="All Clear", command=self.clearData)
        self.clearButton.grid(row=5, column=5)

        # Sort---------------------------
        self.col = Combobox(self.frame, values=(
            'name', 'category', 'qty', 'price', 'date'))
        self.col.grid(row=6, column=1)

        self.order = Combobox(self.frame, values=('ASC', 'DESC'))
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

        # Table---------------------------
        self.frameTable = Frame(master)
        self.frameTable.pack()
        # columns
        columns = ('#1', '#2', '#3', '#4', '#5', '$6')

        self.tree = Treeview(self.frameTable, columns=columns, show='headings')

        # define headings
        self.tree.heading('#1', text='ID')
        self.tree.heading('#2', text='Item')
        self.tree.heading('#3', text='Category')
        self.tree.heading('#4', text='Qty')
        self.tree.heading('#5', text='Price')
        self.tree.heading('#6', text='Date')

        self.tree.pack()

        self.getItem()

    def getItem(self):
        try:
            lst = ItemModel().get()
            for i in lst:
                self.tree.insert('', 'end', values=i)

        except Exception as e:
            messagebox.showerror("Error", e)

    def addItem(self):
        if self.name.get() == "":
            messagebox.showerror("Error", "Please enter name")
        elif self.cate.get() == "":
            messagebox.showerror("Error", "Please enter category")
        elif self.qty.get() == "":
            messagebox.showerror("Error", "Please enter qty")
        elif self.price.get() == "":
            messagebox.showerror("Error", "Please enter price")
        elif self.date.get() == "":
            messagebox.showerror("Error", "Please enter date")
        else:
            try:
                ItemModel().create(self.name.get(), self.cate.get(),
                                   self.qty.get(), self.price.get(), self.date.get())
                self.clearData()
                messagebox.showinfo("Success", "Item added")
            except Exception as e:
                messagebox.showerror("Error", e)

    def updateItem(self):
        if self.name.get() == "":
            messagebox.showerror("Error", "Please enter name")
        elif self.cate.get() == "":
            messagebox.showerror("Error", "Please enter category")
        elif self.qty.get() == "":
            messagebox.showerror("Error", "Please enter qty")
        elif self.price.get() == "":
            messagebox.showerror("Error", "Please enter price")
        elif self.date.get() == "":
            messagebox.showerror("Error", "Please enter date")
        else:
            try:
                ItemModel().update(self.id, self.name.get(), self.cate.get(),
                                   self.qty.get(), self.price.get(), self.date.get())
                self.clearData()
                messagebox.showinfo("Success", "Item updated")
            except Exception as e:
                messagebox.showerror("Error", e)

    def searchItem(self):
        query = self.search.get()
        fetchdata = self.tree.get_children()
        for f in fetchdata:
            self.tree.delete(f)
        try:
            lst = ItemModel().search(query)
            print(lst)
            if len(lst) == 0:
                messagebox.showerror("Error", "No item found")
            else:
                for i in lst:
                    self.tree.insert('', 'end', values=i)

        except Exception as e:
            messagebox.showerror("Error", e)
        # selections = []
        # for child in self.tree.get_children():
        #     # compare strings in  lower cases.
        #     if query in self.tree.item(child)['values']:
        #         print(self.tree.item(child)['values'])
        #         selections.append(child)
        # print('search completed')
        # self.tree.selection_set(selections)

    def sortItem(self):
        order = self.order.get()
        col = self.col.get()
        fetchdata = self.tree.get_children()
        for f in fetchdata:
            self.tree.delete(f)
        try:
            lst = ItemModel().sort(order, col)
            print(lst)
            if len(lst) == 0:
                messagebox.showerror("Error", "No item found")
            else:
                for i in lst:
                    self.tree.insert('', 'end', values=i)

        except Exception as e:
            messagebox.showerror("Error", e)

    def deleteItem(self):
        if self.tree.selection():
            x = self.tree.selection()[0]
            id = self.tree.item(x)['values'][0]
            self.tree.delete(x)
            try:
                ItemModel().delete(id)
                messagebox.showinfo("Success", "Item deleted")
            except Exception as e:
                messagebox.showerror("Error", e)
        else:
            messagebox.showerror(
                "Error", "Please select the row you want to delete")

    def editItem(self):
        if self.tree.selection():
            x = self.tree.selection()[0]
            item = self.tree.item(x)['values']
            self.id = item[0]
            self.name.delete(0, END)
            self.cate.delete(0, END)
            self.qty.delete(0, END)
            self.price.delete(0, END)
            self.date.delete(0, END)

            self.name.insert(0, item[1])
            self.cate.insert(0, item[2])
            self.qty.insert(0, item[3])
            self.price.insert(0, item[4])
            self.date.insert(0, item[5])
        else:
            messagebox.showerror(
                "Error", "Please select the row you want to delete")

    def clearData(self):
        self.name.delete(0, END)
        self.cate.delete(0, END)
        self.qty.delete(0, END)
        self.price.delete(0, END)
        self.date.delete(0, END)

        self.tree.delete(0, END)

        self.getItem()

    def clearFrame(self):
        self.frame.destroy()
        self.frameTable.destroy()


# master = Tk()
# obj = Item(master)
# master.mainloop()
