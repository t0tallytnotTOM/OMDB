from tkinter import *


registerPage = Tk()
registerPage.title("Register")

registerPage.configure(bg = "#34495E")
registerPage.geometry("600x250")

L1 = Label(registerPage, text = "PLEASE ENTER YOUR DETAILS TO REGISTER", fg = "#D0D3D4", bg = "#34495E", font = "Georgia 20")
L1.grid(columnspan = 2, sticky = E)

L5 = Label(registerPage, text = "First Name:", fg = "#D0D3D4", bg = "#34495E")
L5.grid(row = 2, sticky = E)

L6 = Label(registerPage, text = "Last Name:", fg = "#D0D3D4", bg = "#34495E")
L6.grid(row = 3, sticky = E)

L7 = Label(registerPage, text = "Email:", fg = "#D0D3D4", bg = "#34495E")
L7.grid(row = 4, sticky = E)

L4 = Label(registerPage, bg = "#34495E")
L4.grid(row = 1)

L2 = Label(registerPage, text = "New Username:", fg = "#D0D3D4", bg = "#34495E")
L2.grid(row = 5, sticky = E)

L3 = Label(registerPage, text = "New Password:", fg = "#D0D3D4", bg = "#34495E")
L3.grid(row = 6, sticky = E)

T1 = Entry(registerPage, bg = "#5D6D7E")
T1.grid(row = 3, column = 1)

T2 = Entry(registerPage, bg = "#5D6D7E")
T2.grid(row = 4, column = 1)

T3 = Entry(registerPage, bg = "#5D6D7E")
T3.grid(row = 2, column = 1)

T4 = Entry(registerPage, bg = "#5D6D7E")
T4.grid(row = 5, column = 1)

T5 = Entry(registerPage, show = "*", bg = "#5D6D7E")
T5.grid(row = 6, column = 1)

L5 = Label(registerPage, bg = "#34495E")
L5.grid(row = 7)

B1 = Button(registerPage, text = "Cancel", bg = "red", fg = "white")
B1.grid(row = 8)

B2 = Button(registerPage, text = "Register", bg = "red", fg = "white")
B2.grid(row = 8, column = 1)

registerPage.mainloop()
