from tkinter import *

def listFilm(name):

    def getCast():
        cast = ""
        for items in filmData[3].split(":"):
            cast += "  " + str(items) + "\n"
        return cast

    with open("films1.txt") as filmsFile:
        filmData = []
        for films in filmsFile:
            films = films.split(",")
            if name in films:
                filmData = films
        ratings = filmData[11].split(":")
        ratings = [float(x) for x in ratings]
        rating = str(round(sum(ratings) / len(ratings), 1))

        root = Tk()
        root.geometry("700x400")
        root["bg"] = "red"

        photo = PhotoImage(file=filmData[9])


        pic = Frame(root)
        pic.place(x=0, y=0)
        picLabel = Label(pic, image=photo).pack()
        name = Frame(root)
        name.place(x=110, y=0)
        nameLabel = Label(name, justify=LEFT, bg="red", text=filmData[0] + ' (' + filmData[1] + ')' + '\n' + rating + " / 10").pack()
        rate = Frame(root)
        rate.place(x=550, y=100)
        rateLabel = Label(rate, text="Rate this film (0 - 10):").pack()
        entry = StringVar()
        rateEntry = Entry(rate).pack()
        rateButton = Button(rate, justify=LEFT, text="Submit", bg="red", fg="black").pack()

        bottomLeft = Frame(root)
        bottomLeft.place(x=0, y=100)
        bottomLabel1 = Label(bottomLeft, bg="red", justify=LEFT, text="Director: " + filmData[2]
                                            + "\nGenre: " + filmData[6]
                                            + "\nRun time: " + filmData[5]
                                            + "\nRelease date: " + filmData[8]
                                            + "\nWatch the trailer: " + filmData[10]
                                            + "\n\nCast: \n" + getCast()).pack()
        comments = Frame(root)
        comments.place(x=400, y=100)
        commentsLabel = Label(comments, text="Add new comment:").pack()
        commentsEntry = Entry(comments).pack()
        commentButton = Button(comments, bg="red", text="Submit").pack()
        title = Frame(root)
        title.place(x=400, y=170)
        titleLabel = Label(title, bg="red", text="Comments:").pack()

        desc = Frame(root)
        desc.place(x=400, y=0)
        descLabel = Label(desc, bg="red", justify=LEFT, text="Description: \n" + filmData[7]).pack()


        root.mainloop()

listFilm('Star Wars')