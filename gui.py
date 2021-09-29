from tkinter import *


def onclick():
    pass


root = Tk()

text = Text(root)
text.insert(INSERT, "PSB Inventory Management System. fisrt col")
text.grid(row=1, column=1)

text2 = Text(root)
text2.insert(INSERT, "PSB Inventory Management System. sencond col")
text2.grid(row=1, column=2)

text3 = Text(root)
text3.insert(INSERT, "PSB Inventory Management System. third col")
text3.grid(row=2, column=2)

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")

root.mainloop()