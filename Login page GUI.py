from tkinter import *

loginPage = Tk()
loginPage.title("Login")
loginPage.configure(bg = "#34495E")
loginPage.geometry("200x100")

L1 = Label(loginPage, text = "Username", fg = "#D0D3D4", bg = "#34495E")
L1.grid(row = 3, column = 5)
L2 = Label(loginPage, text = "Password", fg = "#D0D3D4", bg = "#34495E")
L2.grid(row = 4, column = 5)

T1 = Entry(loginPage)
T1.grid(row = 3, column = 6)
T2 = Entry(loginPage, show = "*")
T2.grid(row = 4, column = 6)

L3 = Label(loginPage, bg = "#34495E")
L3.grid(row = 5)

C1 = Checkbutton(loginPage, text = "Keep me logged in", fg = "#D0D3D4", bg = "#34495E")
C1.grid(row = 5, column = 6)

B1 = Button(loginPage, text = "Login", bg = "red", fg = "white")
B1.grid(row = 7, column = 6)
B2 = Button(loginPage, text = "Cancel", bg = "red", fg = "white")
B2.grid(row = 7, column = 5)

loginPage.mainloop()
