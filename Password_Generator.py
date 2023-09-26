# Password Generator - Victor Freire(devbuda)

from random import choice
from string import ascii_letters
from string import digits
from string import punctuation

def generate_password(length):

    characters = ascii_letters + digits + punctuation

    password = "".join(choice(characters) for _ in range(length))

    return password

password_length = int(input("Enter the number of characters you want: "))

generated_password = generate_password(password_length)

print(f"The generated password is: {generated_password}")
