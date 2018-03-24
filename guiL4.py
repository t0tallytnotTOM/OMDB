from tkinter import *

root = Tk()

lab1 = Label(root, text="Name")
lab2 = Label(root, text="Password")
entry1 = Entry(root)
entry2 = Entry(root)

lab1.grid(row=0, sticky=E)
lab2.grid(row=1, sticky=E)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

c = Checkbutton(root, text="im too lazy to sign out")
c.grid(columnspan=2)

root.mainloop()