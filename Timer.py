# Timer - Victor Freire(devbuda)

from time import sleep

t = input("Enter the time (in seconds): ")

if t.isdigit():
    t = int(t)
else:
    print("Invalid Input")
    quit()

while t:
    minutes, seconds = divmod(t, 60)
   
    timer = f"{minutes:02d}:{seconds:02d}"

    print(timer, end = "\r")
    sleep(1)
    t -= 1

print("\nTimer ended.\n")
