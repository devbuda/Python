# Timer - Victor Freire(devbuda)

from time import sleep

t = input("Informe o tempo(em segundos): ")

if t.isdigit():
    t = int(t)
else:
    print("Entrada inválida")
    quit()

while t:
    minutes, seconds = divmod(t, 60)
   
    timer = f"{minutes:02d}:{seconds:02d}"

    print(timer, end = "\r")
    sleep(1)
    t -= 1

print("\nTemporizador finalizado.\n")
