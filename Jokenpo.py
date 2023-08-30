# Jokenpo - Victor Freire(devbuda)

from random import randint
from time import sleep

def play():
    print("[ 0 ] - ROCK")
    print("[ 1 ] - PAPER")
    print("[ 2 ] - SCISSORS\n")

    user = int(input("CHOICE: ")) 

    print("\nJO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO")
    sleep(1)
    computer = randint(0, 2)

    if user == computer:
        return "\nTie\n"
     
    if is_win(user, computer):
        return "\nYou won\n"
    
    if is_win(computer, user):
        return "\nYou lost\n"

def is_win(player, opponent):
    if (player == 0 and opponent == 2) or (player == 2 and opponent == 1) or (player == 1 and opponent == 0):
        return True 
    
print(play())
