# Password Generator - Victor Freire(devbuda)

from random import choice
from string import ascii_letters
from string import digits
from string import punctuation

def generate_password(length):

    caracteres = ascii_letters + digits + punctuation

    senha = "".join(choice(caracteres) for _ in range(length))

    return senha

comprimento_senha = int(input("Informe a quantidade de caracteres que deseja: "))

senha_gerada = generate_password(comprimento_senha)

print(f"A senha gerada é: {senha_gerada}")
