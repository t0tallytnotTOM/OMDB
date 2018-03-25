films = {}


def getFilms():
    with open("films.txt") as filmsFile:
        for film in filmsFile:
            film = film.split(",")
            name = film[0]
            year = film[1].strip()
            director = film[2].strip()
            cast = film[3].strip()
            age = film[4].strip()
            run_time = film[5].strip()
            genre = film[6].strip()
            description = film[7].strip()
            release_date = film[8].strip()
            picture = film[9].strip()
            trailer = film[10].strip()
            ratings = film[11].strip()

            films[name] = [year, director, cast, age, run_time, genre, description, release_date, picture, trailer, ratings]


def updateFilms():
    with open("films.txt", "r+") as filmsFile:
        filmsFile.truncate()
    for film in films:
        film_data = ""
        for i in range(len(films[film])):
            film_data += str(films[film][i]) + ","
        with open("films.txt", "a+") as filmsFile:
            filmsFile.write(film + "," + film_data + "\n")


def addFilm(name, year, director, cast, age, run_time, genre, description, release_date, picture, trailer):
    cast_list = getCast(cast)
    if name == "" or year == "" or director == "" or cast_list == "" or age == "" or run_time == "" or description == "" or release_date == "" or picture == "" or trailer == "":
        # field left blank
        print("Not all fields have been filled")
        return False
    elif name in films:
        print("Film already added")
        return False
    ratings = ""
    films[name] = [year, director, cast, age, run_time, genre, description, release_date, picture, trailer, ratings]
    updateFilms()
    return True


def getCast(cast):
    cast_list = []
    cast = cast.split(":")
    for actor in cast:
        cast_list.append(actor)

    return cast_list


def addRating(film, new_rating):
    film_data = films[film]
    ratings = film_data[10]
    if ratings == "":
        film_data[10] = new_rating
    else:
        film_data[10] = ratings + ":" + new_rating
    films[film] = film_data
    updateFilms()


def getRating(film):
    film_data = films[film]
    ratings = film_data[10]
    if ratings == "":
        return ""
    ratings_list = []
    ratings = ratings.split(":")
    for rating in ratings:
        ratings_list.append(float(rating))

    rating = round(sum(ratings_list) / len(ratings_list), 1)
    return rating


def getRatingKey(film):
    return film[1]

def sortByRating():
    filmRatings = []
    for film in films:
        rating = getRating(film)
        filmRatings.append([rating, film])
    filmRatings = sorted(filmRatings, reverse=True)
    return filmRatings


operation = input("Enter operation: ")


while operation != "q":
    getFilms()
    if operation == "a":
        name = input("Film name: ")
        year = input("Year:  ")
        director = input("Director: ")
        cast = input("cast: ")
        age = input("Age rating: ")
        run_time = input("Run time: ")
        genre = input("Genre: ")
        description = input("Description: ")
        release_date = input("Release date: ")
        picture = input("Link to Picture: ")
        trailer = input("Link to trailer: ")

        if addFilm(name, year, director, cast, age, run_time, genre, description, release_date, picture, trailer):
            print("Film added successfully")
        else:
            print("New film failed")
    elif operation == "v":
        for film in films:
            film_data = films[film]
            rating = getRating(film)

            cast_list = getCast(film_data[2])
            cast = ""
            for actor in cast_list:
                cast += actor + ", "

            print("name: ", film)
            print("Year: ", film_data[0])
            print("Director: ", film_data[1])
            print("cast: ", cast[:-1])
            print("age: ", film_data[3])
            print("run time: ", film_data[4])
            print("Genre: ", film_data[5])
            print("Description: ", film_data[6])
            print("Release date: ", film_data[7])
            print("Ratings: ", rating)
            print()
    elif operation == "r":
        film = input("Enter film name to rate: ")
        rating = input("Enter rating: ")
        addRating(film, rating)
        print("New rating is: ", getRating(film))
    elif operation == "s":
        print(sortByRating())
    operation = input("Enter operation: ")

