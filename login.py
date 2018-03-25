import hashlib
import uuid
users = {}


def getUsers():
    with open("users.txt") as usersFile:
        for line in usersFile:
            line = line.split(",")
            username = line[0]
            password_hash = line[1].strip()
            users[username] = password_hash


def addUser():

    username = input("Enter your username: ")
    if username in users:
        print("Username already taken")
        return False
    else:
        password = input("Enter your password: ")
        if len(password) < 8:
            print("Password must be over 8 characters long")
            return False
        users[username] = encrypt(password)
        updateUsers()
        return True


def login(username, password):
    if username in users and decrypt(users[username], password):
        print("login successful")
    else:
        print("login failed")


def encrypt(password):
    num = uuid.uuid4().hex
    return hashlib.sha512(num.encode() + password.encode()).hexdigest() + ":" + num


def decrypt(encryptedPassword, usersPassword):
    password, num = encryptedPassword.split(":")
    return password == hashlib.sha512(num.encode() + usersPassword.encode()).hexdigest()


def updateUsers():
    with open("users.txt", "r+") as usersFile:
            usersFile.truncate()
    for user in users:
        username = user
        password = users[user]
        with open("users.txt", "a+") as usersFile:
            usersFile.write(username + "," + password + "\n")


operation = input("Enter operation: ")


while operation != "q":
    getUsers()
    if operation == "a":
        if addUser():
            print("User added successfully")
        else:
            print("Add user failed")
    elif operation == "l":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        login(username, password)
    operation = input("Enter operation: ")
