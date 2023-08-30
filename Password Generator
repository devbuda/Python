# Password Generator - Victor Freire(devbuda)

from random import choice
from string import ascii_letters
from string import digits
from string import punctuation

def generate_password(length):

    # Definindo caracteres "pool" para gerar senha
    caracteres = ascii_letters + digits + punctuation

    # Gerando uma senha selecionando aleatoriamente caracteres "pool"
    senha = "".join(choice(caracteres) for _ in range(length))

    # Retornando a senha gerada
    return senha

# Solicitando ao usuário que insira o comprimento desejado da senha:
comprimento_senha = int(input("Informe a quantidade de caracteres que deseja: "))

# Gerando a senha usando o comprimento especificado:
senha_gerada = generate_password(comprimento_senha)

# Imprimindo a senha:
print(f"A senha gerada é: {senha_gerada}")
