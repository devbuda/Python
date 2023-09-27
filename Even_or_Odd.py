# Even or Odd - Victor Freire(devbuda)

import random

def even_or_odd():
  wins = 0
  defeats = 0

  print("Welcome to the Odd or Even Game")

  while True:
    try:
      player_choose = input("Choose even (e) or odd (o): ").lower()
      if player_choose not in ("e", "o"):
        print("Invalid choice. Please choose 'e' for even or 'o' for odd.")
        continue

      player_number = int(input("Enter a number (1 - 10): "))
      if player_number < 1 or player_number > 10:
        print("Number outside the valid range (1 - 10)")
        continue
    except ValueError:
      print("Invalid entry. Please enter a valid number.")
      continue

    computer_number = random.randint(1, 10)
    total = player_number + computer_number
    result = total % 2 == 0 and player_choose == "o" or total % 2 == 1 and player_choose == "e"

    print(f"You chose {player_number}, the computer chose {computer_number}.")
    if result:
      print("You win!")
      wins += 1
    else:
      print("You lost!")
      defeats += 1

    again = input("Do you want to play again? (Y/N): ").lower()
    if again != "y":
      break

  print(f"\nGame Over! You had {wins} victory(s) and {defeats} defeat(s).\n")

if __name__ == "__main__":
  even_or_odd()
