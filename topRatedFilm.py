def topRated():
    with open("films.txt") as filmsFile:
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
        return maxi + ": " + str(round(highDb[maxi],1))

print(topRated())

# I should say that for this to work, in films.txt, after the last real film
# listing, there should be no more lines i.e. if there are 5 film listings
# then there should only be 5 lines in the file. Also, for a similar reason,
# at the end of each set of ratings, there should be nothing (no commas or 
# colons)

# The idea is that when you login, or go to the home page, or somewhere that
# you can view the top rated film, that this function can be called    :)
