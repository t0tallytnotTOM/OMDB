from tkinter import * # top rated film, display all films

def Lost(filter):
    r=0
    array = []
    with open("films1.txt") as filmsFile:
        for films in filmsFile:
                films = films.split(",")
                if filter in films:
                    name = films[0]
                    pic = films[9]
                    photo = PhotoImage(file=pic)
                    ratings = films[11].split(":")
                    ratings = [float(x) for x in ratings]
                    rating = str(round(sum(ratings) / len(ratings), 1))
                    text = name + "(" + films[1] + ")  -  " + rating + " / 10"

                    picLabel = Label(topList, bg="red", image=photo)
                    picLabel.img = photo
                    picLabel.grid(column=0, row=r, rowspan=10)
                    array.append(picLabel)

                    descLabel = Label(topList, bg="red", text=text)
                    descLabel.grid(column=1, row=r)
                    array.append(descLabel)

                    listingButton = Button(topList, bg="red", text="View Film", command=lambda:listFilm(int(films[0])))
                    listingButton.grid(column=1, row=r + 2)
                    array.append(listingButton)

def topRated():
    with open("films1.txt") as filmsFile:
        highDb = {}
        for film in filmsFile:
            c = 0
            film = film.split(",")
            ratings = film[11]
            name = film[0]
            ratings = ratings.split(":")
            for rate in ratings:
                c += float(rate)
            avg = c / len(ratings)
            highDb[name] = avg
        maxi = max(highDb, key=highDb.get)
        return maxi

root = Tk()
root.geometry("700x550")
root["bg"] = "red"

search = Frame(root, bg="red")
search.place(x=5, y=100)
searchLabel = Label(search, bg="red", text="Search by genre or actor:")
searchLabel.pack()
searchEntry = Entry(search)
searchEntry.pack()
searchButton = Button(search, bg="red", text="Search", command=lambda: List(searchEntry.get()))
searchButton.pack()

top = Frame(root, bg="red")
top.place(x=5, y=100)
topFilmLabel = Label(top, bg="red", text="Top rated film:")
topFilmLabel.pack()

topList = Frame(root, bg="red")
topList.place(x=5, y=190)
topFilm = Label(topList, text=Lost(topRated()))

root.mainloop()
