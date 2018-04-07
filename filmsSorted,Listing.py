from tkinter import *

listing = []
def listFilm(it):
    filmList.place_forget()
    def getCast():
        cast = ""
        for items in films[4].split(":"):
            cast += "  " + str(items) + "\n"                  #when you call the search button, clear the listing [] list List
        return cast

    filmFrame = Frame(root, bg="red")
    filmFrame.place(x=5, y=100)

    with open("films2.txt") as filmsFile:
        theLines = filmsFile.readlines()
        theFilm = theLines[it]
        films = theFilm.split(",")
        ratings = films[12].split(":")
        ratings = [float(x) for x in ratings]
        rating = str(round(sum(ratings) / len(ratings), 1))

        picture = PhotoImage(file=films[10])

        pic = Frame(root)
        pic.place(x=0, y=80)
        pictureLabel = Label(pic, bg="red", image=picture)
        pictureLabel.img = picture
        pictureLabel.pack()
        listing.append(pic)

        name = Frame(root)
        name.place(x=110, y=80)
        nameLabel = Label(name, justify=LEFT, bg="red", text=films[1] + ' (' + films[2] + ')' + '\n' + rating + " / 10")
        nameLabel.pack()
        listing.append(name)

        rate = Frame(root)
        rate.place(x=550, y=100)
        rateLabel = Label(rate, text="Rate this film (0 - 10):")
        rateLabel.pack()
        listing.append(rate)

        entry = StringVar()
        rateEntry = Entry(rate)
        rateEntry.pack()

        rateButton = Button(rate, justify=LEFT, text="Submit", bg="red")
        rateButton.pack()

        bottomLeft = Frame(root)
        bottomLeft.place(x=0, y=180)
        bottomLabel1 = Label(bottomLeft, bg="red", justify=LEFT, text="Director: " + films[3]
                                            + "\nGenre: " + films[7]
                                            + "\nRun time: " + films[6]
                                            + "\nRelease date: " + films[9]
                                            + "\nWatch the trailer: " + films[11]
                                            + "\n\nCast: \n" + getCast())
        bottomLabel1.pack()
        listing.append(bottomLeft)

        comments = Frame(root)
        comments.place(x=400, y=100)
        commentsLabel = Label(comments, text="Add new comment:").pack()
        commentsEntry = Entry(comments).pack()
        commentButton = Button(comments, bg="red", text="Submit")
        commentButton.pack()

        title = Frame(root)
        title.place(x=400, y=170)
        titleLabel = Label(title, bg="red", text="Comments:")
        titleLabel.pack()
        listing.append(comments)
        listing.append(title)

        desc = Frame(root)
        desc.place(x=400, y=0)
        descLabel = Label(desc, bg="red", justify=LEFT, text="Description: \n" + films[7])
        descLabel.pack()
        listing.append(desc)
#-----------------------------------------------------------------------------------------------------------------------
array = []
def Lost(filter):

    search = Frame(root, bg="red")
    search.place(x=5, y=10)
    searchLabel = Label(search, bg="red", text="Search by genre or actor:")
    searchLabel.pack()
    searchEntry = Entry(search)
    searchEntry.pack()
    searchButton = Button(search, bg="red", text="Search", command=lambda: List(searchEntry.get()))
    searchButton.pack()
    array.append(searchButton)
    array.append(searchEntry)
    array.append(searchLabel)

    filmList.place(x=5, y=100)
    r=0
    i=0                                                                       # The problem is that i calls the current value of
    with open("films2.txt") as filmsFile:                                     # i. I need to save the iteration for each film.
        for films in filmsFile:                                               # Is the use of i effective?
                                                                              # The program must know what button was pressed.
                                                                              # You must select the line of films.txt
                                                                              #
            if filter.upper() in films.upper():                               # for films in films1.txt:
                films = films.split(",")                                      #
                name = films[1]                                               # films1.txt must be altered to have iteration numbers
                i = int(films[0])                                             #
                pic = films[10]                                               # 'it' is always equal to 3
                photo = PhotoImage(file=pic)                                  #
                ratings = films[12].split(":")                                # now i is all doopy
                ratings = [float(x) for x in ratings]                         #
                rating = str(round(sum(ratings) / len(ratings), 1))           #
                text = name + "(" + films[2] + ")  -  " + rating + " / 10"

                picLabel = Label(filmList, bg="red", image=photo)
                picLabel.img = photo
                picLabel.grid(column=0, row=r, rowspan=10)
                array.append(picLabel)

                descLabel = Label(filmList, bg="red", text=text)
                descLabel.grid(column=1, row=r)
                array.append(descLabel)

                listingButton = Button(filmList, bg="red", text="View Film", command=lambda i=i: listFilm(i))
                listingButton.grid(column=1, row=r + 2)
                array.append(listingButton)

                r += 10
#-----------------------------------------------------------------------------------------------------------------------
def List(filter):
    for Label in array:
        Label.destroy()
    for l in listing:
        l.destroy()
    Lost(filter)
#-----------------------------------------------------------------------------------------------------------------------
root = Tk()
root.geometry("700x550")
root["bg"] = "red"

filmList = Frame(root, bg="red")
filmList.place(x=5, y=100)

Lost("")

root.mainloop()