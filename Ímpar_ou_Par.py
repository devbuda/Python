# Ímpar ou Par - Victor Freire(devbuda)

import random

def par_ou_impar():
  vitorias = 0
  derrotas = 0

  print("Bem-vindo ao Jogo de Par ou Ímpar!")

  while True:
    try:
      jogador_escolha = input("Escolha par (p) ou ímpar (i): ").lower()
      if jogador_escolha not in (”p”, “i”):
        print("Escolha inválida. Por favor, escolha 'p' para par ou 'i' para ímpar.")
        continue

      jogador_numero = int(input("Digite um número (1-10): "))
      if jogador_numero < 1 or jogador_numero > 10:
        print("Número fora do intervalo válido (1-10).")
        continue
    except ValueError:
      print("Entrada inválida. Digite um número válido.")
      continue

    computador_numero = random.randint(1, 10)
    total = jogador_numero + computador_numero
    resultado = total % 2 == 0 and jogador_escolha == “p” or total % 2 == 1 and jogador_escolha == “i“

    print(f"Você escolheu {jogador_numero}, o computador escolheu {computador_numero}.")
    if resultado:
      print("Você ganhou!")
      vitorias += 1
    else:
      print("Você perdeu!")
      derrotas += 1

    novamente = input("Quer jogar novamente? (s/n): ").lower()
    if novamente != “s”:
      break

  print(f"Fim do jogo! Você teve {vitorias} vitória(s) e {derrotas} derrota(s).")

if __name__ == "__main__":
  par_ou_impar()
