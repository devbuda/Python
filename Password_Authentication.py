# Password_Authentication - Victor Freire(devbuda)

import getpass

database = {"Administrator": "12345678", "User": "87654321"}
username = str(input("Enter your username: "))
password = getpass.getpass("Enter your password: ")

for i in database.keys():
    if username == i:
        while password != database.get(i):
            print("The password is incorrect.")
            password = getpass.getpass("Enter your password again: ")
            break
        print("Verified")
